"""
Elgamal
Choose a large prime number p and a generator g.
1 < x < p - 1, private key=x
y = (g^x)modp, public key=y

1 < k < p - 1
c1 = (g^k)modp
c2 = (M*y^k)modp
ciphertext is (c1, c2)

s = (c1^x)modp
M = (c2*s^{-1})modp
"""

import random

import random

p=257
g=5

x=random.randint(2,p-2)
y=pow(g,x,p)

message=input("Enter the message to encrypt: ")

# Encryption

k=random.randint(2,p-2)
c1=pow(g,k,p)
C2=[(ord(m)*pow(y,k,p))%p for m in message]

print(c1)
print(C2)

# Decryption

s = pow(c1, x, p)
mod_inverse_s = pow(s, -1, p)
decrypted_msg = ''.join([chr((c2 * mod_inverse_s) % p) for c2 in C2])
print("Decrypted message:", decrypted_msg)
