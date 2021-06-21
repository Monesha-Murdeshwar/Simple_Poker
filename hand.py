import tkinter
import os
from tkinter import *
from PIL import ImageTk, Image
import collections

class Hand:
    def __init__(self, deck):
        self.cards = deck.draw_n_cards(5)
        self.card_dir = os.path.join('.','cards')
        self.images = [ImageTk.PhotoImage(Image.open(os.path.join(self.card_dir,self.cards[i]+'.png')).resize((50, 100), Image.ANTIALIAS)) for i in range(5)]

    def discard(self, deck, positions):
        for p in positions:
            self.cards[p] = deck.draw_a_card()
            self.images[p] = ImageTk.PhotoImage(Image.open(os.path.join(self.card_dir,self.cards[p]+'.png')).resize((50, 100), Image.ANTIALIAS))

    def one_pair(self, hand_value):
        occurences = collections.Counter(hand_value)
        rank_pair=[]
        for card in occurences:
            if occurences[card] == 2:
                rank_pair.append(card)
        if len(rank_pair)!=1:
            return False
        return rank_pair+[val for val in hand_value if val not in rank_pair]
    
    def two_pair(self, hand_value):
        occurences = collections.Counter(hand_value)
        rank_pair=[]
        for card in occurences:
            if occurences[card] == 2:
                rank_pair.append(card)
        if len(rank_pair)!=2:
            return False
        rank_pair.sort()
        return rank_pair+[val for val in hand_value if val not in rank_pair]

    def three_kind(self,hand_value):
        occurences = collections.Counter(hand_value)
        rank_pair=[]
        for card in occurences:
            if occurences[card] == 3:
                rank_pair.append(card)
        if len(rank_pair)!=1:
            return False
        return rank_pair+[val for val in hand_value if val not in rank_pair]
    
    def four_kind(self,hand_value):
        occurences = collections.Counter(hand_value)
        rank_pair=[]
        for card in occurences:
            if occurences[card] == 4:
                rank_pair.append(card)
        if len(rank_pair)!=1:
            return False
        rank_pair.sort()
        return rank_pair+[val for val in hand_value if val not in rank_pair]

    def full_house(self,hand_value):
        if self.three_kind(hand_value) and self.one_pair(hand_value):
            return [self.three_kind(hand_value)[0],self.one_pair(hand_value)[0]]
        else:
            return False

    def straight(self,hand_value):
        hand_value.sort(reverse=True)
        if hand_value==range(hand_value[0],hand_value[0]+5):
            return [hand_value[0]+5]
        else:
            return False
    
    def flush(self,hand_value,hand_suit):
        if hand_suit.count(hand_suit[0])==5:
            return hand_value
        else:
            return False

    def straight_flush(self,hand_value,hand_suit):
        if self.straight(hand_value) and self.flush(hand_value,hand_suit):
            return self.selfstraight(hand_value)
        else:
            return False
    
    def royal(self,hand_value,hand_suit):
        if self.straight_flush(hand_value,hand_suit) and hand_value[0]==10:
            return True

    def evaluation(self):
        values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
        hand_value=[]
        hand_suit = []
        for i in range(5):
            if self.cards[i][0] in values:
                val =  values[self.cards[i][0]]
            else:
                val =  int(self.cards[i][0])
            hand_value.append(val)
            hand_suit.append(self.cards[i][1])
        hand_value.sort(reverse=True)

        if self.royal(hand_value,hand_suit):
            return (10,10)
        elif self.straight_flush(hand_value,hand_suit):
            return (9,self.straight_flush(hand_value))
        elif self.four_kind(hand_value):
            return (8,self.four_kind(hand_value))
        elif self.full_house(hand_value):
            return (7,self.full_house(hand_value))
        elif self.flush(hand_value,hand_suit):
            return (6,self.flush(hand_value))
        elif self.straight(hand_value):
            return (5,self.straight(hand_value))
        elif self.three_kind(hand_value):
            return (4,self.three_kind(hand_value))
        elif self.two_pair(hand_value):
            return (3,self.two_pair(hand_value))
        elif self.one_pair(hand_value):
            return (2,self.one_pair(hand_value))
        else:
            return (1,hand_value)
