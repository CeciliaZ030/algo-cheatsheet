use rug::Integer;
use rug::{rand::RandState};
use std::collections::HashMap;

#[derive(Debug)]
struct PublicInfo {
	Gx: Integer,
	Gy: Integer,
	a: Integer,
	b: Integer,
	P: Integer,
}

fn main() {

    println!("Hello, world!");

	/*		Public Info		*/

    let Gx = "48439561293906451759052585252797914202762949526041747995844080717082404635286";
    let Gy = "36134250956749795798585127919587881956611106672985015071877198253568414405109";
    let a = "-3";
    let b = "41058363725152142129326129780047268409114441015993725554835256314039467401291";
    let P = "115792089210356248762697446949407573530086143415290314195533631308867097853951";


    // Package exampe for Operator Overloading

    let test = a.parse::<Integer>().unwrap();
    let c: Integer = test * -10;
	println!("Example \n 	{:?} multiplication", c);
	println!("	{:?} division floor", c.clone() / 4);
	println!("	{:?} square", c.clone().square());


    let publicInfo = PublicInfo {
    	Gx: Gx.parse::<Integer>().unwrap(),
		Gy: Gy.parse::<Integer>().unwrap(),
		a: a.parse::<Integer>().unwrap(),
		b: b.parse::<Integer>().unwrap(),
		P: P.parse::<Integer>().unwrap(),
    };
	println!("#bits of P {:?}", publicInfo.P.significant_bits());

	/*		Key Generation		*/

	// random private key
	let mut rand = RandState::new();
	let sk = Integer::from(100);//publicInfo.P.clone().random_below(&mut rand);
	//comput public key by Eliptic Curve addition
	let pk = EC_mul(&publicInfo, &sk);
	println!("sk {:?}, pk {:?}", sk, pk);




	let mut client_list: HashMap<Vec<u8>, String> = HashMap::new();
	client_list.insert(vec![1u8, 2u8], "shabi".to_string());
	client_list.insert(vec![1u8, 3u8], "zhizhang".to_string());
	client_list.insert(vec![1u8, 2u8], "laozai".to_string());
	println!("{:?}", client_list);



}

fn EC_mul(pi: &PublicInfo, sk: &Integer) -> (Integer, Integer) {

	let mut xR = pi.Gx.clone();
	let mut yR = pi.Gx.clone();
	let mut _sk = sk.clone();

	while _sk > 1 {

		let slope : Integer = (3 * xR.clone().square() + pi.a.clone()) / (2 * yR.clone());

		xR = slope.clone().square() - 2 * xR.clone();

		let diff = xR.clone() - yR.clone();
		yR = slope * diff - yR.clone();
		_sk -= 1;
	}

	return (xR, yR)
}









