import sys
import random


class deck:

       
    
    def __init__(self, deckNum = 1):
        self.S = 'Spades'
        self.D = 'Diamonds'
        self.H = 'Hearts'
        self.K = 'Clubs'
        self.playdeck = []
        self.discardpile = []
        x = 0
        while x < deckNum:
            self.playdeck = self.playdeck + self.createDeck()
            x = x + 1
        self.shuffleDeck(50)
    
    
    def createDeck(self):
        S = 'Spades'
        D = 'Diamonds'
        H = 'Hearts'
        K = 'Clubs'    
        deck = [('Ace', S), ('Ace', D), ('Ace', H),('Ace', K),
        (2, S), (2, D), (2, H),(2, K),
        (3, S), (3, D), (3, H),(3, K),
        (4, S), (4, D), (4, H),(4, K),
        (5, S), (5, D), (5, H),(5, K),
        (6, S), (6, D), (6, H),(6, K),
        (7, S), (7, D), (7, H),(7, K),
        (8, S), (8, D), (8, H),(8, K),
        (9, S), (9, D), (9, H),(9, K),
        (10, S), (10, D), (10, H),(10, K),
        ('Jack', S), ('Jack', D), ('Jack', H),('Jack', K),
        ('Queen', S), ('Queen', D), ('Queen', H),('Queen', K),
        ('King', S), ('King', D), ('King', H),('King', K)]
        return deck
        
    def shuffleDeck(self, shufcount):
        x = 0
        while x < shufcount:
            random.shuffle(self.playdeck)
            x = x + 1
            