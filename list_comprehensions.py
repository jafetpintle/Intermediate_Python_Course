"""
List comprehensions es una contrucción sintátca para crear una lista
basada en listas existentes.
"""

from random import randrange


def run():
    #Simple form to make a list of squares
    # squares = []
    # for i in range(1 , 101) :
    #     if(i % 3 != 0):
    #         squares.append(i**2)

    #List of squares using list comprehension
    squares = [i**2 for i in range(1,101) if i%3 != 0]
    #STRUCTURE[ element = Cada elemento que se agregará a la lista
    #           for element in iterable = Ciclo del cual se extraeran elementos de otra lista o element iterable
    #           if condition] = Condicion para filtrar los elementos del ciclo
    #print(squares)

    """
    Challenge: Using list comprehension, make a list of all multiplies of 4 that are also multiples of
    6 and 9 up to 5 digits
    """

    #Using module equals to 36 because 36 es the least common multiple
    square_challenge = [i for i in range(1,100000) if  i%36== 0]
    print(square_challenge)   
    

if __name__ == "__main__":
    run()