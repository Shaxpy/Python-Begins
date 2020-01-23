# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 20:02:03 2019

@author: SHASHWAT PANDEY
"""
import re 

password = input()
t = 0
while True:
    if not re.search("[a-z]",password):
        t=1     
        break
    elif not re.search("[0-9]",password):
        t=1     
        break
    elif not re.search("[A-Z]",password):
        t=1     
        break
    elif not re.search("[$#@]",password):
        t=1     
        break
    elif not (len(password)<6):
        t=1     
        break
    elif not (len(password)>12):
        t=1     
        break
    else:
        t=0
        print("Valid Password")
if t==1:
    print("Invalid Password")
        
