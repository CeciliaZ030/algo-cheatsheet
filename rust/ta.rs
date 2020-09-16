fn main() {

	let points: Vec<u128> = vec![1, 2, 3, 4];
	let values: Vec<u128> = vec![1, 8, 27, 64];
	let P = 199u128;
	let mut roots: Vec<u128> = Vec::new();
	for i in 0..P {
		roots.push(i as u128);
	}
	let evals = lagrange_interpolation_field(points.clone(), values, roots, P);
	println!("field \n{:?}", evals);

	let points: Vec<i128> = vec![1, 2, 3, 4];
	let values: Vec<i128> = vec![1, 8, 27, 64];
	let mut roots: Vec<i128> = Vec::new();
	for i in 0..P {
		roots.push(i as i128);
	}
	let evals = lagrange_interpolation(points, values, roots);
	println!("regular \n{:?}", evals);

	//Brute force multiplication
	let mut res: Vec<u128> = Vec::new();
	for i in 0..P {
		res.push(i.pow(3u32) % P);
	}
	println!("plug in directly \n {:?}", res);

}

fn lagrange_interpolation (points: Vec<i128>, values: Vec<i128>, roots: Vec<i128>) -> Vec<i128> {
	
	let L = points.len();

	let mut denominators: Vec<i128> = Vec::new();
	for i in 0..L {
		let mut d = 1;
		for j in 0..L {
			if i != j {
				d *= points[i] - points[j];
			}
		}
		denominators.push(d);
	}

	let mut evals: Vec<i128> = Vec::new();
	for r in roots {
		let mut eval = 0i128;
		for i in 0..L {
			let mut li = 1i128;
			for j in 0..L {
				if i != j {
					li *= r - points[j];
				}
			}
			li /= denominators[i];
			eval += li * values[i];
		}
		evals.push(eval);
	}
	
	evals
}

fn lagrange_interpolation_field (points: Vec<u128>, values: Vec<u128>, roots: Vec<u128>, P: u128) -> Vec<u128> {
	
	let L = points.len();

	let mut denominators: Vec<u128> = Vec::new();
	for i in 0..L {
		let mut d = 1;
		for j in 0..L {
			if i != j {
				d *= points[i] + P - points[j];
				d %= P;
			}
		}
		d = (d as u128).modpow(&(P - 2u128), &P);
		denominators.push(d);
	}

	let mut evals: Vec<u128> = Vec::new();
	for r in roots {
		let mut eval = 0u128;
		for i in 0..L {
			let mut li = 1u128;
			for j in 0..L {
				if i != j {
					li *= r + P - points[j];
					li % P;
				}
			}
			li *= denominators[i] % P;
			eval += li * values[i] % P;
		}
		evals.push(eval % P);
	}
	
	evals
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
