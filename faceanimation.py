import time
import os

# As you can see, its not very optimal 
def smile1():
    print(" _______ ")
    print(" | - - | ")
    print(" |     | ")
    print(" |     | ")
    print(" | \_/ |  ")
    print(" |_____| ")


def smile2():
    print(" _______ ")
    print(" | - - | ")
    print(" |     | ")
    print(" |     | ")
    print(" | ___ |  ")
    print(" |_____| ")

def smile3():
    print(" _______ ")
    print(" | \ / | ")
    print(" |     | ")
    print(" |  _  | ")
    print(" | / \ |  ")
    print(" |_____| ")
  
if __name__ == "__main__":
  time.sleep(.1)
  smile1()
  time.sleep(.5)
  smile2()
  time.sleep(.5)
  smile3()
  time.sleep(.5)
