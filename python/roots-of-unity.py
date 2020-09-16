#For the input, please enter a prime number.
#Definition of primitive roots of unity: An integer A (1 ≤ A ≤ P–1) is a primitive root of unity (mod P) if A^K is not congruent to 1 (mod P) for 1 ≤ K ≤ P–2. (P is a prime number)
#I hope you enjoy this code ^^
import math


def is_prime(n):
    if n < 0 or n == 0:
        return False
    else:
        for i in range (2,int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True


def primitive_root_of_unity(p):
    if is_prime(p):
        primitive_roots = list(map(lambda x: str(x), list(filter(lambda x: all([i != 1 for i in [x**k%p for k in range (1,p-1)]]),[a for a in range (1,p)]))))
        if len(primitive_roots) == 1:
            print ("Primitive root of unity (mod {0}) is {1}.".format(p, primitive_roots[0]))
        else:
            print ("Primitive roots of unity (mod {0}) are {1}.".format(p,", ".join(primitive_roots)))
            a = [int(r) ** 4 % p for r in primitive_roots]
            print(1 in a)
    else:
        print ("Please enter a prime number.")


p = int(23)

primitive_root_of_unity(p)