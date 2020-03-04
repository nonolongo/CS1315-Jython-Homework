# Noah Longhi
# nlonghi3@gatech.edu 
# I worked on the homework assignment alone, using only this semester's course materials.

# PROBLEM 1: Why do Nickels Exist?
def change(money):
  print "You recieved an even $" + str(int(money)) +  " dollars back."
  
# PROBLEM 2: Shapes{s} of You
def approachAllAngles(numOfSides):
  D = ((numOfSides - 2)*180)/numOfSides
  print "Each angle in a regular polygon with " + str(numOfSides) + " sides measure " + str(D) + "."

# PROBLEM 3: ABC, Easy as [1],[2],[3]
def sortMusic(artistName):
  print str(artistName) + " starts with the letter " + str(artistName[0:1])+ "."
  
# PROBLEM 4: Storm Area 51, They Can't Stop All of Us
def decoder(word1, word2):
  print str(word1[0::2]), str(word2[1::2])
  
# PROBLEM 5: High Steaks Computer Problem
def nope(word):
  x = len(word)
  y = (x - 3)/2
  z = (x/2) + 2
  print str(word[0:y:1]) + str(word[z::1])
  
  
  
  