"""
**An ECB/CBC detection oracle**

Now that you have ECB and CBC working:
Write a function to generate a random AES key; that's just 16 random bytes.
Write a function that encrypts data under an unknown key --- that is, a function that generates a random key and encrypts under it.

The function should look like:
encryption_oracle(your-input)
=> [MEANINGLESS JIBBER JABBER]

Under the hood, have the function append 5-10 bytes (count chosen randomly) before the plaintext and 5-10 bytes after the plaintext.

Now, have the function choose to encrypt under ECB 1/2 the time, and under CBC the other half (just use random IVs each time for CBC). 
Use rand(2) to decide which to use.

Detect the block cipher mode the function is using each time. You should end up with a piece of code that, 
pointed at a block box that might be encrypting ECB or CBC, tells you which one is happening.
"""


import os
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encrypt_data_with_mode(data, key_size):
    key = os.urandom(key_size)
    cipher = AES.new(key, AES.MODE_CBC)
    append_before = os.urandom(random.randint(5,10))
    append_after = os.urandom(random.randint(5,10))
    data = append_before + data + append_after

    padded_data = pad(data, AES.block_size)

    if random.randint(0, 1) == 0:
        mode = 'ECB'
        cipher = AES.new(key, AES.MODE_ECB)
        iv = None
        encrypted_data = cipher.encrypt(padded_data)
        return mode, key, iv, encrypted_data
    else:
        mode= 'CBC'
        iv = os.urandom(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(padded_data)
        return mode, key, iv, encrypted_data

def detect_encryption(encrypted_data):
    blocks = [encrypted_data[i:i+AES.block_size] for i in range(0, len(encrypted_data), AES.block_size)]

    if len(blocks) != len(set(blocks)):
        return 'ECB'
    else:
        return 'CBC'


if __name__ == "__main__":
    plaintext= b'An ECB/CBC detection oracle'
    mode, key, iv, encrypted_data = encrypt_data_with_mode(plaintext,16)
    detected_mode = detect_encryption(encrypted_data)

    print(f"Actual mode: {mode}")
    print(f"Detected mode: {detected_mode}")
    print(f"AES key: {key.hex()}")
    if iv:
        print(f"Initialization vector: {iv.hex()}")
    print(f"Encrypted Data: {encrypted_data.hex()}")

