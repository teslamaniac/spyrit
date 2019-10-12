#NOTE: THIS SCRIPT IS WRITTEN IN PYTHON 2.7. AS SUCH, IT WILL NOT WORK IN PYTHON 3 UNTIL 
#SOMEONE DECIDES TO REPLACE ALL THE 'raw_input's WITH 'input's AND PUT BRACKETS AROUND THE 'print' ARGUMENTS.

#UPDATE: MAY HAVE BEEN UPDATED TO 3.7


'''TO DO LIST
1. add more items
2. make the monsters more interesting.
3. make multiple endings
4. make items usable and make interactive objects in a room
'''
def showInstructions():
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  use [item] [WIP]
  quit
  help
''')

def showStatus():  
  print('---------------------------')
  print('You are in ' + currentRoom)
  print('Inventory: ' + str(inventory))
  if "item" in rooms[currentRoom]:
    print('You see ' + rooms[currentRoom]['item'])
  print(rooms[currentRoom]['roomdesc'])
  print('---------------------------')
    

inventory = []

rooms = {
  'Hall' : {
    'south' : 'Kitchen',
    'east': 'Dining Room',
    'north': 'Attic',
    'west': 'The Box',
    'item': 'a key',
    'roomdesc': """
You look around you.
The room is bland, take a few pictures and remnants of a life not worth living.
There are doors all around you; north, south, east and west.
"""
    },
  'Kitchen' : {
    'north': 'Hall',
    'south': 'Basement',
    'item': 'the bridgekeeper',
    'roomdesc' : '''
You look around you.
The Bridgekeeper stares at you annoyingly.
The doorways have been blocked.
'''
    },
  'Dining Room' : {
    'west': 'Hall',
    'east': 'Lounge Room',
    'roomdesc' : """
You look around you.
"""
    },
  'Lounge Room' : {
    'west': 'Dining Room',
    'roomdesc' : """
You look around you.
"""
    },
  'Basement' : {
    'north': 'Kitchen',
    'back-item': 'sacrificial altar',
    'back-item-event': """
The door slams behind you.
A candle comes alight, spreading a dim red light throughout the room.
The sounds of demonic chanting grows louder and louder until they are deafening.
The fabric of darkness weaved onto the altar, growing and threading around and around, until a fully-fledged demon appears before you.
'Whasit?' asks the demon drunkenly, gripping the edges of the altar to prevent him from falling off the world.
'Immin amiddl o a parteh. Some poor ol' bloke hates 'em so nae I'm havin' the time o' me life'
'If you aren't gonna speak then y'may's'll apologize'
'Nae? Okay thun...'
Darkness folds back on itself, and the demon disappeared into the void.
""",
    'roomdesc' : """
You look around you.
"""
    },
  'Attic' : {
    'south' : 'Hall',
    'roomdesc' : """
You look around you.
"""
    },
  'The Box' : {
    'down' : 'Hell',
    'roomdesc' : """
You look around you.
"""
    },
  'Hell': {
    'item': 'death',
    'roomdesc' : """
You look around you.
"""
    }
  }

currentRoom = 'Hall'

showInstructions()

def kitchenEncounter():
  showStatus()
  print("You see the bridgekeeper...")
  user_input =  input("'What is the average windspeed of unladen swallow?'")
  if user_input.lower() == "african or european?":
    print("'I... don't know...'")
    print("The room grows dim as a force of black energy fills the room.")
    print("A shadowed claw extended from the window pane, and pulled him out through it.")
    print("The Bridgekeeper dies.")
    return True
  elif '11' in user_input or '24' in user_input or '40' in user_input:
    print("'You may pass...'")
    print("As you move through the kitchen, you push the bridgekeeper out of the open window.")
    print("The Bridgekeeper dies.")
    rooms[currentRoom]['roomdesc'] = '''
You look around you.
The room is eerily empty
The doorways have been cleared.'''
    return True
  else:
    return False

while True:

  showStatus()
  move = ''
  while move == '':
    move = input(">")
  move = move.lower().split()

  if move[0] == 'go':
    if move[1] in rooms[currentRoom]:
      currentRoom = rooms[currentRoom][move[1]]
      continue
    else:
      print("You can't go that way!")
      continue
  if move[0] == 'get':
    if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      inventory += [move[1]]
      print(move[1] + " got!")
      del rooms[currentRoom]['item']
      continue
    elif 'back-item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['back-item']:
      print("You can't get environmental items!")
      continue
    else:
      print("Cannae get " + move[1] + "!")
      continue
  if 'item' in rooms[currentRoom] and 'the bridgekeeper' in rooms[currentRoom]['item']:
    if kitchenEncounter() == True:
      del rooms[currentRoom]['item']
      continue
    else:
      print("You died...")
      thing = input("Do you want to play again? [Y/N]: ")
      if thing.upper() == "N":
        break
      else:
        currentRoom = 'Hall'
        inventory = []
  if move[0] == "use":
    if 'back-item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['back-item']:
      print(rooms[currentRoom]['back-item-event'])
    else:
      print("Cannae use " + move[1] + "!")
  if move[0] == "quit":
    break
  if move[0] == "help":
    showInstructions()
  else:
    print("That command was invalid. Please try again.")
