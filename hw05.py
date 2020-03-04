# Noah Longhi
# nlonghi3@gatech.edu 
# I worked on the homework assignment alone, using only this semester's course materials.

# PROBLEM 1: It's Time to Cook
def mexico(filename):
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    setRed(p, r * 1.3)
    setGreen(p, g * 1.3)
    setBlue(p, b * 0.7)
  return pic
  
# PROBLEM 2: Once in a Blue Moon
def blueMoon(filename):
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    g = getGreen(p)
    b = getBlue(p)
    setGreen(p, g * 3)
    setBlue(p, b * 3)
  return pic
# PROBLEM 3: Not Feeling GRAY-t
def grayscale(filename):
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    avg = (r+g+b)/3
    avg = avg * 0.65
    setRed(p, avg)
    setGreen(p, avg)
    setBlue(p, avg)
  return pic
  
# PROBLEM 4: Dali Party
def saintOfPaint(filename):
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    setGreen(p, b/4)
    setBlue(p, r)
    setRed(p, g*2)
  return pic

  
# PROBLEM 5: Don't Eat Expired Foods
def roadTrip(filename):
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    setRed(p, 255-r)
    setBlue(p, 130-b)
  return pic
    