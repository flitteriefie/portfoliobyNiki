# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:04:37 2020

@author: sznik
"""

#Find Cost of Tile to Cover W x H Floor - Calculate the total cost 
#of tile it would take to cover a floor plan of width and height, 
#using a cost entered by the user.

cost_of_tile = int(input("please enter the cost of the tile: "))
h_tile = int(input("please nter the height of the tile: "))
w_tile = int(input("please enter the width of the tile: "))
w_room = int(input("widht of the room: "))
h_room = int(input("height of room: "))

t_surface = h_tile * w_tile
r_surface = w_room * h_room

if r_surface / t_surface > 0:
    num = r_surface / t_surface
    fin_cost = num * cost_of_tile
    print("it would tale", fin_cost, "to tile the room")