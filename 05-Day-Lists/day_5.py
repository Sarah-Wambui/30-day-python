# List 
# is a collection which is ordered and changeable(modifiable). Alllow duplicate members
# Can be empty or it may have different data type items

# How to create a List
# a. Using list built-in function
lst = list()
print(lst)

# b. Using square brackets, []
l = []
print(len(l))

# We use len() to find the length of a list
fruits = ['bananas', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'potato', 'cabbage', 'onion', 'carrot']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'MongoDB', 'Python', 'Flask']

print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))

# lists can have different data types
list_data = ['Sarah', 250, True, {'country':'Finland', 'city':'Helsinki'}]

# Accessing List items using Positive indexing
fruit = ['bananas', 'orange', 'mango', 'lemon']
first_fruit = fruit[0]
last_index = len(fruit) - 1
last_fruit = fruit[last_index]
print(first_fruit)
print(last_fruit)

# Accessing List Items Using Negative indexing
frt = ['bananas', 'orange', 'mango', 'lemon']
first_f = frt[-4]
last_f = frt[-1]
print(first_f)
print(last_fruit)

# Unpacking List Item
ls = ['banana', 'orange', 'mango', 'lemon','lime','apple']
fruit0, fruit1, fruit2, fruit3, *rest = ls
print(fruit0)
print(fruit1) 
print(fruit2) 
print(fruit3) 
print(rest)  
