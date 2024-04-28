from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def encrypt_AES(key, plaintext):
    iv = b'\x00' * 16  # You should use a cryptographically secure random IV in practice

    # Create AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Get a padder
    padder = padding.PKCS7(algorithms.AES.block_size).padder()

    # Pad the plaintext
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Create the encryptor and encrypt the plaintext
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    return iv + ciphertext

def decrypt_AES(key, ciphertext):
    # Extract the initialization vector and ciphertext
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]

    # Create AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Create the decryptor and decrypt the ciphertext
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Get an unpadder
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()

    # Unpad the plaintext
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext

password = b"mysecretpassword"
plaintext = b"Hello, AES!"
print("Plaintext:", plaintext)

key = password[:32]

encrypted_data = encrypt_AES(key, plaintext)
print("Encrypted:", encrypted_data)

decrypted_data = decrypt_AES(key, encrypted_data)
print("Decrypted:", decrypted_data.decode('utf-8'))
