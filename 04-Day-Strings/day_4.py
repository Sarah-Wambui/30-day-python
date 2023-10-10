# Any data type written as text is a string.
# Any data type under single, double of tripple quote are strings
# To ckeck the length of a string use the len() method

# A string could be a single character
letter = "S"
print(letter)

# a string with single quotes
greetings = 'Hello, World!'
print(greetings)
print(len(greetings))

# String with double quotes
sentence = "Never once has it closed your mind that life is too short."
print(sentence)

# String with tripple quotes
multiple_string = """ While the world looks upon me as I struggle alone
they say I have nothing but they are so wrong, in my heart I'm rejoicing
Ihow wish they could see, thank you Lord for your blessings on me.
"""
print(multiple_string)

# String Concatenation
first_name = "Sarah"
last_name = "Wambui"
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(first_name) > len(last_name))

# Escape Sequences in Strings
#  In Python and other programming languages \ followed by a character is an escape sequence.
#  \n: new line
print("I hope everyone is enjoying the Python Challenge. \n Are you? ")


# String Formatting
# In Python there are many ways of formatting strings.
# Another new string formatting is string interpolation, f-strings
fname = "Asabenah"
lname = "Yetayeh"
language = "Python"
formated_string = f"I am {fname} {lname}. I teach."
print(formated_string)

    # Python String as Sequences of Characters
# In Python strings are sequences of characters, and share their basic methods
# of access with other Python ordered suquences of objects- lists ans tuples

# Unpacking Characters
# The simpliest way of extracting single characters from strings is to unpack them into correspind variables
languages = "Python"
a, b, c, d, e,f = languages
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Accessign Characters in Strings by index
# In programming counting starts from zero. 
# Therefore the first letter of a string is at zero index and the last letter of a string is the length of a string minus one.
lang = "Python"
first_letter = lang[0]
print(first_letter)
second_letter = lang[1]
print(second_letter)
last_index = len(lang) - 1
last_letter = lang[last_index]
print(last_letter)
l_name = lang[-1]
print(l_name)

# Slicing Python Strings
# In Python we can slice strings into substrings

l = "Python"
first_three = l[0:3]   #starts at zero index and up to 3 but not include 3
print(first_three)
last_three = l[3:6]
print(last_three)

# Reversing a string
# We can easily reverse strings in Python
greetings = 'Hello World!'
print(greetings[::-1])
# Sllicing Characters while slicing
# It is possible to skip characters while slicing by passing step argument to clice method
lan = "Python"
pto = lan[0:6:2]
print(pto)

# String Methods
# 1. captitalize() -- Converts the first character of string to capital letter
challenge = "thirty days of python"
print(challenge.capitalize())

# 2. count()
# returns occurrences of substring in string
song = "This is a song from my heart"
print(song.count("s"))

# 3. endswith()
# Checks if a string ends with a specified ending
wind = "You don't know where it comes from or where it is going"
print(wind.endswith("ing"))
print(wind.endswith("tion"))

