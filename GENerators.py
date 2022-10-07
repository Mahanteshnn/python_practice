# l=[1, 2, 3, 4]
# def func(a):
#     for num in a:
#         yield num **2
# print(list(func(l)))
#
# res=((num**2) for num in l)
# print(list(res))

#####################################3
# items=["flipkart",2021,"gmail",1.2,[1,2,3],2+3j,True]
# def func(a):
#     for item in a:
#         if isinstance(item,(int,float,complex,bool)):
#             yield item
# print(tuple(func(items)))
#########################################
# names=["bob","steve","alex","maya","john"]
# def func(a):
#     for word in a:
#         if len(word) % 2 !=0:
#             yield word[::-1]
# print(list(func(names)))
###########################################
# items=["flipkart",2021,"gmail",1.2,[1,2,3],2+3j,True]
# def func(a):
#     for item in a:
#         if isinstance(item,(int,float,complex,bool)):
#             yield  str(item)[::-1]
#         else:
#             yield item
# print(list(func(items)))
##############################################
# import math
# PI=math.pi
# print(PI)
#
# def func(num):
#     for i in range(num):
#         yield round(PI,i)
# print(list(func(6)))
#
# #expression
# res=(round(PI,i) for i in range(6))
# print(list(res))

###############################################
# A FUNCTION TAKES VARIABLE NUMBER OF POSITIONAL ARGUMENTS AS INPUT.HOW TO CHECK
# IF THE ARGUMENT THAT ARE PASSED ARE MORE THAN 5

# def func(*args):
#         if len(args)>5:
#             yield f"{len(args)} is greter than 5"
#         else:
#             yield f"{len(args)} is less than 5"
# print(list(func(16,2,5,3,3,6,6)))

     # O R

# def func(*args):
#     if len(*args) > 5:
#         yield f"{len(*args)} is greter than 5"
#     else:
#         yield f"{len(*args)} is less than 5"
#
#
# print(list(func("This is monty")))

##################################################################################
# W a generater func to print the below output
#
# func("TRACXN",0)   #SHOULD PRINT RCN
# func("TRACXN",1)   #SHOULD PRINT TAX

# def func(num,string):
#
# print(list(func("TRACXN")))




################################################################################333
# W A GENERATOR FUNC TO GENERATE 10 PHIBONACCI SERIES NUMBERS

def func(a):
    n1=0
    n2=1
    for i in range (a):
        yield n1
        n3=n1+n2
        n1 = n2
        n2 = n3
print(list(func(10)))


##################################################################################
# PYTHON PROGRAM FOR HOW TO CHECK IF A GIVEN NUMBER IS FIBONACCHI NUMBER

def func(a):
    n1=0
    n2=1
    for i in range (a+1):
        yield n1
        n1,n2=n2,n1+n2
print(list(func(10)))

################################################################################3
#GENERATE A LIST OF NAMES STARTING WITH VOWELS IN THE GIVEN STRING

names=['laura',"steve", "bill","james","greig","scott","alex","ive"]

def func(a):
    for name in names:
        if name[0] in "aeiuoAEIOU":
            yield name
print(list(func(names)))

##########################################################################
# GENERAT EXPRESSION TO SUM THE FACTORIAL OF NUMBERS FROM 1-5

def facto (num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
        yield fact
print(list(facto(5)))

# EXPRESSION
from math import factorial
g=(factorial(i) for i in range(1,6))
print(list(g))

 # [FOR SUM THE VALUE USE BELOW EXPRESSION]

from math import factorial
g=(factorial(i) for i in range(1,6))
print(sum(list(g)))