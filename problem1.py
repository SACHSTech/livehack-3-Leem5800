"""
***************************************************
Filename: LiveHack #3 problem1.py
Description: Determine which group a player is in
Author: Lee. M
Date: 03/03/2021
***************************************************
"""
# define variables
****** Tournament Tracker ******
Group_1_wins = int(input("Enter a number"))
for i in range (5,6):
  if i == 5:
    print ("W")
    print ("W")
    print ("W")
    print ("L")
    print ("W")
    print ("W")
    print ("Your team is in Group 1")
  else:
    print ("W")
    print ("W")
    print ("W")
    print ("W")
    print ("W")
    print ("W")
    print ("Your team is in Group 1")
    
Group_2_wins = int(input("Enter a number"))
  for i in range (3,4):
if i == 3:
  print ("W")
  print ("L")
  print ("W")
  print ("L")
  print ("L")
  print ("W")
  print ("Your team is in Group 2")
else:
  print ("W")
  print ("W")
  print ("L")
  print ("L")
  print ("W")
  print ("W")
  print ("Your team is in Group 2")

Group_3_wins = int(input("Enter a number"))
   for i in range (1,2):
if i == 1:
  print ("L")
  print ("L")
  print ("W")
  print ("L")
  print ("L")
  print ("L")
  print ("Your team is in Group 1")
else:
  print ("W")
  print ("L")
  print ("L")
  print ("L")
  print ("W")
  print ("L")
  print ("Your team is in Group 1")

Eliminated_group = int(input("Enter a number"))
  for i in range (0):
    if i == 0:
    print ("L")
    print ("L")
    print ("L")
    print ("L")
    print ("L")
    print ("L")
    print ("Your team is eliminated from the tournament")