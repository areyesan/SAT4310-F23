# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 13:40:30 2023

@author: abel reyes
"""


#import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

root = tk.Tk()
'''
widgets are added here

'''


'''
Label example

'''
#w = Label(root, text='Michigan Tech!', width=20, height=10, bg = 'gray60', font=("Helvetica", 14))
#w.pack()

'''
Text example

'''

#root.title('Text Widget Demo')
#T = Text(root, height=20, width=50)
#T.pack()



'''
Canvas example

'''

#root.geometry('800x600')
#root.title('Canvas Demo - Rectangle')
#canvas = tk.Canvas(root, width=600, height=400, bg='white')
#canvas.pack(anchor=tk.CENTER, expand=True)
#canvas.create_rectangle((100, 100), (300, 200), fill='blue')

'''
Message example

'''

#root.title('Message Demo')

#messageVar = Message(root, text = 'This is Python course!')
#messageVar.config(bg='yellow')
#messageVar.pack( )

'''
Button example

'''

root.geometry('500x300')
root.title('Button Demo')
button = tk.Button(root, text='Stop', width=55, font = 25, command=root.destroy)
#button.pack()
button.grid(columnspan=2, column=0, row=0)
button2 = tk.Button(root, text='parar', width=55, font = 25, command=root.destroy)
button2.grid(column=4, row=0)



#
#root.geometry('600x600')
#root.resizable(False, False)
#root.title('Image button Demo')
#
#def download_clicked():
#    tk.messagebox.showinfo(title='Information', message='Python button clicked!')
#    
#Python_icon=tk.PhotoImage(file='python.png')
#
#Python_button=ttk.Button(root, image=Python_icon, text='Python', compound=tk.TOP, command=download_clicked)
#
#Python_button.pack(ipadx=15, ipady=15, expand=True)



'''
CheckButton example

'''

#
#root.geometry('300x100')
#root.resizable(False, False)
#root.title('CheckButton Demo')
#
#var1 = tk.IntVar()
#tk.Checkbutton(root, text='male', font = 25, variable=var1).grid(row=0, sticky=W)
#var2 = tk.IntVar()
#tk.Checkbutton(root, text='female', font = 25, variable=var2).grid(row=1, sticky=W)



'''
RadioButton example

'''

#def sel():
#    selection="You selected the option "+var.get()
#    label.config(text=selection)
#
#root.geometry("300x200")
#root.title("Radio Button Demo")
#var=StringVar(value="Default")
#rb1=Radiobutton(root, text="Option 1", variable=var, value='Python', command=sel)
#rb1.pack()
#rb2=Radiobutton(root, text="Option 2", variable=var, value='Java', command=sel)
#rb2.pack()
#rb3=Radiobutton(root, text="Option 3", variable=var, value='C++', command=sel)
#rb3.pack()
#
#label=Label(root)
#label.pack()


'''
Entry example

'''


#root.geometry('300x200')
#root.resizable(False, False)
#root.title('Entry Demo')
#
#Label(root, text='First Name').grid(row=0)
#Label(root, text='Last Name').grid(row=1)
#Label(root, text = 'Address').grid(row=2)
#e1 = Entry(root).grid(row=0, column=1)
#e2 = Entry(root).grid(row=1, column=1)
#e3 = Entry(root).grid(row=2, column=1)


'''
Frame example

'''

#root.geometry("300x150")
#root.title("frame demo")
#
#frame=tk.Frame(root, bg="skyblue3", width=100, height=50)
#frame['borderwidth']=2
#frame['cursor']='circle'
#frame['relief']='sunken'
#frame.pack()
#
#redbutton=tk.Button(frame, text='Red', fg='red')
#redbutton.pack(side= LEFT)
#
#brownbutton=tk.Button(frame, text='Brown', fg='brown')
#brownbutton.pack(side= RIGHT)
#
#bluebutton=tk.Button(frame, text='Blue', fg='blue')
#bluebutton.pack(side= TOP)
#
#blackbutton=tk.Button(frame, text='Black', fg='black')
#blackbutton.pack(side= BOTTOM)


'''
Menu example

'''

#root.title('Menu Demo')
#
#menu = Menu(root)
#root.config(menu=menu)
#
## the first menu
#filemenu = Menu(menu)
#menu.add_cascade(label='File', menu=filemenu)
#filemenu.add_command(label='New')
#filemenu.add_separator()
#filemenu.add_command(label='Exit', command=root.destroy)
#
## the second menu
#helpmenu = Menu(menu)
#menu.add_cascade(label='Help', menu=helpmenu)
#helpmenu.add_command(label='About')

'''
Scale example

'''

#master = Tk()
#w = Scale(master, from_=0, to=50).pack()
#w = Scale(master, from_=0, to=200, orient=HORIZONTAL).pack()



root.mainloop()
