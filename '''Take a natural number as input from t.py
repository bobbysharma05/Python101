'''Take a natural number as input from the user and calculate the sum of the following
series'''

n = int(input("Enter the natural number = "))
sum = 1 - (1/(2**n))
print("The sum is ",sum)
