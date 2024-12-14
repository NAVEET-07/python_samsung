n=int(input())
j=0
count=0
k=2
no=0
while(1):
    count=0
    for i in range(1,k+1):
        if(k%i==0):
            count+=1
    if(count==2):
        # if(k==n-1):
        no+=1
        print(f"{no} : {k}")
    if(no==n):
            
            print(k)
            break
    k=k+1
    
print(f"total : {j}")
        