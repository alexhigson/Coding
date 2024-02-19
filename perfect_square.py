# function to determine whether an input integer is a perfect square

def is_square(n):
    import math
    if n < 0:
        return False
    else:
        sqrt = math.sqrt(n)
        return sqrt.is_integer()

print(is_square(3600))