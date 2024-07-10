"""
Find the single character XOR from 
04.txt

"""

from challenge3 import single_byte_xor

with open('./04.txt','r') as f:
   
    decrypted_text={}

    for line in f:
        ciphertext = bytes.fromhex(line.strip())
        decrypt = single_byte_xor(cipher=ciphertext)

        if decrypt:
            decrypted_text[line]=decrypt  
    print(decrypted_text)