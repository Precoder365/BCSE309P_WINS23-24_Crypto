"""
Elgamal DS

Select prime q
Aplha=primitiveRoot(q)
1<Xa<q-1
Ya=((alpha)^Xa)modq

PrivateKey->Xa
PublicKey->{q,alpha,Ya}

m=H(m) 0<=m<=q-1

1<=k<=q-1 and gcd(k,q-1)=q-1

s1=(alpha^k)modq
s2=k^-1(m-Xa*s1)modq-1

(s1,s2)

To verify at other side:
v1=(alpha^m)modq
v2=(Ya^s1)*(s1^s2)modq

If v1==v2: Signature valid
Else: not
"""

import random
import math

def generate_private_key(q):
    return random.randint(2, q - 2)

def generate_public_key(q, alpha, private_key):
    return pow(alpha, private_key, q)

def generate_signature(q, alpha, private_key, message):
    while True:
        k = random.randint(2, q - 2)
        if math.gcd(k, q - 1) == 1:
            break

    s1 = pow(alpha, k, q)
    s2 = (pow(k, -1, q - 1) * (message - private_key * s1)) % (q - 1)
    
    return (s1, s2)

def verify_signature(q, alpha, public_key, message, signature):
    s1, s2 = signature
    v1 = pow(alpha, message, q)
    v2 = (pow(public_key, s1, q) * pow(s1, s2, q)) % q
    
    return v1 == v2

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

q = 23
alpha = 5

private_key = generate_private_key(q)
public_key = generate_public_key(q, alpha, private_key)

message = random.randint(0, q - 1)

signature = generate_signature(q, alpha, private_key, message)

valid_signature = verify_signature(q, alpha, public_key, message, signature)

print("Prime (q):", q)
print("Primitive Root (alpha):", alpha)
print("Private Key:", private_key)
print("Public Key:", public_key)
print("Message:", message)
print("Signature (s1, s2):", signature)
print("Is Signature Valid?", valid_signature)
