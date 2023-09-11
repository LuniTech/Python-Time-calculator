#Created by Zipho Innocent Lunika
#def add_time(start, duration):
def add_time(startTime, duration, dayOfWeek=""):
  startTime = startTime.replace(":", " ")
  currentTime = startTime.split()
  #print(currentTime)
  duration = duration.replace(":", " ")
  toAddArr = duration.split()
  currentTime[0] = int(currentTime[0])  #we convert the current time here!
  currentTime[1] = int(currentTime[1])
  toAddArr[0] = int(toAddArr[0])
  toAddArr[1] = int(toAddArr[1])

  longFormat = currentTime[0]
  #this is for making it a 24 hour clock

  if (currentTime[2] == "PM"):
    longFormat = 12 + currentTime[0]
  longFormat += toAddArr[0]
  #hourCarry=None;
  daysCarry = 0
  eveningMorning = "AM"
  #adding the minutes:
  minutes = currentTime[1] + toAddArr[1]
  if (minutes > 60):
    longFormat = longFormat + 1
    minutes = minutes - 60
#dealing with the hours:

  while (longFormat >= 24):
    longFormat = longFormat - 24
    daysCarry = daysCarry + 1

#check if the long-format is greater than 12 and change EveningMorniing
  print("longFormat ===", longFormat)
  if (longFormat >= 12):
    print("Condition True!!")
    eveningMorning = "PM"
    if (longFormat != 12):
      longFormat = longFormat - 12
  elif (longFormat == 0):  #condition for 0:00
    if (eveningMorning != "PM"):
      eveningMorning = "AM"
      longFormat = 12
# now to deal with the day of the week
  daysOfWeek = [
    "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
    "sunday"
  ]
  #print("dayOfweek == "+dayOfWeek)
  if (dayOfWeek != ''):
    if (dayOfWeek.lower() in daysOfWeek):
      pointerIndex = daysOfWeek.index(dayOfWeek.lower())
      daysCarryCountDown = daysCarry
      #print("daysCarryCountDown",)
      while (daysCarryCountDown != 0):
        pointerIndex = pointerIndex + 1
        if (pointerIndex == 7):
          pointerIndex = 0
        daysCarryCountDown = daysCarryCountDown - 1
#its all making sense. Now for the final display:
  if (minutes < 10):
    finalTime = str(longFormat) + ":0" + str(minutes) + " " + eveningMorning
  else:
    finalTime = str(longFormat) + ":" + str(minutes) + " " + eveningMorning
  if (dayOfWeek == '' and daysCarry > 0):
    if (daysCarry == 1):
      finalTime = finalTime + " (next day)"
    else:
      finalTime = finalTime + " (" + str(daysCarry) + " days later)"
  elif (dayOfWeek.lower() in daysOfWeek):
    if (daysCarry == 0):
      finalTime = finalTime + ", " + (daysOfWeek[pointerIndex][0]).upper() + (
        daysOfWeek[pointerIndex])[1:]
    elif(daysCarry==1):
            finalTime=finalTime+ ", "+(daysOfWeek[pointerIndex][0]).upper()+(daysOfWeek[pointerIndex])[1:]+" (next day)"  
    elif (daysCarry > 1):  #WE DID NOT DO FOR ONE YET. REVISIT THIS PART
      finalTime = finalTime + ", " + (daysOfWeek[pointerIndex][0]).upper() + (
        daysOfWeek[pointerIndex])[1:] + " (" + str(daysCarry) + " days later)"

#daysOfWeek = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
  return finalTime


#print(add_time("3:50 PM", "3:10"))
#print(add_time("11:43 AM", "00:20"))
#print(add_time("10:10 PM", "3:30"))
#print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("5:00 AM", "01:30"))

#  return new_time
