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
    
    def output_text(self,score_human, score_AI):
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

        result = "AI : " + hand_names[score_AI[0]] + "\n You : " + hand_names[score_human[0]]
        winner ="\n Winner : "
        if score_human[0] > score_AI[0]:
            winner += "You"
        elif score_human[0] < score_AI[0]:
            winner += "AI."
        else:
            sorted_human = sorted(score_human[1], reverse=True)
            sorted_AI =  sorted(score_AI[1], reverse=True)
            i = 0
            while i < len(sorted_human):
                if sorted_human[i] > sorted_AI[i]:
                    result += "\n You have HigherX."
                    winner += "You"
                    break
                elif sorted_human[i] < sorted_AI[i]:
                    result += "\n AI has HigherX."
                    winner += "AI"
                    break
                i+=1
        result += winner
                
        return result

    def play(self, hand_human, hand_AI, deck, human_card_space, AI_card_space, states, commentry, play_button, reset_button):
        discarded_states = [state.get() for state in states]
        positions = [i for i,n in enumerate(discarded_states) if n==0]
        hand_human.discard(deck, positions)     
        for i in range(5):
            AI_card_space[i].config(image=hand_AI.images[i])
            if i in positions:
                human_card_space[i].config(image=hand_human.images[i])

        score_human = hand_human.eval()
        score_AI = hand_AI.eval()

        if (score_human[0] > score_AI[0]):
            self.player_cash += 50
            self.ai_cash -=50
        else:
            self.player_cash -= 50
            self.ai_cash += 50

        result = self.output_text(score_human, score_AI)
        commentry.config(text=result)
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

        commentry = tkinter.Label(master, text="Select Retainable Cards")
        commentry.grid(row=1, column=0, columnspan=5)

        player_cash_label = tkinter.Label(master, text="Player = $"+str(self.player_cash))
        player_cash_label.grid(row=4, column=3, columnspan=1)

        ai_cash_label = tkinter.Label(master, text="AI = $"+str(self.ai_cash))
        ai_cash_label.grid(row=4, column=4, columnspan=1)

        human_card_space = [tkinter.Label(master) for i in range(5)]
        AI_card_space = [tkinter.Label(master) for i in range(5)]
        discard_states = []
        back = ImageTk.PhotoImage(Image.open(os.path.join(self.card_dir,'red_back.png')).resize((50, 100), Image.ANTIALIAS))

        
        for i in range(5):
            AI_card_space[i].grid(row=0, column=i)
            human_card_space[i].grid(row=2, column=i)
            human_card_space[i].config(image=hand_human.images[i])
            discard_card = tkinter.IntVar()
            chk = tkinter.Checkbutton(master, variable=discard_card)
            chk.grid(row=3,column=i)
            discard_states.append(discard_card)
        
        reset_button = tkinter.Button(master, text='PLAY AGAIN', command=lambda: self.resetGame(master, commentry, player_cash_label, ai_cash_label, AI_card_space))
        reset_button.grid(row = 4, column = 1)
        self.disable(reset_button)

        play_button = tkinter.Button(master, text='DRAW', command=lambda: self.play(hand_human, hand_AI, deck, human_card_space, AI_card_space, discard_states, commentry, play_button, reset_button))
        play_button.grid(row=4, column=0)

        master.mainloop()
    
    def resetGame(self, master, commentry, player_cash_label, ai_cash_label,AI_card_space):
        deck = Deck()
        hand_AI = Hand(deck)
        hand_human = Hand(deck)

        reset_text = "Select retainable cards"
        commentry.config(text=reset_text)

        human_card_space = [tkinter.Label(master) for i in range(5)]
        AI_card_space = [tkinter.Label(master) for i in range(5)]
        discard_states = []
        back = ImageTk.PhotoImage(Image.open(os.path.join(self.card_dir,'red_back.png')).resize((50, 100), Image.ANTIALIAS))
        
        for i in range(5):
            AI_card_space[i].grid(row=0, column=i)
            AI_card_space[i].config(image=back)
            human_card_space[i].grid(row=2, column=i)
            human_card_space[i].config(image=hand_human.images[i])
            discard_card = tkinter.IntVar()
            chk = tkinter.Checkbutton(master, variable=discard_card)
            chk.grid(row=3,column=i)
            discard_states.append(discard_card)
        
        reset_button = tkinter.Button(master, text='PLAY AGAIN', command=lambda: self.resetGame(master, commentry, player_cash_label, ai_cash_label, AI_card_space))
        reset_button.grid(row = 4, column = 1)
        self.disable(reset_button)
        play_button = tkinter.Button(master, text='DRAW', command=lambda: self.play(hand_human, hand_AI, deck, human_card_space, AI_card_space, discard_states, commentry, play_button, reset_button))
        play_button.grid(row=4, column=0)

        player_cash_label.config(text="Player = $"+str(self.player_cash))
        ai_cash_label.config(text="AI = $"+str(self.ai_cash))

