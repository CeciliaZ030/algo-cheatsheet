use criterion::*;
use std::time::Duration;
use hex::decode;

use bench_testing::*;


//🌰 在外面定义函数
fn fibonacci(n: u64) -> u64 {
    match n {
        0 => 1,
        1 => 1,
        n => fibonacci(n-1) + fibonacci(n-2),
    }
}

//🌰
fn power(x: u32) {
    let a = x^99;
}



//把你要bench的那一组都放在这里
//👇下面 criterion_group! 写清楚你要测bench_fib

fn bench_fib(c: &mut Criterion) {

	test();

	//🌰
    c.bench_function("fib 20", |b| b.iter(|| fibonacci(black_box(20))));

    /*🌰
	Bench with input
	先specify x，把x作为reference丢进去
	“power_bench” 是这个bench的名字
	cmd内容：power_bench/1024  
    */
    let x: u32 = 1024;
    c.bench_with_input(BenchmarkId::new("power_bench", x), &x, |b, &s| {
        b.iter(|| power(s));
    });

}




/**		🌰Becnchmark Group🌰 	**/



fn bench_simple(c: &mut Criterion) {

	/*
	之前是c.bench_function()或者c.bench_with_input()
	现在通过c.benchmark_group("My Group")搞成了一组
	*/
    let mut group = c.benchmark_group("My Group");

    // Now we can perform benchmarks with this group
    group.bench_function("Bench 1", |b| b.iter(|| 1 ));
    group.bench_function("Bench 2", |b| b.iter(|| 2 ));
    
    // It's recommended to call group.finish() explicitly at the end, but if you don't it will
    // be called automatically when the group is dropped.
    group.finish();
}

fn bench_nested(c: &mut Criterion) {

    let mut group = c.benchmark_group("My Second Group");
    // We can override the configuration on a per-group level
    group.measurement_time(Duration::from_secs(1));

    // We can also use loops to define multiple benchmarks, even over multiple dimensions.
    for x in 0..3 {
        for y in 0..3 {
            let point = (x, y);
            //这里format的作用只是做每个bench的名字
            //因为每个(x,y)是不一样的可能要区别 “Multiply x * y"
            let parameter_string = format!("{} * {}", x, y);
            group.bench_with_input(BenchmarkId::new("Multiply", parameter_string), &point,
                |b, (p_x, p_y)| b.iter(|| p_x * p_y));

        }
    }
    
    group.finish();
}

fn bench_throughput(c: &mut Criterion) {
    let mut group = c.benchmark_group("Summation");
     
    for size in [1024, 2048, 4096].iter() {

        // Generate input of an appropriate size...
        let input = vec![1u64, *size];

        // We can use the throughput function to tell Criterion.rs how large the input is
        // so it can calculate the overall throughput of the function. If we wanted, we could
        // even change the benchmark configuration for different inputs (eg. to reduce the
        // number of samples for extremely large and slow inputs) or even different functions.
        group.throughput(Throughput::Elements(*size as u64));

        //Throughput是你告诉bench_with_input你丢进去的input有多大

        group.bench_with_input(BenchmarkId::new("sum", *size), &input,
            |b, i| b.iter(|| i.iter().sum::<u64>()));
        group.bench_with_input(BenchmarkId::new("fold", *size), &input,
            |b, i| b.iter(|| i.iter().fold(0u64, |a, b| a + b)));
    }

    group.finish();
}


//criterion_group!(benches, bench_simple, bench_nested, bench_throughput);


/* 👌 简洁写法，bench_fib函数里面有你要跑的所有bench
criterion_group!(benches, bench_fib);
*/
//👌也可通过criterion_group! specify如何跑bench
criterion_group!{
    name = benches;
    // This can be any expression that returns a `Criterion` object.
    config = Criterion::default().significance_level(0.1).sample_size(100);
    targets = bench_fib, bench_simple, bench_nested, bench_throughput
}
criterion_main!(benches);