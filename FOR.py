# a='hello world'
# for char in a:
#     print(char,end="")

   # [O R]

# a='hello world'
# for char in range(len(a)):
#          print(a[char])
############################################################
#(2)traverse through a set
# s={100,90,80}
# for elem in s:
#     print(elem)
          #[OR]
# s={100,90,80}
# for elem in range(len(s)):
#     print(s[elem])
#{RANGE wont support for set and dictionary because it wont support for slicing and indexing}

############################################################
#traversing through a dictionary
#keys
# d={"a":1,"b":10,"c":30}
# for key in d:
#     print(key)
# #VALUES
# for val in d:
#     print(d[val],end=" ")
############################################################
# Iterate over a string in reverse order
# s="yo yo honey sing"
# for char in s[::-1]:
#     print(char, end=" ")
    #[OR]
# s="yo yo honey sing"
# for char in range(len(s)-1,-1,-1):
#     print(s[char])
##########
#indexing and char
# s="yo yo honey sing"
# for ind in range(len(s)):
#     print((ind,s[ind]))
###########33

# s="yo yo honey sing"
# for item in enumerate(s):
#     print(item[0],item[1],end=",")

###############################
# l=[10,20,30,40]
# s="kinghfhf"
# for item in zip(l,s):
#     print(item)
   #[OR]
# l=[10,20,30,40]
# s="kinghfhf"
# for item1,item2 in zip(l,s):
#     print()
####################
# l=[10,20,30,40]
# s="kinghfhf"
# from itertools import zip_longest
# for item in zip_longest(l,s, fillvalue=1):
#     print(item,end=",")  #op   (10, 'k'),(20, 'i'),(30, 'n'),(40, 'g'),(1, 'h'),(1, 'f'),(1, 'h'),(1, 'f'),
###############################################

#traversing throuh Dictionary


# only keys and only value
# d={"a":10,"b":30,"c":100}
# for keys in d:
#     print(keys, end=",")

# d={"a":10,"b":30,"c":100}
# for keys in d.keys():
#     print(keys)
#
# for values in d.values():
#     print(values)
#
# for item in d.items():
#     print(item)
#
# for keys,values in d.items():
#     print(keys,values)
#######################################################

# s="python is a programming language"
# words= s.split()
# d={}
# for lett in words:
#     d[lett]=len(lett)
# print(d)
# ############################################
# i="virat"
# d={}
# for ind,char in enumerate(i):
#     d[ind]=char
# print(d)
##############################################3
# s="hello my name id monty and monty is bunny"
# words=s.split()
# d={}
# for num in set(words):
#     d[num]= words.count(num)
# print(d)
# ####################################################
# s="hello my name id monty and monty is bunny"
# words=s.split()
# d={}
# for dict in words:
#     d[dict]=words.count(dict)
# print(d)
# ####################################################3
