import math 
num=int(input("Enter the number"))

root= math.sqrt(num)
root= math.floor(root)

if(root*root==num):
    print("the given nuber is perfect square number ")
else:
    print("the given nuber is not perfect square number ")