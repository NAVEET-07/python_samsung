num =int(input("Enter the number : "))
sum=0
#for i in (num):
   #342342 print(type(i))
    #i=int(i)
    #sum+=i
#print(sum)

rem=0
while(num>0):
    rem=num%10
    num=int(num//10)
    sum+=rem
    #print(rem)
print(sum)