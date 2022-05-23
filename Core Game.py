import random, copy, sys, pygame
from pygame.locals import *
from random import randint
pygame.init()
pygame.display.set_caption('Primary Diablo 2 Gameplay')
BOARDWIDTH = 10  # how many spaces wide the board is
BOARDHEIGHT = 6 # how many spaces tall the board is
WINDOWWIDTH = 800 # width of the program's window, in pixels
WINDOWHEIGHT = 800 # height in pixels

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

FPS = 60 # frames per second to update the screen
global SPACESIZE
SPACESIZE = 56 # size of the tokens and individual board spaces in pixels
global XMARGIN
XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * SPACESIZE) / 2)
global YMARGIN
YMARGIN = int((WINDOWHEIGHT - BOARDHEIGHT * SPACESIZE) / 2)

XRightSide = WINDOWWIDTH - XMARGIN
YBottomSide = WINDOWHEIGHT - YMARGIN
WHITE = [255, 255, 255]
BGCOLOR = [70,70,70]

listception = []
for x in range(BOARDWIDTH):
        listception.append([])
        for y in range(BOARDHEIGHT):
                listception[x].append([randint(0,0),randint(0,150),randint(200,255)])
                if listception[x]>0 and listception[x-1][y][1] < listception[x][y][1] :
                        if listception[x][y][1] - (listception[x-1][y][1]) > 6:
                                listception[x][y][1] +=6
                                if listception[x][y][1] > 150:
                                        listception[x][y][1] = listception[x][y][1] -150



REDTOKENIMG = pygame.image.load('4row_red.png')
REDTOKENIMG = pygame.transform.smoothscale(REDTOKENIMG, (SPACESIZE, SPACESIZE))
SwordPic = pygame.image.load('Sword.gif').convert_alpha()
SwordPic = pygame.transform.scale2x(SwordPic)
SwordPic = pygame.transform.smoothscale(SwordPic, (SPACESIZE, SPACESIZE* 3))

TopazPic = pygame.image.load('Topaz.gif').convert_alpha()
TopazPic = pygame.transform.scale2x(TopazPic)
TopazPic = pygame.transform.smoothscale(TopazPic, (SPACESIZE, SPACESIZE))

BookPic = pygame.image.load('book.gif').convert_alpha()
BookPic = pygame.transform.scale2x(BookPic)
BookPic = pygame.transform.smoothscale(BookPic, (SPACESIZE, SPACESIZE*2))

ShieldPic = pygame.image.load('stormGuild.gif').convert_alpha()
ShieldPic = pygame.transform.scale2x(ShieldPic)
ShieldPic = pygame.transform.smoothscale(ShieldPic, (SPACESIZE*2, SPACESIZE*3))

SpikedPic = pygame.image.load('SpikedShield.gif').convert_alpha()
SpikedPic = pygame.transform.scale2x(SpikedPic)
SpikedPic = pygame.transform.smoothscale(SpikedPic, (SPACESIZE*2, SPACESIZE*3))

AerinPic = pygame.image.load('AerinShield.gif').convert_alpha()
AerinPic = pygame.transform.scale2x(AerinPic)
AerinPic = pygame.transform.smoothscale(AerinPic, (SPACESIZE*2, SPACESIZE*4))

SabrePic = pygame.image.load('LightSabre.gif').convert_alpha()
SabrePic = pygame.transform.scale2x(SabrePic)
SabrePic = pygame.transform.smoothscale(SabrePic, (SPACESIZE*2, SPACESIZE*3))

RunePic = pygame.image.load('OhmRune.png').convert_alpha()
RunePic = pygame.transform.scale2x(RunePic)
RunePic = pygame.transform.smoothscale(RunePic, (SPACESIZE*1, SPACESIZE*1))

OrbPic = pygame.image.load('Orb.gif').convert_alpha()
OrbPic = pygame.transform.scale2x(OrbPic)
OrbPic = pygame.transform.smoothscale(OrbPic, (SPACESIZE*1, SPACESIZE*3))

SteelPic = pygame.image.load('SteelArmor.gif').convert_alpha()
SteelPic = pygame.transform.scale2x(SteelPic)
SteelPic = pygame.transform.smoothscale(SteelPic, (SPACESIZE*2, SPACESIZE*3))

VictorPic = pygame.image.load('VictorArmor.gif').convert_alpha()
VictorPic = pygame.transform.scale2x(VictorPic)
VictorPic = pygame.transform.smoothscale(VictorPic, (SPACESIZE*2, SPACESIZE*3))

JavelinPic = pygame.image.load('Javelin.gif').convert_alpha()
JavelinPic = pygame.transform.scale2x(JavelinPic)
JavelinPic = pygame.transform.smoothscale(JavelinPic, (SPACESIZE*1, SPACESIZE*4))

s1x1 = [[0,0]]
s1x2 = [[0,0],[0,1]]
s1x3 = [[0,0],[0,1],[0,2]]
s1x4 = [[0,0],[0,1],[0,2],[0,3]]
s2x2 = [[0,0],[0,1],[1,1],[1,0]]
s2x3 = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2]]
s2x4 = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3]]

itemList = [[s1x1,TopazPic],[s1x2,BookPic],[s1x3,SwordPic],[s2x3,ShieldPic],[s2x3,SpikedPic]\
,[s2x4,AerinPic],[s2x3,SabrePic],[s1x1,RunePic],[s1x3,OrbPic],[s2x3,SteelPic],[s2x3,VictorPic],[s1x4,JavelinPic]]

nameList = ['TopazPic','BookPic','SwordPic','ShieldPic','SpikedPic','AerinPic','SabrePic','RunePic','OrbPic','SteelPic','VictorPic','JavelinPic']
picList = [TopazPic,BookPic,SwordPic,ShieldPic,SpikedPic,AerinPic,SabrePic,RunePic,OrbPic,SteelPic,VictorPic,JavelinPic]

global testList
testList = [[2,6],[0,5],[0,2],[0,3]]

objectList = []
boardList   = [[]] * BOARDWIDTH

NewItem = False


for x in range(BOARDWIDTH):
    boardList[x] = [0]* BOARDHEIGHT



class Object():
    def __init__(self):

        global XMARGIN
        global YMARGIN
        global SPACESIZE
        global testList
        self.SpotList = []
        self.Map = []
        self.doOnce = True

    def func(self,xf,yf,XOffset,YOffset,boardList,mapList,Pic,ItemIndex):

        if self.doOnce:
            self.SpotList = copy.copy(boardList)
            #                   |
            #                   | this F'er
            #                   V
            self.Map = copy.copy(mapList)

            self.doOnce = False
        self.Index = ItemIndex
        self.Pic = Pic
        self.column = int((xf - XOffset - (XMARGIN)) / SPACESIZE)
        self.row    = int((yf - YOffset - (YMARGIN)) / SPACESIZE)

        self.posX = (self.column * SPACESIZE) + XMARGIN
        self.posY = (self.row    * SPACESIZE) + YMARGIN







def main():
    CurrentItem = 0
    NewItem = False
    xh = 0
    yh = 0

    while True:

        xp, yp = pygame.mouse.get_pos()



        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                if NewItem == True:
                    NewItem = False
                else:
                    NewItem = True

            if ((xp > XMARGIN) and (xp < (WINDOWWIDTH-XMARGIN))) and ((yp > YMARGIN) and (yp < (WINDOWHEIGHT-YMARGIN))):

                if event.type == MOUSEBUTTONDOWN and (event.button == 4 or event.button == 5):
                    NewItem = True
                    if CurrentItem == len(itemList)-1:
                        CurrentItem = 0
                    else:
                        CurrentItem += 1
                    xh, yh = hoverPlace(CurrentItem)
                    XSelect = ((xh * 2) - SPACESIZE)/2
                    YSelect = ((yh * 2) - SPACESIZE)/2



                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Occupied = False
                    SwitchSpot = True

                    if NewItem:
                        ObjectInSpot = 0
                        currentList = copy.deepcopy(itemList[CurrentItem][0])
                        objectList.append(Object())
                        objectList[-1].func(xp,yp,XSelect,YSelect,copy.deepcopy(itemList[CurrentItem][0]), currentList, itemList[CurrentItem][1],CurrentItem)
                        Obj = objectList[-1]

                        for spot in Obj.SpotList:
                            SpotX = (spot[0] + Obj.column)
                            SpotY = (spot[1] + Obj.row)

                            if (SpotX > -1 and SpotX < BOARDWIDTH) and (SpotY > -1 and SpotY < BOARDHEIGHT):
                                if boardList[SpotX][SpotY] != 0:
                                    if ObjectInSpot == 0:
                                        ObjectInSpot = boardList[SpotX][SpotY]

                                    elif ObjectInSpot != boardList[SpotX][SpotY]:
                                        SwitchSpot = False
                                    else:
                                        Occupied = True
                                        print "NEIN!"
                            else:
                                Occupied = True
                                print "NIEMALS!"


                        if Occupied == False:
                            if SwitchSpot == False:
                                count = 0
                                for spot in Obj.SpotList:
                                    SpotX = (spot[0] + Obj.column)
                                    SpotY = (spot[1] + Obj.row)

                                    boardList[SpotX][SpotY] = Obj

                                    Obj.Map[count][0] = SpotX
                                    Obj.Map[count][1] = SpotY

                                    count += 1
                                    NewItem = False



                        else:
                            del objectList[-1]

                    elif NewItem == False:
                        column = (xp - XMARGIN)/SPACESIZE
                        row    = (yp - YMARGIN)/SPACESIZE

                        if boardList[column][row] != 0:
                            Map = boardList[column][row].Map
                            for spot in Map:

                                ExiledObject = boardList[spot[0]][spot[1]]
                                boardList[spot[0]][spot[1]] = 0

                            ExiledIndex = objectList.index(ExiledObject)
                            NewItem = True
                            CurrentItem = ExiledObject.Index
                            del objectList[ExiledIndex]






                    elif NewItem == True:
                        if Occupied == False:
                            if SwitchSpot == True:

                                column = (xp - XMARGIN) / SPACESIZE
                                row = (yp - YMARGIN) / SPACESIZE

                                if boardList[column][row] != 0:
                                    Map = boardList[column][row].Map
                                    for spot in Map:
                                        ExiledObject = boardList[spot[0]][spot[1]]
                                        boardList[spot[0]][spot[1]] = 0


                                count = 0
                                for spot in Obj.SpotList:
                                    SpotX = (spot[0] + Obj.column)
                                    SpotY = (spot[1] + Obj.row)

                                    boardList[SpotX][SpotY] = Obj

                                    Obj.Map[count][0] = SpotX
                                    Obj.Map[count][1] = SpotY

                                    count += 1






                                    ExiledIndex = objectList.index(ExiledObject)
                                    NewItem = True
                                    CurrentItem = ExiledObject.Index
                                    del objectList[ExiledIndex]









        DISPLAYSURF.fill(BGCOLOR)
        for xb in range(BOARDWIDTH):
            for yb in range(BOARDHEIGHT):
                pygame.draw.rect(DISPLAYSURF, listception[xb][yb],(XMARGIN + (xb * SPACESIZE), YMARGIN + (yb * SPACESIZE), SPACESIZE, SPACESIZE))
        if len(objectList) > 0:
            for obj in objectList:
                DISPLAYSURF.blit(obj.Pic, (obj.posX, obj.posY))

        if NewItem == True:
            DISPLAYSURF.blit(itemList[CurrentItem][1], (xp - xh, yp - yh))

        pygame.display.update()



def hoverPlace(CurrentItem):

    Rect = pygame.Surface.get_rect(itemList[CurrentItem][1])
    xh = Rect[2]
    yh = Rect[3]

    return xh / 2, yh / 2


main()