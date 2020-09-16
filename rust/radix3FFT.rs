fn main() {

/**		input 		**/

	let P = 433u128; //4610415792919412737u128;
	let r = 150u128; //2230453091198852918u128;

	let mut arr: Vec<u128> = Vec::new();
	for i in 0..9 {
		arr.push(i as u128);
	}


/**		foward 		**/


	let L = arr.len();
	let mut w_matrix: Vec<u128> = Vec::new();
	for i in 0..L {
		w_matrix.push(r.modpow(&(i as u128), &P));	
	}
	inplace_bitreverse(&mut arr);
	radix3_DFT_omega(&mut arr, &P, &w_matrix);
	println!("\ntransform {:?}", arr);
	let transformed = arr.clone();

/**		backword 		**/

	inplace_bitreverse(&mut arr);
	let mut w_matrix_: Vec<u128> = Vec::new();
	let inv_w = r.modpow(&(P - 2u128), &P);
	for i in 0..L {
		w_matrix_.push(inv_w.modpow(&(i as u128), &P));	
	}
	

	radix3_DFT_omega(&mut arr, &P, &w_matrix_);
	let L_inverse = (L as u128).modpow(&(P - 2u128), &P);
	for i in 0..L {
		arr[i] = &arr[i] * &L_inverse % P;
	}
	println!("inversed {:?}", arr);

// ======================================================
	
	//Reconstruct with Lagrange on the first 5 points

	let mut w_slice = vec![0u128; 11];
	for i in 0..11 {
		w_slice[i] = i as u128;
	}
	let mut roots = w_matrix.clone();
	roots.push(5u128);	
	println!("\nlagrange {:?}", lagrange_interpolation_field(&w_matrix, &transformed, &roots, &P));
	
// ======================================================
	
	//Brute force multiplication
	let mut res: Vec<u128> = Vec::new();
	for i in 0..w_matrix.len() {
		let mut s = 0u128;
		for j in 0..arr.len() {
			let w: u128 = 7u128.pow((i * j) as u32);
				println!("{:?}", w);
 
			s += arr[j] * w;
			//println!("	{:?}",  w );
		}
		res.push(s);
	}
	println!("res not field {:?}", res);
	println!("{:?}", lagrange_interpolation(&w_matrix, &transformed, &roots));

	//Brute force multiplication
	let mut res: Vec<u128> = Vec::new();
	for i in 0..roots.len() {
		let mut s = 0;
		for j in 0..arr.len() {
			//let mut w = r.modpow(&(i as u128), &P);
			let w = roots[i].modpow(&(j as u128), &P);
			s += arr[j] * w % P;
			//println!("	{:?}",  w );
		}
		res.push(s % P);
	}
	println!("res {:?}", res);

}
fn lagrange_interpolation_field (points: &Vec<u128>, values: &Vec<u128>, roots: &Vec<u128>, P: &u128) -> Vec<u128> {
	
	let L = points.len();

	let mut denominators: Vec<u128> = Vec::new();
	for i in 0..L {
		let mut d = 1;
		for j in 0..L {
			if i != j {
				if points[i] > points[j]{
					d *= (points[i] - points[j]);
				} else {
					d *= (points[j] - points[i]);
				}
				//d %= P;
			}
		}
		d = (d as u128).modpow(&(P - 2u128), &P);
		denominators.push(d);
	}
	println!("demon {:?}", denominators);

	let mut evals: Vec<u128> = Vec::new();
	for r in roots {
		let mut eval = 0u128;
		for i in 0..L {
			let mut li = 1u128;
			for j in 0..L {
				if i != j {
					if r > &points[j] {
						li *= (r - points[j]);
					} else {
						li *= (points[j] -r);
					}
					//li %= P;
				}
			}
			li = li * denominators[i];
			eval += li * values[i];
		}
		evals.push(eval % P);
	}
	
	evals
}

fn lagrange_interpolation (points: &Vec<u128>, values: &Vec<u128>, roots: &Vec<u128>) -> Vec<u128> {
	
	let L = points.len();

	let mut denominators: Vec<u128> = Vec::new();
	for i in 0..L {
		let mut d = 1;
		for j in 0..L {
			if i != j {
				d *= (points[i] - points[j]);
			}
		}
		denominators.push(d);
	}

	let mut evals: Vec<u128> = Vec::new();
	for r in roots {
		let mut eval = 0u128;
		for i in 0..L {
			let mut li = 1u128;
			for j in 0..L {
				if i != j {
					li *= (r - points[j]);
				}
			}
			li /= denominators[i];
			eval += li * values[i];
		}
		evals.push(eval);
	}
	
	evals
}

pub fn radix3_DFT_omega(a: &mut Vec<u128>, P: &u128, w_matrix: &Vec<u128>) {
	
	let L = a.len();
	let w = w_matrix[L/3];
	let w_sqr = w_matrix[L/3*2];
	//println!("\n{:?}, {}", w, w_sqr);

	let mut i = 1;
	while i < L {
		let jump = 3 * i;
		let stride = L/jump;
		//println!("{}", i);
		for j in 0..i {
			//println!("	factor {:?}, {}", (w_matrix[j * stride] as f64).log2(), (w_matrix[2 * j * stride] as f64).log2());
			let mut pair = j;
			while pair < L {
				let (x, y, z) = (a[pair],
								a[pair + i] * w_matrix[j * stride] % P,
								a[pair + 2 * i] * w_matrix[2 * j * stride] %P);
				//println!("{:?}, {}, {}", x, y, z);
				a[pair] 	  	= (x + y + z) % P;
				a[pair + i]   	= (x % P + w * y % P + w_sqr * z % P) % P;
                a[pair + 2 * i] = (x % P + w_sqr * y % P + w * z % P) % P;
				
				pair += jump;
			}
		}
		i = jump;
	}
}

pub fn DFT_radix3_(data: &mut Vec<u128>, P: &u128, r: &u128) -> Vec<u128> {
    
    //radix3 bit reverse
    let mut t = 0usize;
    let L = data.len();
    let tri_L = trigits_len(L - 1);
    let mut trigits = vec![0; tri_L];

    for i in 0..L {
        if t > i {
            data.swap(t, i);
        }
        for j in 0..tri_L {
            if trigits[j] < 2 {
                trigits[j] += 1;
                t += 3usize.pow((tri_L-j-1)as u32);
                break;
            } else {
                trigits[j] = 0;
                t -= 2 * 3usize.pow((tri_L-j-1)as u32);
            }
        }
    }
    //println!("{:?}", data);

    //radix3 DFT
    let mut step = 1;
    let w = r;
    let tri_w = r.modpow(&((L/3) as u128), P);
    let tri_w_sq = tri_w * tri_w % P;
	//println!("{:?}, {}",tri_w, tri_w_sq);

    while step < L {
        let jump = 3 * step;
        let factor_stride = w.modpow(&((L/step/3) as u128), P);
        //println!("{} s {}", step, factor_stride);

        let mut factor = 1;
        for group in 0usize..step {
            let factor_sq = factor * factor % P;
            //println!("	factor {:?}, {}", factor, factor_sq);

            let mut pair = group;
            while pair < data.len() {
                let (x, y, z) = (data[pair],
                                 data[pair + step] * factor % P,
                                 data[pair + 2 * step] * factor_sq % P);

                data[pair] = (x + y + z) % P;
                data[pair + step] = (x % P + tri_w * y % P+ tri_w_sq * z % P) % P;
                data[pair + 2 * step] = (x % P + tri_w_sq * y % P+ tri_w * z % P) % P;
                pair += jump;
            }
            factor = factor * factor_stride % P;
        }
        step = jump;
    }
    data.clone()
}

fn round_to_pow3(n: usize) -> usize {
	let mut v = 1;
    while v < n {
        v *= 3;
    }
    v
}

pub fn trigits_len(n: usize) -> usize {
    let mut result = 1;
    let mut value = 3;
    while value < n + 1 {
        result += 1;
        value *= 3;
    }
    result
}


pub fn inplace_bitreverse(data: &mut Vec<u128>) {
    //radix3 bit reverse
    let mut t = 0usize;
    let L = data.len();
    let tri_L = trigits_len(L - 1);
    let mut trigits = vec![0; tri_L];
    //println!("tri_L {:?}", tri_L);

    for i in 0..L {
        if t > i {
        	//println!("swap");
            data.swap(t, i);
        }
        for j in 0..tri_L {
            if trigits[j] < 2 {
                trigits[j] += 1;
                t += 3usize.pow((tri_L-j-1)as u32);
                break;
            } else {
                trigits[j] = 0;
                t -= 2 * 3usize.pow((tri_L-j-1)as u32);
            }

        }
        //println!("i {}, t {}, {:?}",i, t, trigits);
    }
    //println!("{:?}", data);
}

/** Arithmatic util **/

pub trait ModPow<T> {
    fn modpow(&self, exponent: &T, modulus: &T) -> T;
}

impl ModPow<u128> for u128 {
    /// Panics if the modulus is zero.
    fn modpow(&self, exponent: &Self, modulus: &Self) -> Self {

        assert!(*modulus != 0u128, "divide by zero!");
        if exponent == &0u128 {
            return 1
        }

        let mut base = self % modulus;
        let mut exp = exponent.clone();
        let mut res = 1;

        while exp > 0 {
            if exp % 2u128 == 1 {
                res = res * base % modulus;
            }
            exp >>= 1;
            base = base * base % modulus;
        }
        return res
    }
}