use std::any::type_name;

fn type_of<T>(_: T) -> &'static str {
    type_name::<T>()
}

fn main(){

	let a : i64 = 99;
	let b = a as i64;
	let c: i32 = 3;
	let d = c as u64;

	println!("{}, {}, {}, {}", type_of(a), type_of(b), type_of(c), type_of(d));

	let d = (a + b) % c;
	println!("{:?}", type_of(d));

}
