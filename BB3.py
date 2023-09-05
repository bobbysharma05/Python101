x = float(input("Enetr the length of side1 of triangle = "))
y = float(input("Enetr the length of side2 of triangle = "))
z = float(input("Enetr the length of side3 of triangle = "))
if x<=0 or y<=0 or z<=0:
    print("Invalid input")
elif x==y==z:
    print("Invalid Input")    
elif x<(y+z) or y<(x+z) or z<(y+x):
    print("It forms a triangles.")
elif x==(y+z) or y==(x+z) or z==(y+x):
    print("It does not forms a triangles.")
else:
    print("Invalid input")       
