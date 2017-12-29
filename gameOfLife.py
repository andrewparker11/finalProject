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
    return [['0']*20,['0']*20,['0']*20,['0']*20,['0']*20,['0']*20,['0']*20,['0']*20,['0']*20,['0']*20,]
     
def reDrawAll():
    for row in range(0,10):
        for col in range(0,10):
            if data['Board'][row][col] == '0':
                Sprite(whiteSquare,(30*row,30*col))
            if data['Board'][row][col] == 1:
                Sprite(blackSquare,(30*row,30*col))
    
    
def mouseClick():
    if event.x > 0 and event.x < 30 and event.y > 0 and event.y < 30:
        Sprite(blackSquare,(0,0))
    elif event.x > 0 and event.x < 30 and event.y > 30 and event.y < 60:
        Sprite(blackSquare,(0,30))
    elif event.x > 0 and event.x < 30 and event.y > 60 and event.y < 90:
        Sprite(blackSquare,(0,60))
    elif event.x > 0 and event.x < 30 and event.y > 90 and event.y < 120:
        Sprite(blackSquare,(0,90))
    elif event.x > 0 and event.x < 30 and event.y > 120 and event.y < 150:
        Sprite(blackSquare,(0,120))
    elif event.x > 0 and event.x < 30 and event.y > 150 and event.y < 180:
        Sprite(blackSquare,(0,150))
    elif event.x > 0 and event.x < 30 and event.y > 180 and event.y < 210:
        Sprite(blackSquare,(0,180))
    elif event.x > 0 and event.x < 30 and event.y > 210 and event.y < 240:
        Sprite(blackSquare,(0,210))

#sprite(board[row][col],' ',end = '') #end is keyword



if __name__ == '__main__':
    
    data = {}
    data['Board'] = buildBoard()
    data['frames'] = 0
    
    reDrawAll()


    App().run()
    App().listenMouseEvent('click',mouseClick)