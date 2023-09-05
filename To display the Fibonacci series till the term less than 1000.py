'''To display the Fibonacci series till the term less than 1000.
'''

a=0
b=1
c=0

while (c<1000):
    c=a+b
    print(c)
    
    b=a
    a=c