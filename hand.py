import tkinter
import os
from tkinter import *
from PIL import ImageTk, Image

class Hand:
    def __init__(self, deck):
        self.cards = deck.draw_n_cards(5)
        self.card_dir = os.path.join('.','cards')
        self.images = [ImageTk.PhotoImage(Image.open(os.path.join(self.card_dir,self.cards[i]+'.png')).resize((50, 100), Image.ANTIALIAS)) for i in range(5)]

    def discard(self, deck, positions):
        for p in positions:
            self.cards[p] = deck.draw_a_card()
            self.images[p] = ImageTk.PhotoImage(Image.open(os.path.join(self.card_dir,self.cards[p]+'.png')).resize((50, 100), Image.ANTIALIAS))

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

    
    #     def onepair(hand):
    #         vhand=valhand(hand)
    #         pairvalue=[]
    #         for i in vhand:
    #             if vhand.count(i)==2:
    #                 pairvalue.append(i)
    #         if len(pairvalue)!=2:
    #             return False
    #         for i in pairvalue:
    #             vhand.remove(i)
    #         pairvalue=list(set(pairvalue))
    #         pairvalue.sort()
    #         return pairvalue+vhand
    
    #     def twopair(hand):
    #         vhand=valhand(hand)
    #         pairvalue=[]
    #         for i in vhand:
    #             if vhand.count(i)==2:
    #                 pairvalue.append(i)
    #         if len(pairvalue)!=4:
    #             return False
    #         for i in pairvalue:
    #             vhand.remove(i)
    #         pairvalue=list(set(pairvalue))
    #         pairvalue.sort()
    #         return pairvalue+vhand
    
    #     def threekind(hand):
    #         vhand=valhand(hand)
    #         pairvalue=[]
    #         for i in vhand:
    #             if vhand.count(i)==3:
    #                 pairvalue.append(i)
    #         if len(pairvalue)!=3:
    #             return False
    #         for i in pairvalue:
    #             vhand.remove(i)
    #         pairvalue=list(set(pairvalue))
    #         return pairvalue+vhand
        
    #     def straight(hand):
    #         vhand=valhand(hand)
    #         vhand.reverse()
    #         if vhand==range(vhand[0],vhand[0]+5):
    #             return [vhand[0]+5]
    #         else:
    #             return False
        
    #     def flush(hand):
    #         vhand=valhand(hand)
    #         shand=suithand(hand)
    #         if shand.count(shand[0])==5:
    #             return vhand
    #         else:
    #             return False
        
    #     def fullhouse(hand):
    #         if threekind(hand) and onepair(hand):
    #             return [threekind(hand)[0],onepair(hand)[0]]
    #         else:
    #             return False
        
    #     def fourkind(hand):
    #         vhand=valhand(hand)
    #         pairvalue=[]
    #         for i in vhand:
    #             if vhand.count(i)==4:
    #                 pairvalue.append(i)
    #         if len(pairvalue)!=4:
    #             return False
    #         for i in pairvalue:
    #             vhand.remove(i)
    #         pairvalue=list(set(pairvalue))
    #         return pairvalue+vhand
        
    #     def straightflush(hand):
    #         if straight(hand) and flush(hand):
    #             return straight(hand)
    #         else:
    #             return False
        
    #     def royal(hand):
    #         if straightflush(hand) and valhand(hand)[0]==10:
    #             return True
    
    #     if royal(self.cards):
    #         return (10,10)
    #     elif straightflush(self.cards):
    #         return (9,straightflush(self.cards))
    #     elif fourkind(self.cards):
    #         return (8,fourkind(self.cards))
    #     elif fullhouse(self.cards):
    #         return (7,fullhouse(self.cards))
    #     elif flush(self.cards):
    #         return (6,flush(self.cards))
    #     elif straight(self.cards):
    #         return (5,straight(self.cards))
    #     elif threekind(self.cards):
    #         return (4,threekind(self.cards))
    #     elif twopair(self.cards):
    #         return (3,twopair(self.cards))
    #     elif onepair(self.cards):
    #         return (2,onepair(self.cards))
    #     else:
    #         return (1,valhand(self.cards))
