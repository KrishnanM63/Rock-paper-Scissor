from tkinter import *
import random
from tkinter import messagebox


choice=['Rock','paper','scissors']
emoji={'Rock':'🪨','paper':'🗞️','scissors':'✂️'}

your_score=0
computer_score=0
def update_score():
    score.set(f"Me: {your_score}  computer: {computer_score}")
def reset():
    global your_score
    global computer_score
    your_score=0
    computer_score=0
    result.set("Make your move!")
    update_score()
    

def play(user_choice):
    global your_score
    global computer_score
    computer_choice=random.choice(choice)
    print(computer_choice)
    if user_choice==computer_choice:
        result.set(f"Computer: {computer_choice}{emoji[computer_choice]}\n Tie")
      
    elif(user_choice=="Rock") and (computer_choice=="scissors")\
    or (user_choice=="scissors") and (computer_choice=="paper")\
    or (user_choice=="paper") and (computer_choice=="Rock"):
        your_score+=1
       
        result.set(f"Computer: {computer_choice}{emoji[computer_choice]}\n you win")
        update_score()
          
        
    else:
        computer_score+=1
        result.set(f"Computer: {computer_choice}{emoji[computer_choice]}\n computer win")
        update_score()
    
krish=Tk()
krish.title("Rock_Paper_Scissors ")
krish.geometry("450x500")
score=StringVar()
score.set("Me:0  Computer:0")
Label(krish,text="🎮 Rock Paper Scissor 🎮",font=("Arial",20,"bold"),fg="blue").place(x=50,y=30)
Label(krish,textvariable=score,font=("Arial",20,"bold")).place(x=100,y=100)

btnfrm=Frame(krish)
btnfrm.place(x=50,y=180)

Button(btnfrm,text="Rock 🪨",font=("Arial",12,"bold"),fg="orange",bg="#ccd5ae",width=10,command=lambda:play("Rock")).grid(row=2,column=2)

Button(btnfrm,text="Paper 🗞️",font=("Arial",12,"bold"),fg="orange",bg="#ccd5ae",width=10,command=lambda:play("paper")).grid(row=2,column=3,padx=5)
Button(btnfrm,text="Scissors ✂️",font=("Arial",12,"bold"),fg="orange",bg="#ccd5ae",width=10,command=lambda:play("scissors")).grid(row=2,column=4,padx=5)

result=StringVar()
result.set("Make your move!")
Label(krish,textvariable=result,font=("Arial",10,"bold")).place(x=160,y=240)

cntbtn=Frame(krish).place(x=160,y=200)

Button(text="Reset",font=("Arial",10,"bold"),width=10,bg="green",fg="white",command=reset).place(x=120,y=290)
Button(text="Exit",font=("Arial",10,"bold"),width=10,bg="red",fg="white",command=krish.destroy).place(x=250,y=290)
krish.mainloop()
