# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
def main(parola):
    special_char="@#*"
    parole_valide=[]

    valid=False

    has_lowercase=False
    has_uppercase=False
    has_digit=False
    has_special_char=False

    if len(parola)>12 or len(parola)<6:
        return False
    for char in parola:
        if char.isupper():
            has_uppercase=True
        elif char.islower():
            has_lowercase=True
        elif char.isdigit():
            has_digit=True
        elif char in special_char:
            has_special_char=True
    if has_lowercase and has_uppercase and has_digit and has_special_char:
        return True
    return False
print(main("2w3E*"))