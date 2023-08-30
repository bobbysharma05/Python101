'''You need to repeatedly ask for student marks in 3 subjects (each out of 100), Physics,
Chemistry and Mathematics, and display the grade and scholarship amount of the
student based on their average marks. Stop when the user enters tell it to exit the
loop.'''

while True:
    x = int(input("Enter the marks of Physics = "))
    y = int(input("Enter the marks of CHemistry = "))
    z = int(input("Enter the marks of Maths = "))
    avg = (x+y+z)/3
    if avg>=90:
        print("Grade - A and Scholarship - 100%")
    elif avg>=80:
        print("Grade - B and Scholarship - 50%")    
    elif avg>=70:
        print("Grade - C and Scholarship - 25%")
    elif avg<70:
        print("Grade - D and No Scholarship")    
    else:
        exit_choice = input("Enter 'exit' to stop or press Enter to continue: ")
        if exit_choice.lower() == "exit":
            break 
