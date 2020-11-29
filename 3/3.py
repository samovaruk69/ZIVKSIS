from Crypto.Cipher.DES3 import DES3Mode
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass

Cipher = DES3.new(key,DES3.MODE_CFB)
plaintext = b'hello my best friend'
msg = Cipher.iv + Cipher.encrypt(plaintext)