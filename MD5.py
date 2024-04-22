import hashlib

def md5_hash(message):
    md5 = hashlib.md5()
    md5.update(message.encode('utf-8'))
    return md5.hexdigest()

plaintext = input("Enter the plaintext: ")

hashcode = md5_hash(plaintext)
print("MD5 Hash:", hashcode)
