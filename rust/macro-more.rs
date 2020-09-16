//🌰 作用域
/** 
*	mod里面可以看到外面的
*	
**/
macro_rules! m1 { () => (println!("m1");) }
// Visible here: `m1`.

mod foo {
    // Visible here: `m1`.
    #[macro_export]//👌在mod里面加 #[macro_export]可以把接下来的宏导出
    macro_rules! m2 { () => (println!("m2")); }
    // Visible here: `m1`, `m2`.
}

// Visible here: `m1`.

#[macro_use]//👌在mod之前加 #[macro_use]可以把里面的宏导出
mod bar {
    // Visible here: `m1`.
    macro_rules! m4 { () => (println!("m4")); }
    // Visible here: `m1`, `m4`.

}

// Visible here: `m1`, `m4`.
fn main() { 
	m1!();
	m2!();
	m4!();

//🌰 关于vec!
	let a = [1, 2, 3];
/*	数据直接在stack上
	stack:

	+-----------+
	| 1 | 2 | 3 |
	+-----------+
*/
	let b: &[u32] = &[1, 2, 3];
/*	stack上有一个指针指向内存放着数据
	         stack:
	                 +-----------+
	                 | 1 | 2 | 3 |
	                 +-----------+
	                 ^
	         +---+   |
	pointer: | * |---|
	         +---+
	length:  | 3 |
	         +---+
*/
	let c = vec![1, 2, 3];
/*	vec是一个stack上的数据结构，含有指针指向存放数据的内存
	            stack:       heap:
	            +---+     +-----------+---+
	pointer:    | * |---->| 1 | 2 | 3 |...|
	            +---+     +-----------+---+
	length:     | 3 |
	            +---+
	capacity:   | 4 |
	            +---+
*/

}

//🌰 关于try!
use std::fs::File;

fn foo() -> std::io::Result<()> {
    let f = try!(File::create("foo.txt"));
    Ok(())
}
//👇expand之后等于👇

fn foo2() -> std::io::Result<()> {
    let f = File::create("foo.txt");
    let f = match f {
        Ok(t) => t,
        Err(e) => return Err(e),
    };
    Ok(())
}

