#import modules from directory
import sys
sys.path.append('elliptic_arithmetic')

from finite_field import PrimeGaloisField, FieldElement
from elliptic_curve import EllipticCurve, Point
from sign_verify import Signature, PrivateKey
import elliptic_curve
import random
import sign_verify

# secp256k1 elliptic curve equation: y² = x³ + 7

# Prime of the finite field
P: int = (
    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
)
field = PrimeGaloisField(prime=P)

# Elliptic curve parameters A and B of the curve : y² = x³ + Ax + B
A: int = 0
B: int = 7
secp256k1 = EllipticCurve(
    a=A,
    b=B,
    field=field
)
# Generator point of the abelian group 
G = Point(
    x=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
    y=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
    curve=secp256k1
)

# Order of the group generated by G, such that N * G = I
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141



#Point at infity
I = Point(x=None, y=None, curve=secp256k1)
elliptic_curve.I = I
elliptic_curve.elliptic_curve = secp256k1

#add N and G to sign_verify module
sign_verify.N = N
sign_verify.G = G

#tests


assert I == N * G

m = 255
key = PrivateKey(random.randint(1, N - 1))
pub = key.secret * G
sign = key.sign(m)
assert sign.verify(m, pub) == True
assert sign.verify(m+1, pub) == False




