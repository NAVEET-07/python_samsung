print("1 : cloudly\n2 : Sunny \n \n Enter the environment :")
a=int(input())
if(a==1):
    print("It is raining say yes or no")
    if(input()=="yes"):
        print("go out with umbrella")
    else:
        print("go as you wish")
elif(a==2):
    b=input("1: sunny\n2: hot\n")
    if(b==1):
        print(" go out as you wish")
    elif(b==2):
        print("then go out with jacket")
    