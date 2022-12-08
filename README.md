#Encrypter module

Custom Base58 coding/decoding module

#Module usage

Importing the module for Base 58 encoding and decoding
'''python
from encripter import Encripter
'''

#Encoding
Input:
'''python
from encripter import Encripter
encripter = Encripter()
text_to_encode = "Test string to encode"
text_encoded = encripter.b58encode(text_to_encode)
print(text_encoded)
'''

Output:
'''
6C11q3kb5UkAaE5hfb1WMZ78KUsEt
'''


#Decoding
Input:
'''python
from encripter import Encripter
encripter = Encripter()
text_to_decode = "6C11q3kb5UkAaE5hfb1WMZ78KUsEt"
text_decoded = encripter.b58decode(text_to_decode)
print(text_decoded)
'''

Output:
'''
Test string to encode
'''
