def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_length = len(key)
    for i in range(len(plaintext)):
        shift = ord(key[i % key_length]) - 65
        if plaintext[i].isalpha():
            if plaintext[i].islower():
                ciphertext += chr(((ord(plaintext[i]) - 97 + shift) % 26) + 97)
            else:
                ciphertext += chr(((ord(plaintext[i]) - 65 + shift) % 26) + 65)
        else:
            ciphertext += plaintext[i]
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        shift = ord(key[i % key_length]) - 65
        if ciphertext[i].isalpha():
            if ciphertext[i].islower():
                plaintext += chr(((ord(ciphertext[i]) - 97 - shift) % 26) + 97)
            else:
                plaintext += chr(((ord(ciphertext[i]) - 65 - shift) % 26) + 65)
        else:
            plaintext += ciphertext[i]
    return plaintext

plaintext = "HELLO WORLD"
key = "KEY"
encrypted_text = vigenere_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
