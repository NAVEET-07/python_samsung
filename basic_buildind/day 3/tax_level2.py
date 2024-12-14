name = input('Enter name of the employee: ')
id = int(input('Enter Id of the employee: '))
basic_salary = float(input('Enter monthly basic salary of the employee: '))
allowances = float(input('Enter special allowances of the employee: '))
bonus = float(input('Enter bonus percentage: '))

gross_monthly_salary = basic_salary + allowances 
gross_annual_salary  = (gross_monthly_salary * 12) + (bonus / 100) * (12 * gross_monthly_salary)

print('%-4s %-12s %-14s %-12s %-9s %-14s %-s'%("ID", "NAME", "BASIC-SALARY", "ALLOWANCES","BONUS(%)", "MONTHLY-SALARY", "ANNUAL-SALARY"))
print('*' * 85)
print('%-4d %-12s %-14.2f %-12.2f %-9.2f %-14.2f %-.2f'%(id, name, basic_salary, allowances, bonus, gross_monthly_salary, gross_annual_salary))
sd=50000
ts=gross_annual_salary-sd
print(f"Standard Deduction ={sd}\nTaxable salary = {ts}")

n=int(input("ENter the "))
if(n>0 and n<300000):
    per=0
elif(n<600000):
    per=5
elif(n<900000):
    per=10
elif(n<1200000):
    per=15
elif(n<1500000):
    per=20
else:
    per=30
print("ARe you nelonf to the Section 67A \n1: Yes\n2:No")
m=int(input())
if(m==1):
    if(n<700000):
        total=n*per*0.01
    
