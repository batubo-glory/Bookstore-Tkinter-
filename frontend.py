"""
A program that stores this book information:
Title, Author
Year, ISBN

User Can:

View all records
Search an entry
Add entry
Update entry
Delete
Close

"""

from tkinter import *
from backend import Database

database = Database("books.db")

def get_selected_row(event):
    try:
        global get_selected_tuple
        index = list1.curselection()[0]
        get_selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END, get_selected_tuple[0])
        e2.delete(0, END)
        e2.insert(END, get_selected_tuple[1])
        e3.delete(0, END)
        e3.insert(END, get_selected_tuple[2])
        e4.delete(0, END)
        e4.insert(END, get_selected_tuple[3])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END, row)

def add_command():
    database.insert(title_text.get(), author_text.get(),year_text.get(),isbn_text.get())
    list1.insert(END, (title_text.get(), author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    database.delete(get_selected_tuple[0])

def update_command():
    database.update(get_selected_tuple[0], title_text.get(), author_text.get(),year_text.get(),isbn_text.get())


window = Tk()

window.wm_title("Glory's Bookstore")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=3)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=3)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row=0, column=2)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row=0, column=4)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row=1, column=2)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row=1, column=4)

list1 = Listbox(window, height=10, width=30)
list1.grid( row=2, column=1, rowspan=6, columnspan=2)

list1.bind("<<ListboxSelect>>", get_selected_row)

scroll_bar = Scrollbar(window)
scroll_bar.grid(row=2, column=3, rowspan=6)

list1.configure(yscrollcommand = scroll_bar.set)
scroll_bar.configure(command = list1.yview)

view_button = Button(window, text="View", width=13, command = view_command)
view_button.grid(row=2, column=4)

search_button = Button(window, text="Search", width=13, command = search_command)
search_button.grid(row=3, column=4)

add_button = Button(window, text="Add", width=13, command = add_command)
add_button.grid(row=4, column=4)

update_button = Button(window, text="Update", width=13, command = update_command)
update_button.grid(row=5, column=4)

delete_button = Button(window, text="Delete", width=13, command = delete_command)
delete_button.grid(row=6, column=4)

close_button = Button(window, text="Close", width=13, command = window.destroy)
close_button.grid(row=7, column=4)


window.mainloop()