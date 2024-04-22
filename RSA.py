""" RSA - Rivest Shamir Aldeman
Public key -> Known to all users in the N/W (encryption)
Private key -> Kept secret (decryption)

Select 2 large nos p and q
n=p*q
phi(n)=(p-1)*(q-1)
1<e<phi(n) and gcd(phi(n),e))=1
edmodphi(n)=1 => d=(e^-1)modphi(n)

Public key={e,n}
Private key={d,n}

Encryption: C=(M^e)modn
Decryption: M=(C^d)modn"""

import random
import math

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while math.gcd(phi, e) != 1:
        e = random.randrange(2, phi)
    
    d = pow(e, -1, phi)
    
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)

p = 61
q = 53
public_key, private_key = generate_keypair(p, q)
print("Public key:", public_key)
print("Private key:", private_key)

message = "Pren here"
print("Original message:", message)

encrypted_msg = encrypt(public_key, message)
print("Encrypted message:", encrypted_msg)

decrypted_msg = decrypt(private_key, encrypted_msg)
print("Decrypted message:", decrypted_msg)
