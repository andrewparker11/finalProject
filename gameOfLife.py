#Andrew Parker
#Dec.15,2017
#Game of Life by John Conway

#Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by overpopulation.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


from ggame import *

#colors 
white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
blackOutline = LineStyle(1,black)

#polygons, text
whiteSquare = RectangleAsset(50,50,blackOutline,white) 
blackSquare = RectangleAsset(50,50,blackOutline,black)
textBox =  RectangleAsset(100,50,blackOutline,white) 
startText = TextAsset('start',fill=black,style='bold 20pt Times')

#Builds the Matrix for the Game
def buildBoard():
    return [['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,]
     

#redraws the Board when next generation occurs and sprites the live or dead cells, also sprites start box
def reDrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,10):
        for col in range(0,10):
            if data['Board'][row][col] == '0':
                Sprite(whiteSquare,(50*row,50*col))
            if data['Board'][row][col] == '1':
                Sprite(blackSquare,(50*row,50*col))
            
    Sprite(textBox,(550,400))
    Sprite(startText,(575,405))


#Listens for mouseclick and sprites box where appropriate 
def mouseClick(event):
    if event.x > 550 and event.x < 650:
        if event.y > 400 and event.y < 450:
            nextGeneration()
    else:
        rx = event.x//50 
        ry = event.y//50
        data['Board'][rx][ry] = '1'
        reDrawAll()
    
#counts the number of neighbors for living or dead clels
def numNeighbors(row,col):
    n = 0
    
    if row<9 and data['Board'][row+1][col] == '1':
        n = n+1
    if row>0 and data['Board'][row-1][col] == '1':
        n = n+1
    if col<9 and data['Board'][row][col+1] == '1':
        n = n+1
    if col>0 and data['Board'][row][col-1] == '1':
        n = n+1
    if row>0 and col>0 and data['Board'][row-1][col-1] == '1':
        n = n+1
    if row<9 and col<9 and data['Board'][row+1][col+1] == '1':
        n = n+1
    if row<9 and col>0 and data['Board'][row+1][col-1] == '1':
        n = n+1
    if row>0 and col<9 and data['Board'][row-1][col+1] == '1':
        n = n+1
    return n
    

#lays out the rules for the next generation
def nextGeneration():
    data['Board2'] = buildBoard()
                
    for row in range(0,10):
        for col in range(0,10): 
            n = numNeighbors(row,col)
            if data['Board'][row][col] == '1':
                if n < 2: 
                    data['Board2'][row][col] = '0'
                if n == 2:
                    data['Board2'][row][col] = '1'
                if n == 3: 
                    data['Board2'][row][col] = '1'
                if n > 3:
                    data['Board2'][row][col] = '0'
            if data['Board'][row][col] == '0':
                if n == 3:
                    data['Board2'][row][col] = '1'
            
    data['Board'] = data['Board2']
                
    reDrawAll()

#runs the game
if __name__ == '__main__':
    
    data = {}
    data['Board'] = buildBoard()
    data['Board2'] = buildBoard()

    reDrawAll()

    App().run()
    App().listenMouseEvent('click',mouseClick)