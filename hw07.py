# Noah Longhi
# nlonghi3@gatech.edu 
# I worked on the homework assignment alone, using only this semester's course materials.

# PROBLEM 1: Right to Life, Libery, and Better Flag Designs
def lazyFlag(filename):
  pic = makePicture(filename)
  w = getWidth(pic)
  h = getHeight(pic)
  middleX = w/2
  for x in range(middleX - 50, middleX + 50):
    for y in range(h):
      pix = getPixelAt(pic, x, y)
      setColor(pix, blue)
  middleY = h/2
  for y in range(middleY - 50, middleY + 50):
    for x in range(w):
      pix = getPixelAt(pic, x, y)
      setColor(pix, blue)
  return pic

# PROBLEM 2: MIRROR-cle
def mirror(filename):
  pic=makePicture(filename)
  w=getWidth(pic)
  h=getHeight(pic)
  canvas = makeEmptyPicture(2*w, h)
  for x in range(w/2):
    for y in range(h):
      pixL=getPixelAt(pic, x,y)
      c=getColor(pixL)
      pixR=getPixelAt(pic, (w-1)-x ,y)
      setColor(pixR, c)      
  for x in range(w):
    for y in range(h):
        pix1 = getPixelAt(pic, x, y)
        pix2 = getPixelAt(canvas, x, y)
        pix3 = getPixelAt(canvas, x+w, y)
        setColor(pix2, getColor(pix1))
        setColor(pix3, getColor(pix1))
  
  return canvas

# PROBLEM 3: Rain Drop, Crop Top
def crop(filename):
  pic = makePicture(filename)
  w = getWidth(pic)
  h = getHeight(pic)
  picture = makeEmptyPicture(w, h)
  for x in range(w): 
    for y in range(h):
      if x > w*1/3 and x < w*2/3:
        pix1 = getPixelAt(pic, x, y)   
        pix2 = getPixelAt(picture, x-w*1/3, y)
        pix3 = getPixelAt(picture, x, y)
        pix4 = getPixelAt(picture, x+w*1/3, y)      
        setColor(pix2, getColor(pix1))
        setColor(pix3, getColor(pix1))
        setColor(pix4, getColor(pix1))
  pixels = getPixels(picture)   
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    x = getX(p)
    y = getY(p)
    if x <= w*1/3:
      setRed(p, r*0.75)
      setGreen(p, g*0.75)
    if x >= w*1/3 and x < w*2/3:
      setRed(p, r*0.5)
      setGreen(p, g*0.5)
    if x >= w*2/3:
      setRed(p, r*0.25)
      setGreen(p, g*0.25)
  return picture

# PROBLEM 4: SpongeBob SquarePants: Whale Out of Water
def whaleOfAJourney(filename): 
  src = makePicture("whale.jpg")
  picture = makePicture(filename)
  h=getHeight(picture)
  w=getWidth(picture)
  srcH=getHeight(src)
  srcW=getWidth(src)
  for x in range(getWidth(src)):
    for y in range(getHeight(src)):
      sPix=getPixelAt(src, x, y)
      sClr=getColor(sPix)
      dstX = x+(w*1/2)-(srcW/2)
      dstY = y+(h*1/2)-(srcH/2)
      d = distance(sClr, white)
      if d > 20:
        dPix= getPixelAt(picture, dstX, dstY)
        setColor(dPix, sClr)

  return picture

# PROBLEM 5: Blending
def blendAPic(f1, f2):
  pic1 = makePicture(f1)
  pic2 = makePicture(f2)
  w1 = getWidth(pic1)
  h1 = getHeight(pic1)
  w2 = getWidth(pic2)
  h2 = getHeight(pic2)
  w = min(w1, w2)
  h = min(h1, h2)
  result = makeEmptyPicture(w,h)
  for x in range(w):
    for y in range(h):
      pix1 = getPixelAt(pic1, x, y)
      pix2 = getPixelAt(pic2, x, y)
      r1 = getRed(pix1)
      g1 = getGreen(pix1)
      b1 = getBlue(pix1)
      
      r2 = getRed(pix2)
      g2 = getGreen(pix2)
      b2 = getBlue(pix2)
      
      r = 0.5 * r2 + (0.5) * r1
      g = 0.5 * g2 + (0.5) * g1
      b = 0.5 * b2 + (0.5) * b1
      c = makeColor(r,g,b)
      
      pix = getPixelAt(result, x, y)
      setColor(pix, c)
  return result

def textTest():
  f = open(getMediaPath("Chapter01.txt"), "r")
  lines = f.readlines()
  for line in lines:
    line = line.strip()
    line = line.split("\n")
    if len(line) >= 3:
      print line
    else:
      continue