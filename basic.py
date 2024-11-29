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

# calendar function
def calendar_open():
    year = int(yinput.get())
    calendar_window = Tk()
    calendar_window.geometry("550x600")
    calendar_window.title("Year present")
    calendar_window.config(background="SlateBlue1")
    calendar_content = calendar.calendar(year)
    calendar_output = Label(calendar_window,text=calendar_content,font="Consolas 10 bold")
    calendar_output.grid(row=1,column=1,padx=20)
    def destroy_calendar():
        calendar_window.destroy()
    exit1 = Button(calendar_window,text="Exit Window",bg="SeaGreen",fg="snow",command=(destroy_calendar))
    exit1.grid(row=2,column=1)
    calendar_window.mainloop()


# Add a label(text)
emptylabel = Label(window,bg="SlateBlue1",width=20)
clabel = Label(window,text="Calendar for any year",bg="SlateBlue1",fg="snow",font=("Comic Sans MS",15,"bold"))
ylabel = Label(window,text="Write any year here",bg="SlateBlue1",fg="snow",font=("Comic Sans MS",11,"bold"))
#entry widget
yinput = Entry(window)
#button
show = Button(window,text="Show Calendar",bg="SeaGreen",fg="snow",command=calendar_open)
exit = Button(window,text="Exit Window",bg="SeaGreen",fg="snow",command=exit)

#position
emptylabel.grid(row=1,column=1)#grid system
clabel.grid(row=1,column=2)
ylabel.grid(row=2,column=2)
yinput.grid(row=3,column=2)#can't skip sequence number, or use other method
show.grid(row=4,column=2)
exit.grid(row=5,column=2)



#start the gui
window.mainloop()
