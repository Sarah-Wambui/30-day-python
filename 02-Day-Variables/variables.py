import math
# Variables in python

first_name = "Sarah"
last_name = "Wambui"
country = "Kenya"
city = "Nairobi"
age = 27
is_married = False
skills = [ "HTML", "CSS", "JS", "React", "Python", "Flask"]
person_info  = {
    "first_name": "Sarah",
    "last_name" : "Wambui",
    "country": "Kenya",
    "city": "Nairobi"
}

# Printing the values stored in the varibles

print("First name:", first_name)
print("First name length:", len(first_name))
print("Last name:", last_name)
print("Last name length:", len(last_name))
print("Country:", country)
print("City:", city)
print("Age:", age)
print("Married:", is_married)
print("Skills:", skills)
print("Personal Info:", person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = "Sebastian", "Mwangi", "Kenya", 2, False
print(first_name, last_name, country, age, is_married)


# Exercise level 2
# 1. check the data types of variables using type()
print(type(first_name))
print(type(age))
print(type(skills))
print(type(person_info))

# 2. Use len()
print(len(first_name))
#  Int has no len() print(len(age))
print(len(skills))
print(len(person_info))

# 3. compare the length of first_name and last_name
if len(first_name)  > len(last_name):
    print("first name is longer than last name")
else:
    print("last name is longer than first name")

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# i. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)

# ii. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)

# iii. Multiply num_two and num_one and assign the value to a variable product
product= num_one * num_two
print(product)

# iv. Multiply num_two and num_one and assign the value to a variable product
division = num_one / num_two
print(division)

# v. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two
print(remainder)

# v. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)

# vii. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = (num_one / num_one)
print(math.floor(floor_division))

#  5. The radius of a circle is 30 meters
# i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
r = 30 
area_of_circle = math.pi * (30 ** 2)
print(area_of_circle)
# ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = r * 2
print(circum_of_circle)

# iii. Take radius as user input and calculate the area.
radi= float(input("The radius of circle is:  " ))
area_circle = math.pi * (radi * 2)
print(area_circle)

# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("My first_name is:  ")
last_name = input("My last_name is:  ")
country = input("I come from:  ")
age = input("My age is:  ")
print("First name is :", first_name)
print("Last name is :", last_name)
print("I come from a country called:", country)
print(f"I am {age} years old" )

# 7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
# python3
# >>> help("keywords")
# Here is a list of the Python keywords.  Enter any keyword to get more help.

# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not   

