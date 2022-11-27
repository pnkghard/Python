# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 00:31:24 2022

@author: dhpcap
"""

print("hello world")


print("hello" + "jenny")

print("hello" +"  " +"jenny")

print("new line can be created" +"  " +"with a backlash  and n")

print("hello mr." +" "+input("what is your name?")+","+("how are you"))


name=input("what is your name ?")
length=len(name)
print(name)
print(length)



a=input("enter the value of a")
print(a)
b=input("enter the value of b")
print(b)
temp=a
a=b
b=temp
print("a value is =" + a)
print("b value is =" + b)

var1 = 0o10
var2 = 0x10
print(var1)
print(var2)
print(type(var1))
print(type(var2))