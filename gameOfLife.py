#Andrew Parker
#Dec.15,2017
#Game of Life by John Conway

from ggame import *

#buildBoard
def buildBoard():
    board = [['a','b','c'],['d','e','f'],['g','h','i']]
     
def reDrawAll():
    for row in range(0,3):
        for col in range(0,3):
            sprite(board[row][col],' ',end = '') #end is keyword
        sprite()