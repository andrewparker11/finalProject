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
    x = 0 
    y = 0
    n = 0 
    for row in range(0,10):
        for col in range(0,10):
            if data['Board'][row][col] == '0':
                Sprite(whiteSquare,(30*row+100,30*col+64))
            if data['Board'][row][col] == 1:
                Sprite(blackSquare,(30*row+100,30*col+64))
        x = x + 1
        y = y + 1
        n = n + 1


#sprite(board[row][col],' ',end = '') #end is keyword




if __name__ == '__main__':
    
    
    data = {}
    data['Board'] = buildBoard()
    data['frames'] = 0
    
    reDrawAll()


    App().run()