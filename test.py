import time

#Variable Swapper

""" 
var1 = input("enter the first variable: ")
var2 = input("enter the second variable: ")

print("Now with a little trick of magic the variables will be swapped")

var1, var2 = var2, var1

print("The value of the first variable is: ", var1)
print("The value of the second variable is: ", var2)
 """

#String Concatenation + Age in 5 years

""" 
while True:
    fname = str(input("Enter your first name: "))
    lname = str(input("Enter your last name: "))

    if fname.isalpha() and lname.isalpha():
        while True:
            try:
                age = int(input("Enter your age: "))
                if age < 0:
                    print("Age cannot be negative")
                else:
                    break #inner loop
            except:
                print("Age can only be interger numbers")
        age += 5
        print(fname + " " + lname + ", you will be " + str(age) + " years old in 5 years")
        break #outer loop
    else:
        print("Invalid Name. Names can only contain alphabetic characters. Try again!") 
"""

#Area Calculation

def triangle_area():
    try:
        base = float(input("Base: "))
        height = float(input("Height: "))
        if base <= 0 or height <= 0:
            print("Invalid input. Base/Height cannot be 0 or negative")
        else:
            return print(round(float((base * height) * 0.5),2))
    
    except:
        print("Invalid input, make sure you only typed numbers")

def circle_area():
    try:
        radius = float(input("Radius: "))
        if radius <= 0:
            print("Invalid input. Radius cannot be 0 or negative for area")
        else:
            return print(round(float(radius ** 2) * 3.14, 2))
    except:
        print("Invalid input, make sure you only typed numbers")

def rectangle_area():
    try:
        length = float(input("Length: "))
        width = float(input("Width: "))
        if length <= 0 or width <= 0:
            print("Invalid input. Length/Width cannot be 0 or negative")
        else:
            return print(round(float(length * width), 2))
    except:
        print("Invalid input, make sure you only typed numbers")

while True:
    choice = input("\nChoose what geometric figure you want to calculate the area:\n\n1. Triangle\n2. Circle\n3. Rectangle\n\n")

    if choice == "1":
        triangle_area()
        break
    elif choice == "2":
        circle_area()
        break
    elif choice == "3":
        rectangle_area()
        break
    else:
        print("Invalid Choice")
    time.sleep(1)
    continue