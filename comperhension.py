# # C O M P E R H E N S I O N
#
# # normal
# l=[1,2,3,4]
# for item in l:
#     print(item**2)
#
# #comperhension
# res=[item **2 for item in l]
# print(res)
#
# # or
#
# print([item **2 for item in l])
# #####################################
# names=["steve","eve","prabhug"]
# list=[]
# for words in names:
#     list.append(len(words))
# print(list)
#
# res=[len(word)for word in names]
# print(res)
#
# ######################################3
#
# s="hello world"
# l=[]
# print([(ind,char)for ind,char in enumerate(s)])
#
# #####################################################
#
# l=[]
# for num in range (1,50):
#      if num%2 ==0:
#          l.append(num)
# print(l)
#
# res=[num for num in range(1,50) if num%2 == 0]
# print(l)
#
# ###################################################
# names=['suniil','prem','prabhu','apple',"om","umar"]
# l=[]
# for vow in names:
#     if vow[0] in "aeiouAEIOU":
#         l.append(vow)
# print(l)
#
# res=[vow for vow in names if vow in "aeiouAEIOU"]
# print(l)
# ##########################################################
# names=['sunil','prem','prabu','apple',"om","umarr","aishup","vinodr"]
# l=[]
# for word in names:
#     if len(word)%2 !=0:
#         l.append(word[::-1])
#     else:
#         l.append(word)
# print(l)
#
# res=[word[::-1] if len(word)%2 !=0 else word]
# print(l)
# ###############################################################
# nums=[1,2,3,4,5]
# d={}
# for sq in nums:
#     d[sq]=sq**2
# print(d)
#
# res={sq:sq**2 for sq in nums}
# print(d)
# #####################################################################3
# senten="python is a programming language and it is sun"
# word=senten.split()
# d={}
# for dict_ in word:
#     d[dict_]=len(dict_)
# print(d)
#
# res={dict_:len(dict_)for dict_ in word}
# print(d)
#
# #####################################################################3
# d={"a":10,"b":20,"c":30}
# d1={}
#
# for key,value in d.items():
#     d1[value]=key
# print(d1)
#
#   W R O N G
#
# d1=d.keys()
# d.keys()=d.values()
# d.values()=d1
# print(d1)
#
#     D I F F I  C U L T
#
# for key in d:
#     value= d[key]
#     d1[value]=key
# print(d1)
#
# res={value:key for key, value in d.items()}
# print(res)
#
# #######################################3
# s="helloo"
# d={}
# for ch in s:
#     d[ch]=s.count(ch)
# print(d)
#
# res={ch:s.count(ch) for ch in s}
# print(d)
#
# #######################################
#
# s="python is programming language means chutiyappa "
# words=s.split()
# d={}
# for ind,word in enumerate(words):
#     if ind% 2 == 0:
#         d[ind]=word[::-1]
#     else:
#         d[ind]=word
# print(d)
#
# res={ind:word[::-1] if ind%2 == 0 else word for ind, word in enumerate(words)}
# print(res)
#
