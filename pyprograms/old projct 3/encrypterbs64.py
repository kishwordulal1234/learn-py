import base64


def encrypter(w):
    finaal_text = base64.b64encode(w.encode())
    print(f" your final encrypted text {finaal_text}")


    
text_encrypt = input(" inter the text to encrypt ")
encrypter(text_encrypt)



def decrypter(k):
    decrypted_text = base64.b64decode(k)
    drrict = decrypted_text.decode()
    print(f"your final decrypted text is {drrict}")

to_decrypt = input("inter the text to decrypt ")
decrypter(to_decrypt)