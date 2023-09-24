'''Find the sum of the series where x and a positive error ϵ is taken as input from the user. The 
value of F(x) is displayed along with the minimum number of terms that gives the valid result 
such that 
 | Fi(x) – Fi-1(x) | < ϵ where i is the term count
1. F = Σn ( 1 / 2 )n where n is the term count'''



error = float(input("Enter the error : "))
if error<0:
    print("Invalid Input") 
i=2
count_=0
while True:
    Func = (1/2)**i
    Sunc = (1/2)**(i-1)
    i+=1
    count_+=1
    if abs(Func - Sunc) < error:
        print("Invalid Input")
        break
print(count_)
print("The sum of this series is ",Func)
 
         
