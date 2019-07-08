# There is nothing in this file.
print("Hello world")

name = "Smush"
name2 = "Stumpy"
name3 = "Boy Abby"

print(name)
print(name2)
print(name3)

# This is a list!
# It can store multiple pieces of information!
names = ["Smush", "Stumpy", "Boy Abby"]

print(names)

# len will tell you how long a list is
print(len(names))

# len will tell you how long a string is
print(len("Smushface"))

number_of_cats = len(names)
print(f"I have {number_of_cats} cats")

# We have people! With ages!
ages = [4, 50, 32, 13, 102]

# But how many people???
print(f"We have {len(ages)} people")

# functions - print, len, etc
# print is a function, it prints stuff
# len is a function, it counts stuff

print(len(ages))

print("The largest age is", max(ages))
print("The smallest age is", min(ages))
print("The total of all the ages is", sum(ages))

# "standard library"
# libraries, packages, modules
import statistics

print("The median age is", statistics.median(ages))
print("The mean age is", statistics.mean(ages))
print("The variance of the ages is", statistics.stdev(ages))


print("Hello", names)

# Say hello to each of my cats
for name in names:
  print("Hello", name)

# "Give me the first thing in names"
name = names[0]
print(name)

# "Give me the second thing in names"
name = names[1]
print(name)

# "Give me the third thing in names"
name = names[2]
print(name)

# Say hello to each of the ages??
# If you are ___ years old, you were born in _____
# ages = [4, 50, 32, 13, 102]
for age in ages:
  year = 2019 - age
  print(f"Hello {age}, you were born in {year}")


# First age
print(ages[0])
# Second age
print(ages[1])
# Last age
print(ages[-1])
# Second to last age
print(ages[-2])

# print(ages[100])

name_smush = "Smush"
age_smush = 12
color_smush = "tabby"

name_stumpy = "Stumpy"
age_stumpy = 11
color_stumpy = "white and tabby"

# a ****dictionary****
smush = {
  'name': 'Smush',
  'age': 12,
  'color': 'tabby'
}

# name, age and color are called KEYS
# Stumpy, 11, white and tabby are called VALUES
stumpy = {
  'name': 'Stumpy',
  'age': 11,
  'color': 'white and tabby'
}

print(smush['name'])
print(stumpy['color'])


print(smush.keys())
print(smush.values())

# I'm real mean
print("How many things do we know about smush?", len(smush.keys()))

