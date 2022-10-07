# def prime (num):
#     for i in range(2,num):
#         for i in range(2,num):
#             if num % i==0:
#                 print("not prime")
#                 break
#         else:
#             print("prime")
# prime(5)
#
# def prime_series(start, end):
#     for num in range(start,end):
#         for i in range(2,num):
#             if num % i==0:
#                 break
#     else:
#         print(num)
#
# prime_series(1,10)
# ##################################3b
# b=100
# def add():
#     b=20
# add()
# print(b)
# ############################################
#      A S S I G N M E N T    P R A C T I C E

# TYPES OF ARGUMENT
# 1) POSITIONAL ARGUMENTS (<--/)
#
# def add(a,b,/):
#        print(a+b)
#
# add(1,2)
# # add(a=1,b=2) type error
# #############################3
# def mul (a,/,b):
#        print(a*b)
# mul(10,b=5)
# #########################33
# def add(*,a,b):
#        print(a+b)
# add(a=10,b=30)
# # add(10,b=30): Typerror
# #########################
# def add (a,*,b):
#        print(a+b)
# add(10,b=90)
# ##########################
# def add(a,/,b,*,c,d):
#        print(a+b+c+d)
# add(10,20,c=40,d=100)
# add(10,b=20,c=40,d=100)
################################
# def add(*args):
#        print(sum(args))
# add()
# add(1,2,3,70)
###########################3
# def prem(*args):
#   print(sum(args))
# prem(2,6)
###########################3
# def prem(**kwargs):
#   print(kwargs)
# prem(a=1,b=3)
# #######################3
# def add(*args):
#   print(sum(args))
# add(1,2)
# ##########################
# def add(*args,**kwargs):
#   print(sum(args),kwargs)
# add(1,2,a=10,v=30)
# ###############################3
# def add(*args):
#   print(sum(args))                #P A C K I N G
# add(123,123)
# #################
# l=[10,30,40]
# def add(a,b,c):                   # U N P A C K I N G
#   print(a,b,c)
# add(*l)
####################################
# a='good morning'
# def greet(msg=a):
#   print(msg)
# greet()
# greet("hello")
# ####################################
# a='man of the match'
# def man(msg=a):
#   print(msg)
# man()
# man("virat")
#######################################
# def len_(iterable):
#    count=0
#    for yo in iterable:
#      count+=1
#        print(yo)
# len_("hai")
########################################
# def le(iterable):
#    count=0
#    for num in iterable:
#         count+=1
#    print(count)
#
#
# le("hai")
# le("good mor")
######################################
# def prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             print(prime)
#             break
#     else:
#         print("not a prime")
# prime(4)
###############################3
# def ser(start,end):
#     for num in range(start,end):
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)
# ser(1,10)
#######################################
# def cont(*args,**kwargs):
#     print(len(args))
#     print(len(kwargs))
# cont(1,2,3,a=60,u=60)
######################################33
# a="hi everyone"
# def greet(msg=a):
#     print(msg)
# greet()
# greet("yo man")
#####################################
# def checkargs(*args,**kwargs):
#     if len(args)+len(kwargs)>5:
#         print("greater")
#     else:
#         print("lesser")
# checkargs(2,4,a=10,n=60,m=30)
######################################

# def last(digit):
#     return digit%10
# print(last(145))
#
#  #[O R]
#
# def last(digit):
#     print(digit%10)
# last(145)


##################################################

# NTH PRIME

