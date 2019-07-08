#  There was nothing in this file.
print("Hello world!")

name = "Smush"
name2 = "Stumpy"
name3 = "Boy Abby"

print(name)
print(name2)
print(name3)

#  functions (eg print, len, etc.) & lists (bracketed [])

names = ["Smush","Stumpy", "Boy Abby"]
print(names)
print(len(names))

num_cats = len(names)
print(f"Soma has {num_cats} cats.")

name = names[0]   # 0 is first item in the list
print(name)
name = names[1]   # 1 is the second
print(name)
name = names[-1]   # -1 is the last item in the list
print(name)

#  the "standard library" 

ages = [4, 50, 32, 13, 102]

print(ages)
print(f"We recorded {len(ages)} ages.")
print(f"The largest (maximum recorded) age is {max(ages)}.")
print(f"The smallest (minimum recorded) age is {min(ages)}.")
print(f"The total (sum) of all the ages is {sum(ages)}.")

#  import libraries (aka packages, modules) 

import statistics
print(f"The median age is {statistics.median(ages)}.")
print(f"The mean age is {statistics.mean(ages)}.")
print(f"The variance of the ages is {statistics.variance(ages)}.")
print(f"The standard deviation of the ages is {statistics.stdev(ages)}.")

print(f"Hello, {names}.")
for name in names:
  print(f"Hello, {name}.")

year_current = 2019
for age in ages:
  print(f"Happy birthday, {age} year old you. You were probably born in {year_current-age}")

# or better
for age in ages:
  year_birth = year_current-age
  print(f"Happy birthday, {age} year old you. You were probably born in {year_birth}")

#   attributes
name_smush = "Smush"
age_smush = 12
color_smush = "tabby"

name_stumpy = "Stumpy"
age_stumpy = 11
color_stumpy = "tabby"


#   dictionaries (curly {})
smush = {
  "name": "Smush",
  "age": 11,
  "color": "tabby"
}

stumpy = {
  'name': 'Stumpy',
  'age': 11,
  'color': 'white and tabby'
}

print(smush['name'])
print(stumpy['color'])

# name, age, color are KEYS
# Smush, 11, tabby are VALUES

print(smush.keys())
print(smush.values())







