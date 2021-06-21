from random import shuffle
class Deck:
    def __init__(self):
        values = list('23456789JQK')+['10']
        suits = ['H','D','S','C']
        deck = [v+s for s in suits for v in values]
        shuffle(deck)
        self.deck = deck

    def draw_a_card(self):
        return self.deck.pop()

    def draw_n_cards(self,n):
        return [self.draw_a_card() for i in range(n)]