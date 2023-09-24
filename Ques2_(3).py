''' Find the sum of the following series for N terms, where N is taken as input from the user and 
display the result till exactly 9 decimal places.

 F(x) = 1 + x/1 + x2
/2 + x3
/3 + x4
/4 + ….. + N terms (Take x also as input)'''



terms = int(input("Enter the number of terms = "))
x= float(input("Enter the value of x"))
sum=1
for i in range(1,terms):
    sum+=((x**i)/i)
print("Sum till", terms, "terms are :",sum)
