import random 
global pick
global randomrps
global rps
print("""To start the game enter correct letter.
  R - Rock
  P - Paper
  S - Scissors """)
while True:
  rps = ["r", "p", "s"]
  randomrps = random.choice(rps)
  randomrps = random.choice(rps)
  pick = input("Your pick: ").lower()
  if pick == str("r") and randomrps == str("s"):
    print("Rock crushes scissors... You WON!")
  elif randomrps == str("r") and pick == str("s"):
    print("Rock crushes scissors... You Lost!")    
  elif pick == str("p") and randomrps == str("r"):
    print("Paper covers rock... You WON!")
  elif randomrps == str("p") and pick == str("r"):
    print("Paper covers rock... You Lost!")
  elif pick == str("s") and randomrps == str("p"):
    print("Scissors cuts paper... You WON!")
  elif randomrps == str("s") and pick == str("p"):
    print("Scissors cuts paper... You Lost!")
  elif pick == randomrps:
    print("TIE!")
