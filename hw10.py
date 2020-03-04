# Noah Longhi
# nlonghi3@gatech.edu 
# I worked on the homework assignment alone, using only this semester's course materials.

# PROBLEM 1: They See Me Rollin', They Hatin'
def rolling(filename):
  f = open(getMediaPath()+filename, "r")
  header = f.readline()
  header = header.strip()
  headers = header.split(",")
  lines = f.readlines()
  print "We are going to toilet paper these people's houses:"
  for line in lines:
    line = line.strip()
    line = line.split(",")
    if line[1] != "candy" or line[2] == "0" or line[2] == "1":
      print line[0]
    else:
      continue
  f.close()
  
# PROBLEM 2: New Heights
def heights(country):
  f = open(getMediaPath()+"heights.csv", "r")
  header1 = f.readline()
  lines = f.readlines()
  for line in lines:
    line = line.strip()
    line = line.split(",")
    if line[0] == country:
      sum = 0.0
      sum += float(line[1])
      sum += float(line[2])
      avg = sum/2
  f.close()
  f = open(getMediaPath()+"taHeights.csv", "r")
  header2 = f.readline()
  lines = f.readlines()
  for line in lines:
    line = line.strip()
    line = line.split(",")
    if float(line[1]) < avg:
      print line[0]
    else:
      continue
  f.close

# PROBLEM 3: Who Needs Calculators?
def mathTables(number):
  f = open(getMediaPath()+"MathTables.csv", "w")
  header = ["Number","Number * 8","Number ** 3","Number % 2"]
  for i in range(len(header)-1):
    f.write(header[i] + ",")
  f.write(header[-1] + "\n")
  for i in range(1,number+1):
    f.write(str(i) + ",")
    f.write(str(i*8) + ",")
    f.write(str(i**3) + ",")
    f.write(str(i%2) + "\n")
  f.close()
  
# PROBLEM 4: Basic Witches
def basicWitches(costumes):
  max = 0
  x = costumes.values()
  for each in x:
    if each > max:
      max = each
  for each in costumes:
    if costumes[each] == max:
      z = each
  print "Don't be a " + z + "!"
  print "There are " + str(max) + " people dressed as a " + z + " already."

# PROBLEM 5: Who You Gonna Call? CodeBuster!
def candyStash(filename):
  d = {"Trick": 0, "Treat":0}
  f = open(getMediaPath()+filename, "r")
  header = f.readline()
  lines = f.readlines()
  for line in lines:
    line = line.strip()
    line = line.split(",")
    if line[1] == "candy":
      d["Treat"] = d["Treat"] + int(line[2])
    else:
      d["Trick"] = d["Trick"] + int(line[2])
  print d
  f.close()