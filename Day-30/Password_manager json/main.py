from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    email = email_entry.get()
    password = password_entry.get()
    search_data = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showwarning(title="Error", message="No Data File Found")
    else:
        if search_data in data.keys():
            password = data[f"{search_data}"]["password"]
            messagebox.showinfo(title=search_data,message=f"Email: {email} \nPassword: {password} ")
        else:
            messagebox.showwarning(title="Error", message="No details for the website exists")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password" : password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else :
        try:
            with open("data.json", "r") as data_file:
                #reading old data
                data =  json.load(data_file)

        except:
            with open("data.json", "w") as data_file:

                #saving updated data
                json.dump(new_data, data_file, indent=4)


        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(new_data, data_file, indent=4)

        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Buttons

gen_pass_button = Button(text="Generate Password",command=generate_password)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search",command=find_password, width=13)
search_button.grid(column=2, row=1)

# Entries

email_entry = Entry(width=53)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,"ragulkumar@gamil.com")

website_entry = Entry(width=34)
website_entry.grid(column=1, row=1)
website_entry.focus()

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

window.mainloop()