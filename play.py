# coding: utf8
from mingus.midi import fluidsynth
import time
from random import randint
import Tkinter
import tkMessageBox

fluidsynth.init('FluidR3_GM.sf2',"alsa")


# maing dictionary for interval names
intervals = {  1 : "kleine Sekunde", \
2 : "große Sekunde" , \
3 : "kleine Terz" , \
4 : "große Terz" , \
5 : "Quart" , \
6 : "Tritonus" , \
7 : "Quinte" , \
8 : "kleine Sexte" , \
9 : "große Sexte" , \
10 : "kleine Septime" , \
11 : "große Septime" , \
12 : "Oktave" , \
13 : "Oktave + kleine Sekunde" , \
14 : "Oktave + große Sekunde" , \
15 : "Oktave + kleine Terz" , \
16 : "Oktave + große Terz" , \
17 : "Oktave + Quart" , \
18 : "Oktave + Tritonus" , \
19 : "Oktave + Quinte" , \
20 : "Oktave + kleine Sexte" , \
21 : "Oktave + große Sexte" , \
22 : "Oktave + kleine Septime" , \
23 : "Oktave + große Septime" , \
24 : "2 Oktaven" }



def start_training():

   for i in range(0,100):
     lower = randint(30,55)
     upper = lower + randint(2,20)
     diff = upper - lower

     tkMessageBox.showinfo(" ", "Play interval!")

     fluidsynth.play_Note(lower,0,100)
     fluidsynth.play_Note(upper,0,100)
     time.sleep(1)

     tkMessageBox.showinfo(" ", "Show solution!")

     s =  str(intervals[diff]) + "\n" + str(diff) + " Halbtonschritte"
     tkMessageBox.showinfo("Answer is: ", s)


window = Tkinter.Tk()

B = Tkinter.Button(window, text ="Click here to start interval training!", command = start_training)
B.pack()
window.mainloop()
