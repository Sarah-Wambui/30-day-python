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

# slicing items from a List
f = ['banana', 'orange', 'mango', 'lemon','lime','apple']
all_fruits = f[0:6]
all_fruit = fruit[0:]
orange_and_mango = f[1:3]
print(all_fruits)
print(all_fruit)
print(orange_and_mango)

# Mofifying Lists
many_fruits =  ['banana', 'orange', 'mango', 'lemon']
many_fruits[0] = 'avocado'
print(many_fruits)
many_fruits[1] = 'apple'
print(many_fruits)

# Checking Items in a List
fruite =  ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruite
print(does_exist)
do_exist = 'lime' in fruite
print(do_exist)

# Adding Items to a List
fruite.append('lime')
print(fruite)
fruite.append('apple')
print(fruite)

# Inserting Items into a List
# We can use insert() method to insert a single item at a specified index in a list.
# insert(index, item)
fruite = ['banana', 'orange', 'mango', 'lemon']
fruite.insert(2, 'apple')
print(fruite)
fruite.insert(3, 'lime')
print(fruite)

# Removing Items from a List
# remove(item)
# The remove method removes a specified item from a list
fruite = ['banana', 'orange', 'mango', 'lemon']
fruite.remove('banana')
print(fruite)
fruite.remove('lemon')
print(fruite)

# Removing Items Using pop
# Remove the last item if not specified index
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)
# Remove the item at the specified index
fruit.pop(0)
print(fruit)

# Removing Items using del
#  The del keyword removes the specified index and it can also be used to delete items within index range.
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)

# Copying a List
# It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1.
fruits  = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

# Joining Lists
# There are several ways to join, concatenate, two or more lists in Python
# Plus OPerator(+)
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
# Joining using extend
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)

# Counting Items in a list
# The count() method returns the number of times an item appears in a list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           

# Reversing a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)

# Sorting List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
