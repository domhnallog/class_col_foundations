## PYTHON PARTS

# SYNTAX HIGHLIGHTING

# To get your Python skills together, you'll use my tutorial from http://littlecolumns.com/learn/python/ - going up to chapter 13 is probably a good idea.

# Inspired by the BBC's "Your life on earth" - http://www.bbc.com/earth/story/20141016-your-life-on-earth - we will be creating a program to analyze the year a user was born in.

# Please create a brand new file named homework-01-lastname.py
# The first line should be a comment with your full name
# The second line should be a comment with the date
# The third line should be a comment "Homework 1"

# When run from the command line, this file should
# 1. Prompt the user for their year of birth, and tell them (approximately):

year = input("What year were you born? ")

# I'm going to be comparing this year to a lot of numbers,
# so it should probably always be a number
year = int(year)
print(year)

# 2. How old the user is
age = 2019 - year
print(age)

# 3. How many times the user's heart has beaten

# "magic number"
heartbeats = age * 42000000

# making a bunch of variables for readability
bpm = 75
beats_per_year = bpm * 60 * 24 * 365
heartbeats = age * beats_per_year

# Hoping you remember what the numbers mean
heartbeats = age * 75 * 60 * 24 * 365

print(heartbeats)

# 4. How many times a blue whale's heart has beaten
whale_heartbeats = age * 8 * 60 * 24 * 365
print("The whale's heart has beaten " + str(whale_heartbeats) + " times")

print("The whale's heart has beaten", whale_heartbeats, "times")

print(f"The whale's heart has beaten {whale_heartbeats:,} times")

print("The whale's heart has beaten {0} times".format(whale_heartbeats))


# 5. How many times a rabbit's heart has beaten
rabbit_heartbeats = age * 130 * 60 * 24 * 365
print(rabbit_heartbeats)
if rabbit_heartbeats > 1000000:
  million_heartbeats = int(rabbit_heartbeats / 1000000)
  print(f"The rabbit's heart has beaten {million_heartbeats} million times")

# 6. If the answer to (5) is more than a million, say "XXX million" instead of the very long raw number
# 7. How old they are in Venus years
# 8. How old they are in Neptune years
# 9. Whether they are the same age as you, older or younger
# 10. If older or younger, how many years difference
# 11. If they were born in an even or odd year
# 12. Which US President was in office when they were born (1935 onward)


# D R Y
# Don't
# Repeat 
# Yourself
# If someone says they were born in the future, try asking them again (assume they'll do it right the second time).

# https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States



if year >= 2017:
  print("Trump")
#elif int(year) >= 2009 and int(year) <= 2017:
#elif 2017 >= int(year) >= 2009:
elif year >= 2009:
   print("Obama")
elif year >= 2001:
   print("W Bush")
elif year >= 1993:
   print("Clinton")
#elif year >= 1989:
elif year > 1988:
   print("HW Bush")
else:
  print("Someone else")

# If you do this, watch your ordering
# if year >= 1989:
#   print("HW Bush")
# elif year >= 1993:
#   print("Clinton")
# elif year >= 2001:
#   print("W Bush")
