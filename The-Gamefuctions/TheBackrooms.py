from time import sleep
import sys
import time
import os
import random
import winsound
crazy = 0
entities = 0
wayout = 0
def startgame():
  while crazy <= 6:
    print(f"Sanity Meter: {crazy}")
    time.sleep(1)
    if wayout == 5:
      print("You are walking through the rooms and you see a glitched wall.")
      time.sleep(1)
      print("You try to go through the wall with your hand but when it touched the wall it actualy when through")
      time.sleep(1)
      print("you are suprised so you jump through the wall and your back in the waiting room its 12:17")
      time.sleep(1)
      crazy = 30
    if entities == 1:
      print("You hear a weird sound. You walk futher into the rooms and the sound coming closer.")
      time.sleep(1)
      print("When you come a round a corner you see a weird entity.")
      time.sleep(1)
      choice = input("""What are you going to do?
      A(Run away.
      B(Walk towards to entity.
      C(Do nothing: """).lower()
      if choice == 'a':
        print("You run as fast as you can.")
        crazy += 1
        entities = 0
        time.sleep(1)
      elif choice == 'b':
        print("You are walking towards to entity when you suddenly pas out, when you wake up you realize the entity is gone")
        entities = random.randint(1, 10)
        crazy += 3
        entities = 0
        time.sleep(1)
      elif choice == 'c':
        print("You did nothing. You suddenly pas out, when you wake up you realize the entity is gone ")
        crazy += 3
        entities = 0
        time.sleep(1)
      elif choice == 'd':
        print ("You repeated your fine. But youre not and you runaway as fast as you can")
        entities = 0
        time.sleep(1)
    elif entities == 3:
      print("Youre walking through the rooms when you see a weird entity.")
      time.sleep(1)
      print("its hanging from the wall.")
      time.sleep(1)
      choice = input("""What are you going to do?
      A(Run away.
      B(Walk towards to entity.
      C(Do nothing: """).lower()
      if choice == 'a':
        print("You run as faraway from the entity.")
        time.sleep(1)
        crazy += 1
        entities = 0
      elif choice == 'b':
        print("You are walking towards to entity when suddenly the lights go out when the lights turned on again, you realize the entity is gone")
        crazy += 3
        time.sleep(1)
        entities = 0
      elif choice == 'c':
        print("You did nothing. suddenly the lights go out when the lights turned on again, you realize the entity is gone ")
        crazy += 3
        time.sleep(1)
        entities = 0
      elif choice == 'd':
        print ("You repeated your fine. But youre not and you runaway as fast as you can")
        entities = 0
        time.sleep(1)
    elif entities == 5:
      print("when you are walking through the rooms you see a window.")
      time.sleep(1)
      print("You walk towards the window and see a weird figure.")
      time.sleep(1)
      choice = input("""What are you going to do?
      A(Run away.
      B(Walk towards to figure.
      C(Do nothing: """).lower()
      if choice == 'a':
        print("You run as fast as you can away from the window.")
        time.sleep(1)
        crazy += 1
        entities = 0
      elif choice == 'b':
        print("You are walking towards to figure when the window suddenly disapeared, you think its all in your head")
        time.sleep(1)
        crazy += 2
        entities = 0
      elif choice == 'c':
        print("You did nothing. when the window suddenly disapeared, you think its all in your head ")
        crazy += 2
        time.sleep(1)
        entities = 0
      elif choice == 'd':
        print ("You repeated your fine. But youre not and you runaway as fast as you can")
        entities = 0
        time.sleep(1)
    elif entities == 7:
      print("youre walking though the rooms when you see in the distance a weird entity.")
      time.sleep(1)
      print("its to big for the room and its hands are no-clipping through the wall.")
      time.sleep(1)
      choice = input("""What are you going to do?
      A(Run away.
      B(Walk towards to entity.
      C(Do nothing: """).lower()
      if choice == 'a':
        print("You run as fast as you can away from the entity before it sees you.")
        time.sleep(1)
        crazy += 1
        entities = 0
      elif choice == 'b':
        print("You are walking towards to entity, but you realize the entity walks towards you.")
        time.sleep(1)
        print("when the entity is a meter away from you it suddenly disapeared.")
        time.sleep(1)
        crazy += 3
        entities = 0
      elif choice == 'c':
        print("You did nothing. The entity sees you when it is a meter away from you it suddenly disapeared. ")
        time.sleep(1)
        crazy += 3
        entities = 0
      elif choice == 'd':
        print ("You repeated your fine. But youre not and you runaway as fast as you can")
        time.sleep(1)
        entities = 0
    elif entities == 9:
      print("You see a little spider in the corner in the room.")
      time.sleep(1)
      choice = input("""What are you going to do?
      A(walk away.
      B(Walk towards to spider.
      C(Do nothing: """).lower()
      if choice == 'a':
        print("You walk slowly away from the spider.")
        time.sleep(1)
        entities = 0
      elif choice == 'b':
        print("You are walking towards to spider, when suddenly the wall is covered in spiders. You walk away")
        time.sleep(1)
        crazy += 1
        entities = 0
      elif choice == 'c':
        print("You did nothing. when suddenly the wall is covered in spiders. You walk away")
        time.sleep(1)
        crazy += 1
        entities = 0
      elif choice == 'd':
        print ("You repeated your fine. You walk away from the spiders")
        time.sleep(1)
        crazy -= 1
        entities = 0
    elif crazy == 0:
      choice = input("""What are you going to do?
      A(Try to search the other rooms
      B(Walk through the rooms
      C(Do nothing: """).lower()
      if choice == 'a':
        print("You searched the other room, But you found nothing.")
        time.sleep(1)
      elif choice == 'b':
        print("You walk room after room but nothing is changing")
        time.sleep(1)
        crazy += 1
      elif choice == 'c':
        print("You did nothing.")
        time.sleep(1)
      elif choice == 'd':
        print ("You repeated your fine.")
        crazy = 0
        time.sleep(1)
    elif crazy == 1:
      choice = input("""You think your going crazy. What are you going to do?
      A(Scream for help.
      B(Walk too the other rooms
      C(Do nothing: """).lower()
      if choice == 'a':
        print("You screamed but no one heard you.")
        time.sleep(1)
        crazy += 1
      elif choice == 'b':
        print("You walk room after room but nothing is changing")
        time.sleep(1)
        wayout = random.randint(1, 20)
        crazy += 1
      elif choice == 'c':
        print("You did nothing.")
        time.sleep(1)
        crazy += 1
      elif choice == 'd':
        print ("You repeated your fine.")
        time.sleep(1)
        crazy -= 1
    elif crazy == 2:
      choice = input("""What are you going to do?
      A(Check phone.
      B(Walk futher.
      C(Do nothing: """).lower()
      if choice == 'a':
        print("You check your phone but no signal.")
        time.sleep(1)
        crazy += 1
      elif choice == 'b':
        print("Youre continue to walk through the rooms")
        entities = random.randint(1, 10)
        wayout = random.randint(1, 20)
        time.sleep(1)
        crazy += 1
      elif choice == 'c':
        print("You did nothing.")
        time.sleep(1)
        crazy += 1
      elif choice == 'd':
        print ("You repeated your fine.")
        time.sleep(1)
        crazy -= 1
    elif crazy == 3:
      choice = input("""What are you going to do?
      A(rest a bit.
      B(Walk futher through the rooms.
      C(Do nothing: """).lower()
      if choice == 'a':
        print("You rested a bit youre a bit calmer.")
        time.sleep(1)
        crazy -= 1
      elif choice == 'b':
        print("You walk room after room. It looks all the same")
        entities = random.randint(1, 10)
        wayout = random.randint(1, 20)
        crazy += 1
        time.sleep(1)
      elif choice == 'c':
        print("You did nothing.")
        time.sleep(1)
        crazy += 1
      elif choice == 'd':
        print ("You repeated your fine.")
        time.sleep(1)
        crazy -= 1
    elif crazy == 4:
      choice = input("""What are you going to do?
      A(Walk back.
      B(Walk futher through the rooms.
      C(Do nothing: """).lower()
      if choice == 'a':
        print("You walked back but it all looks the same.")
        entities = random.randint(1, 10)
        wayout = random.randint(1, 20)
        crazy += 1
        time.sleep(1)
      elif choice == 'b':
        print("You walk room after room. It looks all the same")
        entities = random.randint(1, 10)
        wayout = random.randint(1, 20)
        crazy += 1
        time.sleep(1)
      elif choice == 'c':
        print("You did nothing.")
        crazy += 1
        time.sleep(1)
      elif choice == 'd':
        print ("You repeated your fine.")
        crazy -= 1
        time.sleep(1)
    elif crazy == 5:
      choice = input("""What are you going to do?
      A(Help.
      B(Walk futher through the rooms.
      C(Do nothing: """).lower()
      if choice == 'a':
        print("you tried to scream for help, But nothing came out of your mouth.")
        crazy += 1
      elif choice == 'b':
        print("You walk room after room. It looks different but all the same")
        entities = random.randint(1, 10)
        wayout = random.randint(1, 20)
        crazy += 1
        time.sleep(1)
      elif choice == 'c':
        print("You did nothing.")
        crazy += 1
        time.sleep(1)
      elif choice == 'd':
        print ("You repeated your fine.")
        crazy -= 1
        time.sleep(1)
    elif crazy == 6:
      choice = input("""What are you going to do?
      A(Do nothing.
      B(Walk futher through the rooms.
      C(Do nothing: """).lower()
      if choice == 'a':
        print("You did nothing.")
        crazy += 1
        time.sleep(1)
      elif choice == 'b':
        print("You walk room after room. It is all the same")
        entities = random.randint(1, 10)
        wayout = random.randint(1, 20)
        crazy += 1
        time.sleep(1)
      elif choice == 'c':
        print("You did nothing.")
        crazy += 1
        time.sleep(1)
      elif choice == 'd':
        print ("You repeated your fine.")
        crazy -= 1
        time.sleep(1)
print("""
████████╗██╗░░██╗███████╗
╚══██╔══╝██║░░██║██╔════╝
░░░██║░░░███████║█████╗░░
░░░██║░░░██╔══██║██╔══╝░░
░░░██║░░░██║░░██║███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

██████╗░░█████╗░░█████╗░██╗░░██╗██████╗░░█████╗░░█████╗░███╗░░░███╗░██████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔════╝
██████╦╝███████║██║░░╚═╝█████═╝░██████╔╝██║░░██║██║░░██║██╔████╔██║╚█████╗░
██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║░╚═══██╗
██████╦╝██║░░██║╚█████╔╝██║░╚██╗██║░░██║╚█████╔╝╚█████╔╝██║░╚═╝░██║██████╔╝
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░""")
time.sleep(5)
os.system("cls")
string = """It was approximately 12:15 when I entered the Johnson County Community Health Clinic. 
I was there for an appointment I had set up weeks ago, just a routine checkup.
I passed the empty waiting area a small area, and approached the woman at the front desk.

“I have an appointment with Dr. Pebins?” I asked.
“What time?”
“12:30,” I replied.
She began typing something into her keyboard.
“Ah, yes,” she responded. “Gary Johnston?”
“Mhm.”
“Yes, I’ll tell the doctor. Please fill this out.”

She handed me a clipboard which held a simple fill-out form. I walked back to the waiting area, took a seat, and began to fill out the form.
I was about halfway done with filling in my information, when I slumped back. I noticed something very peculiar my head never hit the wall. In fact, it felt like it went IN.
I got up, quite frightened, and looked at the wall. Nothing. So, I reached to touch the wall. And my fingers went through it. I recoiled in shock.
“What the hell was that?” I thought, as I reached to touch the wall again Then,
suddenly, I lost my balance, tripped, and fell directly through the wall. I fell face-first onto some dirty tan carpeting.
Upon getting back up, I realized that I was in a completely different room. Well, not really a room, per se more so a set of rooms
The walls were covered in gross tan patterned wallpaper. There was also an overwhelming stench of moist carpet.

In time your Sanity Meter goes slowly up, how lower the meter the better the chance to survive.
Press sometimes D to repeat your fine. """

for letter in string:
  sleep(0.045)
  sys.stdout.write(letter)
  sys.stdout.flush()

time.sleep(5)
os.system("cls")

winsound.PlaySound("hey.wav", winsound.SND_ASYNC + winsound.SND_LOOP | winsound.SND_ALIAS )

choice = input("""What are you going to do?
A(Search the room for clues
B(Try to go through the wall
C(Do nothing: """).lower()

if choice == 'a':
  print("You found nothing.")
  time.sleep(1)
  crazy = 0
elif choice == 'b':
  print("Your hand wont go through the wall. You realize your stuck in this room")
  time.sleep(1)
  crazy += 1
elif choice == 'c':
  print("You did nothing.")
  time.sleep(1)
  crazy = 0
elif choice == 'd':
  print ("You repeated your fine.")
  time.sleep(1)
  crazy = 0

startgame()

if crazy == 30:
  print("congratulations you escaped the backrooms")
  time.sleep(1)
  input('press enter to exit')
elif crazy < 30:
  print("You no-clipped through the ground of the backrooms")
  time.sleep(1)
  print("youre falling till the end of time")
  time.sleep(1)
  input('press enter to exit')