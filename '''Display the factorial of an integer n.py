'''Display the factorial of an integer number input by the user. Consider invalid cases'''


num = int(input("Enter the number = "))
if num<0:
       print("Invalid input")
elif num==0:
       print("Invalid input")
else:
      fact=1
      i=1
      while True:
       fact *= i
       i += 1
       if i==(num+1):
            print("Factorial is ",fact)
            
       