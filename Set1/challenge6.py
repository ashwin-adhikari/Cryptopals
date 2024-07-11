"""
The file ./06.txt has been base64 encoded, after being encrypted with repeating-key XOR.
Challenge : To decrypt it.

Algorithm:
1. Read the Encrypted File
    First we may need to decode the file to get encrypted data.

2. Hamming Distance Function
    Hamming distance tells how many bits are different between two pieces of data.
    For example, comparing "this is a test" and "wokka wokka!!!" gives a Hamming distance of 37.

3. Guessing the key length(KEYSIZE)
    we guess the length in range  2 to 40.
    For each keysize we compare pieces of encrypted data to see how different they are using the hamming distance
    We normalize this distance by dividing by KEYSIZE
    The KEYSIZE with smallest normalized distance is likely the correct one.

4. Break Cipher into blocks
    once we have best KEYSIZE we break entire encrypted data into chunks of this length.
    This means if KEYSIZE is 4, we divide the data into chunks of 4 bytes each.

5. Transpose the Blocks
    We then rearrange these chunks. Instead of looking at each chunk as a whole, we group the first byte of each chunk together, the second byte of each chunk together, and so on.

6. Solve Each Block
    Each of these new groups (transposed blocks) is treated as if it was encrypted by a single character XOR.
    We already know how to solve single-character XOR by trying all possible characters and seeing which one makes the most sense in English.

7. Combine the Key Bytes
    After solving each transposed block, we get a single character key for each block.
    Combining these characters gives us the full repeating key used for encryption.

8. Decrypt the Ciphertext
    Finally, we use this key to decrypt the entire encrypted data to get the original message.

"""
"""
Set 1, Challenge 6
"""


import base64
from challenge3 import single_byte_xor
from challenge5 import repeating_xor
from itertools import combinations

def hamming_dist(str1, str2):
    assert len(str1) == len(str2)
    return sum(bin(byte1 ^ byte2).count("1") for byte1, byte2 in zip(str1, str2))


max_keysize = 40
def find_keysize(ciphertext):
    distances = []
    for keysize in range(2, max_keysize+1):
        chunks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext),keysize)] 
        pairs = list(combinations(chunks[:4], 2))
        # combination() function creates combination of the elements
        # if chunks[:4] = [A, B, C, D] => combination would be [(A,B), (A,C), (A,D), (B,C),(C,D)]
        # if we used zip them it would generate [(A,B), (B,C), (C,D)] 
        distance = sum(hamming_dist(a, b) for a, b in pairs)
        # each chunk's hamming distance is computed
        normalized_distance = distance / keysize
        distances.append((keysize, normalized_distance))
        # mormalized distance is appended to list
    # it returns min value of 0th element ie keysize after referencing minimum value of 1st element ie normalized distance  
    return min(distances, key=lambda x: x[1])[0]

    

def break_into_blocks(ciphertext, keysize):
    return [ciphertext[i:i+keysize] for i in range(0, len(ciphertext),keysize)]

def transpose_blocks(blocks,keysize):
    transposed = [] 
    for i in range(keysize):
        transposed_block = b''.join([block[i:i+1] for block in blocks if len(block) > i])
        transposed.append(transposed_block)
    return transposed

def decrypt_single_char_xor(block):
    best_score = float('-inf')
    best_key = 0

    for candidate_key in range(256):
        decrypted_message = single_byte_xor(block, candidate_key)
        score = score_text(decrypted_message)

        if score > best_score:
            best_score = score
            best_key = candidate_key
        
    return best_key

def score_text(text):
    frequency = { 'a' :  8.167,  'b' : 1.492, 'c' : 2.782, 'd' : 4.253,
                'e' : 12.702,  'f' : 2.228, 'g' : 2.015, 'h' : 6.094,
                'i' :  6.966,  'j' : 0.153, 'k' : 0.772, 'l' : 4.025,
                'm' :  2.406,  'n' : 6.749, 'o' : 7.507, 'p' : 1.929,
                'q' :  0.095,  'r' : 5.987, 's' : 6.327, 't' : 9.056,
                'u' :  2.758,  'v' : 0.978, 'w' : 2.360, 'x' : 0.150,
                'y' :  1.974,  'z' : 0.074, ' ' : 15 }
    return sum([frequency.get(chr(byte), 0) for byte in text.lower()])



if __name__ == "__main__":
    assert hamming_dist(b'this is a test', b'wokka wokka!!!') == 37
    file_path = r'C:\Users\Ripple\Desktop\Cryptopals\Cryptopals\Set1\06.txt'
    with open(file_path,'r') as f:
        ciphertext_base64 = f.read().strip()

    ciphertext = base64.b64decode(ciphertext_base64.replace("\n",""))# Decode the base64 encoded content to get the ciphertext

    keysize = find_keysize(ciphertext) # find the best Keysizze
    print(f"best keysize: {keysize}")

    blocks = break_into_blocks(ciphertext,keysize) 
    # break into blocks of the best KEYSIZE

    transposed_blocks = transpose_blocks(blocks,keysize) #transpose the blocks

    key = bytes([decrypt_single_char_xor(block) for block in transposed_blocks])  # Find the key by solving each transposed block
   
    decrypted_message = repeating_xor(ciphertext,key)
    print("key:", key.decode())
    print("Decrypted Message: ")
    print(decrypted_message.decode())

