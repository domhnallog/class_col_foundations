# Question 1
# What is the output of the code below?
i = 5
print(5 * 5) # 25
print(i) # 5
print("cat" + "dog") # catdog
print("cat", "dog") # cat dog
print("cat", 5, 4, "dog") # cat 5 4 dog
print("i") # i

# Question 2
# What is wrong here????
print("5" + "5") # 55
print(5 + 5) # 10
print(str(5) + "5") # 55
print(5 + int("5")) # 10

print("Hello")
Hello = 12345
print(Hello)

# Question 3
# What's wrong with this statement?
n = 2 # n is now 2
n == 25 # This line doesn't do anything
print(n == 25) # False
print(n) # Prints "2"
if n == 2:
  print("two")

# Question 4
# The command to list the files in a directory
# ls : all the files in a directory
# ls -l : in a long long list
# ls -la : also shows hidden files

# Question 5 is MISSING

# Question 6


# elif => Python
# elsif => Ruby
# else if

# if n == 100:
#   print("great job!!")
# elif n > 50:
#   print("you did fiiiiine I guess")
# else:
#   print("you didn't do a great job???")

n = -5
print(n)
if n > 0:
  print("A")
  if n >= 3:
    print("B")
    print("C")
  elif n > 2:
    print("D")
  else:
    print("E")
elif n > -2:
  print("F")
else:
  print("G")
if n < 5:
  print("H")
