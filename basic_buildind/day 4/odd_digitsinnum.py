num="23445"
sum=0
for i in num:
    i=int(i)
    
    if(i%2!=0):
        sum+=i
        print(f"  {i}= {sum}")
print(sum)