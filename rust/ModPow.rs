trait ModPow<T> {
	fn modpow(&self, exponent: &T, modulus: &T) -> T;
}

impl ModPow<u32> for u32 {
	/// Panics if the modulus is zero.
	fn modpow(&self, exponent: &Self, modulus: &Self) -> Self {

	    assert!(*modulus != 0u32, "divide by zero!");
	    if exponent == &0u32 {
	        return 1
	    }

	    let mut base = self % modulus;
	    let mut exp = exponent.clone();
	    let mut res = 1;

	    while exp > 0 {
	    	if exp % 2u32 == 1 {
	    		res = res * base % modulus;
	    	}
	    	exp >>= 1;
	    	base = base * base % modulus;
	    	println!("exp {:?}, res {:?}, base {:?}", exp, res, base);
	    }
	    return res
	}
}