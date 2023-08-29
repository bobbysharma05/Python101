"""The program should accept an unknown number of ages from the keyboard until
zero is entered. If the age is greater than or equal to 100 output “You have lived
a century”, otherwise if age is greater than or equal to 55 output “Great Age to
Relax” otherwise output “Welcome aboard”."""


x = int(input("Enter your age = "))
if x>=100:
    print("You have lived a century")
elif x>=55:
    print("Great age to relax") 
elif x==0:
    print("Invalid input")
else:
    print("Welcome Abroad")       
