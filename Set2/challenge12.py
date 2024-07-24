"""
Step 1: Copy the Oracle Function and Modify it for ECB Encryption
Step 2: Discover the Block Size
Step 3: Detect ECB Mode
Step 4: Decrypt the Unknown String

"""
     
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
from os import urandom
from itertools import count

block_size = AES.block_size
key_size = 32

def pc7(b: bytes, block_size: int= 16) -> bytes:
    if block_size == 16:
        pad_len = block_size - (len(b) % block_size)
    else:
        pad_len = block_size - (len(b) % block_size)
    return b+ bytes([pad_len]) * pad_len

def make_oracle():
    _key = urandom(key_size)
    file_path = r'C:\Users\Ripple\Desktop\Cryptopals\Cryptopals\data\12.txt'
    with open(file_path, 'r') as f:
        _ciphertext = base64.b64decode(f.read())
    
    def oracle(plaintext: bytes) -> bytes:
        plaintext = pc7(plaintext + _ciphertext)
        cipher = AES.new(_key, AES.MODE_ECB)
        return cipher.encrypt(plaintext)
    
    return oracle

def find_block_size_and_postfix_length(enc) -> tuple[int, int]:
    block_size = None
    postfix_len = None

    l = len(enc(b"A"))
    for i in count(2):
        l2 = len(enc(b"A" * i))
        if l2 > l:
            block_size = l2 -l
            postfix_len = l -i
            break
    
    assert block_size is not None
    assert postfix_len is not None
    return block_size, postfix_len


def detect_ecb(oracle):
    ct = oracle(bytes(32))
    if ct[:16] == ct[16:32]:
        return True
    raise Exception("oh no!")

def bytes_to_chunks(b: bytes, chunk_size: int) -> list[bytes]:
    chunks = [b[ind:ind+chunk_size] for ind in range (0, len(b), chunk_size)]
    return chunks 

def guess_byte(prefix: bytes, target: bytes, oracle) -> bytes:
    for b in range(256):
        b = bytes([b])
        msg = prefix + b
        first_block = oracle(msg)[:16]
        if first_block == target:
            return b
    raise Exception("Oh no")

if __name__ == "__main__":
    oracle = make_oracle()
    block_size, postfix_len = find_block_size_and_postfix_length(oracle)
    print(f"{block_size =}")
    print(f"{postfix_len =}")
    assert block_size == AES.block_size

    assert detect_ecb(oracle)

    ciphertext = [bytes_to_chunks(oracle(bytes(15-n)), block_size) for n in range(16)]
    transposed = [block for blocks in zip(*ciphertext) for block in blocks]
    blocks_to_attack = transposed[:postfix_len]

    from time import sleep
    pt = bytes(15)
    for block in blocks_to_attack:
        pt += guess_byte(pt[-15:], block, oracle)
        print(pt[15:])
        sleep(0.1)
    pt = pt[15:]

    print("DONE")
    print(pt.decode())

