#[derive(Debug)]
struct Foo;

#[derive(Debug, Copy, Clone)]
struct Bar<T> {
	field: T
}

fn main(){
	let x = Foo;
	let y = x;
	/*
	println!("{:?}", x); 	🙅‍♂️
					 ^ value borrowed here after move
	*/
	let x = Bar::<i32>{
		field: 5i32
	};
	let y = x;
	println!("{:?}", x);	//👌

}

/*

What's the difference between Copy and Clone?

	For example, the implementation of Clone for String needs to copy the pointed-to string buffer in the heap. 
	A simple bitwise copy of String values would merely copy the pointer
	leading to a double free down the line. 
	For this reason, String is Clone but not Copy.

*/

struct Cat<T>(T);
struct Dog<T: ?Sized>(T);

//👌
struct i32_Dog(Dog<i32>);
struct i32_Cat(Cat<i32>);
struct i32Arr_Dog(Dog<[i32]>);
/*
🙅‍♂️
struct i32Arr_Cat(Cat<[i32]>);
因为 Dog 是 ?Sized 所以我们知道它可有可无固定大小
然而 Cat 里面一定要是个 Static Sized 数据结构
*/

trait CatT {}
trait DogT: Sized {}

struct Animal;
impl CatT for Animal {}
impl DogT for Animal {}

const c: &dyn CatT = &Animal; //👌 注意 main 外面不能用 let
/*
const d: &dyn DogT = &Animal; //🙅‍♂️ 因为 DogT 有 Sized，就不能搞成 Trait Obj 了
*/
