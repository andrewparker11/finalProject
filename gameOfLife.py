#Andrew Parker
#Dec.15,2017
#Game of Life by John Conway

from ggame import *

#buildBoard
def buildBoard():
    board = [['0','0','0','0','0','0','0','0','0','0']['0','0','0','0','0','0','0','0','0','0']['0','0','0','0','0','0','0','0','0','0']['0','0','0','0','0','0','0','0','0','0']['0','0','0','0','0','0','0','0','0','0']['0','0','0','0','0','0','0','0','0','0']['0','0','0','0','0','0','0','0','0','0']['0','0','0','0','0','0','0','0','0','0']['0','0','0','0','0','0','0','0','0','0']['0','0','0','0','0','0','0','0','0','0']['0','0','0','0','0','0','0','0','0','0']]
     
def reDrawAll():
    for row in range(0,3):
        for col in range(0,3):
            sprite(board[row][col],' ',end = '') #end is keyword




if __name__ == '__main__':
    
    data = {}
    data['buildBoard'] = 0
    data['frames'] = 0


App().run()