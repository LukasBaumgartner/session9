def add_numbers(a, b, c=0):
    """
    Adds 2 or 3 numbers
    :param a: first number
    :param b: second number
    :param c: third number
    :return: result of addition of two/three numbers
    """
    return a + b + c

print(add_numbers(1, 2, 3))
print(add_numbers(5, 7, 3))

# a function can call itself (recursive function)
def factorial(n):
    """
    Calculates the factorial of n
    :param n: number
    :return:
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def rec_factorial(n):
    if n==0:
        return 1
    else:
        return n * rec_factorial(n-1)

print(factorial(6))
print(rec_factorial(6))

# functions can call other functions

def bond_greeting(first, last, lang="esp"):
    """
    Does the bond greeting
    :param first: first name
    :param last: last name
    :param lang: language
    :return: the greeting
    """
    if lang == "en":
        return english_greeting(first, last)
    elif lang == "fr":
        return french_greeting(first, last)
    elif lang == "esp":
        return spanish_greeting(first, last)

def english_greeting(first, last):
    return f"The name is: {last}, {first} {last}"

def french_greeting(first, last):
    return f"Je mappelle: Le{last}, {first} Le{last}"

def spanish_greeting(first, last):
    return f"Me llamo: {last}ito, {first}isito {last}ito"

print(bond_greeting("James", "Bond", "esp"))