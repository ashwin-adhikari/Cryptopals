"""
The Base64-encoded content 07.txt has been encrypted via AES-128 in ECB mode under the key

"YELLOW SUBMARINE".
(case-sensitive, without the quotes; exactly 16 characters; I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too).

Decrypt it. You know the key, after all.

Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.
"""
import base64
from Crypto.Cipher import AES

def decrypt_aes(cipher, key):
    data = AES.new(key, AES.MODE_ECB)
    return data.decrypt(cipher)

if __name__ == "__main__":
    filepath = r'C:\Users\Ripple\Desktop\Cryptopals\Cryptopals\data\07.txt'
    with open(filepath,'r') as f:
        cipher = base64.b64decode(f.read())
    
    key = b'YELLOW SUBMARINE'
    print(decrypt_aes(cipher,key).decode())
    
