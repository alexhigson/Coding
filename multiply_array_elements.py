def grow(arr):
    product = 1
    for i in arr:
        product = product * i
    return product
print(grow([2, 3, 4]))