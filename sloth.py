# Text-based game about a sloth

print("Welcome to the Sloth Adventure!")

# Set up variables
name = input("What is your name? ")
energy = 10
hunger = 0
thirst = 0
predators = 0

# Start the game loop
while energy > 0 and predators < 12:
  # Print current status
  print(f"\nEnergy: {energy}")
  print(f"Hunger: {hunger}")
  print(f"Thirst: {thirst}")
  print(f"Predators: {predators}")
  
  # Get player's next action
  print("\nWhat would you like to do next?")
  action = input("[E]at, [D]rink, [S]leep, or [W]ander? ")

  # Take action based on player's input
  if action.lower() == "e":
    hunger -= 5
    if hunger < 0:
      hunger = 0
    energy += 3
    predators = 1
    print("You eat some tasty leaves and gain some energy.")
  elif action.lower() == "d":
    thirst -= 5
    if thirst < 0:
      thirst = 0
    energy += 3
    predators += 1
    print("You drink some water and feel refreshed.")
  elif action.lower() == "s":
    energy += 10
    hunger += 2
    thirst += 2
    predators += 2
    print("You sleep for a while and feel well rested.")
  elif action.lower() == "w":
    predators -= 2
    if predators < 0:
        predators = 0
    energy -= 3
    hunger += 1
    thirst += 1
    
    print("You wander around and explore your surroundings.")
  else:
    print("Invalid action. Please try again.")
  
  # Decrease energy, hunger, and thirst over time
  energy -= 1
  hunger += 1
  thirst += 1
  predators += 1
# Game over
if predators < 12:
    print("oh no you got eaten")
elif energy > 0:
    print(f"\nOh no, {name} has run out of energy and died! Game over.")