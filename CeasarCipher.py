def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

text = "Pren"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Encrypted:", encrypted_text)  
decrypted_text = caesar_decipher(encrypted_text, shift)
print("Decrypted:", decrypted_text)  
