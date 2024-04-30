"""
Elgamal DS

Select prime q
Aplha=primitiveRoot(q)
1<Xa<q-1
Ya=((alpha)^Xa)modq

PrivateKey->Xa
PublicKey->{q,alpha,Ya}

m=H(m) 0<=m<=q-1

1<=k<=q-1 and gcd(k,q-1)=1

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

p = 67
g = 5

x = random.randint(2, p - 2)
y = pow(g, x, p)

message = input("Enter message: ")

k = random.randint(2, p - 2)
while math.gcd(k, p - 1) != 1:
    k = random.randint(2, p - 2)

s1 = pow(g, k, p)
S2 = [(pow(k, -1, p - 1) * (ord(m) - x * s1)) % (p - 1) for m in message]

print(s1)
print(S2)

v1 = [pow(g, ord(m), p) for m in message]
v2 = [(pow(y, s1, p) * pow(s1, s2, p)) % p for s2 in S2]

if v1 == v2:  
    print("Valid")
else:
    print("Invalid")
