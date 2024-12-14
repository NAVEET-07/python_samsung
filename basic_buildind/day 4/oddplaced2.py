num="23445"
count=1
sum=0
for i in num:
    i=int(i)
    if count%2!=0:
        if(i%2==0):
            sum+=i
            print(f"{count}  {i}= {sum}")
    count+=1
print(sum)