from tkinter import *
import calendar

#create a new window
window = Tk()
# size of window
window.geometry("500x300")

#name of window
window.title("Calendar App")

#background of the window
window.config(background="SlateBlue1")

# Add a label(text)
emptylabel = Label(window,bg="SlateBlue1",width=20)
clabel = Label(window,text="Calendar for any year",bg="SlateBlue1",fg="snow",font=("Comic Sans MS",15,"bold"))
ylabel = Label(window,text="Write any year here",bg="SlateBlue1",fg="snow",font=("Comic Sans MS",11))
#entry widget
yinput = Entry(window)
#button
show = Button(window,text="Show Calendar",bg="SeaGreen",fg="snow")
exit = Button(window,text="Exit Window",bg="SeaGreen",fg="snow")

#position
emptylabel.grid(row=1,column=1)#grid system
clabel.grid(row=1,column=2)
ylabel.grid(row=2,column=2)
yinput.grid(row=3,column=2)#can't skip sequence number, or use other method
show.grid(row=4,column=2)
exit.grid(row=5,column=2)

#start the gui
window.mainloop()