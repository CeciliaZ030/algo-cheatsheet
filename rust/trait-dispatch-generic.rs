use std::ops::Mul;
use std::marker::Copy;

//基本

trait Foo {
    fn method(&self) -> String;
}
impl Foo for u8 {
    fn method(&self) -> String { format!("u8: {}", *self) }
}

impl Foo for String {
    fn method(&self) -> String { format!("string: {}", *self) }
}

//这个叫做：Static Dispatch
//Rust will create a special version of do_something() for both u8 and String, and then replace the call sites with calls to these specialized functions. 
//搞了这个 wrapper 之后相当于 do_something 可以 takein 多个类的输入值
fn do_something<T: Foo>(x: T) {
    x.method();
    //只要x是一个impl了Foo trait的类
    //就能保证x有method()这个函数
}

//Trait Object & Dhnamic Dispatch
//这个更骚
fn do_something2(x: &Foo) {
    x.method();
}
/**
Trait objects, like &Foo or Box<Foo>, 
are normal values that store a value of any type that implements the given trait,
where the precise type can only be known at runtime.
所以 Dynamic

&Foo
Box<Foo>
&x as &Foo

为什么要用 pointer 来造 Trait Object？
	关于这个 Obj 我们只知道他 impl 这个 Trait，不知道多大
	所以 do_something2(x: &Foo) 的时候一定要用 pointer

**/



fn main() {

    let x = 5u8;
    let y = "Hello".to_string();

    do_something2(&x as &Foo);
    do_something2(&y as &Foo);
    do_something(x);
    do_something(y);

    let a = field::<u64> {
    	p: 9u64
    };
    call_mul(a);
}

#[derive(Debug)]
struct field<T> {
	p: T
}

trait FP<T>
where
	T: Mul + Copy,
{
	fn mul(&self, other: T) -> <T as Mul>::Output;
}


// impl<T, U> FP<U> for field<T>
// where
// 	T: Mul, U: MUl
// {
// 	fn mul(&self, other: U) -> <T as Mul>::Output {
// 		let some_root = self.p * other;
		//不允许你通过Generic糊弄过去，它就是不让你乘两个不一样的type
		//因为 u32 * u64 这种就是不允许的，你必须自己impl
// 		some_root
// 	}
// }

impl<T> FP<T> for field<T>
where
	T: Mul + Copy,
{
	fn mul(&self, other: T) -> <T as Mul>::Output {
		let some_root = self.p * other;
		some_root
	}
}
//我的天这个太复杂
//	1. declare trate 的时候T就要 Copy + Mul
//	2. return <T as Mul>::Output 大概output是std::ops::Mul中的type Output
//	3. impl 中的 T 也要 Copy + Mul，这样 fn mul 里面才能直接 self * other
//	4. 他就是不许你在不同的type直接进行unsafe操作，同时自己称乘自己也unsafe所以也要 Copy

impl FP<u32> for field<u64> {
	fn mul(&self, other: u32) -> u32 {
		let some_root = (self.p as u32) * other;
		some_root
	}
}

//具体 impl 只能像上面那样对每种类各搞一遍

fn call_mul<T: FP<u32>>(x: T) {
	x.mul(7u32);
}

//骚操作

pub trait Foo2 {
	type Output;
	fn foo(&self) -> <Self as Foo2> :: Output;
}

struct Bar;

impl Foo2 for isize {
	type Output = usize;
	fn foo(&self) -> usize {42}
}

fn baz<I: Foo2<Output = Bar>>(x: &<I as Foo2>::Output) {
	unimplemented!();
}

fn baz2<I>(x: &<I as Foo2>::Output) where I: Foo2<Output=Bar> {}

/*
人家真正的乘法是这样操作的
用 Macro 写 impl 的码
直接一个 mul_impl! { usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 f32 f64 }
涵盖所有数据结构


#[lang = "mul"]
#[stable(feature = "rust1", since = "1.0.0")]
#[rustc_on_unimplemented(
    message = "cannot multiply `{Rhs}` to `{Self}`",
    label = "no implementation for `{Self} * {Rhs}`"
)]
#[doc(alias = "*")]
pub trait Mul<Rhs = Self> {
    /// The resulting type after applying the `*` operator.
    #[stable(feature = "rust1", since = "1.0.0")]
    type Output;

    /// Performs the `*` operation.
    #[must_use]
    #[stable(feature = "rust1", since = "1.0.0")]
    fn mul(self, rhs: Rhs) -> Self::Output;
}

macro_rules! mul_impl {
    ($($t:ty)*) => ($(
        #[stable(feature = "rust1", since = "1.0.0")]
        impl Mul for $t {
            type Output = $t;

            #[inline]
            #[rustc_inherit_overflow_checks]
            fn mul(self, other: $t) -> $t { self * other }
        }

        forward_ref_binop! { impl Mul, mul for $t, $t }
    )*)
}

mul_impl! { usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 f32 f64 }

*/



