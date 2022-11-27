# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 12:28:18 2022

@author: dhpcap
"""

# =============================================================================
'''
Unpack the following tuple into 4 variables
aTuple = (10, 20, 30, 40)
'''

aList=[]
num=int(input("Enter the number of Element u need for Tuple = "))
for i in range(1,num+1):
    a=int(input(f"Enter the {i} tuple element --> "))
    aList.append(a)
    aTuple=tuple(aList)
print(aTuple)

#for i in range(num):
 #   a=aTuple[i]
    
  #  print(f"{i}---> {a}")


bList=[]
num=(int(input("Enter the number of Element u need for Tuple = ")))
for i in range(num):
    a= (input(f"Enter the {i} tuple element --> "))
    bList.append(a)
    bTuple=tuple(bList)
print(bTuple)


if len(aTuple) == len(bTuple):
    for x,y in zip(aTuple,bTuple):
        print(f"{y}---->{x}")
else:
    print("Invalid")
    

list=[1,2,3,4,5,6]
#list.pop(2)
print(list)
list2=list.copy()
print(list2)
print(list.index(1))
list.remove(1)
print(list)
list=[1,2,3,4,5,6]
print(min(list))
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)
print(thistuple[-4:])
txt = "Hello, welcome to my world."
txt.isalpha()
s = {1,3 2}
s.pop()
print(s)




# =============================================================================
