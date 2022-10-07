##even or odd (1)
num=29
if num % 2==0:
    print("inte is even")
else:
    print("it is a odd")
#inline
print("is even"if num % 2==0 else "its odd")

#(2)
#palindrom or not
s ="hello man"
if s==s[::-1]:
 print("palindrom")
else:
 print("not palindrom")

 #(II)
 m="1,2,3,4,5"
 if m==m[::-1]:
     print("yes")
 else:
     print("no")
#(III)
 p=1234321
 if p==p:
    print("yes")
 else:
    print("noooo")
#(3)
#alphabet/digit/spcl char/
 c="7"
 if c.isalpha():
    print("c it is alpha")
 elif c.isdigit():
    print("c is a digit")
 else:
    print("it is a special")
#(4)
#vowel or not
ch="M"
if ch in "aeiouAEIOU":
    print("it is vowel")
else:
    print("it is constant")

#(5)
#given var is alpha without using inbuilt method (so use ord cha)
M=ord("9"),ord("z"),ord("A"),ord("Z")
print(M)
M=chr(122)
print(M)

c="l"
if (ord("a")<=ord(c)<=ord("z")) or (ord("A")<=ord(c)<=ord("Z")):
    print("char is alphabet")
else:
    print("it is not a alpah")

#####################3
#(6) is start with vowel or not
a="abc"
if a[0] in "aeiouAEIOU":
    print("yes start")
else:
    print("no not strat")
##############################
#(7) empty or not
ile=[1,2,3]
if ile:
    print("it is not empty")
else:
    print("it is empty")
######################
#(8) lower to upper

# monty="e"
# if (ord("a")<=ord(monty)<=ord("z")):
#     print(monty(ord(monty)-32))
# elif (ord("A")<=ord(monty)<=ord("Z")):
#     print(monty(ord(monty) + 32))
# else:
#     print("not a alphabet")

#######
#even number of element
s="bangloree" #it is having length of char 9=(b a n g l o r e e) and 9 is not even
if len(s)%2==0:
    print("it has even")
else:
    print("no it wont")

############################3
#check sequence if it is sequence reverse it
s="banglore"
if isinstance(s,(list,tuple,str)):
    print("it is sequence")
    print(s[::-1])
else:
    print("it is a name")
###################################
#check given dictionary is even if it is even add 1 more key value pair and prind dictionary(d)
d={1:"a",2:"b"}
if len(d)%2==0:
    d[3]="c"
    print(d)
else:
    print("odd")
########################################
#print the largest number
a=60
b=200
c=500
if a>b and a>c:
    print("a is greater")
elif b>c and b>c:
    print("b is greater")
else:
    print("c is greater")
#######################################
#check first digit is even or not
n=123
if int(str(n)[0])%2==0:
    print("even")
else:
    print("odd")
####################################3
# #leap year or not
# year=2020
# if year%4==0:
#     print("leap")
# else:
#     print("its not leap")
# ######################################3
# #perfect square o
# num=36
# sqr = num**.5    #(36)^0.5=(36)^(1/2)=6
# if sqr**2==num: #sqr=6       ___ 6**2=36 ____36==num
#     print("perfect sq")
# else:
#     ("not perfect sq")
# #######################################
# num=89
# sqr=num**.5
# if sqr**2
# ########################################3
char = "a"
if char.isalpha():
    print("char is an alphabet")
elif char.isdigit():
    print("char is a number")
else:
    print("char is a special character")