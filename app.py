import random

# Testing data defined before game starts
mate = "Lillian"
equipment = []
# Place mission function here to playtest that specific mission
morale = 0
health = 4

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

def display_stats():
  lineBreak()
  print(f"|HEALTH: {health}|{mate} MORALE: {morale}|")
  print(f"EQUIPMENT ABOARD THE {ship}: {equipment}")
  lineBreak()

def game_over(reason):
  if reason == "off course":
    print("And with your last command you sail off into the distance ..... got lost, and are never seen again.")
    exit()

def first_pirate_attack():
  global morale
  global health
  global equipment
  print('You get a bad feeling. You scan the surrounding waters for the tell tale dark shadows just below the surface that preempt an attack from the depths. But this time the source for concern isn\'t from below the water but speeding just above it. Four armed men are quickly approaching straight towards your boat. YOUR boat! It\'s not looking good. These men are definitely pirates.')
  lineBreak()
  choice = input(f"""
a: Try to outrun them. It doesn't look hopeful but it may be your only chance.

b: Fight. The pirates will learn to regret their life choices.

c: Surrender. Hope they are merciful.
""")
  if choice == "a":
    if morale > 2: # escape
      mission_list.append(pirate_attack2)
      print("The pirates didn't expect your vessel to be as fast as it was and they give up for easier prey. That was close.")
      travel()
    else:
      stolen = random.choice(equipment)
      equipment.remove(stolen)
      health = health - 1
      print(f'You max the engine but they overtake you. They steal your {stolen} and because you ran they pistol whip you.')
      display_stats()
      travel()
  if choice == "b":
    if mate == "Viktoria":
      mission_list.append(pirate_attack2)
      print("It's clear to you ... and eventually to the pirates that Viktoria is no stranger to using a knife. The pirates are easily fended off. Viktoria's pride is evident. And the ship is safe.")
      morale = morale + 1
      display_stats()
      travel()
    if mate == "Cristo":
      mission_list.append(pirate_attack2)
      print("Cristo doesn't put up much of a fight. In fact the pirates seem genuinely amused at his attempts. They decide to let you be but you can hear their laughter long after they get too far away to see. Cristo seems more than a little insulted.")
      morale = morale - 1
      display_stats()
      travel()
    if mate == "Lillian":
      mission_list.append(pirate_attack2)
      print("Lillian really put up a fight. The pirates easily overtake your boat. And they take all your equipment no problem.")
      display_stats()
      lineBreak()
      print("You gather yourself and keep moving forward")
      travel()
    if mate == "Jacob":
      mission_list.append(pirate_attack2)
      print("Jacob is no stranger to stress or combat. He handles himself well and the pirates retreat to find easier prey.")
      lineBreak()
      travel()
  if choice == "c":
    mission_list.append(pirate_attack2)
    print("Surprisingly the pirates are quite cordial. They are borderline apologetic. But ... they do take all your equipment though. That was a given.")
    equipment = []
    lineBreak()
    travel()

def pirate_attack2():
  print("pirate attack 2 goes here")

def shark_chasers():

  print('The radio buzzes to life.  The voice of a middle aged man. A documentary producer who explains that the crew for his hit show "Shark Chasers" is stranded on a small, tide reliant island off the coast while they were shooting an episode of his hit show. He begs you to rescue the crew of his hit show before high tide returns and erases the island, and in turn, his hit show.')

  result = input(f"""
  
a: Decline. You’re not a fan of the show.

b: Agree, but only after you've made sure the Seabeast isn't in the area. 

c: Agree to drop everything and head out there.

d: Ask {mate} if they've heard of Shark Chasers.

e: Watch a few episodes of Shark Chasers before deciding what to do.

WHAT DO YOU DO: """)

  if result == "a":
    print('The producer is stunned off by your indifference to human life despite being a soulless human being himself. He signs off and you never hear from him again.')
    lineBreak()
    print(f'You search the area and find nothing. {mate} doesn\'t look at you the same afterwards')
    global morale
    morale =  morale - 1
    display_stats()
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
      lineBreak()
      shark_chasers2("rush")
  elif result == "e":
    print('After watching one and half episodes of Shark Chasers, you determine the crew is not worth saving. But you go all the same, because it would be cruel not to.')
    lineBreak()
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
    display_stats()
    travel()

  if time == "super late":
    print(f'By the time you reach the island, it is gone. The hide tide swallowed the small island and no one can be found. You do find a camera bobbing in the serf. You choose not to examine the footage on the tape. {mate} doesn\'t say anything but you can tell they feel you could have done more.')
    global morale
    morale = morale - 1
    display_stats
    travel()

  if time == "rush":
    pick = random.choice(available_equipment_list)
    available_equipment_list.remove(pick)
    equipment.append(pick)
    print(f'You find the crew teetering on the tide island, fighting off a pack of circling great whites with a boom mic. You pull them out, just as their small island is swallowed by high tide. They are grateful and the producer gives you a reward of {pick} upon returning them to the Cove. The next episode of Shark Chasers is dedicated captain {name}. It however, continues to be poorly made.')
    display_stats()
    travel()

  if time == "super rush":
    pick = random.choice(available_equipment_list)
    available_equipment_list.remove(pick)
    equipment.append(pick)
    print(f'You find the production crew on the tide created island, sun burnt, dehydrated, but otherwise in good spirits. You ferry them back to the port. They are grateful and the producer gives you a reward of {pick} upon returning them to port. The next episode of Shark Chasers is dedicated to captain {name}. It however, continues to be poorly made.')
    display_stats()
    travel()

def lost_at_sea():
  global morale
  print("""You come upon a dingy in the open sea. Miraculously, there is still a man alive on the
raft. But there are also signs that there may have been a struggle on board. Scraps of
bright colored clothing that don’t match the man’s clothes and dried blood on a
second life jacket. You ask the man if there was anyone with him and he says no one
else survived when their ship sunk. You:
""")
  lineBreak()
  choice = ""

  if ("Food" in equipment):
    choice = input("""a. Let him on board.

b. Cut him loose and pray that no one else finds him before the sea swallows him whole.

c. Give him food and water, but ask that he stay on his raft and tow him to the nearest port.
""")
  else:
    choice = input("""a. Let him on board.

b. Cut him loose and pray that no one else finds him before the sea swallows him whole.
""")

  if choice == "a":
    print(f'The man immediately takes {mate} hostage with a knife.')
    if mate == "Viktoria":
      print('But it\'s the last mistake he makes. Viktoria flips him over. In the scuffle the man hits his head on the railing. He falls overboard with the smallest of splashes. Viktoria berates you for letting him on board in the first place')
      travel()
    elif mate == "Cristo":
      print('The fear in Cristo\'s eyes has you moving faster than the man anticipated. You pull Cristo free, and the man escapes overboard. You are inured but safe. Cristo is in shock but he still manages to help you bandage your wound.')
      health = health - 1
    elif mate == "Jacob":
      print('You aren\'t sure what the man was thinking, but Jacob easily overpowers him. You tie him up to the railing of the stern. While discussing what to do with him on the bow you hear a splash. As you both make your way to the back all that remains on is an untied rope. Hopefully he doesn\'t find his hurt anyone else on his search for dry land')
      travel()
    elif mate == "Lillian":
      print('You try to talk to him, but he does not listen. There is a scuffle. Both you and Lillian are injured but the man falls overboard. You try to locate him but he is gone. You leave quickily, brusied and broken')
      health = health - 1
      morale = morale - 1
      display_stats()
  elif choice == "b":
    print('You see the evidence. It does not feel right. You leave without giving aid.')
    if mate == "Lillian":
      print('Lillian protests your lack of assistence to a man in need regardless of his appearance. You insist you did the right thing but she is not happy')
      morale = morale - 1
      display_stats()     
    elif mate == "Cristo":
      print("Cristo agrees with your decision. He feels a lot better about it.")
      morale = morale + 1
      display_stats()
    travel()

  elif choice == "c" and "Food" in equipment:
    print(f'While towing the man into port, a large rapturous tentacle reaches up from the depths and drags him under kicking and screaming. He is gone before you can help him. You turn to {mate} and they stare off in the distance, “the sea is God’s eye and within it, you are judged so.” Was it the seabeast? More likely one of it\'s smaller offspring. No point in staying around. Time to move on.')
    travel()
  else:
    print('That was not an option. Pick again.')
    lineBreak()
    lost_at_sea()

################################ Start of App ################################

mission_list = [shark_chasers, lost_at_sea, first_pirate_attack]
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
  available_equipment_list.remove(pick)
  equipment.append(pick)

else:
  pick = random.choice(available_equipment_list)
  available_equipment_list.remove(pick)
  equipment.append(pick)

  print(f"Okay again. That's not an option. Tell you what ... I'll just load up the {pick}")

display_stats()
input(f"Okay Captain {name}. Any parting words before your voyage? :")


lineBreak(2)

print("""........ And with your parting words you are off on your journey.""")

lineBreak(4)

travel()