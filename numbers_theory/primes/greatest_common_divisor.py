"""
from page 201 of comp prog handbook

gcd is the greatest number that divides both a and b


Euclid's algorithm:
    gcd(a,b) = gcm(b,a%b) 
    fox ex: gcd(24,36)



                 a*b
lcm(a,b) =  -------------
               gcd(a,b)
"""



def gcd(a : int,b: int) -> int:
    if b == 0: return a
    return gcd(b,a%b)


print(gcd(36,24))
