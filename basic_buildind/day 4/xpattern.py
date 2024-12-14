import sys

# python table.py 14

num = int(sys.argv[1])
for i in range(1,num+1):
    for j in range(1,num+1):
        if(i == j or j==num-i+1):
            print("n",end='')
        else:
            print("  ",end='')
    print()