"""
RSA

Select 2 large nos p and q
n=p*q
phi(n)=(p-1)*(q-1)
1<e<phi(n) and gcd(phi(n),e))=1
edmodphi(n)=1 => d=(e^-1)modphi(n)

Public key={e,n}
Private key={d,n}

S=(M^d)modn

To verify:
M'=(S^e)modn

if M'===M then valid
Else not
"""

import random
import math

def generate_keypair():
    p = 17
    q = 23
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    while True:
        e = random.randint(2, phi - 1)
        if math.gcd(phi, e) == 1:
            break
    
    d = pow(e,-1, phi)
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

def sign_message(message, private_key):
    d, n = private_key
    signature = pow(message, d, n)
    return signature

def verify_signature(message, signature, public_key):
    e, n = public_key
    decrypted_msg = pow(signature, e, n)
    # print("Here",decrypted_msg)
    return decrypted_msg == message

public_key, private_key = generate_keypair()
message = 123
signature = sign_message(message, private_key)
valid_signature = verify_signature(message, signature, public_key)

print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)
print("Message:", message)
print("Signature:", signature)
print("Is Signature Valid?", valid_signature)
