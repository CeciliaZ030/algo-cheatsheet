use std::thread;
use std::sync::mpsc;
use std::sync::{Mutex, Arc};

fn main() {

	/*🌰
	跑出来是这样
	thead 0
	thead 5
	main thead
	main thead
	main thead
	main thead
	main thead
	thead 7
	thead 1
	thead 8
	thead 2
	thead 9
	🙅‍♂️
	每个thread的进程是随机的，其中没有3，4，6
	因为跑到println前main thread结束了
	*/
	let mut c = vec![];

	for i in 0..10 {
		//此处必须有 move 因为不能borrow
		//main thread结束之后你borrow的本尊就死了
		c.push(thread::spawn( move || {
			println!("thead {:?}", i);
		}));
	}

	for j in 0..5 {
		println!("mianin thead");
	}

	let mut c = vec![];

	/*👌
	-thead 0
	-thead 1
	main thead
	-thead 2
	-thead 3
	main thead
	main thead
	-thead 4
	main thead
	main thead
	main thead
	-thead 5
	-thead 6
	-thead 7
	-thead 8
	-thead 9
	main thead
	main thead
	main thead

	最后 join 所有 thread back to main
	所以main必须等所有子进程结束
	*/
	for i in 0..10 {
		//此处必须有 move 因为不能borrow
		//main thread结束之后你borrow的本尊就死了
		c.push(thread::spawn( move || {
			println!("-thead {:?}", i);
		}));
	}

	for j in c {
		println!("main thead");
		j.join();
	}

	// Channel
	/*🌰
	tx: transmiter, rx: reciever
	两个thread交流
	*/
	let (tx, rx) = mpsc::channel();
	thread::spawn(move || {
		println!("tx send {:?}", 42);
		tx.send(42).unwrap();
	});
	// rx.recv() 会block mian thread的运行
	// 逼人家等到自己收到42
	println!("rx got {:?}", rx.recv().unwrap());


	/*🌰
	std::sync::mpsc -> multiple producer single consumer
	可以clone tx制造多个transmiter对应一个reciever
	*/
	let (tx, rx) = mpsc::channel();
	for i in 0..10 {
	    let tx = tx.clone();
	    thread::spawn(move|| {
	        tx.send(i).unwrap();
	    });
	}
	for _ in 0..10 {
	    let j = rx.recv().unwrap();
	    println!("{:?}", j);
	}


	//Mutex

	/*🌰
	c 是被所有线程share的mutex，在某一时间点只有一个线程有c的access
	用的时候要锁上，不用担时候开锁
	*/
	let c = Arc::new(Mutex::new(0));
	let mut hs = vec![];

	for _ in 0..10 {
		//关键： clone c 的 reference 而不是 c 本身
		//这这一步相当于拿到了钥匙🔑 
		//而且这一步必须clone 不clone的话 c 本身就进去了没法reuse
		let c = Arc::clone(&c);
		let h = thread::spawn(move || {
			let mut num = c.lock().unwrap();
			*num += 1;
		});
		hs.push(h);
	}

	for h in hs {
		h.join().unwrap();
	}

	println!("Result: {:?}", *c.lock().unwrap());

}

