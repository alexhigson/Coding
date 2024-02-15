# code that returns the sum of the squares of a list of numbers

def square_sum(*args): # *args means you can pass in any number of arguments, so the list of numbers could be 1 or 100 
    result = sum(i**2 for i in args) # ** for a power
    print(result)
    return result
square_sum(1, 2, 3)