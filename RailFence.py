def rail_fence_encrypt(text, rails):
    rail_list = [''] * rails

    rail_index = 0
    direction = 1

    for char in text:
        rail_list[rail_index] += char
        rail_index += direction
        if rail_index == rails - 1 or rail_index == 0:
            direction *= -1

    encrypted_text = ''.join(rail_list)
    return encrypted_text

def rail_fence_decrypt(ciphertext, rails):
    rail_list = [''] * rails

    rail_index = 0
    direction = 1

    rail_lengths = [0] * rails
    for i in range(len(ciphertext)):
        rail_lengths[rail_index] += 1
        rail_index += direction
        if rail_index == rails - 1 or rail_index == 0:
            direction *= -1

    rail_index = 0
    char_index = 0

    for i in range(len(ciphertext)):
        rail_list[rail_index] += ciphertext[i]
        char_index += 1
        if char_index == rail_lengths[rail_index]:
            rail_index += 1
            char_index = 0

    original_text = ''
    for i in range(rails):
        original_text += rail_list[i]

    return original_text

plaintext = "meeting postponed"
rails = 2
encrypted_text = rail_fence_encrypt(plaintext, rails)
print("Encrypted:", encrypted_text)

decrypted_text = rail_fence_decrypt(encrypted_text, rails)
print("Decrypted:", decrypted_text)
