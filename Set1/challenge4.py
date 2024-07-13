"""
Find the single character XOR from 
04.txt

"""

from challenge3 import test_keys_and_decrypt
file_path = r'C:\Users\Ripple\Desktop\Cryptopals\Cryptopals\data\04.txt'
with open(file_path,'r') as f:
   
    decrypted_text={}

    for line in f:
        ciphertext = bytes.fromhex(line.strip())
        decrypt = test_keys_and_decrypt(cipher=ciphertext)

        if decrypt:
            decrypted_text[line]=decrypt  
    print(decrypted_text)