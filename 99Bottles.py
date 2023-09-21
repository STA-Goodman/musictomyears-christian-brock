# Eli, Jace, Christian, Mya, Brandon
# 9/21/23
# Play 99 bottles of milk using winsound

# It's not our fault if it's skips, winsound is bad

import winsound as sound
import time

tripletTime = 100
sleepTime = 0.1

D = 294
E = 330
F = 349
FSHARP = 370
G = 392
A = 440

for bottles in range(99, 0, -1):
  print("{0} bottles of milk on the wall\n{0} bottles of milk\nTake one down, pass it around\n{1} bottles of milk on the wall\n".format(bottles, bottles-1))

  for i in range(3):
    sound.Beep(G, tripletTime)
    time.sleep(sleepTime)

  for i in range(3):
    sound.Beep(D, tripletTime)
    time.sleep(sleepTime)

  for i in range(3):
    sound.Beep(G, tripletTime)
    time.sleep(sleepTime)

  sound.Beep(G, tripletTime*6)
  time.sleep(sleepTime*6)

  for i in range(3):
    sound.Beep(A, tripletTime)
    time.sleep(sleepTime)

  for i in range(3):
    sound.Beep(E, tripletTime)
    time.sleep(sleepTime)

  sound.Beep(A, tripletTime*12)
  time.sleep(sleepTime*12)

  sound.Beep(FSHARP, tripletTime*6)
  time.sleep(sleepTime*6)

  sound.Beep(FSHARP, tripletTime*3)
  time.sleep(sleepTime*3)

  sound.Beep(FSHARP, tripletTime*6)
  time.sleep(sleepTime*10)

  for i in range(3):
    sound.Beep(FSHARP, tripletTime*3)
    time.sleep(sleepTime*3)
  
  sound.Beep(FSHARP, tripletTime*6)
  time.sleep(sleepTime*6)

  for i in range(4):
    sound.Beep(D, tripletTime)
    time.sleep(sleepTime)

  sound.Beep(E, tripletTime)
  time.sleep(sleepTime)
  sound.Beep(F, tripletTime)
  time.sleep(sleepTime)

  for i in range(3):
    sound.Beep(G, tripletTime)
    time.sleep(sleepTime)

  sound.Beep(G, tripletTime*6)
  time.sleep(sleepTime*6)