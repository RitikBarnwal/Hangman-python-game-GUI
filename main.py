from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title('Hangman Game - Guess the Cities')
window.config(bg="RoyalBlue4")

word_list= ['MUMBAI','DELHI','BANGLORE','HYDRABAD','AHMEDABAD','CHENNAI','KOLKATA','SURAT','PUNE','JAIPUR','AMRITSAR','ALLAHABAD','RANCHI','LUCKNOW','KANPUR','NAGPUR','INDORE','THANE','BHOPAL','PATNA','GHAZIABAD','AGRA','FARIDABAD','MEERUT','RAJKOT','VARANASI','SRINAGAR','RAIPUR','KOTA','JHANSI']
#Adding spaces to the word and keeping it in dictionary
word_dict = dict()
for each_word in word_list:
  word_dict[each_word]=" ".join(each_word)

photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), 
PhotoImage(file="images/hang2.png"),
PhotoImage(file="images/hang3.png"), 
PhotoImage(file="images/hang4.png"), 
PhotoImage(file="images/hang5.png"),
PhotoImage(file="images/hang6.png"), 
PhotoImage(file="images/hang7.png"), 
PhotoImage(file="images/hang8.png"),
PhotoImage(file="images/hang9.png"), 
PhotoImage(file="images/hang10.png"), 
PhotoImage(file="images/hang11.png")]


def newGame():
    global numberOfGuesses
    global the_word_withSpaces
    numberOfGuesses=0
    the_word=random.choice(word_list)
    the_word_withSpaces = word_dict[the_word]
#rest of the code goes here later
    lblWord.set(' '.join("_"*len(the_word)))

def guess(letter):
  global numberOfGuesses
  if numberOfGuesses<11:
    txt = list(the_word_withSpaces)
    guessed = list(lblWord.get())
    if the_word_withSpaces.count(letter)>0:
      for c in range(len(txt)):
        if txt[c]==letter:
          guessed[c]=letter
        lblWord.set("".join(guessed))
        if lblWord.get()==the_word_withSpaces:
          messagebox.showinfo("Hangman","You guessed it!")
    else:
      numberOfGuesses += 1
      imgLabel.config(image=photos[numberOfGuesses])
      if numberOfGuesses==11:
        messagebox.showwarning("Hangman","Game Over")



lblWord = StringVar()
Label(window, textvariable=lblWord,font=('consolas 24 bold'),bg="RoyalBlue4",fg="White").grid(row=2, column=0 ,columnspan=10,padx=10,pady=20)

imgLabel=Label(window)
imgLabel.grid(row=1, column=1, columnspan=3, padx=10, pady=40)
imgLabel.config(bg="Royalblue4")
  
  
#count for the letters from A to Z
count=0
#count for the button
button_on_each_row = 5
for each_letter in range(ord("A"),ord("Z")+1):
    letter = chr(each_letter)
    Button(window, text=letter,font=('Helvetica 14 bold'),command=lambda letter=letter:guess(letter), width=5 ,bg="RoyalBlue4", fg="white").grid(row=(1+count//button_on_each_row)+2,column=count%button_on_each_row)
    count+=1
Button(window, text="New\nGame",font=("Helvetica 10 bold"),width=6,bg="RoyalBlue4",fg="white").grid(row=9, column=2)

newGame()
window.mainloop()