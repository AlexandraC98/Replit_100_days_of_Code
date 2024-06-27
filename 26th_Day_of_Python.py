import os
import time
import pygame
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')

def pause():
  pygame.mixer.pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  sound.play()
  while True:
    # Start taking user input and doing something with it
    user_input=input("Press 'p' to pause, 'r' to resume, 'q' to quit: ")
    if user_input=="p":
      pause()
    elif user_input=="r":
      pygame.mixer.unpause()
    elif user_input=="q":
      sound.stop()
      break
    else:
      print("Invalid input. Please try again.")

while True:
  # clear the screen
  os.system("clear")
  # Show the menu
  print("\033[35m","🎵 MyPOD Music Player", "\033[0m")
  # take user's input
  print("Press 1 to Play")
  print("Press 2 to Pause")
  print("Press 3 to Exit")
  user_input=input("Your choice: ")
  # check whether you should call the play() subroutine depending on user's input
  if user_input=="1":
    play()
  elif user_input=="2":
    pause()
  elif user_input=="3":
    break
  else:
    print("Invalid input. Please try again.")
  time.sleep(2)
