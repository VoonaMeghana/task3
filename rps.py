import random
from tkinter import *
#dictionary and vars
schema ={
    "rock":{"rock":1,"papper":0,"scissor":2},
    "papper":{"rock":2,"papper":1,"scissor":0},
    "scissor":{"rock":0,"papper":2,"scissor":1},
}

comp_score = 0
player_score= 0

#functions
def outcome_handler(player_choice):
    global comp_score
    global player_score
    outcomes = ["rock", "papper", "scissor"]
    random_number = random.randint(0,2)
    computer_choice=outcomes[random_number]
    result =schema[player_choice][computer_choice]
    if result == 2:
        player_score=player_score + 2
        player_score_label.config(text="player:"+str(player_score))
        outcome_label.config(fg="blue",text="outcome : player won")
    elif result == 1:
        player_score=player_score + 1
        comp_score=comp_score+1

        player_score_label.config(text="player:"+str(player_score))
        computer_score_label.config(text="computer:"+str(comp_score))
        outcome_label.config(fg="blue",text="outcome : draw")
    elif result==0:
        comp_score=comp_score+2
        computer_score_label.config(text="computer:"+str(comp_score))
        outcome_label.config(fg="blue",text="outcome : computer won")

#MAIN SCREEN
master = Tk()
master.title("ROCK-PAPER-SCISSOR")
#labels
Label(master,text="ROCK-PAPER-SCISSOR",font=("calbri",14)).grid(row=0,sticky=N,pady=10,padx=200)
Label(master,text="please select an option",font=("calbri",12)).grid(row=1,sticky=N,pady=10)
player_score_label=Label(master,text="player:0",font=("calbri",12))
player_score_label.grid(row=2,sticky=W)
computer_score_label=Label(master,text="computer:0",font=("calbri",12))
computer_score_label.grid(row=2,sticky=E)
player_choice_label =Label(master,font=("calbri",12))
player_choice_label.grid(row=3,sticky=E)
computer_choice_label =Label(master,font=("calbri",12))
computer_choice_label.grid(row=3,sticky=E)
outcome_label=Label(master,font=("calibri",12))
outcome_label.grid(row=3,sticky=N)
#buttons
Button(master,text="rock",width=15,command=lambda: outcome_handler("rock")).grid(row=4,sticky=W,padx=5,pady=5)

Button(master,text="paper",width=15,command=lambda: outcome_handler("papper")).grid(row=4,sticky=N,pady=5)
Button(master,text="scissor",width=15,command=lambda: outcome_handler("scissor")).grid(row=4,sticky=E,padx=5,pady=5)
#dummy label
Label(master).grid(row=5)
master.mainloop()


