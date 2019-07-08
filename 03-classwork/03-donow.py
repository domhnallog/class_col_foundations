# # 1) I have a list called bubblegum. How do I get the first element? The last element?
#  bubblegum[0]
#  bubblegum[-1]

# # 2) What function or method…
# #  …tells how many elements are in a list?
# len(bubblegum)
# # …replaces text in a string with other text?
# name.replace("o","a")
# # …gives you the keys of a dictionary?
# movie.keys()



# 3) What is the output of the following code? Which lines give you errors?

# borough_name = 'Manhattan'
# z = [ 'Manhattan', 'Queens' ]                          
# x = { 'borough_name': 'Manhattan', 'population': 500 } 
# y = {
# 'Manhattan': 500,
# 'Queens': 200
# }

# print x['borough_name']
# print x[borough_name]
# print x[0]
# print y['borough_name']
# print y[borough_name]
# print y[0]
# print z['borough_name']
# print z[borough_name]
# print z[0]

###EDITED
borough_name = 'Manhattan'
z = [ 'Manhattan', 'Queens' ]       #list
x = {                               #dict
'borough_name': 'Manhattan',
'population': 500 }  
y = {                               #dict
'Manhattan': 500,
'Queens': 200
}

print(x['borough_name'])    #prints manhattan
print(x[borough_name])      #key not found, it's a list, use the next
print(x[0])
print(y['borough_name'])
print(y[borough_name])      #bname is a string, so 
print(y[0]                  #key not found, it's a list, use the next
print(z['borough_name'])    #error
print(z[borough_name])
print(z[0])

# 4)  Print out each art piece’s name. 
# art_pieces = [
# { ‘title’: ‘Gold Star’, ‘year’: 1805 }, 
# { ‘title’: ‘Blunderbuss‘, ‘year’: 1800 },
# { ‘title’: ‘Chairlift’, ‘year’: 1976 },
# { ‘title’: ‘Rancor’, ‘year’: 2002 }
# ]

# 5) Given the following, write code to calculate how many murders we have in total.

murders = { 'Albany': 23, 'Kings County': 10, 'Rochester': 7, 'Yonkers': 9 }

# sloppy
murders['Albany'] + murders['Kings County'] + murders['Rochester'] + murders['Yonkers']

#nice!
sum(murders.values())


other_murders = [
  { 'name': 'Albany', 'murders': 23 }
  { 'name': 'Kings County', 'murders': 10 }
  { 'name': 'Rochester', 'murders': 7 }
  { 'name': 'Yonkers', 'murders': 9 }

  murder_count = [other['murders'] for other in other_murders]
  sum(murder_count)