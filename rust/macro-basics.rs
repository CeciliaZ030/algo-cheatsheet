//Macros
//宏的机制是在预编译阶段对已经定义的宏进行替换或者展开, 即：把宏按照名称替换成宏的内容

/*
*	Function-like procedural macros
*	
*	Use ! to invoke, unhygienic because the output token stream was simply written inline to the code
*	it's affected by external items and also affects external imports.
*/


//🌰1 自己定义一波vec命名为vac
macro_rules! vac {
    ( $( $x:expr ),* ) => {					//* 代表 vac![1,2,....] 后面可重复多次
        {
            let mut temp_vec = Vec::new();
            $(
                temp_vec.push($x);
            )*								//此处又来 * 故每看到一个 $x 就要 temp_vec.push($x);
            temp_vec
        }
    };
}
/*
在一个匹配器中，每一个元变量都有一个片段分类符（fragment specifier），确定它匹配的哪种句法。

ident：一个标识符。例如：x，foo
path：一个受限的名字。例如：T::SpecialA
expr：一个表达式。例如：2 + 2；if true then { 1 } else { 2 }；f(42)
ty：一个类型。例如：i32；Vec<(char, String)>；&T
pat：一个模式。例如：Some(t)；(17, 'a')；_
stmt：一个单独语句。例如：let x = 3
block：一个大括号界定的语句序列，或者一个表达式。例如：{ log(error, "hi"); return 12; }
item：一个项。例如：fn foo() { }，struct Bar
meta：一个“元数据项”，可以在属性中找到。例如：cfg(target_os = "windows")
tt：一个单独的记号树
*/

/** 👌
*	左侧可以是任何语句，但是$e必须是tokenTree中定义的东西，代表intake的变量
*	右边 => 要 match 到实质的 rust code
**/
macro_rules! foo {
    (x ~ $e:expr) => (println!("mode X: {}", $e));
    (y -> $e:expr) => (println!("mode Y: {}", $e));
}

//🌰2 骚操作
macro_rules! o_O {
    ($
    	($x:expr; [ $( $y:expr ),* ]);*	
    ) => {
        &[ $($( $x + $y ),*),* ]		//(x1; [y11, y12, ...], x2; [y21, y22, ...],...
    }									//返回 [x1+y11, x1+y12,....], [x2+y21, x2+y22,....]
}

/* 🙅‍♂️
macro_rules! gg {
    () => (let x = 3;);
}
因为宏不知道expand时会不会与compile-time的环境命名相冲，比如之前已经有个x
*/
//👌
macro_rules! not_gg {
    ($v:ident) => (let $v = 3;);
    //命名一定要pass进去
}

//🌰3 Recursive Macro
#[allow(unused_must_use)]
macro_rules! write_html {
    ($w:expr, ) => (());

    ($w:expr, $e:tt) => (write!($w, "{}", $e));

    ($w:expr, $tag:ident [ $($inner:tt)* ] $($rest:tt)*) => {{
        write!($w, "<{}>", stringify!($tag));
        write_html!($w, $($inner)*);
        write!($w, "</{}>", stringify!($tag));
        write_html!($w, $($rest)*);
    }};
}

fn main() {

	//🌰1
	let x: Vec<u32> = vac![1, 2, 3];
	let y: Vec<u32> = {
	    let mut temp_vec = Vec::new();
	    temp_vec.push(1);
	    temp_vec.push(2);
	    temp_vec.push(3);
	    temp_vec
	};
	assert_eq!(x, y);

	//👌
	foo!(y -> 3);
	foo!(x ~ 8);
	/*
	foo!(z -> 5); 🙅‍♂️
	foo!(y ~ 8); 🙅‍♂️
	因为宏没有定义过 z 或者y ~ 
	*/

	//🌰2
	let o_0 = o_O!(10; [1, 2, 3];
        		   20; [4, 5, 6]);
	println!("{:?}", o_0);

	//🌰3
	use std::fmt::Write;
    let mut out = String::new();

    write_html!(&mut out,
        html[
            head[title["Macros guide"]]
            body[h1["Macros are the best!"]]
        ]);
    println!("{:?}", out);
	
}


/*🌰4	BigUint中的宏调用

macro_rules! impl_to_biguint {
    ($T:ty, $from_ty:path) => {
        impl ToBigUint for $T {
            #[inline]
            fn to_biguint(&self) -> Option<BigUint> {
                $from_ty(*self)
            }
        }

        impl IntoBigUint for $T {
            #[inline]
            fn into_biguint(self) -> Option<BigUint> {
                $from_ty(self)
            }
        }
    };
}

impl_to_biguint!(i8, FromPrimitive::from_i8);

👇相当于替换成对i8的实现👇

impl ToBigUint for i8 {
	#[inline]
	fn to_biguint(&self) -> Option<BigUint>{
		FromPrimitive::from_isize($self)
	}
}
impl IntoBigUint for i8 {
    #[inline]
    fn into_biguint(self) -> Option<BigUint> {
        FromPrimitive::from_isize(self)
    }
}

*/
