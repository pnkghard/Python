  # -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 23:43:46 2022

@author: dhpcap
"""

num=int(input("enter number"))
print("the number is :"+str(num))
print(f"the number is : {num} {5*3}")
print("the number is :",num)
a=12
b=25
print("the number is {1} another value is {0}", format(a,b))

v=13j
b=complex(69)
print(type(v))
print(type(b))
    

a=15
b=57
c=54
print(a,b,c,sep=",")
print("hello baby",end =" ")
print("wanna fun!!")


a=15
b=57
c=54


print(a+b)
print(a-b)
print(a*b)
print(b/a)

print("hello"*2)
print("*"*2)


age=int(input("enter the age"))
if age<=5:
    print("ur in kindrgarder")
    print("u can't vote")
elif age>5 and age<=12:
    print("ur in primary")
    print("u can't vote")
elif age<18:
    print("ur in school")
    print("u can't vote")
else:
    print("ur in college")
    print("congo u can vote")
        
    