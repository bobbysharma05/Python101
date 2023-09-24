''' Find the sum of the following series for N terms, where N is taken as input from the user and 
display the result till exactly 9 decimal places.
1/1! + 1/2! + 1/3! + 1/4! + … + 1/N!'''


terms = int(input("Enter the number of terms = "))
sum=0
fact=1
for j in range(1,terms+1):
    fact*=j
    sum+=(1/fact)
print("Sum till", terms, "terms are :",sum)

            
