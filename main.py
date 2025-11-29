import animation
import os
import random
import time
print("Please play with all caps on")
def pickWord():
  words_path = os.path.join(os.path.dirname(__file__), "Words.txt")
  import random
  words = []
  f = open(words_path, "r")
  for w in f:
    words.append(w.rstrip())
  r = random.randint(0, len(words)-1)
  f.close()
  return words[r].upper()

def createSecretArray(word):
  s = []
  for v in word:
    s.append(v)
  return s

def buildHintArray(secretArray):
	s = []
	for v in secretArray: 
		s.append("__")
	return s

def printHintArray(hintArray):
	for v in hintArray:
		print(v, end=" ")


def checkLetter(secretArray, letter):
  for v in secretArray:
    if letter == v:
      return True
  return False

def updateHintArray(secretArray, hintArray, letter):
  i = 0
  for v in secretArray:
    if v== letter:
      hintArray[i] = letter
    i= i + 1

def isWordGuessed(hintArray):
    for v in hintArray:
        if v == "__":
            return False
    return True

w = pickWord()


secretArray = createSecretArray(w)

hintArray = buildHintArray(secretArray)

playerGuesses = 6
wrongGuesses = []

while playerGuesses > 0 and isWordGuessed(hintArray) == False:
  printHintArray(hintArray)
  print("")
  print("")
  print("The Incorrect Letters:",wrongGuesses)
  print("The Guesses You Have Remaining:", playerGuesses)
  
  #if playerGuesses == 6:
   # animation.animationLose1()
  #if playerGuesses == 5:
   # animation.animationLose2()
  #if playerGuesses == 4:
    #animation.animationLose3()
  #if playerGuesses == 3:
   # animation.animationLose4()
  #if playerGuesses == 2:
    #animation.animationLose5()
  #if playerGuesses == 1:
   # animation.animationLose6()

  user = input("Please enter your letter: ")
  
  if checkLetter(secretArray, user) == True:
    correctLetterAnimation = random.randint(1,7)
    rareAnimation = random.randint(1,100)
    if correctLetterAnimation == 1:
      animation.animationRight1()
      time.sleep(2)
    if correctLetterAnimation == 2:
      animation.animationRight2()
      time.sleep(2)
    if correctLetterAnimation == 3:
      animation.animationRight3()
      time.sleep(2)
    if correctLetterAnimation == 4:
      animation.animationRight4()
      time.sleep(2)
    if correctLetterAnimation == 5:
      animation.animationRight5()
      time.sleep(2)
    if correctLetterAnimation == 6:
      animation.animationRight6()
    if rareAnimation == 1:
      animation.animationRareRight7()
      time.sleep(2)

    updateHintArray(secretArray, hintArray, user)
  if checkLetter(secretArray, user) == False:
    playerGuesses = playerGuesses - 1
    wrongGuesses.append(user)

  if isWordGuessed(hintArray) == False:
    os.system("clear")
    
  if playerGuesses == 0 or isWordGuessed(hintArray) == True:
    animation.animationLose7()
    print("THE SECRET WORD WAS:", w,)	
    print("THANKS FOR PLAYING!")

