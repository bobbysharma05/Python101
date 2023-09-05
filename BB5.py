x = int(input("Enter the 5 digit number = "))
a = x%10
b = x//10
c = b%10
d = b//10
e = d%10
f = d//10
g = f%10
h = f//10
rev_digit = ((a*10000)+(c*1000)+(e*100)+(g*10)+h)
if x==rev_digit:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
