# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 23:44:42 2023

@author: abel reyes
"""

#Import libraries

import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3

##enter function
def enter_data():
    accept=term_var.get()
    if accept=="Accepted":
        title=game_entry.get()
        year=year_entry.get()
        city=city_entry.get()
        console=console_cb.get()
        
        
        # Create Table
        conn = sqlite3.connect('data.db')
        table_create_query = '''CREATE TABLE IF NOT EXISTS gta 
                (release_title TEXT, release_year TEXT, city TEXT, console text, registration text)
        '''
        conn.execute(table_create_query)
        cursor = conn.cursor()
        
        
        # Insert Data
        data_insert_query = '''INSERT INTO gta VALUES 
        (?, ?, ?, ?, ?)'''
        data_insert_tuple = (title, year, city,
                              console, accept)       
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        conn.close()
    
        
    else:
        
        tk.messagebox.showwarning(title="Error",
                                  message="You have not accepted the terms and conditions")

    

    


##clear function
def clear_data():
    game_entry.delete(0, END)
    year_entry.delete(0, END)
    city_entry.delete(0, END)
    console_cb.set('')
    terms_cbutton.deselect()


##Create the window
window=tk.Tk()
window.geometry("800x600")
window.title("Class Example")
window.resizable(False, False)

##Define main frame

main_frame=tk.Frame(window)
main_frame.pack()



## Defining game frame --  tk.LabelFrame  -- tk.Label  -- tk.Entry  -- ttk.Combobox
game_frame=tk.LabelFrame(main_frame, text="Game Information")
game_frame.grid(row=0, column=0)

## Defining widgets within info frame
title_label=tk.Label(game_frame, text="Game title")
title_label.grid(row=0, column=0)#, padx=20, pady=10)

year_label=tk.Label(game_frame, text="Release Year")
year_label.grid(row=0, column=1)

city_label=tk.Label(game_frame, text="City")
city_label.grid(row=0, column=2)


game_entry=tk.Entry(game_frame)
game_entry.grid(row=1, column=0)



year_entry=tk.Entry(game_frame)
year_entry.grid(row=1, column=1)


city_entry=tk.Entry(game_frame)
city_entry.grid(row=1, column=2)

console_label=tk.Label(game_frame, text="Console")
console_label.grid(row=2, column=0)

console_cb=ttk.Combobox(game_frame, values=["Switch", "PS5", "Xbox", "PC"])
console_cb.grid(row=3, column=0)


##Padding with loop
for widget in game_frame.winfo_children():
    widget.grid_configure(padx=20, pady=10)




## Defining terms frame --  tk.LabelFrame  
term_frame=tk.LabelFrame(main_frame, text="Terms & Conditions")
term_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)


#Defining widgets within terms_frame --  tk.Checkbutton  --  tk.StringVar


term_var=tk.StringVar(value="Not Accepted")
terms_cbutton=tk.Checkbutton(term_frame, text="I accept the terms and conditions",
                             variable=term_var,
                             onvalue="Accepted",
                             offvalue="Not Accepted")

terms_cbutton.grid(row=0, column=0)

#Defining buttons  --  tk.Button
enter_button=tk.Button(main_frame, text="Enter Data", command=enter_data)
enter_button.grid(row=2, column=0, sticky="news", padx=20, pady=10)
clear_button=tk.Button(main_frame, text="Clear Data", command=clear_data)
clear_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


window.mainloop()





