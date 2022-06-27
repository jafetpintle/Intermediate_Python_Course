"""
List comprehensions es una contrucción sintátca para crear una lista
basada en listas existentes.
"""

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
    print(squares)

    
    
    

if __name__ == "__main__":
    run()