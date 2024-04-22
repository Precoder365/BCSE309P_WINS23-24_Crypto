import hashlib

def sha512_hash(plaintext):
    sha512_hash = hashlib.sha512()
    sha512_hash.update(plaintext.encode('utf-8'))
    return sha512_hash.hexdigest()

plaintext = input("Enter the plaintext: ")

hashcode = sha512_hash(plaintext)
print("SHA-512 Hashcode:", hashcode)
