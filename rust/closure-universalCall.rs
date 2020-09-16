//Universal Call
/**
*	Type t impl 两个Trait，这两个Trait里都有函数f
*	那么	t.f()就不行了
**/
trait Cat {
	fn poop(&self){
		println!("Cat pooping");
	}
}
trait Dog {
	fn poop(&self){
		println!("Dog pooping");
	}
}
struct Animal;

impl Cat for Animal {
	fn poop(&self){ println!("Cat pooping");}
}
impl Dog for Animal {
	fn poop(&self){ println!("Dog pooping");}
}
impl Animal {
	fn poop(&self){ println!("Animal pooping");}
}

//Closure 
/**
*	 wrap up a function and free variables for clarity and reuse. 
*	The free variables that can be used come from the enclosing scope
*	‘closed over’ when used in the function.
**/

fn main() {

	let kitty = Animal;
	//👌
	Cat::poop(&kitty);
	Dog::poop(&kitty);
	/*
	如果没有Animal自己的poop，这个就不行
	🙅‍♂️
	kitty.poop();
	*/
	//👌 因为 impl Animal
	kitty.poop();
	//此时如果要Cat poop就要用<kitty as Cat>
	<Animal as Cat>::poop(&kitty);


	//三种syntext一样

	let plus_one = |x: i32| x + 1;
	let plus_one_ = |x: i32| -> i32 { x + 1 };

	assert_eq!(plus_one_(1), plus_one(1));



	//Closures in environment
	/**	
	*	Closure 可以拿外面的 environmental 的变量
	*	相当于 x + mum 不在一个单独的scope里面
	**/

	let num = 5;
	let plus_num = |x: i32| x + num;

	assert_eq!(10, plus_num(5));
	/*
	🙅‍♂️
	let y = &mut num;
	因为 num 还在 plus_num 里用着，不能作为mutable reference借出
	*/

	//👌
	let mut num = 5;
	{
	    let plus_num = |x: i32| x + num;

	} // `plus_num` goes out of scope; borrow of `num` ends.

	let y = &mut num;



	//啥都不放也👌

	let nums = vec![1, 2, 3];
	let takes_nums = || nums;
	/*
	🙅‍♂️ nums 在 takes_nums 被借走了，甚至不能 println
	println!("{:?}", nums);
	*/
	let nums = [1, 2, 3];
	let takes_nums = move |x: i32, y: i32| nums;
	//👌 此时 takes_nums 其实把nums复制了一遍
	//印出来的nums是原品
	println!("{:?}", nums);

	//Taking closures as arguments
	//👌
	let answer = call_with_one(|x| x + 2);
	assert_eq!(3, answer);

	//👌
	let f = add_one;
	let answer = call_with_one(&f);


}

fn plus_one_f (x: i32) -> i32 { x + 1 }


//Taking closures as arguments
//👌
fn call_with_one<F>(some_closure: F) -> i32		//takein 一个 F 返回 i32
    where F: Fn(i32) -> i32 {					//这个 F 是 i32 -> i32 的函数
    some_closure(1)								//令这个函数操作1
}

fn add_one(i: i32) -> i32 {
    i + 1
}

//Function Factory
//👌
fn factory() -> Box<Fn(i32) -> i32> {			//返回一个 i32->i32 函数
    let num = 5;								//必须用 Box 因为不知道返回值大小，只能用指针包起来
    Box::new(move |x| x + num)					
}






