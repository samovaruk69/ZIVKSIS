import os

def crypt(dir):
    import pyAesCrypt
    password = input("Enter pass")
    bufferSize = 512 * 1024
    pyAesCrypt.decryptFile(str(dir),str(os.path.splitext(dir)[0]),password,bufferSize)
    print("file crypted")


dir = input("Enter file name")
crypt(dir)