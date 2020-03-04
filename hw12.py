# Noah Longhi
# nlonghi3@gatech.edu 
# I worked on the homework assignment alone, using only this semester's course materials.

from time import sleep

def animateTurtles():
  # This program is about a turtle named link that is found on an old Legend of Zelda map.
  # Link finds his way around the map and happens upon an enemy of which he slays. However,
  # Link takes damage from this enemy and loses two hearts as a result. He then makes his
  # way to an old master that gives him a special item: a triforce!
  world = makeWorld(480,360)
  
  #Turtle Creation
  link = makeTurtle(world)
  enemy = makeTurtle(world)
  master = makeTurtle(world)
  background = makeTurtle(world)
  text = makeTurtle(world)
  pen = makeTurtle(world)
  
  #Picture Creation
  backgroundPic = makePicture("background.jpg")
  textPic = makePicture("text.jpg")
  
  #Scene Setup 
  background.penUp()
  background.moveTo(0,0)
  background.drop(backgroundPic)
  background.hide()
  text.penUp()
  text.moveTo(0,230)
  text.hide()
  link.penUp()
  link.moveTo(250,400)
  link.setBodyColor(green)
  enemy.penUp()
  enemy.moveTo(80,240)
  enemy.turn(90)
  enemy.setBodyColor(gray)
  master.penUp()
  master.moveTo(240,145)
  master.turn(180)
  master.setBodyColor(blue)
  pen.penUp()
  pen.moveTo(370,70)
  pen.turn(-90)
  pen.penUp()
  pen.setPenColor(black)
  pen.setPenWidth(20)
  pen.hide()
  
  sleep(0.5)
  for each in range(12):
    link.forward(10)
    sleep(0.1)
  link.turn(-90)
  sleep(0.5)
  for each in range(13):
    link.forward(10)
    sleep(0.1)
  for each in range(5):
    link.forward(3)
    enemy.backward(3)
    sleep(0.1)
  for each in range(3):
    link.backward(3)
    enemy.forward(3)
    sleep(0.1)
  sleep(0.25)
  enemy.forward(15)
  sleep(0.25)
  link.setBodyColor(red)
  link.backward(10)
  sleep(0.3)
  
  #Heart Removed
  pen.penDown()
  for each in range(9):
    pen.forward(2)
    sleep(0.1)
  link.setBodyColor(green)
  sleep(0.25)
  enemy.forward(15)
  sleep(0.25)
  link.setBodyColor(red)
  link.backward(10)
  sleep(0.3)  
  pen.penDown()
  for each in range(13):
    pen.forward(1)
    sleep(0.025)
  link.setBodyColor(green)
  link.forward(20)
  sleep(0.25)
  enemy.backward(15)
  enemy.hide()
  sleep(0.5)
  
  link.turn(180)
  sleep(0.25)
  for each in range(12):
    link.forward(10)
    sleep(0.1)
  sleep(0.25)
  link.turn(-90)
  for each in range(6):
    link.forward(10)
    sleep(0.1)
  text.drop(textPic)
  sleep(1)

  def nestedTri(t, size):
     if size < 10:
       return
     else:
       for sides in range(3):
         nestedTri(t, size/2)
         t.forward(size)
         t.turn(120)
         sleep(0.009)

  #w = makeWorld(200,200)

  tf = makeTurtle(world)
  tf.penUp()
  tf.moveTo(75,200)
  tf.penDown()
  tf.hide()
  tf.setPenColor(yellow)
  tf.setPenWidth(7)
  nestedTri(tf, 100)
  
  
  