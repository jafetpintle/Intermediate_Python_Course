import math
from re import I


def run():
    #Saving only numbers that no are divisibles by 3 in a dictionary
    # dict = {}
    # for i in range(1,101):
    #     if(i%3 !=0):
    #         dict.update({i : i**3}) #Other way is dict[i] = i***3

    #Using list comprehension
    dict = {i: i**3 for i in range(1,101) if (i%3 != 0)}
    #print(dict)

    """
    Challenge: Use a dictionary comprehension to sabe de first 1000 numbers with their squares root as values
    """
    print("\n******************\nCHALLENGE\n******************\n")
    dict_challenge = {i: math.sqrt(i) for i in range(1,1001)}
    print(dict_challenge)




if __name__ == "__main__":
    run()