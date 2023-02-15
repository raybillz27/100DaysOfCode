from tkinter import *
# screen
window = Tk()
window.title("my first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="new text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
3


# Entry

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


new_button = Button(text="new button", command=button_clicked)
new_button.grid(column=2, row=0)



window.mainloop()