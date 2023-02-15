from tkinter import *


window = Tk()
window.title("Mile to Km converter")
# window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

label_1 = Label(text="is equal to", font=("times new roman", 16, "bold"))
label_1.grid(column=1, row=1)
label_2 = Label(text="0",  font=("times new roman", 16, "bold"))
label_2.grid(column=2, row=1)
label_3 = Label(text="Miles", font=("times new roman", 16, "bold"))
label_3.grid(column=3, row=0)

label_4 = Label(text="Km", font=("times new roman", 16, "bold"))
label_4.grid(column=3, row=1)


def calculate():
    miles = input_entry.get()
    km = float(miles) * 1.609344
    round_km = round(km, 2)
    label_2.config(text=round_km)


input_entry = Entry(width=7)
input_entry.focus()
input_entry.grid(column=2, row=0)

button = Button(text="calculate", command=calculate)

button.grid(column=2, row=2)


window.mainloop()