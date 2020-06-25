''' Using code from https://www.youtube.com/watch?v=YXPyB4XeYLA freeCodeCamp.org youtube page
    tutorial on gui'''

from tkinter import *
from tkinter import messagebox
import os
import sys
import random
import re
import time
sys.path.append('.')
from deck import deck
from Player import Player

root = Tk()
root.title('Thirty One')
root.geometry('600x650')


gamedeck = deck(1)


hasknock = False


''' Frame work for the gui'''
def dis1():
    p1c4.pack_forget()
    gamedeck.discardpile.append(players[0].hand.pop(0))
    getCards()
    updateDiscard()
    disableDiscard()
    
def dis2():
    p1c4.pack_forget()
    gamedeck.discardpile.append(players[0].hand.pop(1))
    getCards()
    updateDiscard()
    disableDiscard()
    
def dis3():
    p1c4.pack_forget()
    gamedeck.discardpile.append(players[0].hand.pop(2))
    getCards()
    updateDiscard()
    disableDiscard()
        
def dis4():
    p1c4.pack_forget()
    gamedeck.discardpile.append(players[0].hand.pop(3))
    getCards()
    updateDiscard()
    disableDiscard()
    
    
    
root.grid_columnconfigure(0, minsize=25)
root.grid_columnconfigure(1, minsize=25)
root.grid_columnconfigure(2, minsize=25)
root.grid_columnconfigure(3, minsize=25)
root.grid_columnconfigure(4, minsize=25)
root.grid_columnconfigure(5, minsize=25)
root.grid_columnconfigure(6, minsize=25)


frame1 = LabelFrame(root, text='Player 1', padx=5, pady=5, height=11, width=200)
frame2 = LabelFrame(root, text='Player 2', padx=5, pady=5)
frame3 = LabelFrame(root, text='Player 3', padx=5, pady=5)
frame4 = LabelFrame(root, text='Player 4', padx=5, pady=5)
frame3.grid(row= 1, column = 2, columnspan = 4, padx=10, pady=10)
frame2.grid(row= 2, column = 1, rowspan = 4, padx=10, pady=10)
frame4.grid(row= 2, column = 6, rowspan = 4, padx=10, pady=10)
frame1.grid(row= 6, column = 2, columnspan = 4, padx=10, pady=5, sticky='N'+'S'+'E'+'W') 


   
p1card1 = StringVar()
p1card2 = StringVar()
p1card3 = StringVar()
p1card4 = StringVar()
p1card1.set('')
p1card2.set('')
p1card3.set('')
p1card4.set('')
p1c1 = Button(frame1, state=DISABLED, textvariable=p1card1, height=5, width=7, command=dis1)
p1c2 = Button(frame1, state=DISABLED, textvariable=p1card2, height=5, width=7, command=dis2)
p1c3 = Button(frame1, state=DISABLED, textvariable=p1card3, height=5, width=7, command=dis3)
p1c4 = Button(frame1, state=DISABLED, textvariable=p1card4, height=5, width=7, command=dis4)
p1c1.pack(side=LEFT, padx=5, pady=5)
p1c2.pack(side=LEFT, padx=5, pady=5)
p1c3.pack(side=LEFT, padx=5, pady=5)
p1c4.pack(side=LEFT, padx=5, pady=5)
p1c4.pack_forget()

p2card1 = StringVar()
p2card2 = StringVar()
p2card3 = StringVar()
p2card4 = StringVar()
p2card1.set('')
p2card2.set('')
p2card3.set('')
p2card4.set('')
p2c1 = Button(frame2, textvariable=p2card1, height=3, width=11)
p2c2 = Button(frame2, textvariable=p2card2, height=3, width=11)
p2c3 = Button(frame2, textvariable=p2card3, height=3, width=11)
p2c4 = Button(frame2, textvariable=p2card4, height=3, width=11)
p2c1.pack(padx=5, pady=5)
p2c2.pack(padx=5, pady=5)
p2c3.pack(padx=5, pady=5)
p2c4.pack(padx=5, pady=5)
p2c4.pack_forget()
   
p3card1 = StringVar()
p3card2 = StringVar()
p3card3 = StringVar()
p3card4 = StringVar()
p3card1.set('')
p3card2.set('')
p3card3.set('')
p3card4.set('')    
p3c1 = Button(frame3, textvariable=p3card1, height=5, width=7)
p3c2 = Button(frame3, textvariable=p3card2, height=5, width=7)
p3c3 = Button(frame3, textvariable=p3card3, height=5, width=7)
p3c4 = Button(frame3, textvariable=p3card4, height=5, width=7)
p3c1.pack(side=LEFT, padx=5, pady=5)
p3c2.pack(side=LEFT, padx=5, pady=5)
p3c3.pack(side=LEFT, padx=5, pady=5)
p3c4.pack(side=LEFT, padx=5, pady=5)
p3c4.pack_forget()
    
p4card1 = StringVar()
p4card2 = StringVar()
p4card3 = StringVar()
p4card4 = StringVar()
p4card1.set('')
p4card2.set('')
p4card3.set('')
p4card4.set('')
p4c1 = Button(frame4, textvariable=p4card1, height=3, width=11)
p4c2 = Button(frame4, textvariable=p4card2, height=3, width=11)
p4c3 = Button(frame4, textvariable=p4card3, height=3, width=11)
p4c4 = Button(frame4, textvariable=p4card4, height=3, width=11)
p4c1.pack(padx=5, pady=5)
p4c2.pack(padx=5, pady=5)
p4c3.pack(padx=5, pady=5)
p4c4.pack(padx=5, pady=5)
p4c4.pack_forget()
discard = StringVar()
discard.set('')
    
drawPile = Button(root, text='Deck', state=DISABLED, height=5, width=8)
drawPile.grid(row = 3, column = 3, rowspan = 2)
disPile = Button(root, textvariable=discard, state=DISABLED, height=5, width=8)
disPile.grid(row = 3, column = 4, rowspan = 2)

def getdraw():
    optionsFrame.grid_remove()
    players[0].hand.append(gamedeck.playdeck.pop())
    getCards()
    p1c4.pack(side=LEFT, padx=5, pady=5)
    enableDiscard()
    disPile.wait_variable(discard)
def getdiscard():
    optionsFrame.grid_remove()
    players[0].hand.append(gamedeck.discardpile.pop())
    getCards()
    updateDiscard()
    p1c4.pack(side=LEFT, padx=5, pady=5)
    enableDiscard()
    disPile.wait_variable(discard)
def getknock():
    optionsFrame.grid_remove()
    discard.set(discard)
    players[0].hasknock = True



optionsFrame = LabelFrame(root, padx=5, pady=5)
drawButton = Button(optionsFrame, text='Draw\nDeck', command=getdraw)
drawButton.pack(side=LEFT, padx=5, pady=5)
discardButton = Button(optionsFrame, text='Draw\nDiscard', command=getdiscard)
discardButton.pack(side=LEFT, padx=5, pady=5)
knockButton = Button(optionsFrame, text='Knock', command=getknock)
knockButton.pack(side=LEFT, padx=5, pady=5)
    
cardlist = [p1card1, p1card2, p1card3, p1card4, p2card1, p2card2, p2card3, p2card4,
            p3card1, p3card2, p3card3, p3card4, p4card1, p4card2, p4card3, p4card4, discard]
 
    


def createPlayers(lives):
    global players
    players = []
    x = 1
    while int(count) >= x:
        player = Player('Player ' + str(x), lives)
        players.append(player)
        x = x + 1        
    return players


def deal(players, gamedeck):
    x = 0
    while x < 3:
        for player in players:
            player.drawDeck(gamedeck.playdeck)
        x = x + 1
        for player in players:
            player.sortBySuit()
    gamedeck.discardpile.append(gamedeck.playdeck.pop())


def updateDiscard():
    if len(gamedeck.discardpile)>0:
        cardlist[16].set(str(gamedeck.discardpile[-1][0]) + '\nof\n' + gamedeck.discardpile[-1][1])
    else:
        cardlist[16].set('Discard\nPile')


def getCards():
    if len(gamedeck.discardpile)>0:
        cardlist[16].set(str(gamedeck.discardpile[-1][0]) + '\nof\n' + gamedeck.discardpile[-1][1])
    else:
        cardlist[16].set('Discard\nPile')
    for player in players:
        if player.name == 'Player 1':
            if len(player.hand) == 3:
                cardlist[0].set(str(player.hand[0][0]) + '\nof\n' + player.hand[0][1])
                cardlist[1].set(str(player.hand[1][0]) + '\nof\n' + player.hand[1][1])
                cardlist[2].set(str(player.hand[2][0]) + '\nof\n' + player.hand[2][1])
            else:
                cardlist[0].set(str(player.hand[0][0]) + '\nof\n' + player.hand[0][1])
                cardlist[1].set(str(player.hand[1][0]) + '\nof\n' + player.hand[1][1])
                cardlist[2].set(str(player.hand[2][0]) + '\nof\n' + player.hand[2][1])
                cardlist[3].set(str(player.hand[3][0]) + '\nof\n' + player.hand[3][1])
        if player.name == 'Player 2':
            if len(player.hand) == 3:
                cardlist[4].set(str(player.hand[0][0]) + '\nof\n' + player.hand[0][1])
                cardlist[5].set(str(player.hand[1][0]) + '\nof\n' + player.hand[1][1])
                cardlist[6].set(str(player.hand[2][0]) + '\nof\n' + player.hand[2][1])
            else:
                cardlist[4].set(str(player.hand[0][0]) + '\nof\n' + player.hand[0][1])
                cardlist[5].set(str(player.hand[1][0]) + '\nof\n' + player.hand[1][1])
                cardlist[6].set(str(player.hand[2][0]) + '\nof\n' + player.hand[2][1])
                cardlist[7].set(str(player.hand[3][0]) + '\nof\n' + player.hand[3][1])
        if player.name == 'Player 3':
            if len(player.hand) == 3:
                cardlist[8].set(str(player.hand[0][0]) + '\nof\n' + player.hand[0][1])
                cardlist[9].set(str(player.hand[1][0]) + '\nof\n' + player.hand[1][1])
                cardlist[10].set(str(player.hand[2][0]) + '\nof\n' + player.hand[2][1])
            else:
                cardlist[8].set(str(player.hand[0][0]) + '\nof\n' + player.hand[0][1])
                cardlist[9].set(str(player.hand[1][0]) + '\nof\n' + player.hand[1][1])
                cardlist[10].set(str(player.hand[2][0]) + '\nof\n' + player.hand[2][1])
                cardlist[11].set(str(player.hand[3][0]) + '\nof\n' + player.hand[3][1])
        if player.name == 'Player 4':
            if len(player.hand) == 3:
                cardlist[12].set(str(player.hand[0][0]) + '\nof\n' + player.hand[0][1])
                cardlist[13].set(str(player.hand[1][0]) + '\nof\n' + player.hand[1][1])
                cardlist[14].set(str(player.hand[2][0]) + '\nof\n' + player.hand[2][1])
            else:
                cardlist[12].set(str(player.hand[0][0]) + '\nof\n' + player.hand[0][1])
                cardlist[13].set(str(player.hand[1][0]) + '\nof\n' + player.hand[1][1])
                cardlist[14].set(str(player.hand[2][0]) + '\nof\n' + player.hand[2][1])
                cardlist[15].set(str(player.hand[3][0]) + '\nof\n' + player.hand[3][1])       



def turnOptions(lastround):    
    optionsFrame.grid(row= 8, column = 2, columnspan = 4, padx=10, pady=5)
    if lastround == True:
        knockButton.pack_forget()
    
    

def enableDiscard():
    p1c1['state'] = NORMAL
    p1c2['state'] = NORMAL
    p1c3['state'] = NORMAL
    p1c4['state'] = NORMAL

def disableDiscard():
    p1c1['state'] = DISABLED
    p1c2['state'] = DISABLED
    p1c3['state'] = DISABLED
    p1c4['state'] = DISABLED
    
def countHand(playerHand):
    # Counts your total for each suit.  returns total for the suit or suits with the highest value.
    diamonds = 0
    hearts = 0
    spades = 0
    clubs = 0
    x = 0
    while x < len(playerHand):
        card = playerHand[x]
        x = x + 1
        if card[1] == 'Spades':
            if card[0] == 'Ace':
                spades = spades + 11
            elif card[0] == 'King' or card[0] == 'Queen' or card[0] == 'Jack':
                spades = spades + 10
            else:
                spades = spades + card[0]
        elif card[1] == 'Clubs':
            if card[0] == 'Ace':
                clubs = clubs + 11
            elif card[0] == 'King' or card[0] == 'Queen' or card[0] == 'Jack':
                clubs = clubs + 10
            else:
                clubs = clubs + card[0]
        elif card[1] == 'Diamonds':
            if card[0] == 'Ace':
                diamonds = diamonds + 11
            elif card[0] == 'King' or card[0] == 'Queen' or card[0] == 'Jack':
                diamonds = diamonds + 10
            else:
                diamonds = diamonds + card[0]
        elif card[1] == 'Hearts':
            if card[0] == 'Ace':
                hearts = hearts + 11
            elif card[0] == 'King' or card[0] == 'Queen' or card[0] == 'Jack':
                hearts = hearts + 10
            else:
                hearts = hearts + card[0]
    
    countlist = [(diamonds, 'diamonds'), (hearts, 'hearts'),(spades, 'spades'), (clubs, 'clubs')]
    countlist = sorted(countlist, reverse=True)
    
    if countlist[0][0] > countlist[1][0]:
        return [countlist[0][0], countlist[0][1]]
    elif countlist[0][0] == countlist[1][0] and countlist[0][0] > countlist[2][0]:
        return [countlist[0][0], countlist[0][1], countlist[1][1]]
    elif countlist[0][0] == countlist[1][0] and countlist[0][0] == countlist[2][0] and countlist[0][0] > countlist[3][0]:
        return [countlist[0][0], countlist[0][1], countlist[1][1], countlist[2][1]]
    else:
        return [countlist[0][0], countlist[0][1], countlist[1][1], countlist[2][1], countlist[3][1]]
    
    
def compTurn(player):
    highHand = countHand(player.hand)
    if highHand[0] >25:            
        player.hasknock = True
    elif gamedeck.discardpile[-1][1] in highHand and gamedeck.discardpile[-1][0] > 7:
        player.drawDeck(gamedeck.discardpile)
        updateDiscard()
    else:
        player.drawDeck(gamedeck.playdeck)
        getCards()
        
def compLastTurn(player):
    highHand = countHand(player.hand)
    if gamedeck.discardpile[-1][1] in highHand and gamedeck.discardpile[-1][0] > 7:
        player.drawDeck(gamedeck.discardpile)
        updateDiscard()
    else:
        player.drawDeck(gamedeck.playdeck)
        getCards()


def compDiscard(player):
    highHand = countHand(player.hand)
    highValue = highHand.pop(0)        
    lowcard = player.hand[:]
    jacks = []
    queens = []
    kings = []
    aces = []
    y = 0
    while len(lowcard) > y:
        if lowcard[y][0] == 'Jack':
            jacks = jacks + [lowcard[y]]
            lowcard.remove(lowcard[y])
        elif lowcard[y][0] == 'Queen':
            queens = queens + [lowcard[y]]
            lowcard.remove(lowcard[y])
        elif lowcard[y][0] == 'King':
            kings = kings + [lowcard[y]]
            lowcard.remove(lowcard[y])
        elif lowcard[y][0] == 'Ace':
            aces = aces + [lowcard[y]]
            lowcard.remove(lowcard[y])
        else:
            y = y + 1
    lowcard = sorted(lowcard)
    lowcard = lowcard + jacks + queens + kings + aces
    discardlist = []
    if len(highHand) == 1:
        x = 0
        while x < len(lowcard):                
            if lowcard[x][1] == highHand[0]:                    
                x = x + 1
            else:                    
                discardlist.append(lowcard[x])
                x = x + 1
        if len(discardlist) > 0:
            gamedeck.discardpile.append(player.hand.pop(player.hand.index(discardlist[0])))                    
            return
        else:
            gamedeck.discardpile.append(player.hand.pop(player.hand.index(lowcard[0])))
            return
    elif len(highHand) == 2:
        x = 0
        while x < len(lowcard):               
            if lowcard[x][1] == highHand[0] or lowcard[x][1] == highHand[1]:                    
                x = x + 1
            else:                    
                discardlist.append(lowcard[x])
                x = x + 1
        if len(discardlist) > 0:
            gamedeck.discardpile.append(player.hand.pop(player.hand.index(discardlist[0])))
            return
        else:
            gamedeck.discardpile.append(player.hand.pop(player.hand.index(lowcard[0])))
            return
    elif len(highHand) == 3:
        x = 0
        while x < len(lowcard):                
            if lowcard[x][1] == highHand[0] or lowcard[x][1] == highHand[1] or lowcard[x][1] == highHand[2]:                    
                x = x + 1
            else:                    
                discardlist.append(lowcard[x])
                x = x + 1
        if len(discardlist) > 0:
            gamedeck.discardpile.append(player.hand.pop(player.hand.index(discardlist[0])))
            return
        else:
            gamedeck.discardpile.append(player.pop(player.index(lowcard[0])))
            return
    else:
        newdiscard = random.choice(lowcard)
        player.hand.remove(newdiscard)
        gamedeck.discardpile.append(newdiscard)
        return


def endRound(players):
    ''' Calculates all the players scores(using countHand method)
        and prints them from player with the highest score to player with the lowest score'''
    final = []
    losers = []
    for player in players:
        playerHand = countHand(player.hand)
        if playerHand[0] == 31 and len(player.hand) == 3:
            print (player.name + ' has 31!!!')
            index = players.index(player)
            for player in players:
                if player != players[index]:
                    losers.append(player)
            for loser in losers:
                loser.lives = loser.lives - 1
            return
        final.append((playerHand[0], playerHand[1] , player.name))
        print (player.hand)
        print ('\n')
    final = sorted(final, reverse=True)
    x = 0
    while x < len(final):
        print (str(final[x][2]) + ' has ' + str(final[x][0]) + ' in ' + str(final[x][1]))
        x = x + 1
    
    final = sorted(final)
    y = 1
    
    losers.append(final[0])
    print('\n')
    while y < len(final):
        if final[0][0] == final[y][0]:
            losers.append(final[y])
            y = y + 1
        else:
            y = y + 1
    if len(losers) == len(players):
            print ('All players lose a life!')
            for loser in losers:
                for player in players:
                    if loser[2] == player.name:
                        player.lives = player.lives - 1
    else:
        for loser in losers:
            print(loser[2] + ' has lost a life!')
            for player in players:
                if loser[2] == player.name:
                    player.lives = player.lives - 1
    print('\n')
    return

def newHand(players, gamedeck):
    for player in players:
        gamedeck.playdeck = gamedeck.playdeck + player.hand
        player.hand = []
    gamedeck.playdeck = gamedeck.playdeck + gamedeck.discardpile
    gamedeck.discardpile = []
    gamedeck.shuffleDeck(5)


global lastround
lastround = False

 

def game():
    replay = 1
    global players
    has31 = False
    global lastround
    lastOrder = []
    global count
    count = e.get()
    if int(count) > 1 and  int(count) < 5:
        players = createPlayers(3)
        top.destroy()
    else:
        lbl = Label(top, text = 'Please use numbers 2 through 4')
        lbl.pack()
    p1lives = Label(root, text='Lives - ' + str(players[0].lives))
    p1lives.grid(row= 7, column = 2, columnspan = 4)
    while len(players) > 1:
        deal(players, gamedeck)        
        while lastround == False:   
            for player in players:
                if len(gamedeck.playdeck) == 0:
                    break
                print(gamedeck.discardpile)
                if player.name == 'Player 1':
                    getCards()
                    updateDiscard()
                    turnOptions(lastround)
                    print(str(player.hasknock))
                    if player.hasknock == True:
                        print('hello2')
                        lastOrder = players[players.index(player):] + players[:players.index(player)]
                        lastround = True 
                        break
                    print('hello')
                    disPile.wait_variable(discard)
                    is31 = countHand(player.hand)
                    if is31[0] == 31:
                        has31 = True
                        break
                    if len(gamedeck.playdeck) == 0:
                        break   
                else:            
                    compTurn(player)
                    if player.hasknock == False:            
                        getCards()
                        compDiscard(player)
                        updateDiscard()
                        getCards()
                        if len(gamedeck.playdeck) == 0:
                            break   
                    else:
                        lastOrder = players[players.index(player):] + players[:players.index(player)]      
                        lastround = True
                        break
            is31 = countHand(player.hand)
            if is31[0] == 31:
                has31 = True
                break
            if len(gamedeck.playdeck) == 0:
                break   
        print('*******************lastround')
        x = len(lastOrder)
        if has31 == False:
            if len(gamedeck.playdeck) > 0:                    
                while x > 0:
                    for player in lastOrder:
                        is31 = countHand(player.hand)
                        if is31[0] == 31:
                            break
                        if len(gamedeck.playdeck) == 0:
                            break
                        elif player == lastOrder[0]:    
                            x = x - 1
                        else:
                            if player.name == 'Player 1':
                                getCards()
                                updateDiscard()
                                turnOptions(lastround)
                                disPile.wait_variable(discard)                                
                                knockButton.pack(side=LEFT, padx=5, pady=5)
                                is31 = countHand(player.hand)
                                if is31[0] == 31:
                                    break
                                x = x - 1
                            else:
                                compLastTurn(player)
                                getCards()
                                compDiscard(player)
                                updateDiscard()
                                getCards()
                                if is31[0] == 31:
                                    break
                                x = x - 1
                        if len(gamedeck.playdeck) == 0:
                            break
        endRound(players)
        for player in players:
            if player.lives < 0:
                print (player.name + ' has left the game.')                    
                players.remove(player)
            else:
                print(player.name +' has ' + str(player.lives) + ' lives left.')
        p1lives = Label(root, text='Lives - ' + str(players[0].lives))
        p1lives.grid(row= 7, column = 2, columnspan = 4)
        newHand(players, gamedeck)
        lastround = False
        has31 = False
        for player in players:
            player.hasknock = False
        
        
    replay = messagebox.askyesno('Play Again?','Would you like to play again?')       
    if replay == 1:
        playerSelect()
          
    else:
        exit(1)
    return


def playerSelect():
    playerBtn.grid_remove()
    global top
    global e
    top = Toplevel()
    top.title('Player Select')
    lbl = Label(top, text='Enter number of players between 2 and 4')
    lbl.pack()
    e = Entry(top, width = 10)
    e.pack()
    okButton = Button(top, text = 'Ok', command = game)
    okButton.pack()



playerBtn = Button(root, text='Start Game', command=playerSelect, height=4, width = 10)
playerBtn.grid(row=2, column = 3, columnspan = 2, rowspan = 2)




root.mainloop()