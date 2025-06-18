import tkinter as tk

root=tk.Tk()
root.geometry("1280x700")
root.title("Chess")

Header=tk.Frame(root,bg='gray',height=25)
Header.pack(fill='x')
Header2=tk.Frame(root,bg='gray',height=25)
Header2.pack(side='bottom',fill='x')

board=tk.Canvas(root,width=600,height=650)
board.pack(pady=0, padx=0, expand=True)



#extract pieces 
n=int(596/8)
img=tk.PhotoImage(file="white-pawn.png")
whitePawn = img.subsample(2, 2)
img=tk.PhotoImage(file="white-rook.png")
whiteRook=img.subsample(2,2)
img=tk.PhotoImage(file="white-knight.png")
whiteKnight=img.subsample(2,2)
img=tk.PhotoImage(file="white-bishop.png")
whiteBishop=img.subsample(2,2)
img=tk.PhotoImage(file="white-queen.png")
whiteQueeni=img.subsample(2,2)
img=tk.PhotoImage(file="white-king.png")
whiteKingi=img.subsample(2,2)

img=tk.PhotoImage(file="black-pawn.png")
blackPawn = img.subsample(2, 2)
img=tk.PhotoImage(file="black-rook.png")
blackRook=img.subsample(2,2)
img=tk.PhotoImage(file="black-knight.png")
blackKnight=img.subsample(2,2)
img=tk.PhotoImage(file="black-bishop.png")
blackBishop=img.subsample(2,2)
img=tk.PhotoImage(file="black-queen.png")
blackQueeni=img.subsample(2,2)
img=tk.PhotoImage(file="black-king.png")
blackKingi=img.subsample(2,2)
boardPositions=[[0 for j in range(8)] for i in range(8)]
rectangles=[[0 for j in range(8)] for i in range(8)]


#creating board
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            colour='darkgrey'
            colour2='snow'
        else:
            colour='snow'
            colour2='darkgrey'

        x1=j*n
        y1=i*n
        x2 =x1 + n
        y2 =y1 + n
        blockNum=chr(j+97)+str(i+1)
        rectangles[i][j]=board.create_rectangle(x1,y1,x2,y2,fill=colour)
        board.create_text(x2-8, y2-8, text=blockNum, font=("Arial", int(n/8)),fill='black')
        boardPositions[i][j]={'x':int((x1+x2)/2),'y':int( (y1+y2)/2)}

#placing pieces
piecePosition={}
whitePawnlist=[]
blackPawnlist=[]
for j in range(8):
            if j==0:
                    whiteRook1=board.create_image(boardPositions[0][j]['x'],boardPositions[0][j]['y'], image=whiteRook)
                    piecePosition['whiteRook1']=[0,j]
            if j==7:
                    whiteRook2=board.create_image(boardPositions[0][j]['x'],boardPositions[0][j]['y'], image=whiteRook)
                    piecePosition['whiteRook2']=[0,j]
            if j==1:
                    whiteKnight1=board.create_image(boardPositions[0][j]['x'],boardPositions[0][j]['y'], image=whiteKnight)
                    piecePosition['whiteKnight1']=[0,j]
            if j==6:
                    whiteKnight2=board.create_image(boardPositions[0][j]['x'],boardPositions[0][j]['y'], image=whiteKnight)
                    piecePosition['whiteKnight2']=[0,j]
            if j==2:
                    whiteBishop1=board.create_image(boardPositions[0][j]['x'],boardPositions[0][j]['y'], image=whiteBishop)
                    piecePosition['whiteBishop1']=[0,j]
            if j==5:
                    whiteBishop1=board.create_image(boardPositions[0][j]['x'],boardPositions[0][j]['y'], image=whiteBishop)
                    piecePosition['whiteBishop2']=[0,j]
            if j==3:
                    whiteQueen=board.create_image(boardPositions[0][j]['x'],boardPositions[0][j]['y'], image=whiteQueeni)
                    piecePosition['whiteQueen']=[0,j]
            if j==4:
                    whiteKing=board.create_image(boardPositions[0][j]['x'],boardPositions[0][j]['y'], image=whiteKingi)
                    piecePosition['whiteKing']=[0,j]
            whitePawnlist.append(board.create_image(boardPositions[1][j]['x'],boardPositions[1][j]['y'], image=whitePawn))
            
for j in range(8):
            if j==0:
                    blackRook6=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackRook)
                    piecePosition['blackRook6']=[7,j]
            if j==7:
                    blackRook2=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackRook)
                    piecePosition['blackRook2']=[7,j]
            if j==1:
                    blackKnight61=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackKnight)
                    piecePosition['blackKnight6']=[7,j]
            if j==6:
                    blackKnight2=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackKnight)
                    piecePosition['blackKnight2']=[7,j]
            if j==2:
                    blackBishop1=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackBishop)
                    piecePosition['blackBishop6']=[7,j]
            if j==5:
                    blackBishop6=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackBishop)
                    piecePosition['blackBishop2']=[7,j]
            if j==3:
                    blackQueen=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackQueeni)
                    piecePosition['blackQueen']=[7,j]
            if j==4:
                    blackKing=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackKingi)
                    piecePosition['blackKing']=[7,j]
            blackPawnlist.append(board.create_image(boardPositions[6][j]['x'],boardPositions[6][j]['y'], image=blackPawn))


whitePawns=tuple(whitePawnlist)
blackPawns=tuple(blackPawnlist)
for j in range(8):
        piecePosition[whitePawns]=[1,j]
        piecePosition[blackPawns]=[6,j]


#outlining board
all_pieces = [whiteRook1, whiteRook2, whiteKnight1, whiteKnight2, whiteBishop1, 
              whiteQueen, whiteKing, blackRook6, blackRook2, blackKnight61, 
              blackKnight2, blackBishop1, blackBishop6, blackQueen, blackKing]

all_pieces.extend(whitePawnlist)
all_pieces.extend(blackPawnlist)

for piece in all_pieces:
    x,y=board.coords(piece)
    j = int(x/n)
    i=int(y/n)
    print(i,j)

    board.tag_bind(piece, '<Enter>', lambda event,rect=rectangles[i][j]: on_Enter_rect(event,rect))
    board.tag_bind(piece, '<Leave>', lambda event,rect=rectangles[i][j]: on_Leave_rect(event,rect))

def on_Enter_rect(event,rect):
        board.itemconfig(rect, outline='red',width=3)
def on_Leave_rect(event,rect):
        board.itemconfig(rect, outline='black',width=1)


for i in range(8):
        for j in range(8):
                board.tag_bind(rectangles[i][j],'<Enter>',lambda event,rect=rectangles[i][j]: on_Enter_rect(event,rect))
                board.tag_bind(rectangles[i][j],'<Leave>',lambda event,rect=rectangles[i][j]: on_Leave_rect(event,rect))

root.mainloop()