import base64

def crypt_pictures(pict_name):
    image = open(pict_name, 'rb')
    image_read = image.read()
    image_64_encode = base64.encodebytes(image_read)
    image_64_encode_save = open('crypt_pict_64.jpg','wb')
    image_64_encode_save.write(image_64_encode)

def decrypt_pictures(pict_name_1):
    image1 = open(pict_name_1, 'rb')
    image_read1 = image1.read()
    res0 = base64.decodebytes(image_read1)
    res = open('decrypt_pict_64.jpg','wb')
    res.write(res0)

def crypt_page(page_name):
    page = open(page_name, 'rb')
    page_read = page.read()
    page_64_encode = base64.b64encode(page_read)
    page_64_encode_save = open('crypt_page_64.txt','wb')
    page_64_encode_save.write(page_64_encode)


def decrypt_page(page_name_1):
    page1 = open(page_name_1, 'rb')
    page_read1 = page1.read()
    res00 = base64.b64decode(page_read1)
    res1 = open('decrypt_page_64.txt','wb')
    res1.write(res00)

try:
    typ1 = input("Enter crypt or decrypt :")

    if typ1 == 'crypt':
        typ2 = input("Enter file type of crypt :")
        if typ2 == 'pictures':
            pict_name = input("Enter picture filename for crypt :")
            crypt_pictures(pict_name)
        elif typ2 == 'page':
            page_name = input("Enter page filename for crypt :")
            crypt_page(page_name)
        
    elif typ1 == 'decrypt':
        typ2 = input("Enter file type of crypt :")
        if typ2 == 'pictures':
            pict_name_1 = input("Enter pictures filename for decrypt :")
            decrypt_pictures(pict_name_1)
        elif typ2 == 'page':
            page_name_1 = input("Enter page filename for decrypt :")
            decrypt_page(page_name_1)


except IOError as identifier:
    print("Enter correct file name or type of crypt")
    pass

