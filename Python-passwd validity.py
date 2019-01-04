# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 20:02:03 2019

@author: SHASHWAT PANDEY
"""

import re
password="backstreet boys"
t=0
while true:
    if (len(password)<8): 
        flag = -1
        break
    elif not re.search("[a-z]", password): 
        flag = -1
        break
    elif not re.search("[A-Z]", password): 
        flag = -1
        break
    elif not re.search("[0-9]", password): 
        flag = -1
        break
    elif not re.search("[_@$]", password): 
        flag = -1
        break
    elif re.search("\s", password): 
        flag = -1
        break
    else: 
        flag = 0
        print("Valid Password") 
        break
  
if flag ==-1: 
    print("Not a Valid Password")