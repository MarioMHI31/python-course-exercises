def power(num,p):
    if not (type(num)==int or type(num)==float):
        return f"Valoarea {num} este invalida."

    elif not type(p)==int:
        return f"Valoarea aleasa pentru {power} este invalida."
    return num**p
# print(power("x",2))
print(power(10,2))