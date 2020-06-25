import random
import sys
import os
import re

class Player:
    
    def __init__(self, name, lives = 1):  
        self.name = name
        self.hand = []
        self.lives = lives
        self.bid = 0
        self.books = 0
        self.hasknock = False
    def discard(self, card):       
            return self.hand.pop(card)
    
    
    def drawDeck(self, gamedeck, cardNum = 1):
        x = 0
        while x < cardNum:
            self.hand.append(gamedeck.pop())
            x = x + 1

    def sortBySuit(self):
        clubs = []
        hearts = []
        spades = []
        diamonds = []
        sortedhand = []
        ace = []
        king = []
        queen = []
        jack = [] 
        #self.hand = sorted(self.hand, key = lambda x: x[1])
        
        #pulls cards by suits and puts them in their own list
        for card in self.hand:
            if card[1] == 'Clubs':
                clubs.append(card)
            elif card[1] == 'Spades':
                spades.append(card)
            elif card[1] == 'Hearts':
                hearts.append(card)
            elif card[1] == 'Diamonds':
                diamonds.append(card)
        #checks all spades for face cards and pulls them in thier own list
        for card in spades:
            if card[0] == 'Ace':
                ace.append(card)
            elif card[0] == 'King':
                king.append(card)
            elif card[0] == 'Queen':
                queen.append(card)
            elif card[0] == 'Jack':
                jack.append(card)
        
        for card in ace:
            spades.remove(card)
        for card in king:
            spades.remove(card)
        for card in queen:
            spades.remove(card)
        for card in jack:
            spades.remove(card)
        
        #sorts remaing spades and adds them to the sorted hand
        sortedhand = sortedhand + sorted(spades)
        spades = []
        sortedhand = sortedhand + jack
        jack = []
        sortedhand = sortedhand + queen
        queen = []
        sortedhand = sortedhand + king
        king = []
        sortedhand = sortedhand + ace
        ace = []

        for card in hearts:
            if card[0] == 'Ace':
                ace.append(card)
            elif card[0] == 'King':
                king.append(card)
            elif card[0] == 'Queen':
                queen.append(card)
            elif card[0] == 'Jack':
                jack.append(card)
        
        for card in ace:
            hearts.remove(card)
        for card in king:
            hearts.remove(card)
        for card in queen:
            hearts.remove(card)
        for card in jack:
            hearts.remove(card)
        
        #sorts remaing hearts and adds them to the sorted hand
        sortedhand = sortedhand + sorted(hearts)
        hearts = []
        sortedhand = sortedhand + jack
        jack = []
        sortedhand = sortedhand + queen
        queen = []
        sortedhand = sortedhand + king
        king = []
        sortedhand = sortedhand + ace
        ace = []
        
        for card in diamonds:
            if card[0] == 'Ace':
                ace.append(card)
            elif card[0] == 'King':
                king.append(card)
            elif card[0] == 'Queen':
                queen.append(card)
            elif card[0] == 'Jack':
                jack.append(card)
        
        for card in ace:
            diamonds.remove(card)
        for card in king:
            diamonds.remove(card)
        for card in queen:
            diamonds.remove(card)
        for card in jack:
            diamonds.remove(card)
        
        #sorts remaing diamonds and adds them to the sorted hand
        sortedhand = sortedhand + sorted(diamonds)
        diamonds = []
        sortedhand = sortedhand + jack
        jack = []
        sortedhand = sortedhand + queen
        queen = []
        sortedhand = sortedhand + king
        king = []
        sortedhand = sortedhand + ace
        ace = []
        
        for card in clubs:
            if card[0] == 'Ace':
                ace.append(card)
            elif card[0] == 'King':
                king.append(card)
            elif card[0] == 'Queen':
                queen.append(card)
            elif card[0] == 'Jack':
                jack.append(card)
        
        for card in ace:
            clubs.remove(card)
        for card in king:
            clubs.remove(card)
        for card in queen:
            clubs.remove(card)
        for card in jack:
            clubs.remove(card)            
        #sorts remaing clubs and adds them to the sorted hand
        sortedhand = sortedhand + sorted(clubs)
        clubs = []
        sortedhand = sortedhand + jack
        jack = []
        sortedhand = sortedhand + queen
        queen = []
        sortedhand = sortedhand + king
        king = []
        sortedhand = sortedhand + ace
        ace = []
        
        self.hand = sortedhand
        