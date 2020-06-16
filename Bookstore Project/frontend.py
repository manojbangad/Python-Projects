from tkinter import *
from backend import *

def view_command():
    list1.delete(0, END)
    all_books = get_all_books()
    for each_book in all_books:
        list1.insert(END, each_book)

def add_entry():
    insert_book(input_text_isbn.get(), input_text_title.get(), input_text_author.get(), input_text_year.get())
    view_command()


window = Tk()
window.wm_title("Bookstore")

l1 = Label(window, text = "isbn")
l1.grid(row = 0, column = 0)

l1 = Label(window, text = "title")
l1.grid(row = 0, column = 2)

l1 = Label(window, text = "author")
l1.grid(row = 1, column = 0)

l1 = Label(window, text = "year")
l1.grid(row = 1, column = 2)

input_text_isbn = StringVar()
e1 = Entry(window, textvariable = "input_text_isbn")
e1.grid(row = 0, column = 1)

input_text_title = StringVar()
e2 = Entry(window, textvariable = "input_text_title")
e2.grid(row = 0, column = 3)

input_text_author = StringVar()
e3 = Entry(window, textvariable = "input_text_author")
e3.grid(row = 1, column = 1)

input_text_year = StringVar()
e4 = Entry(window, textvariable = "input_text_year")
e4.grid(row = 1, column = 3)

# list1 = Listbox(window, height = 6, width = 35)
list1 = Listbox(window, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

b1 = Button(window, text = "View All", width = 12, command = view_command)
b1.grid(row = 2, column = 3)

b1 = Button(window, text = "Search Entry", width = 12)
b1.grid(row = 3, column = 3)

b1 = Button(window, text = "Add Entry", width = 12, command = add_entry)
b1.grid(row = 4, column = 3)

b1 = Button(window, text = "Update Entry", width = 12)
b1.grid(row = 5, column = 3)

b1 = Button(window, text = "Delete Entry", width = 12)
b1.grid(row = 6, column = 3)

b1 = Button(window, text = "Close", width = 12)
b1.grid(row = 7, column = 3)

window.mainloop()



# Kya hua tera wada
# Jiye toh jiye kaise
# chandani ???
# tum jo aaye jindgi main
#









'''



from tkinter import *
from backend import *


def add_command():
    insert(isbn_text.get(), title_text.get(),author_text.get(),year_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))


def view_command():
    list1.delete(0,END)
    result = view()
    for each_book in result:
        list1.insert(END, each_book)




window = Tk()
window.wm_title("BookStore")

l1 = Label(window, text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

b1=Button(window,text="View all", width=12, command = view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12, command = add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12)
b6.grid(row=7,column=3)

window.mainloop()




'''