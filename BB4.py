x = int(input("Enter the 3 digit number = "))
sum = 0
sum = sum + x%10
x = x//10
sum = sum + x%10
x = x//10
sum = sum + x
y = sum%3
if y==0:
    print("It is divisible by 3")
else:
    print("It is not divisible by 3")