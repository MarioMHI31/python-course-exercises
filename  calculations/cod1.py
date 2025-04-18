# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


def numarul_de_litere_si_cifre(sentence):
    numar_litere=0
    numar_cifre=0
    for char in sentence:
        if char.isdigit():
            numar_cifre+=1
        elif char.isalpha():
            numar_litere+=1
    return f"numarul cifrelor este: {numar_cifre},numarul literelor este: {numar_litere}"
print(numarul_de_litere_si_cifre("Mario are 19 ani."))

