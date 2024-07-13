"""
CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages, despite the fact that a block cipher 
natively only transforms individual blocks.

In CBC mode, each ciphertext block is added to the next plaintext block before the next call to the cipher core.

The first plaintext block, which has no associated previous ciphertext block, is added to a "fake 0th ciphertext block" called 
the initialization vector, or IV.

Implement CBC mode by hand by taking the ECB function you wrote earlier, making it encrypt instead of decrypt 
(verify this by decrypting whatever you encrypt to test), and using your XOR function from the previous exercise to combine them.

/data/10.txt is intelligible (somewhat) when CBC decrypted against "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c)
"""


import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


import sys
import os
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
from Set1.challenge7 import decrypt_aes
from Set1.challenge2 import byte_xor


def cbc_decrypt(ciphertext, key, IV):
    plaintext = b''
    previous_block = IV
    for i in range(0, len(ciphertext), AES.block_size):
        block = ciphertext[i: i+AES.block_size]
        decrypted_block = decrypt_aes(block, key)
        xored_block = byte_xor(decrypted_block, previous_block)
        plaintext += xored_block
        previous_block = block
    return unpad(plaintext, AES.block_size)

if __name__ == "__main__":
    file_path = r'C:\Users\Ripple\Desktop\Cryptopals\Cryptopals\data\10.txt'
    with open(file_path, 'rb') as f:
        ciphertext = f.read().strip()

    ciphertext = base64.b64decode(ciphertext)
    key = b'YELLOW SUBMARINE'  
    iv = b'\x00' * 16  # 16-byte IV of all ASCII 0
    print(cbc_decrypt(ciphertext, key, iv).decode('utf-8', errors='ignore'))
    
