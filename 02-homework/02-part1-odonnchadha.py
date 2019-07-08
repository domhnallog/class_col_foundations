###  Domhnall O'Donnchadha
###  20190530
###  Homework 2, Part 1


# Part 1: Lists

numberlist = [22, 90, 0, -10, 3, 22, 48]
import statistics

print(f"The list: {numberlist}")
print(f"The number of elements: {len(numberlist)}")
print(f"The fourth element: {numberlist[3]}")
print(f"The sum of the second and fourth: {numberlist[1]+numberlist[3]}")
print(f"The largest element: {max(numberlist)}")
print(f"The second largest element: {sorted(numberlist)[-2]}")
print(f"The last element: {numberlist[-1]}")
print(f"The sum of all elements, halved: {sum(numberlist)/2}")
numlistmed = statistics.median(numberlist)
numlistmean = statistics.mean(numberlist)
if numlistmed > numlistmean:
  print(f"The higher of the median or mean: The median ({numlistmed} compared to {numlistmean})")
elif numlistmean > numlistmed:
  print(f"The higher of the median or mean: The mean ({numlistmean} compared to {numlistmed})")

# Part 2: Dictionaries  

movie = {
  'title': 'The Jerk',
  'year': 1979,
  'director': 'Carl Reiner'
}
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and directed by", movie['director'])
movie['budget'] = 4000000
movie['revenue'] = 73691419
if movie['revenue'] < movie['budget']:
  print(f"The film cost ${movie['budget']-movie['revenue']:,} more than it earned. That was a bad investment.")
elif movie['revenue'] >= (movie['budget']*5):
  print(f"The film earned ${movie['revenue']:,}, {int(movie['revenue']/movie['budget']):,}x its costs. That was a great investment.")
else:
  print(f"The film earned ${movie['revenue']:,} on a budget of ${movie['budget']:,}. That was a fine investment.")

population = {
  'Bronx': 1400000,
  'Brooklyn': 2600000,
  'Manhattan': 1600000,
  'Staten Island': 470000,
  'Queens': 2300000
}
print(f"The population of Brooklyn: {population['Brooklyn']:,}")
print(f"The combined population of all boroughs: {sum(population.values()):,}")
print(f"The percent of NYC's population in Manhattan: {round((100 * (population['Manhattan']/sum(population.values()))),1)}%")
