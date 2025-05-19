import os
import base64
from Crypto.Cipher import AES

def encrypt_aes_gcm(plain_text, key):
    nonce = os.urandom(12)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    cipher_text, tag = cipher.encrypt_and_digest(plain_text.encode('utf-8'))
    return {
        'nonce': base64.b64encode(nonce).decode('utf-8'),
        'cipher_text': base64.b64encode(cipher_text).decode('utf-8'),
        'tag': base64.b64encode(tag).decode('utf-8')
    }

def decrypt_aes_gcm(encrypted_data, key):
    nonce = base64.b64decode(encrypted_data['nonce'])
    cipher_text = base64.b64decode(encrypted_data['cipher_text'])
    tag = base64.b64decode(encrypted_data['tag'])
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plain_text = cipher.decrypt_and_verify(cipher_text, tag).decode('utf-8')
    return plain_text
