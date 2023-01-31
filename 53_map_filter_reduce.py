# def cube(x):
#     return x * x * x

# print( cube(2))


li = [2,3,4,5,6,7,9]

# Map mathod take two parameter first is an function and second is operation

# newli = list(map(cube , li))

# We can also use lamda function as an function .....

newli = list(map(lambda x : x * x * x  , li))
print(newli)

# FILTER 

def filter_function(a):
    return a > 4

newfilter = list(filter(filter_function , li))

print(newfilter)

# REDUCE FUnction .....

import functools
from functools import reduce

def sum(x,y):
    return x+y

number = [2,3,4,5,6,5]

newNum = reduce(sum ,number)
print(newNum)