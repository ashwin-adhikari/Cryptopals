"""
The string(HEX string):
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce a base64 encoded value for the string:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
"""

import base64

hex_str = str(input("Enter the hex value:"))
base64_str = base64.b64encode(bytes.fromhex(hex_str)).decode()
print("Base64 value:",base64_str)
