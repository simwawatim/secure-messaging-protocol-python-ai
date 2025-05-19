from Crypto.Cipher import AES # type: ignore
import hashlib
import sys
import binascii

if (len(sys.argv) > 1):
    plaintext = (sys.argv[1])

if (len(sys.argv) > 2):
    password = (sys.argv[2])

    

