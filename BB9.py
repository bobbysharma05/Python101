x = int(input("Enter the basic salary = "))
h = (20*x)/100
t = (5*x)/100
d = (10*x)/100
gross = x + h + t + d
print("Gross Salary is = ",gross)
if gross<300000:
    print("0%")
elif gross<1000000:
    print("10% of the gross salary")
elif gross<2500000:
    print("20% of the gross salary")        
elif gross>2500000:
    print("30% of the gross salary")
    
