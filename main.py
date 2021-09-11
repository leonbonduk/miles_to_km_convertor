from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

Eq_to_label = Label(text="is equal to")
Eq_to_label.grid(column=0,row=1)

#Entries
entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="Enter miles...")

entry.grid(column=1,row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2,row=0)

kms_label = Label(text="kms")
kms_label.grid(column=2,row=1)

conversion_label = Label(text="0")
conversion_label.grid(column=1,row=1)

#Buttons
def action():
    print("Do something")
    # Gets text in entry
    miles_to_convert = float(entry.get())
    kms_converted = miles_to_convert * 1.6
    conversion_label.config(text=kms_converted)

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)

window.mainloop()