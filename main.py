from tkinter import *

FONT_STYLE = ("Arial", 12, "bold")
# conversion_mode = "miles_to_km"


def miles_to_km():
    number = int(input_one.get())
    result = round(number * 1.609, 2)
    result_label.config(text=result)


def km_to_miles():
    number = int(input_one.get())
    result = round(number / 1.609, 2)
    result_label.config(text=result)


def swap():
    # global conversion_mode
    miles = miles_label["text"]
    km = km_label["text"]
    miles_label.config(text=km)
    km_label.config(text=miles)
    if button_convert["text"] == "Convert miles to km":
        button_convert.config(text="Convert km to miles", command=km_to_miles)
    else:
        button_convert.config(text="Convert miles to km", command=miles_to_km)


window = Tk()
window.title("My first GUI program")
window.minsize(width=200, height=60)
window.config(padx=20, pady=10)

# labels
my_label = Label(text="Is equal to", font=FONT_STYLE)
my_label.grid(column=0, row=1)

miles_label = Label(text="Miles", font=FONT_STYLE)
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=0)

km_label = Label(text="Km", font=FONT_STYLE)
km_label.grid(column=2, row=1)

result_label = Label(text="?", font=FONT_STYLE)
result_label.grid(column=1, row=1)

# Input
input_one = Entry(width=15)
input_one.grid(column=1, row=0)

# buttons
button_convert = Button(text="Convert miles to km", command=miles_to_km, font=("Arial", 8, "bold"))
button_convert.grid(column=1, row=2)

button_swap = Button(text="Swap mode", command=swap, font=("Arial", 8, "bold"))
button_swap.grid(column=2, row=2)
button_swap.config(padx=15)

mainloop()
