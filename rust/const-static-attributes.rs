//Const
/*
*	must annotate the type of a const.
*	Constants live for the entire lifetime of a program. 
*	More specifically, constants in Rust have no fixed address in memory. 
*	This is because they’re effectively inlined to each place that they’re used. References to the same constant are not necessarily guaranteed to refer to the same memory address for this reason.
*/

const N: i32 = 5;

//Static
/*
*	Rust provides a ‘global variable’ sort of facility in static items. 
*	They’re similar to constants, but static items aren’t inlined upon use. 
*	This means that there is only one instance for each value, and it’s at a fixed location in memory.
*/

static P: i32 = 5;
static mut M: i32 = 5;

fn main() {

	/* 	👌
	*	因为 M static，并不能搞ownership,所以不安全
	*	一个	tread 对其改动时别的thread也可以，需要弄一个 unsafe block
	*/
	unsafe {
	    M += 1;
	    println!("N: {}", M);
	}

	macos_only();
	needs_foo_or_bar();
}

//Attribute
/*
*	在编译阶段用于为编译提供更多描述信息
*	以便根据这些描述做出一些动态的选择和设置
*/

#[cfg(test)]		//cfg 条件编译 control conditional compilation
mod tests {			//$cargo test 或者用rustc 
					//$rustc const-static-attributes.rs --test
	#[test]
	fn it_works() {
		println!("Yeah!");
	}

	#[test]
	#[should_panic]
	fn check_two() {
		assert_eq!(2, 2);
	}

}

// The function is only included in the build when compiling for macOS
#[cfg(target_os = "macos")]
fn macos_only() {
  println!("macOS only");
}
/*
🙅‍♂️
#[cfg(target_os = "windows")]
fn windows_only(){....}
此时在若在main里call该函数会找不到，因为没有compiled
*/

// 		$rustc const-static-attributes.rs --cfg foo
//或者  $rustc const-static-attributes.rs --cfg bar
#[cfg(any(foo, bar))]
fn needs_foo_or_bar() {
  // ...
}

// This function is only included when compiling for a unixish OS with a 32-bit
// architecture
#[cfg(all(unix, target_pointer_width = "32"))]
fn on_32bit_unix() {
  // ...
}

// $rustc const-static-attributes.rs 			此时compile
// $rustc const-static-attributes.rs --cfg foo 	此时不compile
#[cfg(not(foo))]
fn needs_not_foo() {
  // ...
}

//关于 cfg_attr
/*
#![cfg_attr(test, feature(test, anything_else_only_relevant_for_tests))]
就是往后面加条件
*/


//Lint Check
/*
*	allow(C), deny(C), forbid(C), warn(C)
*	就是编译的时候查什么不查什么
*/
#[warn(missing_docs)]
pub mod m2{
    #[allow(missing_docs)]
    pub mod nested {
        // Missing documentation is ignored here
        pub fn undocumented_one() -> i32 { 1 }

        // Missing documentation signals a warning here,
        // despite the allow above.
        #[warn(missing_docs)]
        pub fn undocumented_two() -> i32 { 2 }
    }

    // Missing documentation signals a warning here
    pub fn undocumented_too() -> i32 { 3 }
}



















