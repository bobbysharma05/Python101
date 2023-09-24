''' Find the sum of the following series for N terms, where N is taken as input from the user and 
display the result till exactly 9 decimal places.
 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + ….. N terms'''


terms = int(input("Enter the number of terms = "))
sum=0
for i in range(1,terms+1):
    sum+=(1/i)
print("Sum till", terms, "terms are :",sum)
