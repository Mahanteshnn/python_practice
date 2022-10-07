#SORTING

# s="hello"
# print(sorted(s))
# print(sorted(s,reverse=True))
# print()
#
# l=[1, 2, 3, 4, 5]
# print(sorted(l))
# print(sorted(l,reverse=True))
# print()
#
# d={"l":10,"a":12,"c":34,"z":5}
# print(sorted(d))
# print(sorted(d,reverse=True))
# print(sorted(d,reverse=True))



# C O S T U M E    S O R T I N G
#   L I S T
# names=["monty","keerti","vicky","sugu","aishu"]
# print(sorted(names))
# print(sorted(names,reverse=True))
# print(sorted(names,key=len))
# print(sorted(names[-1]))

# def lastc(string):         #based on last char (i,u,u,y,y)
#     return string[-1]
# print(sorted(names,key=lastc))
# print(sorted(names,key=lambda string:string[-1]))


#  C O S T O M E  SORTING D I C T I O N A R Y

# d={"wallmart":7,"gmail":5,"google":6,"flip":8}
# print(sorted(d))
# print(sorted(d,reverse=True))
# print(sorted(d.items()))
# print(sorted(d,key=len))

# def lenK(item):
#     return len(item[0])
# print(sorted(d.items(),key=lenK))
# print(sorted(d.items(),key=lambda item:len(item[0])))

# print(sorted(d.items(),key=lambda item:item[0][-1]))

# a="fare"
# b="fear"
# if sorted(a)== sorted(b):
#     print("anagram")
# else:
#     print("not anagram")
#
# a="mango"
# b="apple"
# if sorted(a)== sorted(b):
#     print("anagram")
# else:
#     print("not anagram")

# items=["eat","aet","listen","silent","tea"]
# d={}
# for item in items:
#     sorted_v=" ".join(sorted(item))
#     if sorted_v not in d:
#         d[sorted_v]=[item]
#     else:
#         d[sorted_v].append(item)
# print(d)







