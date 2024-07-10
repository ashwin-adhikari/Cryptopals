# """
# The hex encoded string:
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

# ... has been XOR'd against a single character. Find the key, decrypt the message.

# Devise some method for "scoring" a piece of English plaintext. 
# Character frequency is a good metric. Evaluate each output and choose the one with the best score.
# """

import string

def valid(char):
    valid_list = string.ascii_letters+"'\" ?.\n-:#$_"+"0123456789"
    return char in valid_list

def single_byte_xor(cipher:bytes):
    possible_text= {}
    for key in range(256):
        decrypt_cipher = ''.join(chr(b ^ key) for b in cipher)
        if all(valid(char) for char in decrypt_cipher):
            possible_text[key]=decrypt_cipher
            
    return possible_text

if __name__ == "__main__":
    raw = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    cipher_text = bytes.fromhex(raw)
    print(single_byte_xor(cipher=cipher_text))