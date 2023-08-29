"""Take an integer as input and check whether it is prime or not. Display appropriate
error message in case of invalid input."""

x = int(input("Enter the number = "))

i = 2
c = x%i 
i = i+1
if x!=i and c!=0:
    print("It is a prime number")
else:
    print("It is not a prime number")

   
