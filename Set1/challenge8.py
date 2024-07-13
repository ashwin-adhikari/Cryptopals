"""
In 08.txt file are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; 
the same 16 byte plaintext block will always produce the same 16 byte ciphertext.
"""


def detect_ecb_from_file(ciphertexts):
    for ciphertext in ciphertexts:
        ciphertext = bytes.fromhex(ciphertext)
        blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
        
        for i in range(len(blocks)):
            for j in range(i+1, len(blocks)):
                if blocks[i]==blocks[j]:
                    print("Repeating block: ", blocks[i].hex())
                    print("Hex Value: ", ciphertext.hex())
                    exit(0)


if __name__ == "__main__":
    filepath =  r'C:\Users\Ripple\Desktop\Cryptopals\Cryptopals\Set1\08.txt'
    with open(filepath,'r') as f:
        ciphertexts = f.readlines()
        ciphertexts = [line.strip() for line in ciphertexts]  
    
    print(detect_ecb_from_file(ciphertexts))

