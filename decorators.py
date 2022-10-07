###########################################33
# Q3] assignment
# import time

# count=0
# def outer(func):
#     def inner(*args,**kwargs):
#         global count
#         print(f'executing{func.__name__} function')
#         count+=1
#         func(*args, **kwargs)
#     return inner
# @outer
# def add(a,b):
#     print(a+b)
# add(1,2)
# add(5,5)
# @outer
# def sub(a,b):
#    print(a-b)
# sub(6,2)

##############################################################

# d={}
# def outer(func):
#     def inner(*args,**kwargs):
#         print(f'executing {func.__name__} function')
#         if func.__name__ not in d:
#             d[func.__name__]= 1
#         else:
#             d[func.__name__] += 1
#     return inner
# @outer
# def add(a,b):
#     print(a+b)
# add(10,20)
# add(20,30)
# add(9,41)
# @outer
# def mul(a,c):
#     print(a*c)
# mul(4,5)
# mul(8,5)
# mul(10,9)
#
# @outer
# def sub(b,c):
#     print(b-c)
# sub(80-50)
# sub(100-200)

##############################################

#   # Q3] assignment
# def outer(func):
#     def inner(*args,**kwargs):
#         print(f'executing {func.__name__} function')
#         for repeat in range(4):
#
#             func(*args,**kwargs)
#     return inner
# @outer
# def add(k,m):
#     print(k+m)
# add(5,6)
# add(8,6)
#
# @outer
# def sub(v,m):
#     print(v-m)
# sub(10,5)
#

#############################################
.99999
#############################################
"""
def outer(func):
    def inner(*args,**kwargs):
        print(f'executing {func.__name__} function')
        positive=func(*args,**kwargs)
        return abs(positive)
    return inner

@outer
def sub(k,s):
    return k-s

print(sub(40, 60))
"""
###########################################################################################

##to call funtions with different time lapse
"""
import time
def exetime(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        if func.__name__ == add.__name__ :
            time.sleep(5)
        else:        
            time.sleep(10)
    return wrapper

@exetime
def add(a,b):
    print("wait 5 sec")
    print(a+b)

@exetime
def sub(c,d):
    print("wait 10 sec")
    print(c-d)

add(5,6)
sub(9,5)
"""
################################################################################################
##enumerate
"""
l=[1,2,3,4,5]
s = enumerate(l)
print(list(s))

"""
####################################################################################################
##defaultdict

from collections import defaultdict
s= "marry had a little lamb and lamb had marry lamb lamb lamb  "
s1 = s.split( )
d = defaultdict(bool)
for word in s1:
    d[word] = d[word] + True
print(d)



"""
from collections import defaultdict
s= "marry had a little lamb and lamb had marry "
s1 = s.split( )
d = defaultdict(tuple)
print(d)

"""



