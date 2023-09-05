x = float(input("Enetr the weight(in kg)= "))
y = float(input("Enetr the height (in meters)= "))
z = x/(y**2)
if x<0 or y<0:
    print("Invalid input")
else:
    print("BMI is ",z)
    
    
    
x = float(input("Enetr the weight(in pounds)= "))
y = float(input("Enetr the height (in inchies)= "))
ab = x*0.454
cd = y*0.0254
z = ab/(cd**2)
if x<=0 or y<=0:
    print("Invalid input")
else:
    print("BMI is ",z)
      