import tkinter as tk
from tkinter import *

# window specs
root = Tk()
root.title('Calculator')
root.geometry('408x355')
root.minsize(408, 355)
root.maxsize(408, 355)

# background
root.configure(background='#282828')

num1 = ''
num2 = ''
division = FALSE
multiple = FALSE
sum = FALSE
subtraction = FALSE

# user input
input = Entry(root, width=15,
              borderwidth=4,
              relief=FLAT,
              fg='#FFFFFF',
              bg='#a7a28f',
              font=('futura', 25, 'bold'),
              justify=CENTER)
input.grid(row=0,
           column=0,
           columnspan=4,
           pady=2)

# operation functions


def click_button(num):
    input.insert(END, num)


def division_button():
    global num1
    global division
    division = TRUE
    num1 = input.get()
    input.delete(0, END)


def multiplie_button():
    global num1
    global multiple
    multiple = TRUE
    num1 = input.get()
    input.delete(0, END)


def subtraction_button():
    global num1
    global subtraction
    subtraction = TRUE
    num1 = input.get()
    input.delete(0, END)


def sum_button():
    global num1
    global sum
    sum = TRUE
    num1 = input.get()
    input.delete(0, END)


def clean_button():
    input.delete(0, END)


def total_button():
    global division
    global multiple
    global subtraction
    global sum
    num2 = input.get()
    input.delete(0, END)

    if sum == TRUE:
        input.insert(0, int(num1) + int(num2))
        sum = FALSE

    if multiple == TRUE:
        input.insert(0, int(num1) * int(num2))
        multiple = FALSE

    if subtraction == TRUE:
        input.insert(0, int(num1) - int(num2))
        subtraction = FALSE

    if division == TRUE:
        input.insert(0, int(num1) / int(num2))
        division = FALSE


# division button
div = Button(root,
             text='%',
             padx=40,
             pady=20,
             command=division_button,
             fg='#FFFFFF',
             activeforeground='#FFFFFF',
             bg='#FFA500',
             activebackground='#FFA500',
             relief=FLAT,
             font=('futura', 12, 'bold'))
div.grid(row=0, column=4)

# first line
one = Button(root,
             text='1',
             padx=40,
             pady=20,
             command=lambda: click_button(1),
             fg='#FFFFFF',
             activeforeground='#FFFFFF',
             bg='#708090',
             activebackground='#708090',
             relief=FLAT,
             font=('futura', 12, 'bold'))
one.grid(row=1, column=1)

two = Button(root,
             text='2',
             padx=40,
             pady=20,
             command=lambda: click_button(2),
             fg='#FFFFFF',
             activeforeground='#FFFFFF',
             bg='#708090',
             activebackground='#708090',
             relief=FLAT,
             font=('futura', 12, 'bold'))
two.grid(row=1, column=2)

three = Button(root,
               text='3',
               padx=40,
               pady=20,
               command=lambda: click_button(3),
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#708090',
               activebackground='#708090',
               relief=FLAT,
               font=('futura', 12, 'bold'))
three.grid(row=1, column=3)

# multiplie
div = Button(root,
             text='x',
             padx=44.5,
             pady=20,
             command=multiplie_button,
             fg='#FFFFFF',
             activeforeground='#FFFFFF',
             bg='#FFA500',
             activebackground='#FFA500',
             relief=FLAT,
             font=('futura', 12, 'bold'))
div.grid(row=1, column=4)

# second line
four = Button(root,
              text='4',
              padx=40,
              pady=20,
              command=lambda: click_button(4),
              fg='#FFFFFF',
              activeforeground='#FFFFFF',
              bg='#708090',
              activebackground='#708090',
              relief=FLAT,
              font=('futura', 12, 'bold'))
four.grid(row=2, column=1)

five = Button(root,
              text='5',
              padx=40,
              pady=20,
              command=lambda: click_button(5),
              fg='#FFFFFF',
              activeforeground='#FFFFFF',
              bg='#708090',
              activebackground='#708090',
              relief=FLAT,
              font=('futura', 12, 'bold'))
five.grid(row=2, column=2)

six = Button(root,
             text='6',
             padx=40,
             pady=20,
             command=lambda: click_button(6),
             fg='#FFFFFF',
             activeforeground='#FFFFFF',
             bg='#708090',
             activebackground='#708090',
             relief=FLAT,
             font=('futura', 12, 'bold'))
six.grid(row=2, column=3)

# subtraction
div = Button(root,
             text='-',
             padx=47,
             pady=20,
             command=subtraction_button,
             fg='#FFFFFF',
             activeforeground='#FFFFFF',
             bg='#FFA500',
             activebackground='#FFA500',
             relief=FLAT,
             font=('futura', 12, 'bold'))
div.grid(row=2, column=4)

# third line
seven = Button(root,
               text='7',
               padx=40,
               pady=20,
               command=lambda: click_button(7),
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#708090',
               activebackground='#708090',
               relief=FLAT,
               font=('futura', 12, 'bold'))
seven.grid(row=3, column=1)

eight = Button(root,
               text='8',
               padx=40,
               pady=20,
               command=lambda: click_button(8),
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#708090',
               activebackground='#708090',
               relief=FLAT,
               font=('futura', 12, 'bold'))
eight.grid(row=3, column=2)

nine = Button(root,
              text='9',
              padx=40,
              pady=20,
              command=lambda: click_button(9),
              fg='#FFFFFF',
              activeforeground='#FFFFFF',
              bg='#708090',
              activebackground='#708090',
              relief=FLAT,
              font=('futura', 12, 'bold'))
nine.grid(row=3, column=3)

# sum
div = Button(root,
             text='+',
             padx=45,
             pady=20,
             command=sum_button,
             fg='#FFFFFF',
             activeforeground='#FFFFFF',
             bg='#FFA500',
             activebackground='#FFA500',
             relief=FLAT,
             font=('futura', 12, 'bold'))
div.grid(row=3, column=4)

# four line
zero = Button(root,
              text='0',
              padx=91,
              pady=20,
              command=lambda: click_button(0),
              fg='#FFFFFF',
              activeforeground='#FFFFFF',
              bg='#708090',
              activebackground='#708090',
              relief=FLAT,
              font=('futura', 12, 'bold'))
zero.grid(row=4, column=1, columnspan=2)

clean = Button(root,
               text='C',
               padx=39,
               pady=20,
               command=lambda: clean_button,
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#708090',
               activebackground='#708090',
               relief=FLAT,
               font=('futura', 12, 'bold'))
clean.grid(row=4, column=3)

total = Button(root,
               text='=',
               padx=44.5,
               pady=20,
               command=lambda: total_button,
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#FFA500',
               activebackground='#FFA500',
               relief=FLAT,
               font=('futura', 12, 'bold'))
total.grid(row=4, column=4)

root.mainloop()
