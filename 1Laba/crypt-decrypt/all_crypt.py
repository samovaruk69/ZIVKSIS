import os
import pyAesCrypt


def crypt(dir):
    password = input("Введите пароль: ")
    bufferSize = 512 * 1024
    pyAesCrypt.encryptFile(str(dir),str(dir)+".aes",password,bufferSize)
    print("file crypted")


def decrypt(dir):
    password = input("Введите пароль: ")
    bufferSize = 512 * 1024
    pyAesCrypt.decryptFile(str(dir),str(os.path.splitext(dir)[0]),password,bufferSize)
    print("file decrypted")

 
dir = input("Введине имя файла: ")
enterDo = input("Выберите действие для файла: crypt или decrypt: ")
if enterDo=='crypt':
    crypt(dir)
if enterDo=='decrypt':
    decrypt(dir)



