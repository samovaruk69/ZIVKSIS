import os

def crypt(dir):
    import pyAesCrypt
    password = input("Enter pass")
    bufferSize = 512 * 1024
    pyAesCrypt.encryptFile(str(dir),str(dir)+".aes",password,bufferSize)
    print("file crypted")


dir = input("Enter file name")
crypt(dir)