#Andrew Parker
#Dec.15,2017
#Game of Life by John Conway

from ggame import *

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
blackOutline = LineStyle(1,black)

whiteSquare = RectangleAsset(30,30,blackOutline,white) 
blackSquare = RectangleAsset(30,30,blackOutline,black)

#buildBoard
def buildBoard():
    return [['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,]
     
def reDrawAll():
    for row in range(0,10):
        for col in range(0,10):
            if data['Board'][row][col] == '0':
                Sprite(whiteSquare,(30*row,30*col))
            if data['Board'][row][col] == 1:
                Sprite(blackSquare,(30*row,30*col))
    
    
def mouseClick(event):
    if event.x > 0 and event.x < 30 and event.y > 0 and event.y < 30:
        Sprite(blackSquare,(0,0))
 

#sprite(board[row][col],' ',end = '') #end is keyword



if __name__ == '__main__':
    
    data = {}
    data['Board'] = buildBoard()
#data['frames'] = 0
    
    reDrawAll()


    App().run()
    App().listenMouseEvent('click',mouseClick)