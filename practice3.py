# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:01:16 2022
"""

list=[1,2,3,4,5,6]
print(list.count(4))
list1=[7,8,9]
list.extend(list1)
print(list)

list.append(10)
print(list)
#Add an element at a particular position
list.insert(2,33)
print(list)
#To delete the last element....
list.pop()
print(list)
#To delete the data of a particular index from a particular list...
list.pop(5)
print(list)
#To remove an element from a list....
list.remove(2)
print(list)
if 1 in list:
    list.remove(1)
    print(list)
else:
    print("Element Not Found")
    
if 100 in list:
    print(list.index(100))
else:
    print("Element Not Found")
    
list.reverse()
print(list)
list2=list.copy()
print(list2)

list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)
print(list)

# Create a list 

l=[]
ans="y"
while ans=="y":
        num=int(input("enter the Number:"))
        l.append(num)
        ans=input("Do you want to Continue(y/n)")
        print(l)
        
list3=[1,2,3,5,4,8]

def addnewcourse():
    cname=input("Enter the new Course")
    str.append(cname)
    return True

str=["DAC","HPCAP"]
choice=int(input("1)Add new Course...\n2)Delete the course\n3)Display\n4.Modify Course Name\n5Display a particular course Name...\n6.Sort the Courses"))
if choice==1:
    status=addnewcourse()
    if status=true
    
elif choice==7:     
    print("Thank you for Visiting")
    
    
    
    
    