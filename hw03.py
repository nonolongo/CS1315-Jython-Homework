# Noah Longhi
# nlonghi3@gatech.edu 
# I worked on the homework assignment alone, using only this semester's course materials.

# PROBLEM 1: Hide and Seek
def hideNSeek(x):
  print "Go!"
  for i in range(x):
    print(i+1)
  print "Ready or not, here I come!"

# PROBLEM 2: Mirror Mirror
def reflection(x):
  print str(x[::-1]) + str(x)
  
# PROBLEM 3: IMPORTANT PROBLEM
def important(words):
  for i in range(len(words)):
    x = words[i]
    print words[i] + " starts with the letter: " + x[0]
    
# PROBLEM 4: Spelling Bee
def spellingBee(word):
  print word
  for i in range(len(word)):
     x = word[i]
     print str(i) + ":" + " " + x
     
# PROBLEM 5: What do you meme?
def memeText(name, sentence):
  print str(name) + ": " + str(sentence)
  meme = ""
  i = -1
  for index in sentence:
    if i > 0:
      meme = meme + index.upper()
    else:
      meme = meme + index.lower()
    if index != "":
      i = i*-1
  print "Me: " + meme