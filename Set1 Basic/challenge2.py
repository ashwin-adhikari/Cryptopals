"""
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965

... should produce:

746865206b696420646f6e277420706c6179
"""

# hex1 = "1c0111001f010100061a024b53535009181c"
# hex2 = "686974207468652062756c6c277320657965"

# byte_object1 = bytes.fromhex(hex1)
# byte_object2 = bytes.fromhex(hex2)

# xor_result = bytearray(len(byte_object1))
# for i in range(len(byte_object1)):
#     xor_result[i] = byte_object1[i] ^ byte_object2[i]
 
# xor_result= bytes(xor_result)
# hex_result = xor_result.hex()
# print(hex_result)



def byte_xor(byte1:bytes, byte2:bytes)->bytes:
    xor_result = bytearray(len(byte1))
    for i in range(len(byte1)):
        xor_result[i]= byte1[i] ^ byte2[i]
    
    xor_result = bytes(xor_result)
    hex_result = xor_result.hex()
    return hex_result

if __name__ == "__main__":
    
    hex1 = input("Enter hex:")
    hex2 = input("Enter hex:")
    byte1=bytes.fromhex(hex1)
    byte2=bytes.fromhex(hex2)
    
    print(byte_xor(byte1=byte1,byte2=byte2))

