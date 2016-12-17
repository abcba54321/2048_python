import copy
from graphics import *
from button import *
import time
import random
class Number:
    def __init__(self,wVal,xVal,yVal,number):
        self.w = wVal
        self.x = xVal
        self.y = yVal
        self.num = number
        self.t = Text(Point(xVal,yVal),str(number))
        self.s = Rectangle(Point(xVal-1,yVal-1),Point(xVal+1,yVal+1))
        self.t.setSize(20)
        self.t.draw(wVal)
        self.s.draw(wVal)

    def move(self,dx,dy):
        self.t.move(dx,dy)
        self.s.move(dx,dy)
    def doubleNumber(self):
        self.num *=2
        self.t.setText(str(self.num))
    def undraw(self):
        self.t.undraw()
        self.s.undraw()
    
        

class Game:
    def prepare(self):
        #set blackground
        self.win = GraphWin("game 2048.",400,560)
        self.win.setCoords(0,0,10,14)
        for i in range(4):
            for j in range(4):
                Rectangle(Point(2*j+1,2*i+5),Point(2*j+3,2*i+7)).draw(self.win)

        #set buttons
        self.unButton = Button(self.win,Point(1.8,3.5),1.6,1,"UnDo")
        self.lButton = Button(self.win,Point(1.8,1.5),1.6,1,"<==")
        self.uButton = Button(self.win,Point(4,3.5),1.6,1,"/\\")
        self.dButton = Button(self.win,Point(4,1.5),1.6,1,"\/")
        self.rButton = Button(self.win,Point(6.2,1.5),1.6,1,"==>")
        self.reButton = Button(self.win,Point(8.5,3.5),2,1,"Restart")
        self.qButton = Button(self.win,Point(8.5,1.5),2,1,"Quit")
        self.rButton.activate()
        self.qButton.activate()

        #beginning
        self.l = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.track_list = []
        self.createNumber()
        self.lButton.activate()
        self.uButton.activate()
        self.dButton.activate()
        self.rButton.activate()
        self.quit = 0

    def createNumber(self):
        while True:
            x = random.randint(1,4)
            y = random.randint(1,4)
            num = random.randint(1,2)*2
            if self.l[y-1][x-1] == 0:
                self.l[y-1][x-1] = Number(self.win,2*x,2*y+4,num)
                self.track_list.append(copy.copy(self.l))
                break
        
    def start(self):
        l1 = self.l
        while True:
            q1 = self.win.getMouse()
            if self.qButton.clicked(q1):
                self.quit = 1
                break
            if self.rButton.clicked(q1):
                pass
            if self.lButton.clicked(q1):
                left1 = self.left()
                if True:
                    self.createNumber()
            if self.uButton.clicked(q1):
                self.up()
                self.createNumber()
            if self.dButton.clicked(q1):
                self.down()
                self.createNumber()
            if self.rButton.clicked(q1):
                self.right()
                self.createNumber()
        if self.quit == 1:
            self.win.close()
    def left(self):
        k=0
        for i in range(4):
            m=0
            for j in range(4):
                if self.l[i][j] == 0:
                    m+=1
                if isinstance(self.l[i][j],Number)and m!=0:
                    self.l[i][j].move(-2*m,0)
                    self.l[i][j-m],self.l[i][j] = self.l[i][j],self.l[i][j-m]
                    k+=1
            for j in range(3):
                if isinstance(self.l[i][j],Number)and\
                   isinstance(self.l[i][j+1],Number):
                    if self.l[i][j].num == self.l[i][j+1].num:
                        self.l[i][j+1].move(-2,0)
                        self.l[i][j].undraw()
                        self.l[i][j+1].doubleNumber()
                        self.l[i][j],self.l[i][j+1]=self.l[i][j+1],0
                        k+=1
            m=0
            for j in range(4):
                if self.l[i][j] == 0:
                    m+=1
                if isinstance(self.l[i][j],Number):
                    self.l[i][j].move(-2*m,0)
                    self.l[i][j-m],self.l[i][j] = self.l[i][j],self.l[i][j-m]
        return k      
                        
    def up(self):
        pass
        
    def down(self):
        pass
    def right(self):
        pass
    

def main():
    ga = Game()
    ga.prepare()
    ga.start()
 


main()
    
    
