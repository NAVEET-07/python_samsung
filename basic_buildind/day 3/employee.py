name=input("Enter vthe employee name : ").upper()
emp_id=int(input("Enter the employee ID : "))
ms=int(input("Enter the monthly salary of a Employee : "))
sa=int(input("Enter the special allowance : "))
bp=int(input("Enter the Annual Bonus : "))
mgs= ms+sa
annualgs=(mgs*12)+bp*0.01*mgs*12
print(f"    NAME : {name}\n MONTHLY SALARY : {ms}\n MONTHLY GROSS SALARY{mgs}\n ANNUAL YEARLY SALARY{annualgs}")