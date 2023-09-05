x = float(input("Enetr the length (in meters)= "))
y = float(input("Enetr the length (in meters)= "))
h = float(input("Enetr the height (in meters)= "))
Ar = 0.5*(x+y)*h
if x<=0 or y<=0 or h<=0: 
    print("Invalid input") 
else:
    print("Area of trapezoid",Ar)     
