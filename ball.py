import board
import neopixel as np
import time
import sys
from threading import *
from sshkeyboard import listen_keyboard, stop_listening
from frameMaker import frame,render

print(board.__file__)
print(np.__file__)

# Declarations
led = np.NeoPixel(board.D18, 64, brightness=0.2, auto_write=False)
val = 20
refreshRate = 0.35
start_condition = False

# -----------------Bit Maps--------------
bitmap_P = (
    0b00000000,
    0b01111000,
    0b01000100,
    0b01000100,
    0b01111000,
    0b01000000,
    0b01000000,
    0b00000000)
frame_P = frame(bitmap_P)

bitmap_I = (
    0b00000000,
    0b00111000,
    0b00010000,
    0b00010000,
    0b00010000,
    0b00010000,
    0b00111000,
    0b00000000
)
frame_I = frame(bitmap_I)

bitmap_N = (
    0b00000000,
    0b01000010,
    0b01100010,
    0b01010010,
    0b01001010,
    0b01000110,
    0b01000010,
    0b00000000
)
frame_N = frame(bitmap_N)

bitmap_G = (
    0b00000000,
    0b00111100,
    0b01000010,
    0b01000000,
    0b01001110,
    0b01000010,
    0b00111100,
    0b00000000
)
frame_G = frame(bitmap_G)

bitmap_O = (
    0b00000000,
    0b00011000,
    0b01100110,
    0b01000010,
    0b01000010,
    0b01100110,
    0b00011000,
    0b00000000
)
frame_O = frame(bitmap_O)
# ------------Class definition Player Panels------------

class panel:

    def __init__(self,anchor,r,g,b):
        self.pixelA = anchor
        self.pixelB = anchor+8
        self.r = r
        self.g = g
        self.b = b
        led[anchor] = (r,g,b)
        led[anchor+8] = (r,g,b)
        led.show()

    def move(self, dir):
        if dir == 0 and (self.pixelA-8>=0):
            self.pixelB = self.pixelA
            self.pixelA = self.pixelA - 8
        if dir == 1 and (self.pixelB+8<=63):
            self.pixelA = self.pixelB
            self.pixelB = self.pixelB + 8

    def update(self):
        led[self.pixelA] = (self.r,self.g,self.b)
        led[self.pixelB] = (self.r,self.g,self.b)
        led.show()

#-------------ball definition----------------
class ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.index = 8*y + x
        self.isRight = True
        self.isFalling = True
        self.vertBounds = (0,1,2,3,4,5,6,7,56,57,58,59,60,61,62,63)
        self.latBounds = (0,8,16,24,32,40,48,56,15,23,31,39,47,55,63)
        self.boundary = (0,1,2,3,4,5,6,7,8,15,16,23,24,31,32,39,40,47,48,55,56,57,58,59,60,61,62,63)
        self.flag_OUT = False

    def __str__(self):
        isBoundary  = self.isBoundary()
        return f"Index:{self.index} - X:{self.x}, Y:{self.y}|On Boundary: {isBoundary}\n"

    #------Converters---------
    def toIndex(self):
        return (self.y*8 + self.x)

    #----Condition Checkers-----
    def isBoundary(self):
        if self.index in self.boundary:
            print("On Boundary!\n")
            return True
        else:
            return False

    def isVertBound(self):
        if self.index in self.vertBounds:
            print(f"Ball has hit vertical bounds at {self.index}")
            return True
        else:
            return False

    def isLatBound(self):
        if self.index in self.latBounds:
            print(f"Ball has hit lateral bounds at {self.index}")
            return True
        else:
            return False

    def isCorner(self):
        if self.index in self.corners:
            print(f"Ball has hit the corners at {self.index}")
            return True
        else:
            return False

    def isPanel(self,player1,player2):
        if self.isRight and self.index+1 == player2.pixelA or self.index+1 == player2.pixelB:
            print(f"Ball has hit p2 panel at {self.index}")
            return 2
        elif not self.isRight and self.index-1 == player1.pixelA or self.index-1 == player1.pixelB:
            print(f"Ball has hit p1 panel at {self.index}")
            return 1
        else:
            return 0

    def updatePos(self):
        if self.isRight:
            self.x = self.x + 1
        else:
            self.x = self.x - 1
        if self.isFalling:
            self.y = self.y + 1
        else:
            self.y = self.y - 1

        self.index = self.toIndex()


    #-------Ball Game Logic----------
    def game(self,player1,player2):
        if self.isVertBound():
            if self.index <= 7:
                self.isFalling = True
            else:
                self.isFalling = False
        if self.isLatBound():
            if self.index%8==0:
                return 0
            else:
                return 1
        c = self.isPanel(player1,player2)
        if c == 1:
            self.isRight = True
        if c == 2:
            self.isRight = False

        self.updatePos()

        if self.index == player1.pixelA or self.index == player1.pixelB or self.index == player2.pixelA or self.index == player2.pixelB:
            self.isRight = not self.isRight
            self.isFalling = not self.isFalling 
            self.updatePos()
            if self.isVertBound():
                if self.index <= 7:
                    self.isFalling = True
                else:
                    self.isFalling = False
            
            self.updatePos()


        led.fill((0,0,0))
        player1.update()
        player2.update()
        led[self.index] = (0,val,0)
        player1.update()
        player2.update()
        led.show()
        return -1

def getInput():
    listen_keyboard(on_press = controllerInput, on_release = None, delay_second_char = refreshRate-0.04,debug=True)


x = int(sys.argv[1])
y = int(sys.argv[2])

b = ball(x,y)
p1 = panel(8,10,0,10)
p2 = panel(47,0,10,10)

def controllerInput(key):
    if not start_condition:
        start_condition = True
    if key=='w':
        p1.move(0)
    if key=='s':
        p1.move(1)
    if key=='i':
        p2.move(0)
    if key=='k':
        p2.move(1)

t1 = Thread(target=getInput)
t1.setDaemon(True)
t1.start()        

print(b)
frames = [frame_P, frame_I, frame_N, frame_G, frame_P, frame_O, frame_N, frame_N, frame_G]
while not start_condition:
    for i in frames:
        render(led,i,0,20,0)
        time.sleep(2)

while True:
    state = b.game(p1,p2)
    if state == 0:
        print("PLAYER 2 scores a point")
        time.sleep(2)
    if state == 1:
        print("PLAYER 1 scores a point")
        time.sleep(2)
    if state == 0 or state == 1:
        b = ball(x,y)
    time.sleep(refreshRate)
