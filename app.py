import random

def lineBreak(num = 1):
  print(" ")
  if num > 1:
    lineBreak(num - 1)
  elif num == 1:
    pass

def travel():
  lineBreak
  input(f'"Where to captain?" {mate} asks. South or West. (s/w): ')
  choice = random.choice(mission_list)
  mission_list.remove(choice)
  lineBreak()
  choice()

def game_over(reason):
  if reason == "off course":
    print("And with your last command you sail off into the distance ..... got lost, and are never seen again.")
    exit()

def first_pirate_attack():
  print('first pirate attack goes here')

def shark_chasers():

  print('The radio buzzes to life.  The voice of a middle aged man. A documentary producer who explains that the crew for his hit show "Shark Chasers" is stranded on a small, tide reliant island off the coast while they were shooting an episode of his hit show. He begs you to rescue the crew of his hit show before high tide returns and erases the island, and in turn, his hit show.')

  result = input(f"""a: Decline. You’re not a fan of the show.

  b: Agree, but only after you've made sure the Seabeast isn't in the area. 

  c: Agree to drop everything and head out there.

  d: Ask {mate} if they've heard of Shark Chasers.

  e: Watch a few episodes of Shark Chasers on before deciding what to do.
  
  WHAT DO YOU DO: """)

  if result == "a":
    print('The producer is stunned off by your indifference to human life despite being a soulless human being himself. He signs off and you never hear from him again.')
    lineBreak()
    print(f'You search the area and find nothing. {mate} doesn\'t look at you the same afterwards')
    print(f'|{mate} loses morale|')
    morale = morale - 1
    travel()
    
  elif result == "b":
    print('The producer checks in with you every five minutes with what seems like standard impatience rather than genuine concern for his crew. But finally you are ready to go.')
    shark_chasers2("late")
  elif result == "c":
    print(f'You confirm you and {mate} are leaving right away.')
    shark_chasers2("super rush")
  elif result == "d":
    if mate == "Lillian":
      print('Lillian frowns and explains that Shark Chasers is a dangerous, ill informed nature reality show where the two credential free hosts spread falsities about sharks, claiming they are aggressive nuisances. As she finishes her uncharacteristic rant, Lillian says that you still should save the crew despite them being useless charlatans. So that\'s what you do.')
      shark_chasers2("rush")
    elif mate == "Cristo":
      print('Cristo loves Shark Chasers! He goes on about how cool it is with the two hosts that really know their stuff about how cool and monstrous sharks are. He\'s ready to go shark hunting. So you figure you might as well go help out.')
      shark_chasers2("super rush")
    elif mate == "Viktoria":
      answer = input("""Viktoria doensn't think it's a good idea. The show never interested her and you have better things to do. But ultimately it's up to you. 
      
      HELP OUT THE SHARK CHASERS CREW? (y/n): """)
      if answer == "y":
        shark_chasers2("rush")
      else:
        travel()
    elif mate == "Jacob":
      print("Jacob pauses and finally says \"It's a tough call, but I think we've got to put a hold on our search and go help out.\" You agree and head to the coordinates the producer provides.")
      shark_chasers2("rush")
  elif result == "e":
    print('After watching one and half episodes of Shark Chasers, you determine the crew is not worth saving. But you go all the same, because it would be cruel not to.')
    shark_chasers2("super late")
  else:
    print(f'"{result}" was not an option')
    lineBreak()
    shark_chasers()
    
def shark_chasers2(time):
  if time == "late":
    pick = random.choice(available_equipment_list)
    available_equipment_list.remove(pick)
    equipment.append(pick)
    print(f"""When you finally reach the coordinates, you find one of the gaffers being dragged into the water by a great white. You do not manage to rescue the gaffer, but you get the rest of the production crew aboard before the sharks can pick any of them off. The production crew is grateful and rewards you with {pick}, but the crew know that gaffer’s life could have been saved if you had reacted to their distress call with a sense of urgency.""")
    travel()

  if time == "super late":
    print(f'By the time you reach the island, it is gone. The hide tide swallowed the small island and no one can be found. You do find a camera bobbing in the serf. You choose not to examine the footage on the tape. {mate} doesn\'t say anything but you can tell they feel you could have done more')
    lineBreak
    print(f'|{mate} loses morale|')
    morale = morale - 1
    travel()

  if time == "rush":
    pick = random.choice(available_equipment_list)
    available_equipment_list.remove(pick)
    equipment.append(pick)
    print(f'You find the crew teetering on the tide island, fighting off a pack of circling great whites with a boom mic. You pull them out, just as their small island is swallowed by high tide. They are grateful and the producer gives you a reward of {pick} upon returning them to the Cove. The next episode of Shark Chasers is dedicated captain {name}. It however, continues to be poorly made.')
    travel()
    
  if time == "super rush":
    pick = random.choice(available_equipment_list)
    available_equipment_list.remove(pick)
    equipment.append(pick)
    print(f'You find the production crew on the tide created island, sun burnt, dehydrated, but otherwise in good spirits. You ferry them back to the port. They are grateful and the producer gives you a reward of {pick} upon returning them to port. The next episode of Shark Chasers is dedicated to captain {name}. It however, continues to be poorly made.')
    travel()

def lost_at_sea():
  print('display lost at sea')

# Testing data defined before game starts
mate = "Lillian"
equipment = []
# Place mission function here to playtest that specific mission
morale = 0
health = 4

mission_list = [shark_chasers, first_pirate_attack, lost_at_sea]
available_equipment_list = ["Food", "Explosives", "Guns", "Fish Finder"]

name = input("What's your name sailor? ")

print(f"Well {name}, we're in a bad spot. The Seabeast is attacking our town. Travel and trade has become impossible. You are supposed to be the best.")

lineBreak()

ship = input("Now what's the name of your ship? The_______: ")

lineBreak()

print("And she looks like a fine vessel")

lineBreak()

print("Who are you taking as your first mate? We've tried to find the best. Pick from this lot and be on your way.")

lineBreak()

mate = input(
"""Vikitoria - A woman with eyes of steel and a mysterious past.
Cristo - A youth of 16 or 17. Why is he even an option?
Jacob - A barrel of a man. Ex-military. Said to currently work as an underwater welder.
Lillian - A scientist gentle of heart and interested in learning more about this supposed "beast".
CHOOSE YOUR FIRST MATE: """
)

if mate == "Viktoria" or mate == "Cristo" or mate == "Jacob" or mate == "Lillian":
  print("Great! I'm sure you'll make a fine team!")
else:
  first_mate_list = ["Viktoria", "Cristo", "Jacob", "Lillian"]
  mate = random.choice(first_mate_list)
  print(f"Okay that wasn't a real option so we'll just pick {mate} for you. They'll be as loyal as if you had spelled their name correctly! You'll do fine.")

if mate == "Viktoria":
  morale = 4
elif mate == "Jacob":
  morale = 3
elif mate == "Cristo":
  morale = 4
elif mate == "Lillian":
  morale = 3

lineBreak()

input(f"Now one last thing {name}. What equipment will you and {mate} bring on The {ship}? EQUIPMENT LIST: ")

lineBreak()

pick = input("""Well that's not really an option. Here's what we have:
Food
Explosives
Guns
Fish Finder
PICK THE SINGLE PIECE OF EQUIPMENT YOU ARE BRINGING: """)

if pick == "Food" or pick == "Explosives" or pick == "Guns" or pick == "Fish Finder":
  print(f"I'll get the {pick} loaded right away.")
else:
  pick = random.choice(available_equipment_list)
  available_equipment_list.remove(pick)
  equipment.append(pick)

  print(f"Okay again. That's not an option. Tell you what ... I'll just load up the {pick}")

input(f"Okay Captain {name}. Any parting words before your voyage? :")

lineBreak(2)

print("""........ And with your parting words you are off on your journey.""")

lineBreak(4)

travel()