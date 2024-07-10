# """
# The hex encoded string:
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

# ... has been XOR'd against a single character. Find the key, decrypt the message.

# Devise some method for "scoring" a piece of English plaintext. 
# Character frequency is a good metric. Evaluate each output and choose the one with the best score.
# """

import string

def valid(char):
    valid_list = set(string.ascii_letters+"'\" ?.\n-:#$_"+"0123456789")
    return char in valid_list

def single_byte_xor(input_byte,char_value):
    return bytes([b^char_value for b in input_byte])

def test_keys_and_decrypt(cipher:bytes):
    possible_text= {}
    for key in range(256):
        decrypted_cipher = single_byte_xor(cipher,key)
        decrypted_text = ''.join(chr(b) for b in decrypted_cipher)
        
        if all(valid(char) for char in decrypted_text):
            possible_text[key]=decrypted_text
            
    return possible_text

if __name__ == "__main__":
    raw = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    cipher_text = bytes.fromhex(raw)
    results = test_keys_and_decrypt(cipher_text)
    for key, text in results.items():
        print(f"key: {key}, Decrypted Text: {text}")