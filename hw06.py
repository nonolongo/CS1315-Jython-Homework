# Noah Longhi
# nlonghi3@gatech.edu 
# I worked on the homework assignment alone, using only this semester's course materials.

# PROBLEM 1: Look at the Color Negative Side
def otherSide(filename):
  pic = makePicture(filename)
  w = getWidth(pic)
  for p in getPixels(pic):
    x = getX(p)
    y = getY(p)
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    if x < w/2:
      if r > 150:
        setRed(p, 75)
      if g > 150:
        setGreen(p, 75)
      if b > 150:
        setBlue(p, 75)
      if r <= 150:
        setRed(p, 0)
      if g <= 150:
        setGreen(p, 0)
      if b <= 150:
        setBlue(p, 0)
    if x > w/2:
      setRed(p, 255-r)
      setGreen(p, 255-g)
      setBlue(p, 255-b)
  return pic
  
# PROBLEM 2: Bill Gates Protege
def microsoft(filename):
  pic = makePicture(filename)
  w = getWidth(pic)
  h = getHeight(pic)
  for p in getPixels(pic):
    x = getX(p)
    y = getY(p)
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    if x < w/2:
      if y < h/2:
        setGreen(p, g * 0.25)
        setBlue(p, b * 0.25)
    if x > w/2:
      if y < h/2:
        setRed(p, r * 0.25)
        setBlue(p, b * 0.25)
    if x < w/2:
      if y > h/2:
        setRed(p, r * 0.25)
        setGreen(p, g * 0.25)
    if x > w/2:
      if y > h/2:
        setBlue(p, b * 0.25)
  return pic

# PROBLEM 3: Picture Frame
def picFrame(filename, frameWidth):
  pic = makePicture(filename)
  w = getWidth(pic)
  h = getHeight(pic)
  for x in range(frameWidth):
    for y in range(h):
      pLeft = getPixelAt(pic, x, y)
      setColor(pLeft, pink)
      pRight = getPixelAt(pic, w-1-x, y)
      setColor(pRight, yellow)
  for y in range(frameWidth):
    for x in range(w):
      pTop = getPixelAt(pic, x, y)
      setColor(pTop, orange)
      pBottom = getPixelAt(pic, x, h-1-y)
      setColor(pBottom, cyan)
  return pic
  
# PROBLEM 4: Mercenary Mariners
def battleShip(filename, size):
  pic = makePicture(filename)
  w = getWidth(pic) 
  h = getHeight(pic)
  pixels = getPixels(pic)
  graphColor = makeColor(0, 0, 0)  
  for p in pixels:
    x = getX(p)
    y = getY(p)
    if x%size == 0 or y%size == 0:
      setColor(p, graphColor)
  return pic

# PROBLEM 5: The Artist and the Predator
def art(filename):
  pic = makePicture(filename)
  w = getWidth(pic)
  h = getHeight(pic)
  boxW = (w - 100)/2
  boxH = (h - 100)/2 
  for p in getPixels(pic):
    x = getX(p)
    y = getY(p)
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    avg = (r+g+b)/3
    setRed(p, avg)
    setBlue(p, avg)
    setGreen(p, avg)    
    if (x > boxW and x < w - boxW):
      if (y > boxH and y < h - boxH):
        setRed(p, r)
        setBlue(p, b*0.25)
        setGreen(p, g*0.25)
  return pic                