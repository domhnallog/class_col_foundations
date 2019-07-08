###  Domhnall O'Donnchadha
###  20190604
###  Homework 3, Part 3

# Use csv.DictReader to practice with lists and dictionaries.
# Download the CSV file before you run this code.
import csv
csvfile = open('countries.csv', 'r')
reader = csv.DictReader(csvfile)
data = list(reader)
csvfile.close()
import statistics

# print("The data looks like", data)

# 1. What are the columns in our dataset?
print(f"The dataset columns (raw): {(data[0]).keys()}")

datak = (data[0]).keys()
columns = []
for datumk in datak:
  datumk = datumk.title().replace("Gdp", "GDP").replace("_", " ")
  columns.append(datumk)
seperator = ', '
print(f"The dataset columns (edited): {seperator.join(columns)}")

print("The dataset columns (list):")
for column in columns:
  print("   ", column)

# 2. How many countries do we have in our dataset?
print(f"There are {len(data)} countries total.")

# 3. How many countries in Asia? How about North America?    
count_asia = 0
count_namer = 0
for country in data:
  if country['Continent'] == 'Asia': 
    count_asia = count_asia + 1
  elif country['Continent'] == 'N. America': 
    count_namer = count_namer + 1
print(f"There are {count_asia} countries in Asia and {count_namer} in North America.")

# 4. What is the total population of the world?
pop_global = 0
for country in data:
  pop_global = pop_global + int(country['Population']) 
print(f"The total global population is {pop_global:,}.")

# 5. Which has a larger population, Africa or South America?
pop_samer = 0
pop_afric = 0
for country in data:
  if country['Continent'] == 'S. America': 
    pop_samer = (int(pop_samer)) + (int(country['Population']))
  if country['Continent'] == 'Africa': 
    pop_afric = (int(pop_afric)) + (int(country['Population']))
if pop_samer > pop_afric:
  pop_large = pop_samer 
  pop_large_cont = 'South America'
else:
  pop_large = pop_afric 
  pop_large_cont = 'Africa'
print(f"Of Africa and South America, {pop_large_cont} has the larger population with {pop_large:,}.")

# 6. Calculate the total GDP of each country and print it out (right now it's per capita).
for country in data            [:5]:
  country['GDP_gross'] = (int(country['GDP_per_capita']) * int(country['Population']))
  print(f"The country of {country['Country']} has a gross GDP of ${country['GDP_gross']:,}.")



# 7. What is the median life expectancy of the world?
lifexp = float(country['life_expectancy'])
print(statistics.median(lifexp))
# for country in data            [:5]:
#   # print(country['life_expectancy'])
#   lifexp = country['life_expectancy']
#   # print(lifexp)
#   # print((statistics.median(lifexp)))
#   expc = [[statistics.median] for lifexp in data]
#   print(expc)
  # # lifexp_global_med = lifexp_global_med + float(statistics.median(country['life_expectancy'])) 
# print(f"The global median life expectancy is {lifexp_global_med}.")

# 8. What is the median life expectancy of Europe?
# lifexp_europ_med = 0
# for country in data:            #[:5]:
#   lifexp_europ_med
#   if country['Continent'] == 'Europe': 
# print(f"The global median life expectancy is {lifexp_global_med}.")


# 9. Print out each country that has a below-average life expectancy.

# 10. Print out each country that has a below-average GDP but an above-average life expectancy.

# 11. Calculate the 75th percentile of GDP.

# 12. What percent of the world population has a life expectancy of below 50 years? Above 80 years?

# TIPS
# You know how to get a median if given a list of numbers. For some of these it might be helpful to use your for loop to create a new list of numbers, then calculate the median from it.
# ...for example, with "What is the median life expectancy of Europe?", you'll need to make a new list of only the life expectancies of Europe, then get the median of that list. You'll rely on .append for that (although I'll also teach you a method called list comprehensions).
# You know how to calculate the 50th percentile - it's the median of ALL of the values. The 75th percentile should be the 50th percentile of only the top 50% of the values.
# Feel free to use list comprehensions if they make sense to you!