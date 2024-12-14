m=int(input("enter marks = "))
if(m>0 and m<49):
    r="Fail"
elif(m<79):
    r="Second class "
elif(m<95):
    r="First class"
elif(m<=100):
    r="Distinction"
else:
    r="invalid choice"
print(r)