#Andrew Parker
#Dec.15,2017
#Game of Life by John Conway

from ggame import *

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
blackOutline = LineStyle(1,black)

whiteSquare = RectangleAsset(50,50,blackOutline,white) 
blackSquare = RectangleAsset(50,50,blackOutline,black)

#buildBoard
def buildBoard():
    return [['0']*20,['0']*20,['0']*20,['0']*20,['0']*20,['0']*20,['0']*20,['0']*20,['0']*20,['0']*20,]
     
def reDrawAll():
    for row in range(0,10):
        for col in range(0,10):
            if board[row][col] == 0:
                sprite(whiteSquare)
            if board[row][col] == 1:
                sprite(blackSquare)
                
#sprite(board[row][col],' ',end = '') #end is keyword




if __name__ == '__main__':
    
    data = {}
    data['Board'] = buildBoard()
    data['frames'] = 


App().run()