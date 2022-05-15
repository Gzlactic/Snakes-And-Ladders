import random
import time

import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.config(background='grey')

board = tk.Canvas(root,width=1000,height=1000,borderwidth=0,highlightthickness=0)
board.place(relx=0.5,rely=0.45,anchor=tk.CENTER)

global turn
turn = 'player'

global changeTurn
changeTurn = False

global changeText
changeText = False

global gameWon
gameWon = False

allDice = ['\Dice1.png','\Dice2.png','\Dice3.png','\Dice4.png','\Dice5.png','\Dice6.png']

notif = tk.Label(root,font=("Arial",20), text='Welcome to Snakes and Ladders! Click to roll the dice.',background='grey')
notif.place(relx=0.5,rely=0.925,anchor=tk.CENTER)


def gameSetUp():
    root.geometry("1000x1100")
    root.resizable(False,False)
    
    for x in range(1,11):
        if x % 2 == 0:
            for i in range(1,11):
                xpos =  1000 - (i*100-100)
                ypos = 1000 - (x*100-100)
                if i % 2 == 1:
                    board.create_rectangle(xpos-100,ypos-100,xpos,ypos,fill='green',outline='green')
                else:
                    board.create_rectangle(xpos-100,ypos-100,xpos,ypos,fill='white',outline='white')
        else:
            for i in range(1,11):
                xpos = i * 100
                ypos = 1000 - (x*100-100)
                if i % 2 == 1:
                    board.create_rectangle(xpos-100,ypos-100,xpos,ypos,fill='green',outline='green')
                else:
                    board.create_rectangle(xpos-100,ypos-100,xpos,ypos,fill='white',outline='white')
    for x in range(1,11):
        if x % 2 == 0:
            for i in range(1,11):
                xpos =  1000 - (i*100-100)
                ypos = 1000 - (x*100-100)
                textval = str((x-1)*10+i)
                board.create_text(xpos-50,ypos-50,text=textval,font = ("Arial",30))
        else:
            for i in range(1,11):
                xpos = i * 100
                ypos = 1000 - (x*100-100)
                textval = str((x-1)*10+i)
                board.create_text(xpos-50,ypos-50,text=textval,font = ("Arial",30))
def load():
    global board
    ladders = [['\Ladder1.png',350,735],['\Ladder2.png',750,655],['\Ladder3.png',150,40],['\Ladder4.png',-40,550],['\Ladder5.png',0,110],['\Ladder6.png',800,-10]]
    limg = []
    for i in range(0,len(ladders)):
        ladderid = 'Assets\Ladders' + ladders[i][0]
        limg.append(tk.PhotoImage(file=ladderid))
        root.limg = limg
        board.create_image(ladders[i][1],ladders[i][2],anchor=tk.NW,image = limg[i])
    
    snakes = [['\Snake1.png',300,700],['\Snake2.png',505,410],['\Snake4.png',0,230],['\Snake3.png',-100,300],['\Snake5.png',130,105],['\Snake6.png',575,5],['\Snake7.png',375,5],['\Snake8.png',25,5]]
    simg = []
    for i in range(0,len(snakes)):
        snakeid = 'Assets\Snakes' + snakes[i][0]
        simg.append(tk.PhotoImage(file=snakeid))
        root.simg = simg
        board.create_image(snakes[i][1],snakes[i][2],anchor=tk.NW,image = simg[i])
class Player():
    def __init__(self,master,colour,startPos):
        self.master = master
        self.canvas = board
        self.player = self.canvas.create_oval(startPos[0],startPos[1],startPos[2],startPos[3],fill=colour,outline=colour)
        self.currentPlace = 1
        self.placeOver100 = 0
    def laddercheck(self):
        global turn
        global changeText
        ladderpos = [(4,14),(9,31),(20,38),(28,84),(63,81),(71,91)]
        if turn == 'player':
            self.xoffset = 5
            self.yoffset = 5
        elif turn == 'computer':
            self.xoffset = 5
            self.yoffset = 55
        for i in range(0,len(ladderpos)):
            if ladderpos[i][0] == self.currentPlace:
                self.currentPlace = ladderpos[i][1]
                self.coord = self.canvas.coords(ladderpos[i][1])
                notif.config(text=f'The {turn} has landed on a ladder, they are now on square {ladderpos[i][1]}')
                self.master.update()
                self.canvas.moveto(self.player,self.coord[0]+self.xoffset,self.coord[1]+self.yoffset)
                changeText = True
                time.sleep(1)
    def snakecheck(self):
        global turn
        global changeText
        snakepos = [(17,7),(54,34),(62,18),(64,60),(87,24),(93,73),(95,75),(99,78)]
        if turn == 'player':
            self.xoffset = 5
            self.yoffset = 5
        elif turn == 'computer':
            self.xoffset = 5
            self.yoffset = 55
        for i in range(0,len(snakepos)):
            if snakepos[i][0] == self.currentPlace:
                self.currentPlace = snakepos[i][1]
                self.coord = self.canvas.coords(snakepos[i][1])
                notif.config(text=f'The {turn} has landed on a snake, they are now on square {snakepos[i][1]}')
                self.master.update()
                self.canvas.moveto(self.player,self.coord[0]+self.xoffset,self.coord[1]+self.yoffset)
                changeText = True
                time.sleep(1)
        
    def movePlayer(self,places):
        global turn
        global gameWon
        global changeTurn
        for i in range(0,places+1):
            if self.currentPlace > 99:
                self.canvas.move(self.player,100,0)
                self.placeOver100 += 1
            elif self.currentPlace % 10 == 0:
                self.canvas.move(self.player,0,-100)
            elif self.currentPlace % 20 > 10:
                self.canvas.move(self.player,-100,0)
            else:
                self.canvas.move(self.player,100,0)
            self.currentPlace += 1
            time.sleep(0.25)
            self.master.update()

        self.currentPlace = self.currentPlace - (self.placeOver100*2)
        self.placeOver100 = 0

        if self.currentPlace == 100:
            gameWon = True
            changeTurn = False
            
            dice.diceButton['state'] = 'disabled'
            notif.config(text=f'The {turn} has won! Restart the program to play again.') 
            root.update()
            turn = ''
        else:
            self.laddercheck()
            self.snakecheck()
class Dice():
    def __init__(self,master):
        self.master = master
        self.canvas = board

        self.allDice = allDice

        self.diceid = 'Assets\Dice' + allDice[random.randint(0,5)]
        self.path = Image.open(self.diceid)
        self.load = ImageTk.PhotoImage(self.path)

        self.diceButton = tk.Button(self.master, image = self.load)
        self.diceButton.place(relx=0.5,rely=0.97,anchor=tk.CENTER)

    def rollDice(self,player):
        global turn
        global changeTurn
        
        self.diceButton['state'] = 'disabled'
        self.player = player

        for i in range(1,21):
            time.sleep(i/100)
            global x
            global changeText
            changeText = False
            x = random.randint(0,5)

            self.diceid = 'Assets\Dice' + allDice[x]
            self.path = Image.open(self.diceid)
            self.load = ImageTk.PhotoImage(image=self.path)
            self.diceButton.config(image=self.load)
            root.update()
        if turn == 'player' and not gameWon:
            if x+1 == 6:
                changeText = True
                notif.config(text='You rolled a 6! It is your turn again.')
                changeTurn = False
                root.update()
                self.player.movePlayer(x)
                self.diceButton['state'] = 'normal'
            else:
                changeText = True
                notif.config(text='You rolled a ' + str(x+1) + '.')
                changeTurn = True
                root.update()
                self.player.movePlayer(x)
        elif turn == 'computer' and not gameWon:
            root.update()
            if x+1 == 6:
                notif.config(text='The computer rolled a 6! It is their turn again.')
                self.diceButton['state'] = 'disabled'
                changeTurn = False
                root.update()
                self.player.movePlayer(x)        
            else:
                changeText = True
                notif.config(text='The computer rolled a ' + str(x+1) + '.')
                changeTurn = True
                root.update()
                self.player.movePlayer(x)
        changeText = False

        
def setUp():
    gameSetUp()
    load()
    global user
    user = Player(root,'#FF6961',[5,905,45,945])
    board.tag_raise(user)
    
    global computer
    computer = Player(root,'#A7C7E7',[5,955,45,995])
    board.tag_raise(computer)

setUp()

dice = Dice(root)
dice.diceButton.config(command= lambda: dice.rollDice(user))

def gameOn():
    global turn
    global changeTurn
    global changeText
    if turn == 'player' and not changeText and not gameWon:
        if changeTurn:
            changeTurn = False
            turn = 'computer'
    elif turn == 'computer' and not changeText and not gameWon:
        notif.config(text='It is now the computers turn!')
        dice.rollDice(computer)
        if changeTurn:
            changeTurn = False
            dice.diceButton['state'] = 'normal'
            turn = 'player'
            notif.config(text='Your turn! Click to roll the dice!')
            
    root.after(250,gameOn)

root.after(0,gameOn)
root.protocol("WM_DELETE_WINDOW",exit)
root.mainloop()