name = "Bhika"
age = 21
level = 48
score = 250
playerHealth = 100


print("--------------------")
print("   PLAYER STATUS    ")
print("--------------------")
print("Name: ", name)
print("Age: ", age)
print("Level: ", level)
print("Score: ", score)
print("Player Health: ", playerHealth)
print("--------------------")

print("Monster Appear.")
print("1. Attack")
print("2. Run")
print("--------------------")

action = int(input("Choose your Action: "))

print("You chose: ", action)

monsterHealth = 200

if action == 1:
  attack = 50
  monsterHealth -= attack  
  monsterAttack = 30
  playerHealth -= monsterAttack
  print("You chose to Attack")
  print(f"You dealt {attack} damage")
  print("Monster Health: ", monsterHealth)
  print("Monster attacks!")
  print(f"You took {monsterAttack} Damage")
  print(f"Player Health: {playerHealth}")
elif action == 2:
  print("You chose to Run!")
  
print("--------------------")
print("1. Attack")
print("2. Run")
print("--------------------")

action2 = int(input("Choose your Action: "))
print("You chose: ", action2)

if action2 == 1:
  attack = 50
  monsterHealth -= attack
  monsterAttack = 30
  playerHealth -= monsterAttack
  
  print("You choose to attack!")
  print(f"You dealt {attack} damage")
  print("Monster Health: ", monsterHealth)
  print("Monster attacks!")
  print(f"You took {monsterAttack} Damage")
  print(f"Player Health: {playerHealth}")

elif action2 == 2:
  print("You chose to Run!")

