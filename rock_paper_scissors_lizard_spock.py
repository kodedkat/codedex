import random

# header
print(
"""⋆ ˚｡ ⋆ ˚｡ ⋆✊ ✋ ✌ 🦎 🖖⋆ ｡˚ ⋆ ｡˚ ⋆\n
 Rock Paper Scissors Lizard Spock\n
⋆ ˚｡ ⋆ ˚｡ ⋆✊ ✋ ✌ 🦎 🖖⋆ ｡˚ ⋆ ｡˚ ⋆\n
1. ✊ Rock\n
2. ✋ Paper\n
3. ✌  Scissors\n
4. 🦎🐱 Lizard Cat\n
5. 🤓🖖 Young Sheldon Spock

"""
)
# 4. planning to incorporate a cat motif into my cs projects
# 5. I started watching Young Sheldon with my boyfriend in December 2023, and "erm ackshually ☝️🤓" I quite liked it

# variables
player = int(input("Please choose a number above: "))
computer = random.randint(1, 5)

# invalid input numbers
if player != 1 and player != 2 and player != 3 and player != 4 and player != 5:
  print("Please choose a valid number. ( ｡ •`ᴖ´• ｡)")

# time to battle!
# rock interactions
if player == 1 and computer == 1:
  print("You chose: ✊ \nCPU chose: ✊ \nRock squared. It's a tie. (⇀‸↼)")
elif player == 1 and computer == 2:
  print("You chose: ✊ \nCPU chose: ✋ \nPaper covers Rock. The computer won! ಠ_ಠ")
elif player == 1 and computer == 3:
  print("You chose: ✊ \nCPU chose: ✌ \nRock breaks Scissors. You won! \( ﾟヮﾟ)/🏆")
elif player == 1 and computer == 4:
  print("You chose: ✊ \nCPU chose: 🦎🐱 \nRock crushes Lizard Cat. You won! \( ﾟヮﾟ)/🏆")
elif player == 1 and computer == 5:
  print("You chose: ✊ \nCPU chose: 🤓🖖 \nYoung Sheldon Spock vaporizes Rock. The computer won! ಠ_ಠ")

# paper interactions
if player == 2 and computer == 1:
  print("You chose: ✋ \nCPU chose: ✊ \nPaper covers Rock. You won! \( ﾟヮﾟ)/🏆")
elif player == 2 and computer == 2:
  print("You chose: ✋ \nCPU chose: ✋ \nPaper squared. It's a tie. (⇀‸↼)")
elif player == 2 and computer == 3:
  print("You chose: ✋ \nCPU chose: ✌ \nScissors cut Paper. The computer won! ಠ_ಠ")
elif player == 2 and computer == 4:
  print("You chose: ✋ \nCPU chose: 🦎🐱 \nLizard Cat eats Paper. The computer won! ಠ_ಠ")
elif player == 2 and computer == 5:
  print("You chose: ✋ \nCPU chose: 🤓🖖 \nPaper disproves Young Sheldon Spock. You won! \( ﾟヮﾟ)/🏆")

# scissors interactions
if player == 3 and computer == 1:
  print("You chose: ✌ \nCPU chose: ✊ \nRock breaks Scissors. The computer won! ಠ_ಠ")
elif player == 3 and computer == 2:
  print("You chose: ✌ \nCPU chose: ✋ \nScissors cut Paper. You won! \( ﾟヮﾟ)/🏆")
elif player == 3 and computer == 3:
  print("You chose: ✌ \nCPU chose: ✌ \nScissors squared. It's a tie. (⇀‸↼)")
elif player == 3 and computer == 4:
  print("You chose: ✌ \nCPU chose: 🦎🐱 \nScissors beat Lizard Cat. You won! \( ﾟヮﾟ)/🏆")
elif player == 3 and computer == 5:
  print("You chose: ✌ \nCPU chose: 🤓🖖 \nYoung Sheldon Spock smashes Scissors. The computer won! ಠ_ಠ")

# lizard cat interactions
if player == 4 and computer == 1:
  print("You chose: 🦎🐱 \nCPU chose: ✊ \nRock crushes Lizard Cat. The computer won! ಠ_ಠ")
elif player == 4 and computer == 2:
  print("You chose: 🦎🐱 \nCPU chose: ✋ \nLizard Cat eats Paper. You won! \( ﾟヮﾟ)/🏆")
elif player == 4 and computer == 3:
  print("You chose: 🦎🐱 \nCPU chose: ✌ \nScissors beat Lizard Cat. The computer won! ಠ_ಠ")
elif player == 4 and computer == 4:
  print("You chose: 🦎🐱 \nCPU chose: 🦎🐱 \nLizard Cat squared. It's a tie. (⇀‸↼)")
elif player == 4 and computer == 5:
  print("You chose: 🦎🐱 \nCPU chose: 🤓🖖 \nLizard Cat poisons Young Sheldon Spock. You won! \( ﾟヮﾟ)/🏆")

# young sheldon spock interactions
if player == 5 and computer == 1:
  print("You chose: 🤓🖖 \nCPU chose: ✊ \nYoung Sheldon Spock vaporizes Rock. You won! \( ﾟヮﾟ)/🏆")
elif player == 5 and computer == 2:
  print("You chose: 🤓🖖 \nCPU chose: ✋ \nPaper disproves Young Sheldon Spock. The computer won! ಠ_ಠ Bazinga!")
elif player == 5 and computer == 3:
  print("You chose: 🤓🖖 \nCPU chose: ✌ \nYoung Sheldon Spock smashes Scissors. You won! \( ﾟヮﾟ)/🏆")
elif player == 5 and computer == 4:
  print("You chose: 🤓🖖 \nCPU chose: 🦎🐱 \nLizard Cat poisons Young Sheldon Spock. The computer won! ಠ_ಠ Bazinga!")
elif player == 5 and computer == 5:
  print("You chose: 🤓🖖 \nCPU chose: 🤓🖖 \nYoung Sheldon Spock squared. It's a tie. (⇀‸↼)")

# loop
while True:
  rematch = input("Would you like a rematch? [y/n] ( ◡̀_◡́)ᕤ ")
  if rematch == 'y' or rematch == 'Y':
    print("Starting a rematch... (｡•̯̀ v •̯̀｡)")
    print(
"""⋆ ˚｡ ⋆ ˚｡ ⋆✊ ✋ ✌ 🦎 🖖⋆ ｡˚ ⋆ ｡˚ ⋆\n
 Rock Paper Scissors Lizard Spock\n
⋆ ˚｡ ⋆ ˚｡ ⋆✊ ✋ ✌ 🦎 🖖⋆ ｡˚ ⋆ ｡˚ ⋆\n
1. ✊ Rock\n
2. ✋ Paper\n
3. ✌  Scissors\n
4. 🦎🐱 Lizard Cat\n
5. 🤓🖖 Young Sheldon Spock

"""
      )
      
    player = int(input("Please choose a number above: "))
    computer = random.randint(1, 5)
      
    if player != 1 and player != 2 and player != 3 and player != 4 and player != 5:
      print("Please choose a valid number. ( ｡ •`ᴖ´• ｡)")
      
    if player == 1 and computer == 1:
      print("You chose: ✊ \nCPU chose: ✊ \nRock squared. It's a tie. (⇀‸↼)")
    elif player == 1 and computer == 2:
      print("You chose: ✊ \nCPU chose: ✋ \nPaper covers Rock. The computer won! ಠ_ಠ")
    elif player == 1 and computer == 3:
      print("You chose: ✊ \nCPU chose: ✌ \nRock breaks Scissors. You won! \( ﾟヮﾟ)/🏆")
    elif player == 1 and computer == 4:
      print("You chose: ✊ \nCPU chose: 🦎🐱 \nRock crushes Lizard Cat. You won! \( ﾟヮﾟ)/🏆")
    elif player == 1 and computer == 5:
      print("You chose: ✊ \nCPU chose: 🤓🖖 \nYoung Sheldon Spock vaporizes Rock. The computer won! ಠ_ಠ")
    
    if player == 2 and computer == 1:
      print("You chose: ✋ \nCPU chose: ✊ \nPaper covers Rock. You won! \( ﾟヮﾟ)/🏆")
    elif player == 2 and computer == 2:
      print("You chose: ✋ \nCPU chose: ✋ \nPaper squared. It's a tie. (⇀‸↼)")
    elif player == 2 and computer == 3:
      print("You chose: ✋ \nCPU chose: ✌ \nScissors cut Paper. The computer won! ಠ_ಠ")
    elif player == 2 and computer == 4:
      print("You chose: ✋ \nCPU chose: 🦎🐱 \nLizard Cat eats Paper. The computer won! ಠ_ಠ")
    elif player == 2 and computer == 5:
      print("You chose: ✋ \nCPU chose: 🤓🖖 \nPaper disproves Young Sheldon Spock. You won! \( ﾟヮﾟ)/🏆")
    
    if player == 3 and computer == 1:
      print("You chose: ✌ \nCPU chose: ✊ \nRock breaks Scissors. The computer won! ಠ_ಠ")
    elif player == 3 and computer == 2:
      print("You chose: ✌ \nCPU chose: ✋ \nScissors cut Paper. You won! \( ﾟヮﾟ)/🏆")
    elif player == 3 and computer == 3:
      print("You chose: ✌ \nCPU chose: ✌ \nScissors squared. It's a tie. (⇀‸↼)")
    elif player == 3 and computer == 4:
      print("You chose: ✌ \nCPU chose: 🦎🐱 \nScissors beat Lizard Cat. You won! \( ﾟヮﾟ)/🏆")
    elif player == 3 and computer == 5:
      print("You chose: ✌ \nCPU chose: 🤓🖖 \nYoung Sheldon Spock smashes Scissors. The computer won! ಠ_ಠ")

    if player == 4 and computer == 1:
      print("You chose: 🦎🐱 \nCPU chose: ✊ \nRock crushes Lizard Cat. The computer won! ಠ_ಠ")
    elif player == 4 and computer == 2:
      print("You chose: 🦎🐱 \nCPU chose: ✋ \nLizard Cat eats Paper. You won! \( ﾟヮﾟ)/🏆")
    elif player == 4 and computer == 3:
      print("You chose: 🦎🐱 \nCPU chose: ✌ \nScissors beat Lizard Cat. The computer won! ಠ_ಠ")
    elif player == 4 and computer == 4:
      print("You chose: 🦎🐱 \nCPU chose: 🦎🐱 \nLizard Cat squared. It's a tie. (⇀‸↼)")
    elif player == 4 and computer == 5:
      print("You chose: 🦎🐱 \nCPU chose: 🤓🖖 \nLizard Cat poisons Young Sheldon Spock. You won! \( ﾟヮﾟ)/🏆")

    if player == 5 and computer == 1:
      print("You chose: 🤓🖖 \nCPU chose: ✊ \nYoung Sheldon Spock vaporizes Rock. You won! \( ﾟヮﾟ)/🏆")
    elif player == 5 and computer == 2:
      print("You chose: 🤓🖖 \nCPU chose: ✋ \nPaper disproves Young Sheldon Spock. The computer won! ಠ_ಠ Bazinga!")
    elif player == 5 and computer == 3:
      print("You chose: 🤓🖖 \nCPU chose: ✌ \nYoung Sheldon Spock smashes Scissors. You won! \( ﾟヮﾟ)/🏆")
    elif player == 5 and computer == 4:
      print("You chose: 🤓🖖 \nCPU chose: 🦎🐱 \nLizard Cat poisons Young Sheldon Spock. The computer won! ಠ_ಠ Bazinga!")
    elif player == 5 and computer == 5:
      print("You chose: 🤓🖖 \nCPU chose: 🤓🖖 \nYoung Sheldon Spock squared. It's a tie. (⇀‸↼)")
  else:
    print("Thank you for playing! (*ˊᗜˋ*)/")
    break
