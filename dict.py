# s='abracadabraca'
# word_count={}
# for word in s:
#     word_count[word]=s.count(word)
# print(word)
s = "hello world"
d={}
for vow in s:
 if vow  in "AEIOUaeiou":
  if vow not in d:
    d[vow]=1
  else:
    d[vow]= d[vow] + 1
print(d)

###########
# names=["apple","google","apple","yahoo","yahoo","facebook","apple","gmail","gmail","gmail","gmail"]
# d={}
# for ch in names:
#     if names.count(ch) >1 :
#         d[ch] = names.count(ch)
# print(d)
names = ["apple", "google", "apple", "yahoo", "yahoo", "google", "gmail", "gmail", "gmail"]
d={}
for ind,char in enumerate(names):
    if char not in d:
        d[char] = [ind]
    else:
        d[char].append(ind)
print(d)
###########################
a=[1,2,3,4]
b=[5,6,7,8]
l=[]
for ind in range(len(a)):
    l.append(a[ind] + b[ind])
print(l)
###################

####################3
a=[1,2,3,4]
b=[5,6,7,8]
for values in zip(a,b):
    print(values)

###################
l = [10,0,49]
s = "hai"
for item in zip(l,s):
   print(item)
##################
a=[1,2,3,4]
v=["hello",1,2,3]
#################