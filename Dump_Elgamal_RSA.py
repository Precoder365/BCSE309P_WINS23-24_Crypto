# ----------------------- RSA ------------------------

import random
import math

p=61
q=53

n=p*q

phi=(p-1)*(q-1)

e=random.randint(1,phi-1)
while(math.gcd(e,phi)!=1):
    e=random.randint(1,phi-1)

d=pow(e,-1,phi)

message=input("Enter message to encrypt: ")

# Encryption

cipher=[pow(ord(m),e,n) for m in message]
print(cipher)

# Decryption

plaintext=''.join([chr(pow(c,d,n)) for c in cipher])
print(plaintext)

# ------------------ RSA DS-----------------------------------

import random
import math

p=61
q=53

n=p*q

phi=(p-1)*(q-1)

e=random.randint(1,phi-1)
while(math.gcd(e,phi)!=1):
    e=random.randint(1,phi-1)

d=pow(e,-1,phi)

message=input("Enter message to encrypt: ")

# Signature

sign=[pow(ord(m),d,n) for m in message]
print(sign)

# Decryption

md=''.join([chr(pow(s,e,n)) for s in sign])
print(md)

if(md==message):
    print("Valid")
else:
    print("Not valid")

# ------------------- Elgamal ---------------------

import random

p=23
g=5

x=random.randint(2,p-2)
y=pow(g,x,p)

m=int(input("Enter the message to encrypt: "))

# Encryption

k=random.randint(2,p-2)
c1=pow(g,k,p)
c2=(m*pow(y,k))%p

# Decryption

s=pow(c1,x,p)
decrypted_msg=(c2*pow(s,-1,p))%p
print(decrypted_msg)

# ------------- Elgamal DS ---------------

import random
import math

p = 67
g = 5

x = random.randint(2, p - 2)
y = pow(g, x, p)

m = int(input("Enter message: "))

k = random.randint(2, p - 2)
while math.gcd(k, p - 1) != 1:
    k = random.randint(2, p - 2)

s1 = pow(g, k, p)
s2 = (pow(k, -1, p - 1) * (m - x * s1)) % (p - 1)

v1 = pow(g, m, p)
v2 = (pow(y, s1, p) * pow(s1, s2, p)) % p

if v1 == v2:
    print("Valid")
else:
    print("Not valid")
