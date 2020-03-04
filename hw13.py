# Noah Longhi
# nlonghi3@gatech.edu 
# I worked on the homework assignment alone, using only this semester's course materials

# PROBLEM 1: It's Morse, of Course
def morseCode(message):
  code = {"A":".-","E":".","I":"..","O":"---","U":"..-"}
  s = message
  l = list(s)
  str = ""
  for each in l:
    if each in "Aa":
      str += code["A"]
      continue
    if each in "Ee":
      str += code["E"]
      continue
    if each in "Ii":
      str += code["I"]
      continue
    if each in "Oo":
      str += code["O"]
      continue
    if each in "Uu":
      str += code["U"]
      continue
    else:
      str += each
  print str
  
# PROBLEM 2: Holiday Follies
def christmasCard(foreground, background):
  fg = makePicture(foreground)
  bg = makePicture(background)
  w = getWidth(bg)
  h = getHeight(bg)  
  picture = makeEmptyPicture(w,h)
  for x in range(w):
    for y in range(h):
      pix = getPixelAt(bg, x, y)
      c = getColor(pix)                  
      pix2 = getPixelAt(picture, x, y)
      setColor(pix2, c)
  pixels = getPixels(picture)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    x = getX(p)
    y = getY(p)
    if x <= w*1/3:
      setRed(p, r*2)
      setGreen(p, g*0.5)
      setBlue(p, b*0.5)
    if x>=w*1/3 and x<=w*2/3:
      setRed(p, r*2)
      setGreen(p, g*2)
      setBlue(p, b*2)
    if x >= w*2/3:
      setRed(p, r*0.5)
      setGreen(p, g*2)
      setBlue(p, b*0.5)
  fgH=getHeight(fg)
  fgW=getWidth(fg)
  for x in range(getWidth(fg)):
    for y in range(getHeight(fg)):
      sPix=getPixelAt(fg, x, y)
      sClr=getColor(sPix)
      dstX = x+(w*1/2)-(fgW/2)
      dstY = y+(h*1/2)-(fgH/2)
      d = distance(sClr, white)
      if d > 20:
        dPix= getPixelAt(picture, dstX, dstY)
        setColor(dPix, sClr)
  myFont = makeStyle("Verdana", bold, 48)
  addTextWithStyle(picture, w/8,h/4, "SEASON'S GREETINGS", myFont, black)

  return picture

# PROBLEM 3: Insert Name for Problem Here
def fileStats(files):
  f1 = open(getMediaPath()+"fileStats.csv","w")
  header = ["Filename","Total Words","Ends with 'E'"]
  for i in range(len(header)-1):
    f1.write(header[i]+",")
  f1.write(header[-1]+"\n") 
  for each in files:
    fileName = each
    f = open(getMediaPath()+each,"r")
    lines = f.read()
    #lines.replace("--"," ")   
    lines = lines.split()
    eCounter = 0
    #totalWords = 0
    totalWords = len(lines)
    for line in lines:
      line = line.strip('.,?!-/')
      #line = line.strip('.,?!-/"')
      if len(line) == 0:
        continue
      #totalWords +=1
      if line[-1] in "eE":
        eCounter += 1
     # print line
    f.close()     
    f1.write(fileName + ",")
    f1.write(str(totalWords) + ",")
    f1.write(str(eCounter) + "\n")
  f1.close()

# PROBLEM 4: A Major Switch
def xswitch(dict):
  major = []
  TA = []
  newDict = {}
  for each in dict:
    TA.append(each)
    major.append(dict[each])
  for each in major:
    newDict[each] = "0"
  print newDict

def switch(dict):
  newDict = {}
  for x, y in dict.items():
    if y in newDict:
      newDict[y].append(x)
    else:
      newDict[y] = [x]
  print newDict

# PROBLEM 5: Fibonacci Debauchery 
def fib(n):
  if num == 1:
    print "[1]"
  if num == 2:
    print "[1,1]"
  else:
    a = 1
    b = 1
    c = 1
    list = [1,1]
    for each in range(num):
      a = b
      b = c
      c = a + b
      list.append(c)
    print list