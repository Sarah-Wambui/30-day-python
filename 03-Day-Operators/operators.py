# Boolean
# A boolean data type represents one of the two values: True or False
print(True)
print(False)

     # Operators
# 1. Assignment Operators
# Used to assign values to variables
x = 5
print(x)

# 2. Arithmetic operators
# Addition(+): a + b
# Subtraction(-): a - b
# Multiplication(*): a * b
# Division(/): a / b
# Modulus(%): a % b
# Floor division(//): a // b
# Exponentiation(**): a ** b


# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 9 it means 2 * 2 * 2


#  Exercises- Day 3
# 1. Declare your age as integer variable
age = 27

# 2. Declare your height as a float variable
height = 5.3

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter base:  "))
height = float(input("Enter height:  "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

# 5.  Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter side a:  "))
side_b = float(input("Enter side b:  "))
side_c = float(input("Enter side c:  "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter length:  "))
width = int(input("Enter width:  "))
area_rectangle = length * width
perim = 2 * (length * width)
print(f"The area of rectangle is {area_rectangle}")
print(f"The perimeter of the rectangle is {perim}")

# 7. Use and operator to check if 'on' is found in both 'python' and 'dragon'
if "on" in "python" and "dragon":
    print("on is in both python and dragon")
else:
    print("on is not in present")

# 8. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
pyt= len("python")
drag = len("dragon")
print(pyt)
print(drag)
if pyt > drag:
    print(False)
else:
    print(True)

# 9. Check if type of '10' is equal to type of 10
if type("10") == type(10):
    print("They are of same type")
else:
    print("They are of diferrent data types.")


# 10. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours:  "))
rate = int(input("Enter rate per hour:  "))
earning = hours * rate
print(f"Your weekly earning is {earning}")
