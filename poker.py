import tkinter
import os
from deck import Deck
from hand import Hand
from tkinter import *
from PIL import ImageTk, Image

class Poker:
    def __init__(self):
        self.player_cash = 1000
        self.ai_cash = 1000
        self.card_dir = os.path.join('.','cards')
    
    def summary(self,score_human, score_AI):
        hand_names = {1:'high card',
                    2:'one pair', 
                    3:'two pair', 
                    4:'three of a kind', 
                    5:'a straight', 
                    6:'a flush', 
                    7:'a full house', 
                    8:'four of a kind', 
                    9:'a straight flush', 
                    10:'a royal flush'}

        result = "AI : " + hand_names[score_AI[0]] + "\n You : " + hand_names[score_human[0]] + ".\n Winner : "
        if score_human[0] > score_AI[0]:
            result += "You"
        elif score_human[0] < score_AI[0]:
            result += "AI."
        else:
            sorted_human = sorted(score_human[1], reverse=True)
            sorted_AI =  sorted(score_AI[1], reverse=True)
            i = 0
            while i < len(sorted_human):
                if sorted_human[i] > sorted_AI[i]:
                    result += "You have HigherX. \n Hence winner: You"
                    break
                elif sorted_human[i] < sorted_AI[i]:
                    result += "AI has HigherX. \n Hence winner: AI"
                    break
                i+=1
        return result

    def play(self, hand_human, hand_AI, deck, cardlabels_human, cardlabels_AI, states, announcer, play_button, reset_button):
        states = [state.get() for state in states]
        positions = [i for i in range(len(states)) if not states[i]]
        hand_human.discard(deck, positions)
        for p in positions:
            cardlabels_human[p].config(image=hand_human.images[p])
        for i in range(5):
            cardlabels_AI[i].config(image=hand_AI.images[i])
        score_human = hand_human.evaluation()
        score_AI = hand_AI.evaluation()

        if (score_human[0] > score_AI[0]):
            self.player_cash += 50
            self.ai_cash -=50
        else:
            self.player_cash -= 50
            self.ai_cash += 50

        result = self.summary(score_human, score_AI)
        announcer.config(text=result)
        self.disable(play_button)
        self.enable(reset_button)

    def disable(self,button):
        button.config(state=tkinter.DISABLED)

    def enable(self,button):
        button.config(state=tkinter.ACTIVE)
    
    def mainGame(self):
        master = tkinter.Tk()
        master.title('Simple Five-Card Draw')
        deck = Deck()
        hand_AI = Hand(deck)
        hand_human = Hand(deck)

        announcer = tkinter.Label(master, text="Select the cards you would like to retain")
        announcer.grid(row=1, column=0, columnspan=5)

        player_cash_label = tkinter.Label(master, text="Player = $"+str(self.player_cash))
        player_cash_label.grid(row=4, column=3, columnspan=1)

        ai_cash_label = tkinter.Label(master, text="AI = $"+str(self.ai_cash))
        ai_cash_label.grid(row=4, column=4, columnspan=1)

        cardlabels_human = [tkinter.Label(master) for i in range(5)]
        cardlabels_AI = [tkinter.Label(master) for i in range(5)]
        discard_states = []
        back = ImageTk.PhotoImage(Image.open(os.path.join(self.card_dir,'red_back.png')).resize((50, 100), Image.ANTIALIAS))

        
        for i in range(5):
            cardlabels_AI[i].grid(row=0, column=i)
            # cardlabels_AI[i].config(image=back)
            cardlabels_human[i].grid(row=2, column=i)
            cardlabels_human[i].config(image=hand_human.images[i])
            discard_card = tkinter.IntVar()
            chk = tkinter.Checkbutton(master, variable=discard_card)
            chk.grid(row=3,column=i)
            discard_states.append(discard_card)
        
        reset_button = tkinter.Button(master, text='PLAY AGAIN', command=lambda: self.resetGame(master, announcer, player_cash_label, ai_cash_label, cardlabels_AI))
        reset_button.grid(row = 4, column = 1)
        self.disable(reset_button)

        play_button = tkinter.Button(master, text='DRAW', command=lambda: self.play(hand_human, hand_AI, deck, cardlabels_human, cardlabels_AI, discard_states, announcer, play_button, reset_button))
        play_button.grid(row=4, column=0)

        master.mainloop()
    
    def resetGame(self, master, announcer, player_cash_label, ai_cash_label,cardlabels_AI):
        deck = Deck()
        hand_AI = Hand(deck)
        hand_human = Hand(deck)

        reset_text = "Select the cards you would like to retain"
        announcer.config(text=reset_text)

        cardlabels_human = [tkinter.Label(master) for i in range(5)]
        cardlabels_AI = [tkinter.Label(master) for i in range(5)]
        discard_states = []
        back = ImageTk.PhotoImage(Image.open(os.path.join(self.card_dir,'red_back.png')).resize((50, 100), Image.ANTIALIAS))
        
        for i in range(5):
            cardlabels_AI[i].grid(row=0, column=i)
            cardlabels_AI[i].config(image=back)
            cardlabels_human[i].grid(row=2, column=i)
            cardlabels_human[i].config(image=hand_human.images[i])
            discard_card = tkinter.IntVar()
            chk = tkinter.Checkbutton(master, variable=discard_card)
            chk.grid(row=3,column=i)
            discard_states.append(discard_card)
        
        reset_button = tkinter.Button(master, text='PLAY AGAIN', command=lambda: self.resetGame(master, announcer, player_cash_label, ai_cash_label, cardlabels_AI))
        reset_button.grid(row = 4, column = 1)
        self.disable(reset_button)
        play_button = tkinter.Button(master, text='DRAW', command=lambda: self.play(hand_human, hand_AI, deck, cardlabels_human, cardlabels_AI, discard_states, announcer, play_button, reset_button))
        play_button.grid(row=4, column=0)

        player_cash_label.config(text="Player = $"+str(self.player_cash))
        ai_cash_label.config(text="AI = $"+str(self.ai_cash))

