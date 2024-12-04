
def secondCheck(chars) -> bool:
    increasing = True
    for char in range(len(chars) - 1):

      char1 = int(chars[char])
      char2 = int(chars[char + 1])
      difference = abs(char1 -char2)
      if (difference > 3 or difference < 1):
        return False
      if char == 0:
        if char1 > char2:
          increasing = False
        else: 
          increasing = True
      if char1 > char2 and increasing is True:
        return False
        
      if char1 < char2 and increasing is False:
        return False
        
    return True
safe = 0
with open('input.txt') as f:
  lines = f.readlines()
  for line in lines:
    chars = line.split((' '))
    increasing = True
    isSafe = True
    safety = 0
    secondList = list(chars) 
    backup = list(chars)

    for char in range(len(chars) - 1):


      char1 = int(chars[char])
      char2 = int(chars[char + 1])
      difference = abs(char1 -char2)
      if char == 0:
        if char1 > char2:
          increasing = False
        else: 
          increasing = True
      if (difference > 3 or difference < 1):
        secondOrigin = list(chars)
        secondOrigin.pop(char)
        secondChance = secondCheck(secondOrigin)
        originArr = list(chars)
        originArr.pop(char + 1)
        otherSecondChance = secondCheck(originArr)
        if not secondChance and not otherSecondChance:
            isSafe = False
            break


    #   9, 8, 10, 11

      if char1 > char2 and increasing is True:
        secondOrigin = list(chars)
        secondOrigin.pop(char)
        secondChance = secondCheck(secondOrigin)
        originArr = list(chars)
        originArr.pop(char + 1)
        otherSecondChance = secondCheck(originArr)
        if not secondChance and not otherSecondChance:
            isSafe = False
            break

      elif char1 < char2 and increasing is False:

        secondOrigin = list(chars)
        secondOrigin.pop(char)
        secondChance = secondCheck(secondOrigin)
        originArr = list(chars)
        originArr.pop(char + 1)
        otherSecondChance = secondCheck(originArr)

        if not secondChance and not otherSecondChance:
            isSafe = False
            break

    if isSafe:
      safe+=1
print(safe)



