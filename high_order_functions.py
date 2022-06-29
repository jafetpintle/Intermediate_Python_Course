def run():

    my_list = [1,4,5,6,9,13,19,21]
    print("List: "+str(my_list))

    #Using filter
    #Filter get 2 parameters,-> (Lambda function, Iterable), 
    odd = list(filter(lambda x: x%2 != 0, my_list))
    print("Odd numbers with filter: "+str(odd))

    #Using MAP
    #Pow all the numbers to the square
    square = list(map(lambda x: x**2, my_list))
    print("Square numbers with MAP: "+str(square))

    #Using REDUCE
    #We need to import reduce function
    from functools import reduce
    #Sum all the elements of the list
    sum = reduce(lambda a,b: a+b, my_list)
    print("Sum of all the numbers with REDUCE: "+str(sum))

if __name__ == "__main__":
    run()