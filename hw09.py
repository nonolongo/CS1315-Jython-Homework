# Noah Longhi
# nlonghi3@gatech.edu 
# I worked on the homework assignment alone, using only this semester's course materials.

# PROBLEM 1: F in the Chat
def fInTheChat(filename):
  f = open(getMediaPath() + filename, "r")
  lines = f.readlines()
  y = 0
  emptyString = ""
  for each in lines:
    words = each.split(" ")
    for i in words:
      if i == "":
        pass
      x = i[0:1]
      if x == "F":
        y += 1
      if x == "f":
        y += 1
  if y > 10:
    y += 2
  print "There are " + str(y) + " words that start with f."
  for each in range(y):
    emptyString += "f in the chat. "
  print emptyString
  f.close()

# PROBLEM 2: Solo Words
def firstWords(filename):
  f = open(getMediaPath() + filename, "r")
  lines = f.readlines()
  emptyString = ""
  emptyList = []
  for each in lines:
    each = each.strip()
    words = each.split(" ")
    emptyList += words[0:1]
  for each in emptyList:
    emptyString += each + "\n"
  print emptyString
  f.close()


# PROBLEM 3: Boring
def lines(filename):
  f = open(getMediaPath() + filename, "r")
  line = f.readline()
  str = ""
  while line != "":
    str += line
    line = f.readline()
  starredList = str.split("\n")
  x = 0
  for i in starredList:
    if x%2 == 0:
      print i + "\n"
      x += 1
    else:
      x += 1
  f.close()

# PROBLEM 4: So Very Boring
def variety(word):
  f = open(getMediaPath() + "boring.txt", "w")
  x = word
  y = word[::-1]
  z = ("\n")
  f.write(x + z)
  f.write(y + z)
  f.write(x + y + z)
  f.close()

# PROBLEM 5: Code for the Ages
def goldenAges(list1, list2):
  f = open(getMediaPath() + "TAages.txt", "w")
  list1 = list1[::-1]
  for x in range(len(list1)):
    f.write(list1[x] + " is " + str(list2[x]) + " years old.\n")
  f.close()

