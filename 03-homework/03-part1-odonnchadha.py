###  Domhnall O'Donnchadha
###  20190604
###  Homework 3, Part 1

numbers = [4, 5, 1, 10, 200, 34, 22, 19, 43, 56, 32, 11, 40, 82, 23, 43, 12, 65, 10]
print(f"The list of numbers: {numbers}")

# 1. Count how many numbers are in the list. Use a for loop, do NOT use len.
num_count = 0
for number in numbers:
  num_count = num_count + 1
print(f"Count of numbers: {num_count}")

# if num_count == len(numbers):
#   print("Count of numbers is correct")

# 2. Use a Python method to add a new number to the list. You can pick the number!
numbers.append(55)                  # append() takes exactly one argument
numbers.extend([99, 77])
print(f"The new list of numbers: {numbers}")


# 3. Count how many even numbers are in the list. Use a for loop.
even_count = 0
for number in numbers:
  if number%2:
    even_count = even_count +1
print(f"Count of evens: {even_count}")

# 4. Count how many values are above the mean and how many are below the mean. Use one for loop.
import statistics
num_mean = statistics.mean(numbers) 
above_count = 0
below_count = 0
equal_count = 0
for number in numbers:
  if number > num_mean:
    above_count = above_count + 1
  elif number < num_mean:
    below_count = below_count + 1
  elif number == num_mean:
    equal_count = equal_count + 1
print(f"Count above the mean: {above_count}")
print(f"Count below the mean: {below_count}")
# print(f"Count equal to the mean: {equal_count}")

# 5. Total up the numbers. Use a for loop, do NOT use sum().
num_total = 0
for number in numbers:
  num_total = num_total + number
print(f"Sum of the numbers: {num_total}")

# if num_total == sum(numbers):
#   print("Total of numbers is correct")

# 6. Total up the numbers that are above the mean, and total up the numbers below the mean. Use one for loop, and do not use sum().
above_sum = 0
below_sum = 0
for number in numbers:
  if number > num_mean:
    above_sum = above_sum + number
  elif number < num_mean:
    below_sum = below_sum + number
print(f"Sum above the mean: {above_sum}")
print(f"Sum below the mean: {below_sum}")

# 7. Find the largest number. Use a for loop.
num_largest = 0
for number in numbers:
  if number > num_largest:
    num_largest = number
print(f"Largest number: {num_largest}")

# 8. You have a list of dogs, shown below. BUT YOU GOT ANOTHER DOG!!! His name is Maxwell, please add him to the list.
#   Do NOT just edit the line to be ..., "Blartsburg", "Maxwell" ]
dogs = ["Sparky", "Jane", "Matilda", "Blartsburg"]
print(f"The list of dogs: {dogs}")
dogs.extend(["Maxwell"])
print(f"The new list of dogs: {dogs}")

# 9. Make a list of all dogs that have names of 5 characters or less. Use a for loop.
dog_shortname = list()      # previous test: dog_shortname = '', [], list()  results in empty quotes or brackets
for dog in dogs:
  if len(dog) <= 5:
    dog_shortname = dog_shortname, dog
print(f"The dog(s) with a shortname: {dog_shortname}")

bad_dogs = [aaa.replace('a', 'y') for aaa in dogs]
print(f"Mispelling dogs with replace: {bad_dogs}")

# 10. I'm on a web page with some links about Zurich, and the URL looks like this: http://important-swiss-things.ch/docs/download/ZH (no, it isn't a real URL). Bern is another canton - its abbreviation is BE, so its URL is http://important-swiss-things.ch/docs/download/BE. I want to get this link for every single canton in Switzerland, not just Zurich and Bern, BUT I don't want to type each URL manually. If I give you this list of the canton abbreviations, can you print out all of the URLs?
cantons = [ "ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO", "BS", "BL", "AR", "AI", "SG", "GR", "AG", "TG", "TI", "VD", "VS", "NE", "GE", "JU"]
swiss_url = "http://important-swiss-things.ch/docs/download/"
for canton in cantons:
  print(swiss_url+canton)

# 11. I'm trying to get some top-secret documents from top-secret-secrets.com, and while I know the URL pattern I don't want to type them all out individually! Each secret document has a document ID and is made up of 12 pages, pages "001.pdf" through "012.pdf". Each page is available at a different URL. For example, for the document ID of QQ7LTHM, the pages are available at

# www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/001.pdf
# ...
# www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/012.pdf
document_ids = ['qq7lthm', 'jemsqhg', 'O6itcke', 'cp4Iua0', 'bkijcmo', 'ctoyjrm', 'z8wc6xy', 'zk4Bmm0']
for docid in document_ids:
   docid = docid.upper()
   for i in range(1,13):
    page_no = i
    print(f"http://www.top-secret-pdfs.com/content/secrets/{docid}/page/{page_no:03}.pdf")
