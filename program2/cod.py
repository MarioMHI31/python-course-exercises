#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def gaseste_numere(numar1,numar2):
    numere=[]
    if type(numar1)==int and type(numar2)==int:
        for i in range(numar1, numar2 + 1):
            if i % 7 == 0 and i % 5 != 0:
                numere.append(i)
        return numere
    elif type(numar1)!=int:
        return f"Valoarea {numar1} este invalida."
    elif type(numar2)!=int:
        return f"Valoarea {numar2} este invalida."
print(gaseste_numere("2000",3200))