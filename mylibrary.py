import numpy as np
import cv2 as cv
import math

class ChessBoard:
    def __init__(self,img):
        self.image=img


    #dictionart of chessboard blocks
    #{blockname:(x-axis,y-axis,corner-number,colourtype)
    #colour type:0=white,1=black
    #axises:-1=negative direction,1=positive direction from particular corner
    board_dict={
    'a8':(-1,-1,0,0),'b8':(-1,-1,1,1),'c8':(-1,-1,2,0),'d8':(-1,-1,3,1),'e9':(-1,-1,4,0),'f8':(-1,-1,5,1),'g8':(-1,-1,6,0),'h8':(1,-1,6,1),
    'a7':(-1,-1,7,1),'b7':(-1,-1,8,0),'c7':(-1,-1,9,1),'d7':(-1,-1,10,0),'e7':(-1,-1,11,1),'f7':(-1,-1,12,0),'g7':(-1,-1,13,1),'h7':(1,-1,13,0),
    'a6':(-1,-1,14,0),'b6':(-1,-1,15,1),'c6':(-1,-1,16,0),'d6':(-1,-1,17,1),'e6':(-1,-1,18,0),'f6':(-1,-1,19,1),'g6':(-1,-1,20,0),'h6':(1,-1,20,1),
    'a5':(-1,-1,21,1),'b5':(-1,-1,22,0),'c5':(-1,-1,23,1),'d5':(-1,-1,24,0),'e5':(-1,-1,25,1),'f5':(-1,-1,26,0),'g5':(-1,-1,27,1),'h5':(1,-1,27,0),
    'a4':(-1,-1,28,0),'b4':(-1,-1,29,1),'c4':(-1,-1,30,0),'d4':(-1,-1,31,1),'e4':(-1,-1,32,0),'f4':(-1,-1,33,1),'g4':(-1,-1,34,0),'h4':(1,-1,34,1),
    'a3':(-1,-1,35,1),'b3':(-1,-1,36,0),'c3':(-1,-1,37,1),'d3':(-1,-1,38,0),'e3':(-1,-1,39,1),'f3':(-1,-1,40,0),'g3':(-1,-1,41,1),'h3':(1,-1,41,0),
    'a2':(-1,-1,42,0),'b2':(-1,-1,43,1),'c2':(-1,-1,44,0),'d2':(-1,-1,45,1),'e2':(-1,-1,46,0),'f2':(-1,-1,47,1),'g2':(-1,-1,48,0),'h2':(1,-1,48,1),
    'a1':(-1,1,42,1),'b1':(-1,1,43,0),'c1':(-1,1,44,1),'d1':(-1,1,45,0),'e1':(-1,1,46,1),'f1':(-1,1,47,0),'g1':(-1,1,48,1),'h1':(1,1,48,0)

    }

            
    def changesize(self,s):
        ''' 
            s:size of the image that needed
            function to resize the image accoring to the given size 
        '''
        #function to resize the image
        self.image=cv.resize(self.image, (s,s))




    def drawcir(self,location,s):
        ''' 
            location:position of the block which has to be marked
            s:size of board
            function to draw the circle at the particular block.
        '''
        
        if location not in self.board_dict:
            print("invalid location")
            exit()

        t=self.board_dict[location]
        #tuple unpacking
        x,y,cor_num,color=t

        #calculate the half of the single block side i.e radius for the circle
        radius=math.floor((s/8)/2)

        #to decide which colour circle has to be drawn
        #"1" means the colour of block is 'black' so we fix colour of circle to 'white' and "0" means 'white' so we fix colour of circle to 'black'.
        if color==1:
            rgb=[255,255,255]  #white colour
        else:
            rgb=[0,0,0]         #black colour

        #converting to grayscale
        gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)

        #to find the corners on the chess board
        corners_new = cv.findChessboardCorners(gray, (7,7))
        a1,b1=corners_new[1][cor_num][0]


        #to draw the circle in the desired location on the board
        cv.circle(self.image, (int(a1)+(x*radius),int(b1)+(y*radius)), radius, rgb,-1)




    def show_board(self):
        '''function to show the board'''

        #to show the final window with the circle drawn
        cv.imshow('final', self.image)
        if cv.waitKey(0) & 0xff == 27:
            cv.destroyAllWindows()





#to read the image in the program
img = cv.imread('input_image.png')

#object of ChessBoard class
ob1=ChessBoard(img)

s=int(input("enter the size of the board : "))
location=input("enter the location : ")


#calling changesize function
ob1.changesize(s)

#calling drawcir function
ob1.drawcir(location,s)

#calling show_board function
ob1.show_board()





