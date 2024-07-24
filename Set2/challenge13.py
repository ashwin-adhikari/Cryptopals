from Crypto.Cipher import AES
from os import urandom
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def kv_parsing(kv_string):
    parsed_data = {}
    pairs = kv_string.split('&')
    for pair in pairs:
        key, value = pair.split('=')
        parsed_data[key] = value
    return parsed_data

def profile_for(email):
    sanitized_email= email.replace('&', '').replace('=', '')
    profile = {
        'email': sanitized_email,
        'uid': 10,
        'role': 'user'
    }
    encoded_profile = f"email={profile['email']}&uid={profile['uid']}&role={profile['role']}"
    return encoded_profile

def encrypt_profile(profile,key):
    
    cipher = AES.new(key, AES.MODE_ECB)
    profile_bytes = profile.encode('utf-8')
    padded_profile = pad(profile_bytes, AES.block_size)
    encrypted_profile = cipher.encrypt(padded_profile)
    return base64.b64encode(encrypted_profile).decode('utf-8')    

def decrypt_profile(encrypted_profile,key):
   
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_profile_bytes = base64.b64decode(encrypted_profile)
    decrypted_profile = cipher.decrypt(encrypted_profile_bytes)
    
    print(f"Decrypted Profile (Bytes): {decrypted_profile}")
    return unpad(decrypted_profile, AES.block_size).decode('utf-8')

def create_admin(key):
    key = get_random_bytes(16)
    email1 ="foo@bar.com"
    profile1= profile_for(email1)
    encrypted_profile1 = encrypt_profile(profile1,key)

    email2 = "foobar@admin"
    profile2 = profile_for(email2)
    encrypted_profile2 = encrypt_profile(profile2,key)

    encrypted_profile1 = base64.b64decode(encrypted_profile1)                                                  
    encrypted_profile2 = base64.b64decode(encrypted_profile2)                                                  

    block_size = AES.block_size
    blocks1 = [encrypted_profile1[i:i + block_size] for i in range(0, len(encrypted_profile1), block_size)]
    blocks2 = [encrypted_profile2[i:i + block_size] for i in range(0, len(encrypted_profile2), block_size)]

    manipulated_profile = blocks1[0] + blocks1[1] + blocks2[2] 
    manipulated_profile = base64.b64encode(manipulated_profile).decode('utf-8')

    decrypted_profile = decrypt_profile(manipulated_profile,key)
    return decrypted_profile

if __name__ == "__main__":
    key = get_random_bytes(16)
    kv_string = "foo=bar&baz=qux&zap=zazzle"
    parsed_data = kv_parsing(kv_string)
    print(f"Parsed Data: {parsed_data}")

    profile = profile_for("foo@bar.com")
    encrpted_profile = encrypt_profile(profile,key)
    print(f"Encrypted Profile: {encrpted_profile}")

    decrypted_profile = decrypt_profile(encrpted_profile,key)
    print(f"Decrypted Profile: {decrypted_profile}")

    admin_profile = create_admin(key)
    print(f"Admin Profile: {admin_profile}")