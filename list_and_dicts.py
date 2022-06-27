"""
En python, podemos tener estructuras de datos mucho más complejas, las cuales serían
listas y diccionarios anidados, los cuales nos abren una gran brecha de oportunidades a
la hora de programar.
"""

def run():
    my_list = [1, "Helo", True, 4.5] #Single list and dictionary
    my_dict = {
        "first_name": "Jafet",
        "last_name": "Pintle"
    }

    super_list = [ #List of dictionaries
        {"first_name": "Jafet","last_name": "Pintle"},
        {"first_name": "Juan","last_name": "Rodriguez"},
        {"first_name": "Jesus","last_name": "Gonzalez"},
        {"first_name": "Karla","last_name": "Romero"}
    ]
    
    super_dict = { #Dictionary of list
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-5,30,4],
        "floating_nums":[1.1,4.5,6.43]
    }
    #Print my super list
    for dict in super_list:
        print(dict["first_name"], "-" , dict["last_name"])

    #Print my super dictionary
    for key,value in super_dict.items(): #list .items() return a list of tuple pairs
        print(key, "-", value)


if __name__ == "__main__":
    run()