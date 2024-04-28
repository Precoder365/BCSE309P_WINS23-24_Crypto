from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plain_text = pad(plain_text.encode(), DES.block_size)
    cipher_text = cipher.encrypt(padded_plain_text)
    return cipher_text

def des_decrypt(cipher_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(cipher_text)
    return unpad(decrypted_text, DES.block_size).decode()

plain_text = "This is a very long text that needs to be encrypted using DES. DES is a symmetric encryption algorithm. DES works on 64-bit blocks. DES has a key length of 56 bits. DES is not secure for modern applications."
key = get_random_bytes(8)

cipher_text = des_encrypt(plain_text, key)
print("Cipher text:", cipher_text)

decrypted_text = des_decrypt(cipher_text, key)
print("Decrypted text:", decrypted_text)
