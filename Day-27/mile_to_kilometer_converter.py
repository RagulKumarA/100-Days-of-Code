from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=30, pady=30)

# label

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.configure(padx=20)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

answer_label = Label(text=" 0 ")
answer_label.grid(column=1, row=1)

# button
def calculate():
    user_input = float(input.get())
    convert_mile_to_km = round(user_input * 1.609)
    answer_label.config(text=str(convert_mile_to_km))


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


# Entry

input = Entry(width=10)
input.grid(column = 1, row=0)











window.mainloop()
