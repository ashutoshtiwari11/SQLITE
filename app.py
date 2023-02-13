# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:29:27 2023

@author: marshal
"""

import sqlapp

print(""" THIS IS THE LIST OF FUNCTION AVAILABLE YOU CAN ENTER THE FUNCTION YOU WANNA PERFORM - just use the code
      DELETE one object - 0
      ADD one object -  1
      ADD many object -2
      search database using name - 5
      SHOW all- 11
      """)
inp=input("PLEASE ENTER THE DESIRED FUNCTIONALITY CODE. \n:")
inp=int(inp)
if(inp == 1):
    sqlapp.add_one()
elif (inp == 0):
    sqlapp.delete_one()
elif(inp == 2):
    list=input("PLEASE ENTER LIST")
    sqlapp.add_many(list)
elif(inp == 5):
    sqlapp.email_lookup()
elif(inp == 11):
    sqlapp.show_all()
else:
    print("INVALID QUERRY.")