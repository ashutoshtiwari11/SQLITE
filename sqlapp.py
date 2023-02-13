# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:39:37 2023

@author: marshal
"""

import sqlite3



def show_all():
   
    conn = sqlite3.connect('cusomer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    items= c.fetchall()
    for item in items:
        print(item)
    conn.close()
        
def add_one():
    
    first=input("ENTER NAME: ")
    last=input("ENTER Last Name: ")
    email=input("ENTER Email: ")
    conn = sqlite3.connect('cusomer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)",(first, last, email ))
    conn.commit()
    conn.close()
        
def delete_one():
    show_all()
    id=input('Enter row id to be deleted: \n--')
    conn = sqlite3.connect('cusomer.db')
    c=conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()
 
def add_many(list):
    
    conn = sqlite3.connect('cusomer.db')
    c=conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?, ?, ?)", (list))
    c.execute("SELECT * from customers")
    print(c.fetchall())
    conn.commit()
    conn.close()
    
def email_lookup():
    
    conn = sqlite3.connect('cusomer.db')
    c=conn.cursor()
    name=input("ENTER NAME TO BE SEARCHED:  ")
    c.execute("SELECT * from customers WHERE firstname = (?)",(name,))
    #WE INSERTED TUPLE OTHERWISE EVERY LETER WILL BE CONSIDERED A SEPERATE entry --(name, )
    item=c.fetchall()
    
    print(item)
    conn.commit()
    conn.close()
    
    
    
    
    
    
    
    