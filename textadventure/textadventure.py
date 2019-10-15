# py 3.7
# text adventure - type 1 - uses objects and is long.
# GOTTA COMMENT A LOTTA STUFF!!!
class Location:
    def __init__(self, locationName, directions, description, people = [], items = [], enemies = []):
        # The constructor that makes the object arguments for LOCATION.
        self.locationName = locationName
        self.directions = directions
        self.description = description
        self.people = people
        self.items = items
        self.enemies = enemies
    def ShowInfo(self):
        # function that shows current room info
        # triggered every time you move into a different room.
        import os # relies on os for 'cls' - possible incompatibility with other operating systems besides Windows.
        os.system('cls')
        title = "Current Location: " + self.locationName # prints location, seperated from other sections by a line of '='
        print(title)
        print("="*len(title))
        print("Possible Paths: ") # prints possible paths. 
        print("-"*len(title)) # title seperated from the list of paths by a line of '-', and from the other sections by a line of '='
        for entry in self.directions:
            print(entry + ": " + self.directions[entry]) # prints every possible path.
        print("="*len(title))

        if len(self.people) != 0: # prints people present, if there are any. 
            print("People Present: ") # title separated from list by line of '-', and from other sections by line of '='.
            print("-"*len(title))
            for person in self.people:
                print(person.name)
            print("="*len(title))

       if len(self.enemies) != 0: # prints enemies present, if there are any.
          print("Enemies Present: ") # title separated from list by line of '-', and from other sections by a line of '='.
          print("-"*len(title))
          for enemy in self.enemies:
             print(enemy.name)
          print("="*len(title))
          
        if len(self.items) != 0: # prints items present, if there are any. 
            print("Objects Present: ") # title separated from list by line of '-', and from other sections by a line of '='.
            print("-"*len(title))
            for item in self.items:
                print(item.name)
            print("="*len(title))

    def AddItem(self, itemAdding, amountThrowing): # CONFIRM, CREATOR - creates an item.
        for i in range(amountThrowing):
            self.items.append(itemAdding)
        self.ShowInfo()


class Creature:
    class LevelOneStats:
        def __init__(self, attackPoints, healthPoints, defencePoints):
            # sets constructor for level 1 stats
            self.attackPoints = attackPoints
            self.healthPoints = healthPoints
            self.defencePoints = defencePoints

    class CurrentMaximumStats:
        def __init__(self, attackPoints, healthPoints, defencePoints):
            # sets constructor for maximum stats
            self.attackPoints = attackPoints
            self.healthPoints = healthPoints
            self.defencePoints = defencePoints

    class CurrentStats:
        def __init__(self, attackPoints, healthPoints, defencePoints):
            # sets constructor for current stats
            self.attackPoints = attackPoints
            self.healthPoints = healthPoints
            self.defencePoints = defencePoints

    def __init__(self, name, level, levelOneStats, description):
        # sets constructor for creature info
        self.name = name
        self.level = level
        self.levelOneStats = levelOneStats
        self.description = description
        self.currentMaximumStats = self.SetCurrentMaximumStats(level)
        self.currentStats = self.SetCurrentStats( # sets current stats to the current maximum stats
            self.currentMaximumStats.attackPoints,
            self.currentMaximumStats.healthPoints,
            self.currentMaximumStats.defencePoints
        )      

    def SetCurrentMaximumStats(self, level):
        # function that sets max stats depending on the level
        attackPoints = self.levelOneStats.attackPoints + level - 1 # sets max stats to level number
        healthPoints = self.levelOneStats.healthPoints + level - 1 
        defencePoints = self.levelOneStats.defencePoints + level - 1
        return Creature.CurrentMaximumStats(attackPoints, healthPoints, defencePoints) # returns an object with those attributes

    def SetCurrentStats(self, newAttackPoints, newHealthPoints, newDefencePoints):
        return Creature.CurrentStats(newAttackPoints, newHealthPoints, newDefencePoints) # sets current stats to value

    def TakeDamage(self, damage):
      def DisplayDamageCalculation(): # displays damage calculation
         print("Player attacks " + self.name + ". Enemy takes " + str(damage))
         print(self.name + " now on: " + str(self.currentStats.healthPoints) + "/" + str(self.currentMaximumStats.healthPoints))
      self.currentStats.healthPoints -= damage # calculates damage
      if (self.currentStats.healthPoints <= 0): # tells whether you die or not
         self.currentStats.healthPoints = 0
         self.Die()
         DisplayDamageCalculation()
         print (self.name + " died!") # this rubs the fact that you died in your face over and over again 
      else:
         DisplayDamageCalculation()  # pisses everyone off if you don't die.
         while len(currentLocation.people) > 0:
            currentLocation.people[0].Anger()
         currentLocation.ShowInfo()

    def Die(self): # kills NPC
      if type(self) is Person:
         currentLocation.people.remove(self)
         while len(currentLocation.people) > 0:
            currentLocation.people[0].Anger()
      currentLocation.ShowInfo()

    def HealHP(self, amount): # heals creature (with validation for maximum) 
        if (self.currentHealthPoints + amount > self.currentHealthPoints):
            self.currentHealthPoints = self.currentHealthPoints
        else:
            self.currentHealthPoints += amount
         

class Player(Creature):
   def __init__(self, level, levelOneStats, description = None, name = None):
      Creature.__init__(self, name, level, levelOneStats, description) #takes constructor from creature
      self.inventory = {}

   def Attack(self, weapon, enemy):
      damageTaken = weapon.damage + self.currentStats.attackPoints # damages enemy for weapon's points
      enemy.TakeDamage(damageTaken)

   def AddItemInventory(self, itemAdding):
      foundInInventory = False 
      for item in self.inventory.keys(): # increments item in inventory by 1 if found, and creates one if not found.
         if item.name == itemAdding.name:
            self.inventory[item] += 1
            foundInInventory = True
            break
      if not foundInInventory:
         self.inventory[itemAdding] = 1

   def RemoveItemInventory(self, itemRemoving, amountRemoving):
      foundItem = None
      for item in self.inventory.keys(): # searches for item, and then removes all instances of it if found
         if item.name == itemRemoving.name:
            foundItem = item
            break         
      if foundItem != None:
         self.inventory[foundItem] -= amountRemoving
         if self.inventory[foundItem] == 0:
            self.inventory.pop(foundItem)  

   def DisplayInventory(self):
      currentLocation.ShowInfo() #prints inventory contents
      length = len("Current Location: " + currentLocation.locationName)
      print("Inventory:")
      print("-"*length)
      for item in self.inventory:
         print(item.name + ": x" + str(self.inventory[item]))
      print("="*length)


class Person(Creature):
   def __init__(self, name, level, levelOneStats, description, dialogue):
      Creature.__init__(self, name, level, levelOneStats, description)
      self.dialogue = dialogue
   def Anger(self): # makes NPC into enemy
      currentLocation.enemies.append(self)
      currentLocation.people.remove(self)

class Item:
    def __init__(self, name, description): # sets constructor for item
        self.name = name
        self.description = description


class Potion(Item):
   class RandomHealAmount:
      def __init__(self, minimum, maximum): # WIP. heals a random amount between min & max.
         self.minimum = minimum
         self.maximum = maximum
   def __init__(self, name, description, healAmount, randomHealAmount = None):
      Item.__init__(self, name, description)
      self.healAmount = healAmount # constructor for potion
      self.randomHealAmount = randomHealAmount


class Weapon(Item):
    def __init__(self, name, description, damage):
        Item.__init__(self, name, description)
        self.damage = damage


class Armour(Item):
    def __init__(self, name, description, defence):
        Item.__init__(self, name, description)
        self.defence = defence

      
def MoveLocation(command): # COMMENT THIS BIT 
    global currentLocation
    if len(command) == 1:
        return print("Invalid Command: Need to specify where to move to!")
    if len(command) > 2:
        return print("Invalid Command: Must enter two words only!")
    if command[1] == currentLocation.locationName:
        return print("Invalid Command: You're already in that location!")

    possibleDirections = list(currentLocation.directions.keys())
    possibleLocations = list(currentLocation.directions.values())  
    if command[1] in possibleLocations:
        for L in locationList:
            if command[1] == L.locationName:
                os.system('cls')
                currentLocation = L
                currentLocation.ShowInfo()
                break
    elif command[1] in possibleDirections:
        for L in locationList:
            if currentLocation.directions[command[1]] == L.locationName:
                os.system('cls')
                currentLocation = L
                currentLocation.ShowInfo()
                break
    else:
        return print("Invalid command: Location doesn't exist!")


def RefreshScreen(command):
   if len(command) == 1: # refreshes screen
      currentLocation.ShowInfo()
   else:
      return print("Invalid command: Can only just do 'refresh'!")
   

def TalkToPerson(command): # talks to person. COMMENT THIS LATER
    if len(command) == 1:
        return print("Invalid command: Need to specify who to talk to!")
    if len(command) > 2:
        return print("Invalid command: Can only enter two words!")
   
    possiblePeople = [p.name for p in currentLocation.people]
    if command[1] in possiblePeople:
        for p in currentLocation.people:
            if command[1] == p.name:
                print("*Talk* " + p.name + ": \"" + p.dialogue + "\"")
                break
    else:
        return print("Invalid command: Person does not exist at this location!")


def GetItem(command):
   if len(command) == 1:
      return print("Invalid command: Need to specify what item to get!")
   if len(command) > 2:
      return print("Invalid command: Can only enter two words!")
   if command[1] in [p.name for p in currentLocation.people]:
      return print("Invalid command: No slavery allowed!")

   possibleItems = [item.name for item in currentLocation.items]
   if command[1] in possibleItems:
      for item in currentLocation.items:
         if command[1] == item.name:
            currentLocation.items.remove(item)
            player.AddItemInventory(item)
            currentLocation.ShowInfo()
            break
   else:
      return print("Invalid command: The item does not exist in this location!")


def ThrowItem(command):
    if len(command) == 1:
        return print("Invalid command: Need to specify what item to throw!")
    if len(command) > 3:
        return print("Invalid command: Can only enter three or two words!")

    possibleItems = [item.name for item in player.inventory]
    if command[1] in possibleItems:
        for item in player.inventory:
            if command[1] == item.name:
                if len(command) == 2:
                    player.RemoveItemInventory(item, 1)
                    currentLocation.AddItem(item, 1)
            else:
                try:
                    amountThrowing = int(command[2])
                except ValueError:
                    return print("Invalid command: Throw amount must be an integer!")

                if amountThrowing == 0:
                    return print("Invalid command: What is the point of throwing nothing?")
                if amountThrowing < 0:
                    return print("Invalid command: Throwing negative items does not get you more items!")
                if amountThrowing > player.inventory[item]:
                    return print("Invalid command: You do not have that may of that item!")           
                player.RemoveItemInventory(item, amountThrowing)
                currentLocation.AddItem(item, amountThrowing)
                break
    else:
        return print("Invalid command: Item does not exist in inventory!")
          

def ShowInventory(command):
    if len(command) == 1:
        player.DisplayInventory()
    else:
        return print("Invalid command: Can only do 'inventory'!")


def UseItem(command):
   if len(command) == 1:
      return print("Invalid command: Must specify what item to use!")
   possibleItems = [i.name for i in player.inventory]
   possiblePeople = [p.name for p in currentLocation.people]
   if command[1] in possibleItems or command[1] in possiblePeople:
      for item in player.inventory:
         if command[1] == item.name:
            if type(item) is Potion:
               if len(command) > 2:
                  return print("Invalid command: For potion items just type in the command: 'use <potion name>'!")
               else:
                  if (player.currentHealthPoints == player.levelOneStats.healthPoints):
                     return print("Invalid command: Player HP already maxed!")
                  else:
                     return print("Healed " + str(item.healAmount))
            if type(item) is Weapon:
               if len(command) == 2:
                  return print("Invalid command: Must specify who to use weapon on!")
               elif len(command) > 3:
                  return print("Invalid command: Must enter 3 words!")
               if command[2] in possiblePeople:
                  for person in currentLocation.people:
                     if command[2] == person.name:
                        player.Attack(item, person)
                        break
               else:
                  return print("Invalid command: Enemy does not exist")
         break
   else:
      return print("Invalid command: Item does not exist in inventory")


def ShowDescription(command):
   if len(command) == 1:
      return print("Invalid command: Need to specify what to show info for!")
   if len(command) > 2:
      return print("Invalid command: Can only enter two words!")
   possibleItems = [i.name for i in player.inventory]
   possiblePeople = [p.name for p in currentLocation.people]
      
   if command[1] in possibleItems:
      for item in player.inventory:
         if command[1] == item.name:
            if type(item) is Potion:
               print("*Info* " + item.name + ":")
               print("Type: Potion")
               print("HP Heal: " + str(item.healAmount))
               print("Desc: '" + str(item.description) + "'")
            elif type(item) is Weapon:
               print("*Info* " + item.name + ":")
               print("Type: Weapon")
               print("Damage: " + str(item.damage))
               print("Desc: '" + str(item.description) + "'")
            break
   elif command[1] in possiblePeople:
      for person in currentLocation.people:
         if command[1] == person.name:
            print("*Info* " + person.name + ":")
            print("Desc: '" + person.description + "'")
            print("HP: " + str(person.currentStats.healthPoints))
            print("Atk: " + str(person.currentStats.attackPoints))
            print("Def: " + str(person.currentStats.defencePoints))
            break
   elif command[1] == currentLocation.locationName:
      print("*Info* " + currentLocation.locationName + ": '" + currentLocation.description + "'")            
   else:
      return print("Invalid command:\n-Item does not exist in inventory OR\n-Person does not exist in location OR\n-Player not present in that location!")


def ShowHelpMenu(command):
   if len(command) == 1:
      currentLocation.ShowInfo()
      print("Help Menu:")
      length = len("Current Location: " + currentLocation.locationName)
      print("="*length)
      print("move| move <location name> OR move + <direction>| Moves player to new location")
      print("refresh| refresh| Closes inventory & removes a bunch of useless text")
      print("talk| talk <person name>| Talks to a person")
      print("get| get <item name>| Pick up an item from location")
      print("inventory| inventory| Shows player's inventory")
      print("info| info <item name> OR info <person name>| gives more info")
      print("throw| throw <item name> OR throw <item name > <quantity>| throws an item")
      print("help| help| already in help menu, if don't know how to use help to get help, not my problem")
      print("="*length)
   else:
      return print("Invalid command: Can only just do 'help'!")
   

basement = Location(
   "basement",
   {"north": "house", "west": "garden", "east": "location3", "south" : "location4"},
   "Dark Place. Beware a pedo may be hiding around the corner!",
   [
      Person(
         "nic",
         1,
         Creature.LevelOneStats(1, 6, 1),
         "He is also called nic the dick",
         "Hello there!"),
      Person(
         "michael",
         1,
         Creature.LevelOneStats(1, 1, 1),
         "Stay away from him he is a pedo",
         "Come here little boy! come to papa!"),
      Person(
         "joseph",
         1,
         Creature.LevelOneStats(1, 1, 1),
         "Stay away from him he is a jew",
         "Gimme your money!"),
      Person(
         "jiatee",
         1,
         Creature.LevelOneStats(1, 1, 1),
         "Stay away from him he only hangs out with the cool kids",
         "Go away! You're too uncool for me!")
      ],
   [
      Potion("marijuana", "feels good man!", 50), Potion("marijuana", "feels good man!", 50), Weapon("fly_swatter", "$2 from Woolworths", 3)
      ]
   )

house = Location(
   "house",
   {"north": "basement", "west": "location2", "east": "location3", "south" : "location4"},
   "A very normal looking house, however it may contain some dark secrets in the basement!"
   )

garden = Location(
   "garden",
   {"north": "basement", "west": "location2", "east": "location3", "south" : "location4"},
   "Beautiful garden. To distract you from the house..."
   )

locationList = [basement, house, garden]
commandList = {"move", "refresh", "talk", "get", "inventory", "info", "help", "throw", "use"}

player = Player(1, Creature.LevelOneStats(1, 1, 1))

currentLocation = basement
currentLocation.ShowInfo()
gameOver = False

while gameOver == False: 
    commandEntered = input("Enter a command: ").strip().lower().split()
    
    if commandEntered[0] not in commandList:
       print("invalid command: command doesn't exist!")
    elif commandEntered[0] == "move":    
       MoveLocation(commandEntered)
    elif commandEntered[0] == "refresh":      
       RefreshScreen(commandEntered)
    elif commandEntered[0] == "talk":
       TalkToPerson(commandEntered)
    elif commandEntered[0] == "get":
       GetItem(commandEntered)
    elif commandEntered[0] == "inventory":
       ShowInventory(commandEntered)
    elif commandEntered[0] == "info":
       ShowDescription(commandEntered)
    elif commandEntered[0] == "help":
       ShowHelpMenu(commandEntered)
    elif commandEntered[0] == "throw":
       ThrowItem(commandEntered)
    elif commandEntered[0] == "use":
       UseItem(commandEntered)