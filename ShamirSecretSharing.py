from sympy import nextprime
import random

def generate_polynomial_coeffs(secret, num_shares, prime):
    coeffs = [secret]
    for _ in range(num_shares - 1):
        coeffs.append(random.randint(0, prime - 1))
    return coeffs

def evaluate_polynomial(coeffs, x, prime):
    result = 0
    for coeff in reversed(coeffs):
        result = (result * x + coeff) % prime
    return result

def generate_shares(secret, num_shares, threshold):
    prime = nextprime(secret)
    coeffs = generate_polynomial_coeffs(secret, threshold, prime)
    shares = []
    for x in range(1, num_shares + 1):
        y = evaluate_polynomial(coeffs, x, prime)
        shares.append((x, y))
    return shares

def reconstruct_secret(shares, prime):
    x_values, y_values = zip(*shares)
    secret = 0
    for i, (x_i, y_i) in enumerate(shares):
        num = 1
        den = 1
        for j, (x_j, _) in enumerate(shares):
            if i != j:
                num *= -x_j
                den *= (x_i - x_j)
        lagrange_coeff = (y_i * num * pow(den, -1, prime)) % prime
        secret = (secret + lagrange_coeff) % prime
    return secret

secret = 42  
num_shares = 5  
threshold = 3  

shares = generate_shares(secret, num_shares, threshold)
print("Generated shares:")
for share in shares:
    print("Share:", share)

reconstructed_secret = reconstruct_secret(shares[:threshold], nextprime(secret))
print("Reconstructed secret:", reconstructed_secret)
