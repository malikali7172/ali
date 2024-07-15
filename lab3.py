Q#!......................................

for i in range(1500,2701):
    if i%7 == 0 and i%5 == 0:
        print(f"{i} is the multiple of 5 and divisible by 7")
Q#2..........................................

temp = int(input("Enter temperature in celsius :"))
f = (temp * 9/5) + 32
print(f"{f} farenheit")


temp = int(input("Enter temperature in farenheit :"))
c = (temp -32)*(5/9)
print(f"{c} celsius")

Q#3...........................................

import random

mynum = random.randint(1,9)

step = 3
while(step>0):
    num = int(input("enter your guess you between 1-9:"))
    if num == mynum:
        print("Your guess is right")
        break
    else:
        step-=1
        print(f"Your guess is wrong now you have {step} tries left")
print(mynum)

Q#4................................................

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print("")
for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
Q#5................................................

txt=input("Enter a string ")
new = txt[::-1]
print("String in reverse is :",new)

Q#6................................................

even=0
odd=0
list1=[]
while(True):
    num=int(input("to terminate input enter -1 otherwise something else : "))
    if num !=-1:
        list1.append(num)
    else:
        break
    Q#7..................................................

    my_list = [1452,11.23,1+2j,True,'We',(0,-1),[5,12],{"class":"V","Section":"A"}]
for i in my_list:
    print(f"{i} : type of {i} is {type(i)}")

    Q#8...................................................

    for i in range(7):
    if i==3 or i==6:
        continue
    else:
        print(i)
    Q#9.....................................................

    lst = [0,1]
for i in range(1,50):
    if lst[i]+lst[i-1] <= 50:
        lst.append(lst[i]+lst[i-1])
    else :
        break

print(lst)

for i in list1:
    if i%2==0:
        even+=1
    else:
        odd+=1


print("Even numbers : ",even)
print("odd numbers : ",odd)
Q#9................................................

rows=int(input("Enter no.of rows : "))
col=int(input("Enter no.of columns : "))
arr=[[0 for i in range(rows)] for i in range(col)]
for i in range(rows):
    for j in range(col):
        arr[i][j]=i*j
print(arr)

Q#10.................................................

def is_binary(n):
    if n.isdecimal():
        for i in range(4):
            if n[i]!="0" and n[i]!="1":
                return False
    else:
        return False
    return True   
#------------------------------------------------------   
        
list1=[]
list2=[]
print("To stop input enter -1 ")
while(True):
    txt=input("Enter a binary number of 4 digits : ")
    if txt=="-1":
        break
    elif txt.isdecimal()==False or txt.isalpha()==True:
        print("input is not binary")
    
    elif len(txt)!=4:
        print("invalid size")
    elif is_binary(txt)==True:
        list1.append(txt)
    else:
        print("Number entered in not binary")
    txt=""
for i in list1:
    num=(int(i[3])(23))+(int(i[2])(2*2))+(int(i[1])(2*1))+(int(i[0])(2**0))
    if num%5==0:
        list2.append(i)
print(list2)

Q#11...................................................

letters=0
digits=0

txt=input("Write a alphanumeric string : ")
for i in range(len(txt)):
    if txt[i].isalpha():
        letters+=1
    elif txt[i].isdigit():
        digits+=1
print("Letters : ",letters)
print("digits : ",digits)

Q#12........................................................

password=input("Enter New Password ")
check=1
symbol=0
digit=0
small_alpha=0
capital_alpha=0
list1=['$','#','@']
if len(password)<6 or len(password)>16:
    print("Invalid Password length ")
else:
    for i in range(len(password)):
        temp=password[i]
        if temp in list1:
            symbol+=1
        elif temp.isdigit()==True:
            digit+=1
        elif temp==temp.lower():
            small_alpha+=1
        elif temp==temp.upper():
            capital_alpha+=1
    if symbol==0:
        print("password must contain one of these ",list1)
        check=-1
    if digit==0:
        print("password must contain atleast 1 digit")
        check=-1
    if small_alpha==0:
        print("password must contain atleast 1 small alphabet")
        check=-1
    if capital_alpha==0:
        print("password must contain atleast 1 capital alphabet")
        check=-1
    if check==-1:
        print("Invalid Password ")
    else:
        print("Valid Password")
    print(symbol)
    print(digit)
    print(small_alpha)
    print(capital_alpha)
    print(check)
    