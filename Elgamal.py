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

def generate_keypair(p, g):
    private_key = random.randint(1, p - 2)
    public_key = pow(g, private_key, p)
    
    return private_key, public_key

def encrypt(public_key, g, p, plaintext):
    k = random.randint(1, p - 2) 
    c1 = pow(g, k, p)
    c2 = (plaintext * pow(public_key, k, p)) % p
    
    return c1, c2

def decrypt(private_key, p, c1, c2):
    plaintext = (c2 * pow(pow(c1, private_key),-1, p)) % p
    return plaintext


p = 23  
g = 5   

private_key, public_key = generate_keypair(p, g)

print("Private key:", private_key)
print("Public key:", public_key)

plaintext = 7

c1, c2 = encrypt(public_key, g, p, plaintext)
print("Encrypted message:", (c1, c2))

decrypted_msg = decrypt(private_key, p, c1, c2)
print("Decrypted message:", decrypted_msg)
