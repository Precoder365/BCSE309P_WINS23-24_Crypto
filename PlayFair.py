def prepare_input(text):
    text = text.replace(" ", "")
    text = text.upper()

    text = text.replace("J", "I") #J and I correspond to same pos

    pairs = []
    for i in range(0, len(text), 2):
        try:
            if text[i] == text[i + 1]:
                pairs.append(text[i] + "X")
                i-=1
            else:
                pairs.append(text[i] + text[i + 1])
        except IndexError:
            pairs.append(text[i] + "X")
    return pairs

def generate_table(key):
    table = [[''] * 5 for _ in range(5)]

    key = key.upper().replace("J", "I")

    ind = 0
    for i in range(5):
        for j in range(5):
            if ind < len(key):
                table[i][j] = key[ind]
                ind += 1
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    ind = 0
    for i in range(5):
        for j in range(5):
            if table[i][j] == '':
                while alphabet[ind] in key:
                    ind += 1
                table[i][j] = alphabet[ind]
                ind += 1
    
    return table

def find_letter(letter, table):
    for row in range(5):
        for col in range(5):
            if table[row][col] == letter:
                return row, col

def encrypt(text, key):
    pairs = prepare_input(text)
    table = generate_table(key)

    cipher = ""
    for pair in pairs:
        row1, col1 = find_letter(pair[0], table)
        row2, col2 = find_letter(pair[1], table)

        # If the letters are on the same row, replace them with the letters to their right, wrapping around to the left side if necessary
        if row1 == row2:
            cipher += table[row1][(col1 + 1) % 5]
            cipher += table[row2][(col2 + 1) % 5]
        # If the letters are on the same column, replace them with the letters below them, wrapping around to the top if necessary
        elif col1 == col2:
            cipher += table[(row1 + 1) % 5][col1]
            cipher += table[(row2 + 1) % 5][col2]
        # If the letters form a rectangle, replace them with the letters on the same row but at the other corners of the rectangle
        else:
            cipher += table[row1][col2]
            cipher += table[row2][col1]

    return cipher

def decrypt(text, key):
    pairs = prepare_input(text)
    table = generate_table(key)

    plaintext = ""
    for pair in pairs:
        row1, col1 = find_letter(pair[0], table)
        row2, col2 = find_letter(pair[1], table)

        # If the letters are on the same row, replace them with the letters to their left, wrapping around to the right side if necessary
        if row1 == row2:
            plaintext += table[row1][(col1 - 1) % 5]
            plaintext += table[row2][(col2 - 1) % 5]
        # If the letters are on the same column, replace them with the letters above them, wrapping around to the bottom if necessary
        elif col1 == col2:
            plaintext += table[(row1 - 1) % 5][col1]
            plaintext += table[(row2 - 1) % 5][col2]
        # If the letters form a rectangle, replace them with the letters on the same row but at the other corners of the rectangle
        else:
            plaintext += table[row1][col2]
            plaintext += table[row2][col1]

    return plaintext

key = "MONARCHY"
plaintext = "Substitution technique"
encrypted_text = encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text[:len(plaintext)-plaintext.count(' ')])
