"""
En Python, una funcion lambda es una funcion anonima que carece de nombre.
"""
import string


def run():
    #Palindrome is the variable, this use a string and compare if it is a palindrome
    palindrome = lambda string: string == string[::-1]
    print(palindrome('ana'))


if __name__ == "__main__":
    run()