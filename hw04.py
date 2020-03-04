# Noah Longhi
# nlonghi3@gatech.edu 
# I worked on the homework assignment alone, using only this semester's course materials.

# PROBLEM 1: A Super Fun Problem
def soup(string):
  if len(string) != 4:
    print "That word is not soup."
    return
  for ch in string:
    if ch in "SOUPsoup":
      x = 1
    else:
      x = -1
  if x == 1:
    print "That word is soup."
  else:
    print "That word is not soup."

# PROBLEM 2: High Roller
def blackjack(card):
  if card == 8:
    print card + 13
    print "Congratulations! You win!"
  if card < 8:
    print card + 13
    print "You're still alive. Hit or stand?"
  if card > 8:
    print card + 13
    print "Bust. Sorry, you lose."
    
# PROBLEM 3: cRHYME Against Humanity # FINISH
def rhyme(words):
  print "Words that rhyme with cat:"
  list = words.split(",")
  for each in list:
    x = each[-1:-3:-1]
    if x == "ta":
      print each
      
# PROBLEM 4: Queue Up
def noPuns(words):
  y = 0
  for each in words:
    x = each[0:1]
    if x == "Q":
      y = y + 1
    if x == "q":
      y = y + 1
  print "There are " + str(y) + " words that start with Q."
# PROBLEM 5: MAXnificent
def maximum(numbers):
  x = 0
  y = 0
  for each in numbers:
    if each%2 == 0:
      if x > each:
        pass
      if x < each:
        x = each
  print "The largest even number in the list is " + str(x) + "."
  for each in numbers:
    if each%2 == 1:
      if each > y:
        y = each
      if each < y:
        pass
    
  print "The largest odd number in the list is " + str(y) + "."
      

