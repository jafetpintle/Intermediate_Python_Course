def run():
    #Saving only numbers that no are divisibles by 3 in a dictionary
    # dict = {}
    # for i in range(1,101):
    #     if(i%3 !=0):
    #         dict.update({i : i**3}) #Other way is dict[i] = i***3

    #Using list comprehension
    dict = {i: i**3 for i in range(1,101) if (i%3 != 0)}
    print(dict)

    




if __name__ == "__main__":
    run()