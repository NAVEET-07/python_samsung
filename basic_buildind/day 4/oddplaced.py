num=input()
list=[int(digit) for digit in (num)]
j=0
print(list)
for i in range(1,len(list),2):
    if(list[i]%2==0):
        
        j=j+list[i]
print(j)