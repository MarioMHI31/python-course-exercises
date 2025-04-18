import string
def criptare(message,key):
    chestii_posibile=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation+" "
    print(len(chestii_posibile))
    mesaj_criptat=""
    for letter in message:
        if chestii_posibile.index(letter)+key > len(chestii_posibile)-1:
            mesaj_criptat+=chestii_posibile[(chestii_posibile.index(letter)+key)%len(chestii_posibile)]
        else:
            mesaj_criptat+=chestii_posibile[chestii_posibile.index(letter)+key]
    return mesaj_criptat
"""
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

"""
print(criptare("cana noua",96))
