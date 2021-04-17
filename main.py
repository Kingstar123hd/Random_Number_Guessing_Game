import random
a = random.randint(1,9)
b = random.randint(1,9)
c = random.randint(1,9)
d = random.randint(1,9)
e = random.randint(1,9)
f = random.randint(1,9)
g = random.randint(1,9)
h = random.randint(1,9)
i = random.randint(1,9)
j = random.randint(1,9)
k = random.randint(1,9)
l = random.randint(1,9)
m = random.randint(1,9)
n = random.randint(1,9)
o = random.randint(1,9)
p = random.randint(1,9)
q = random.randint(1,9)
r = random.randint(1,9)
print(f"{a}---{c}---{e}---{g}---{i}---{k}---{m}---{o}---{q}--\n[] |Random number guessing game| []\n{a}---{c}---{e}---{g}---{i}---{k}---{m}---{o}---{q}--")
yn = input('Enter "play" to play \n| ').lower()

def guess (x, y, z):
  if z == True:
    randomnum = random.randint(1,x)
    guess = 0
    print(f"I am thinking of a number between 1 and {x} \n\nYou have {y} tries\n")
    tries = 0
    while guess != randomnum and tries < y:
      if tries < y:
        tries = tries + 1
        remain = y - tries
        guess = int(input("Number: "))
        if guess < randomnum:
          print(f"Guess is too low, {remain} tries remaining")
        elif guess > randomnum:
          print(f"Guess is too high, {remain} tries remaining")
    if tries == y or tries > y:
      print("You ran out of tries!")
    if guess == randomnum:
      print(f"Correct! The correct number was {randomnum}, you got it in {tries} tries!")
  elif z == False:
    randomnum = random.randint(1,x)
    guess = 0
    print(f"I am thinking of a number between 1 and {x} \n\nYou have {y} tries\n")
    tries = 0
    while guess != randomnum and tries < y:
      if tries < y:
        tries = tries + 1
        remain = y - tries
        guess = int(input("Number: "))
        if guess != randomnum:
          print(f"Inncorrect guess, {remain} tries remaining")
    if tries == y or tries > y:
      print("You ran out of tries!")
    if guess == randomnum:
      print(f"Correct! The correct number was {randomnum}, you got it in {tries} tries!")    


if yn == "play":
  arg1 = int(input("How many numbers should there be? \n"))
  arg2 = int(input("How many tries do you want? \n"))
  arg3 = input("Do you want help? [y or n] \n")

  helpp = True

  if arg3 == "y":
    helpp = True
  elif arg3 == "n":
    helpp = False
  else:
    print("I'm sorry I didn't get that, set to default(y)")
    helpp = True

  guess(arg1, arg2, helpp)
