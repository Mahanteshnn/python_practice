##########
# C R E A T  L I S T

# a=[1,2,3]
# b=["a","b","c"]
# for sum_ in zip(a,b):
#     print(sum_)
# [O R]
# a=[1,2,3]
# b=["a","b","c"]
# for ind, char in zip (a,b):
#     print([ind,char])

##########################################
# l=[1,2,3,4,5]
# l1=[]
# for sqr in l:
#
#         l1.append(sqr**2)
#
# print(l1)
################################
# names=["monty","vicky","sugu","guru"]
# l1=[]
# for le in names:
#         l1.append(len(le))
# print(l1)
##############################################

# s="hello world"
# l1=[]
# for ind,char in enumerate(s):
#         l1.append((ind,char))
# print(l1)

##############################################
# l1=[]
# for num in range(1,50):
#         if num%2 ==0:
#                 l1.append(num)
#         else:
#                 l1
# print(l1)

########################################3
# names=['monty','prabhu','yoyoyo','on']
# l1=[]
# for vow in names:
#         if vow[0] in "aeiouAEIOU":
#                 l1.append(vow)
# print(l1)
#########################################3
name=['monty','prabhu','yoyoyo','on']
l1=[]
for res in name:
    if len(res)%2!=0:
        l1.append(res[::-1])
    else:
        l1.append(res)
print(l1)
#############################################
l1=[]
for num in range(1,21):
    if num>1:
      for i in range(2,num):
          if num%i==0:
              break
      else:
          print((num))
print(l1)