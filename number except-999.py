'''Take a positive integer N as input followed by repeatedly taking numbers from the user till the 
time user entered -999. At the end display the count of input numbers that are divisible by N 
and the count of input numbers that are not divisible by N.'''



n = int(input("Enter the positive number = "))
count_yes=0
count_no=0
while n!=(-999):
    num = int(input("Enter the number = ")) #repeatedly taking numbers till -999.
    if n==-999 or num==-999:
        break
    if num%n==0:
        count_yes+=1
    else:
        count_no+=1
    
    
print("The numbers divisible is ",count_yes)
print("The numbers not divisible are ",count_no)