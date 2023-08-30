'''Calculate the roots of a quadratic equation by taking the coefficients as input from
the user. Handle the invalid cases'''

x = float(input("ehter the value of a = "))
y = float(input("ehter the value of b = "))
z = float(input("ehter the value of c = "))       
dt = (y**2)-(4*x*z)
if x==0:
    print("Invalid input")
else:   
    if dt<0:
        print("The roots are complex numbers.")
    elif dt==0:
        roots = (-y)/(2*x)
        print("The roots are real and equal.",roots) 
    else:
        root1 = (-y)+(dt**(0.5))/(2*x)
        root2 = (-y)-(dt**(0.5))/(2*x)
        print("The roots are real and distinct.",root1,root2)         