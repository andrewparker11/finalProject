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
    return [['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,]
     
def reDrawAll():
    for row in range(0,10):
        for col in range(0,10):
            if data['Board'][row][col] == '0':
                Sprite(whiteSquare,(50*row,50*col))
            if data['Board'][row][col] == '1':
                Sprite(blackSquare,(50*row,50*col))
    
    
def mouseClick(event):
    rx = event.x//50 
    ry = event.y//50
    data['Board'][rx][ry] = '1'

def numNeighbors():
    
    
def nextGeneration():



#sprite(board[row][col],' ',end = '') #end is keyword



if __name__ == '__main__':
    
    data = {}
    data['Board'] = buildBoard()
    data['frames'] = 0
    
    reDrawAll()
    numNeighbors()

    App().run()
    App().listenMouseEvent('click',mouseClick)