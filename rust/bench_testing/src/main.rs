#![feature(test)]

extern crate test;

pub fn add_two(a: i32) -> i32 {
    a + 2
}

pub fn inplace_bitreverse(a: &mut Vec<u32>) {

    let L = a.len();
    let L_bitNum = ((L as f64).log2().trunc() as u32);

    for i in 0..L/2 {
        let mut i_rev = 0;
        for j in 0..L_bitNum {
            if (i & (1 << j)) > 0 {
                i_rev |= 1 << ((L_bitNum - 1) - j);   
            }
        }
        let temp = a[i];
        a[i] = a[i_rev];
        a[i_rev] = temp;
    }
}


#[cfg(test)]
mod tests {
    use super::*;
    use test::Bencher;

    #[test]
    fn it_works() {
        assert_eq!(4, add_two(2));
    }

	//🌰
    #[bench]
    fn bench_add_two(b: &mut Bencher) {
        b.iter(|| add_two(2));
    }
/*

	🙅‍♂️ 	b.iter里的closure不能有变量
		(。。好无语)

    #[bench]
    fn bench_add_two(b: &mut Bencher) {
    	let x = 3;
        b.iter(|x| add_two(2));
    }
*/
	//🌰
	#[bench]
    fn bench_add_two_iter(b: &mut Bencher) {
        b.iter(|| {
		    let n = test::black_box(1000);	//循环的上限放在black_box里，确保代码不被optimize
		    (0..n).fold(0, |a, b| a ^ b)	//通过fold做循环
		})
    }

    #[bench]
    fn bench_inplace_bitreverse(b: &mut Bencher) {
    	let mut x = (0..32).collect::<Vec<u32>>();
        b.iter(|| {
		    inplace_bitreverse(test::black_box(&mut x));
		})
    }
}


fn main() {
	unimplemented!();
}