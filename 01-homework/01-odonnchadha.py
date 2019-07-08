###  Domhnall O'Donnchadha
###  20190528
###  Homework 1


###  Intro
import datetime
now = datetime.datetime.now()
yrcur = now.year
name = input("What's your name, friend? ")
yrbirth = input("Pleasure to meet you! And if you don't mind my asking, what year were you born, "+name+"? ")
yrbirth = int(yrbirth)
if yrbirth < yrcur:
  print("Thanks! Very interesting . . . Here's a bit of trivia about your age.")
elif yrbirth >= yrcur:
  yrbirth = input("Are you certain you're being truthful with me, "+name+"? Let's try that year one more time. ")
  yrbirth = int(yrbirth)
  if yrbirth < yrcur:
    print("That's better! Very interesting . . . Here's a bit of trivia about your age.")
  else:
    print("Go home. You're drunk.")
    exit()

###  How old the user is (If date in the future, ask again & assume they'll do it right the second time)
usrage = yrcur-yrbirth
print("If you're", usrage-1, "or", usrage, "years old now, that means:")

###  How many times the user's heart has beaten (if more than a million, say "XXX million")
minpyr = 60 * 24 * 365
hrtrthmn = 65
if usrage*minpyr*hrtrthmn >= 1000000000:
  print("\t Your heart has beaten approximately", round(usrage*minpyr*hrtrthmn*.000000001,2), "billion times.")
elif usrage*minpyr*hrtrthmn >= 1000000:
  print("\t Your heart has beaten approximately", round(usrage*minpyr*hrtrthmn*.000001,2), "million times.")
else:
  print("\t Your heart has beaten approximately", usrage*minpyr*hrtrthmn, "times.")

###  How many times a blue whale's heart has beaten 
hrtrtbwh = 9
lfspnrbtw = 85
if usrage*minpyr*hrtrtbwh >= 1000000000:
  print("\t Comparatively, a blue whale's heart would have beaten only perhaps", round(usrage*minpyr*hrtrtbwh*.000000001,2), "billion times.")
elif usrage*minpyr*hrtrtbwh >= 1000000:
  print("\t Comparatively, a blue whale's heart would have beaten only perhaps", round(usrage*minpyr*hrtrtbwh*.000001,2), "million times.")
else:
  print("\t Comparatively, a blue whale's heart would have beaten only perhaps", usrage*minpyr*hrtrtbwh, "times.")

###  How many times a rabbit's heart has beaten
hrtrtrbt = 135
lfspnrbtw = 2
lfspnrbtd = 10
if usrage*minpyr*hrtrtrbt >= 1000000000:
  print("\t It's not a contest but a rabbit's heart would have clocked", round(usrage*minpyr*hrtrtrbt*.000000001,2), "billion heartbeats in that time.")
elif usrage*minpyr*hrtrtrbt >= 1000000:
  print("\t It's not a contest but a rabbit's heart would have clocked", round(usrage*minpyr*hrtrtrbt*.000001,2), "million heartbeats in that time.")
else:
  print("\t It's not a contest but a rabbit's heart would have clocked", usrage*minpyr*hrtrtrbt, "heartbeats in that time.")
print("\t Though pet rabbits usually only live about 10 years (versus 2 years if wild). So if it is in fact a contest, you're probably winning the long game.")
print("\t Maybe you can get a better handle on your own mortality by measuring your lifespan as", usrage/lfspnrbtd ,"domesticated rabbits (or", int(usrage/lfspnrbtw), "wild).")

###  How old they are in Venus years
yrven = 0.6156
print("\t If you instead counted your life by years as measured on Venus, you'd be able to report yourself as a youthful age "+str(int(usrage*yrven))+".")

###  How old they are in Neptune years
yrnep = 0.0061
print("\t But if you're going to bend the truth, go for broke and use Neptune's standard. There you'd only have "+str(round(usrage*yrnep*100,1))+"% of one year under your belt.")

###  Whether they are the same age as you, older or younger  /  If older or younger, how many years difference
myage = yrcur-1977
if myage > usrage and abs(myage-usrage) == 1:
  print("\t You're younger than I am, "+name+", but only by about", myage-usrage, "year.")
elif myage > usrage:
  print("\t You're younger than I am, "+name+", by about", myage-usrage, "years.")
elif myage < usrage and abs(myage-usrage) == 1:
  print("\t You're older than I am, "+name+", but only by about", usrage-myage, "year.")
elif myage < usrage:
  print("\t You're older than I am, "+name+", by about", usrage-myage, "years.")
elif myage == usrage:
  print("\t You and I are about the same age, "+name+", both being born in "+str(yrbirth)+".")

###  If they were born in an even or odd year
if yrbirth%2 == 1:
  print("\t This may come as a shock but you were born in an odd numbered year. According to an amateur numerology website I just consulted, this portends doom.")
else:
  print("\t This may come as a shock but you were born in an even numbered year. According to an amateur numerology website I just consulted, this portends doom.")

###  Which US President was in office when they were born (1935 onward)
if yrbirth >= 2017:
  uspres = "Donald Trump" 
  prnn = "He"
elif yrbirth >= 2009:
  uspres = "Barack Obama" 
  prnn = "He"
elif yrbirth >= 2001:
  uspres = "George W. Bush" 
  prnn = "He"
elif yrbirth >= 1993:
  uspres = "Bill Clinton" 
  prnn = "He"
elif yrbirth >= 1989:
  uspres = "George H. W. Bush" 
  prnn = "He"
elif yrbirth >= 1981:
  uspres = "Ronald Reagan" 
  prnn = "He"
elif yrbirth >= 1977:
  uspres = "Jimmy Carter" 
  prnn = "He"
elif yrbirth >= 1974:
  uspres = "Gerald Ford" 
  prnn = "He"
elif yrbirth >= 1969:
  uspres = "Richard Nixon" 
  prnn = "He"
elif yrbirth >= 1963:
  uspres = "Lyndon B. Johnson" 
  prnn = "He"
elif yrbirth >= 1961:
  uspres = "John F. Kennedy" 
  prnn = "He"
elif yrbirth >= 1953:
  uspres = "Dwight D. Eisenhower" 
  prnn = "He"
elif yrbirth >= 1945:
  uspres = "Harry S. Truman"
  prnn = "He"
elif yrbirth >= 1933:
  uspres = "Franklin D. Roosevelt"
  prnn = "He"
elif yrbirth <= 1932:
  uspres = "I dunno, Lincoln maybe"
  prnn = "He"
print("\t The President of the United States at the time of your birth was "+uspres+". "+prnn+" has never admitted to any role in that.")


###  US President Dictionary Test
#uspresidents = {
#  2017:"Donald Trump"
#  2009:"Barack Obama"
#  2001:"George W. Bush"
#  1993:"Bill Clinton"
#  1989:"George H. W. Bush"
#  1981:"Ronald Reagan"
#  1977:"Jimmy Carter"
#  1974:"Gerald Ford"
#  1969:"Richard Nixon"
#  1963:"Lyndon B. Johnson"
#  1961:"John F. Kennedy"
#  1953:"Dwight D. Eisenhower"
#  1945:"Harry S. Truman"
#  1933:"Franklin D. Roosevelt"
#  1929:"Herbert Hoover"
#  1923:"Calvin Coolidge"
#  1921:"Warren G. Harding"
#  1913:"Woodrow Wilson"
#  1909:"William Howard Taft"
#  1901:"Theodore Roosevelt"
#}
#for key, uspresident in uspresidents.items():
#  if yrbirth >= int(key):
#    print("\t The President of the United States at the time of your birth was "+uspresident+".")