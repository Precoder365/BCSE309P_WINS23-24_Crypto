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

def generate_private_key(q):
    return random.randint(2, q - 2)

def generate_public_key(q, alpha, private_key):
    return pow(alpha, private_key, q)

def compute_shared_secret(public_key, private_key, q):
    return pow(public_key, private_key, q)

q = 23
alpha = 5

# Alice generates her private key and public key
alice_private_key = generate_private_key(q)
alice_public_key = generate_public_key(q, alpha, alice_private_key)

# Bob generates his private key and public key
bob_private_key = generate_private_key(q)
bob_public_key = generate_public_key(q, alpha, bob_private_key)

# Alice and Bob compute their shared secret
alice_shared_secret = compute_shared_secret(bob_public_key, alice_private_key, q)
bob_shared_secret = compute_shared_secret(alice_public_key, bob_private_key, q)

# Verify if the shared secrets match
key_exchanged_successfully = alice_shared_secret == bob_shared_secret

print("Prime (q):", q)
print("Primitive Root (alpha):", alpha)
print("Alice's Private Key:", alice_private_key)
print("Alice's Public Key:", alice_public_key)
print("Bob's Private Key:", bob_private_key)
print("Bob's Public Key:", bob_public_key)
print("Alice's Shared Secret:", alice_shared_secret)
print("Bob's Shared Secret:", bob_shared_secret)
print("Key Exchanged Successfully?", key_exchanged_successfully)
