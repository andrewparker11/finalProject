#Andrew Parker
#Dec.15,2017
#Game of Life by John Conway

#Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by overpopulation.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


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
            if data['Board'][row][col] == 1:
                Sprite(blackSquare,(50*row,50*col))
    
    
def mouseClick(event):
    rx = event.x//50 
    ry = event.y//50
    data['Board'][rx][ry] = 1
    reDrawAll()

"""

def numNeighbors():
n = 0
    for data['Board'][row][col] == '1' or data['Board'][row][col] == '0':
        if data['Board'][row+50][col] == '1':
            n = n+1
        elif data['Board'][row-50][col] == '1':
            n = n+1
        elif data['Board'][row][col+50] == '1':
            n = n+1
        elif data['Board'][row][col-50] == '1':
            n = n+1
        elif data['Board'][row+50][col-50] == '1':
            n = n+1
        elif data['Board'][row-50][col-50] == '1':
            n = n+1
        elif data['Board'][row+50][col+50] == '1':
            n = n+1
        elif data['Board'][row-50][col+50] == '1':
            n = n+1
            
    
def nextGeneration():
    for n in data['Board'][row][col] == '1':
        if n < 2: 
            data['Board'][row][col] == '0'
        #if n == 2: lives do I even need it 
        if n == 3: 
            data['Board'][row][col] == '0'
    for n in data['Board'][row][col] == '0':
        if n == 3:
            data['Board'][row][col] == '1'
"""
#sprite(board[row][col],' ',end = '') #end is keyword



if __name__ == '__main__':
    
    data = {}
    data['Board'] = buildBoard()
    data['frames'] = 0
    
    reDrawAll()

    App().run()
    App().listenMouseEvent('click',mouseClick)