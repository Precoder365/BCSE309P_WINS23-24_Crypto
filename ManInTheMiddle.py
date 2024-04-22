import random

def generate_private_key(q):
    return random.randint(2, q - 2)

def generate_public_key(q, alpha, private_key):
    return pow(alpha, private_key, q)

def compute_shared_secret(public_key, private_key, q):
    return pow(public_key, private_key, q)

q = 27
alpha = 5

# Attacker generates its private key and public key
attacker_private_key = generate_private_key(q)
attacker_public_key = generate_public_key(q, alpha, attacker_private_key)

# Alice generates her private key and public key
alice_private_key = generate_private_key(q)
alice_public_key = generate_public_key(q, alpha, alice_private_key)

# Bob generates his private key and public key
bob_private_key = generate_private_key(q)
bob_public_key = generate_public_key(q, alpha, bob_private_key)

# Attacker intercepts Alice's public key and sends its own public key to Bob
alice_public_key_attacker = attacker_public_key

# Attacker intercepts Bob's public key and sends its own public key to Alice
bob_public_key_attacker = attacker_public_key

# Alice and Attacker compute their shared secret
alice_shared_secret_attacker = compute_shared_secret(alice_public_key_attacker, attacker_private_key, q)

# Bob and Attacker compute their shared secret
bob_shared_secret_attacker = compute_shared_secret(bob_public_key_attacker, attacker_private_key, q)

print("Prime (q):", q)
print("Primitive Root (alpha):", alpha)
print("Attacker's Private Key:", attacker_private_key)
print("Attacker's Public Key:", attacker_public_key)
print("Alice's Private Key:", alice_private_key)
print("Alice's Public Key (Intercepted by Attacker):", alice_public_key_attacker)
print("Bob's Private Key:", bob_private_key)
print("Bob's Public Key (Intercepted by Attacker):", bob_public_key_attacker)
print("Attacker's Shared Secret with Alice:", alice_shared_secret_attacker)
print("Attacker's Shared Secret with Bob:", bob_shared_secret_attacker)
