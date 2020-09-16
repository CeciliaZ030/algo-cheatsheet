use std::io::{self, BufReader, BufRead};
use std::fs::File;
use std::collections::HashSet;


fn main() {
    //bit_reverse();
    let mut my_vec = (0..512).collect::<Vec<u32>>();
    let mut my_vec2:Vec<u64> = vec![1;50];

    //println!("{:?}", my_vec);
    bench_inplace_bitreverse(&mut my_vec.clone());
    bit_reverse_out(&my_vec);

    //test_ref_iter(&mut my_vec2);
}

fn test_ref_iter(a: &mut Vec<u64>){
    a.iter_mut().for_each(|i| *i = *i * 6u64);
    println!("{:?}", a);
}

fn read_input(input : &str)  -> io::Result<()> {
    let f = File::open("outfile.txt")?;
    let f = BufReader::new(f);

    let mut v: Vec<u64> = Vec::new();

    for line in f.lines() {
        println!("hello world");
        for i in line.unwrap().split(","){
            v.push(i.trim().parse::<u64>().unwrap());
        }
        
    }
    println!("{:?}", v[0]);
    bit_reverse();

    Ok(())
}

fn bit_reverse() {
    
    let L = 32;
    let L_bitNum = ((L as f64).log2().trunc() as u32);

    for i in 0..L {
        let mut i_rev = 0;
        for j in 0..L_bitNum {
            if (i & (1 << j)) > 0 {
                i_rev |= 1 << ((L_bitNum - 1) - j);   
            }
        }
        println!("{:?}, {}", i, i_rev);
    }
}

fn bit_reverse_out(a: &Vec<u32>) -> Vec<u32> {
    
    let L = a.len();
    let L_bitNum = ((L as f64).log2().trunc() as u32);

    let mut b = Vec::new();

    for i in 0..L {
        let mut i_rev = 0;
        for j in 0..L_bitNum {
            if (i & (1 << j)) > 0 {
                i_rev |= 1 << ((L_bitNum - 1) - j);   
            }
        }
        b.push(a[i_rev]);
        //println!("{:?}, {}", i, i_rev);
    }
    println!("ouplace {:?}", b);
    b
}

pub fn bench_inplace_bitreverse(a: &mut Vec<u32>) {

    let L = a.len();
    let mut j = 0;
    for i in 0..L {
        if j > i {
            a.swap(i, j);
        }
        let mut mask = L >> 1;
        while j & mask != 0 {
            j &= !mask;
            mask >>= 1;
        }
        j |= mask;
    }

    println!("inplace {:?}", a);
}
