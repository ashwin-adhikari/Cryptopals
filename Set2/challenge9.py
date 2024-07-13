"""
A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of plaintext into ciphertext. 
But we almost never want to transform a single block; we encrypt irregularly-sized messages.

One way we account for irregularly-sized messages is by padding, creating a plaintext that is an even multiple of the blocksize. 
The most popular padding scheme is called PKCS#7.

So: pad any block to a specific block length, by appending the number of bytes of padding to the end of the block. For instance,

"YELLOW SUBMARINE"
... padded to 20 bytes would be:

"YELLOW SUBMARINE\x04\x04\x04\x04"
"""

def pkcs7_padding(data, block_size):
    if len(data) < block_size:
    # this will add padding for string which are smaller than blocksize
        padding_length = block_size - (len(data) % block_size)
        padding = bytes(b'\x04' * padding_length)
    
        return data + padding
    else:
        return "Error"
    #this will add padding after the given block size if it doesn't encounter bytes,
    # if there are bytes then this will not replace bytes but add the padding after bytes end.
    # for e.g if block size is 10 the given string has 16byte so this will add padding after 10th byte upto 10 padding values.
    # but there are byte values upto 16th byte so after 16th byte it will add the padding values ==> b'YELLOW SUBMARINE\x04\x04\x04\x04'

if __name__ == "__main__":
    data = b'YELLOW SUBMARINE'
    block_size = 20
    output = pkcs7_padding(data,block_size)
    print(output)