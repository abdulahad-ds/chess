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
                    whiteBishop2=board.create_image(boardPositions[0][j]['x'],boardPositions[0][j]['y'], image=whiteBishop)
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
                    blackRook1=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackRook)
                    piecePosition['blackRook6']=[7,j]
            if j==7:
                    blackRook2=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackRook)
                    piecePosition['blackRook2']=[7,j]
            if j==1:
                    blackKnight1=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackKnight)
                    piecePosition['blackKnight6']=[7,j]
            if j==6:
                    blackKnight2=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackKnight)
                    piecePosition['blackKnight2']=[7,j]
            if j==2:
                    blackBishop1=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackBishop)
                    piecePosition['blackBishop6']=[7,j]
            if j==5:
                    blackBishop2=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackBishop)
                    piecePosition['blackBishop2']=[7,j]
            if j==3:
                    blackQueen=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackQueeni)
                    piecePosition['blackQueen']=[7,j]
            if j==4:
                    blackKing=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackKingi)
                    piecePosition['blackKing']=[7,j]
            blackPawnlist.append(board.create_image(boardPositions[6][j]['x'],boardPositions[6][j]['y'], image=blackPawn))


for i in range(8):
        piecePosition[f'whitePawn{i+1}'] = [1,i]
        piecePosition[f'blackPawn{i+1}'] = [6,i]



white_pieces={
        'whiteRook1': whiteRook1,
        'whiteRook2': whiteRook2,
        'whiteKnight1': whiteKnight1,
        'whiteKnight2': whiteKnight2,
        'whiteBishop1': whiteBishop1,
        'whiteBishop2': whiteBishop2,
        'whiteQueen': whiteQueen,
        'whiteKing': whiteKing
}
for i in range(8):
        white_pieces[f'whitePawn{i+1}'] = whitePawnlist[i]

black_pieces={
        'blackRook1': blackRook1,
        'blackRook2': blackRook2,
        'blackKnight1': blackKnight1,
        'blackKnight2': blackKnight2,
        'blackBishop1': blackBishop1,
        'blackBishop2': blackBishop2,
        'blackQueen': blackQueen,
        'blackKing': blackKing
}
for i in range(8):
        black_pieces[f'blackPawn{i+1}'] = blackPawnlist[i]

all_pieces = white_pieces.copy()
all_pieces.update(black_pieces)



#outlining board
for piece in all_pieces.values():
    x,y=board.coords(piece)
    j = int(x/n)
    i=int(y/n)

    board.tag_bind(piece, '<Enter>', lambda event,rect=rectangles[i][j]: on_Enter_rect(event,rect))
    board.tag_bind(piece, '<Leave>', lambda event,rect=rectangles[i][j]: on_Leave_rect(event,rect))

def on_Enter_rect(event,rect):
        board.itemconfig(rect, outline='black',width=6)
def on_Leave_rect(event,rect):
        board.itemconfig(rect, outline='black',width=1)

def outline():
        for i in range(8):
                for j in range(8):
                        board.tag_bind(rectangles[i][j],'<Enter>',lambda event,rect=rectangles[i][j]: on_Enter_rect(event,rect))
                        board.tag_bind(rectangles[i][j],'<Leave>',lambda event,rect=rectangles[i][j]: on_Leave_rect(event,rect))
def back():
      if len(clicked)>0:  
        for rects in clicked[-1]:
                board.itemconfig(rects,width=0)
                board.tag_bind(rects,'<Enter>',lambda event,rect=rects: on_Enter_rect(event,rect))
                board.tag_bind(rects,'<Leave>',lambda event,rect=rects: on_Leave_rect(event,rect))
                board.tag_unbind(rects,'<Button-1>')


def promotion (piece):
        pass

def pawn_moves(piece):
        empty=True
        move=[]
        x,y=piecePosition[piece]
        move_position=[]
        if piece in white_pieces:
                if x<7:
                        move_position=[x+1,y]
                        for key,value in piecePosition.items():
                                if move_position == value:
                                        empty=False 
                                        break
                        if (empty):
                                move.append(move_position)
                        Empty=True
                if x==1:
                        move_position=[x+2,y]
                        for key,value in piecePosition.items():
                                if move_position == value:
                                        empty=False 
                                        break
                if (empty):
                        move.append(move_position)
                if x<7 and y<7:
                        move_position = [x+1,y+1]
                        for key,value in piecePosition.items():
                                if move_position == value and key in black_pieces:
                                        move.append(move_position)
                if y>0 and x<7:
                        move_position = [x+1,y-1]
                        for key,value in piecePosition.items():
                                if move_position == value and key in black_pieces:
                                        move.append(move_position)
        elif piece in black_pieces:
                if x>0:
                        move_position=[x-1,y]
                        for key,value in piecePosition.items():
                                if move_position == value:
                                        empty=False 
                                        break
                        if (empty):
                                move.append(move_position)
                        Empty=True
                if x==6:
                        move_position=[x-2,y]
                        for key,value in piecePosition.items():
                                if move_position == value:
                                        empty=False 
                                        break
                if (empty):
                        move.append(move_position)
                if y<7 and x>0:
                        move_position = [x-1,y+1]
                        for key,value in piecePosition.items() and key in white_pieces:
                                if move_position == value:
                                        move.append(move_position)
                if x>0 and y>0:
                        move_position = [x-1,y-1]
                        for key,value in piecePosition.items():
                                if move_position == value and key in white_pieces:
                                        move.append(move_position)
        return move
def rook_moves(piece):
                move=[]
                empty=True
                x,y=piecePosition[piece]
                move_position=[]
                i=1
                while i<=x :
                        move_position=[x-i,y]
                        for key,value in piecePosition.items():
                                        if move_position == value:
                                                empty=False
                                                if piece in white_pieces:
                                                        if key in black_pieces:
                                                                move.append(move_position)
                                                        break
                                                if piece in black_pieces:
                                                        if key in white_pieces:
                                                                move.append(move_position)
                                                        break
                        if empty:
                                move.append(move_position)
                        else:
                                break
                        i+=1
                i=1
                empty=True
                while i<=7-x :
                        move_position=[x+i,y]
                        for key,value in piecePosition.items():
                                        if move_position == value:
                                                empty=False
                                                if piece in white_pieces:
                                                        if key in black_pieces:
                                                                move.append(move_position)
                                                        break
                                                if piece in black_pieces:
                                                        if key in white_pieces:
                                                                move.append(move_position)
                                                        break
                        if empty:
                                move.append(move_position)
                        else:
                                break
                        i+=1
                i=1
                empty=True
                while i<=y :
                        move_position=[x,y-i]
                        for key,value in piecePosition.items():
                                        if move_position == value:
                                                empty=False
                                                if piece in white_pieces:
                                                        if key in black_pieces:
                                                                move.append(move_position)
                                                        break
                                                if piece in black_pieces:
                                                        if key in white_pieces:
                                                                move.append(move_position)
                                                        break
                        if empty:
                                move.append(move_position)
                        else:
                                break
                        i+=1
                i=1
                empty=True
                while i<=7-y:
                        move_position=[x,y+i]
                        for key,value in piecePosition.items():
                                        if move_position == value:
                                                empty=False
                                                if piece in white_pieces:
                                                        if key in black_pieces:
                                                                move.append(move_position)
                                                        break
                                                if piece in black_pieces:
                                                        if key in white_pieces:
                                                                move.append(move_position)
                                                        break
                        if empty:
                                move.append(move_position)
                        else:
                                break
                        i+=1
                return move
def knight_moves(piece):
        empty=True
        move=[]
        x,y=piecePosition[piece]
        move_position=()
        knight_moves = [
        (-2, -1), (-2, +1),
        (-1, -2), (-1, +2),
        (+1, -2), (+1, +2),
        (+2, -1), (+2, +1)]
        for i,j in knight_moves:
                move_position=[x+i,y+j]
                if 0 <= x+i <= 7 and 0<= y+j <=7:
                        empty=True
                        for key,value in piecePosition.items():
                                        if move_position == value:
                                                empty=False
                                                if piece in white_pieces:
                                                        if key in black_pieces:
                                                                move.append(move_position)
                                                        break
                                                elif piece in black_pieces:
                                                        if key in white_pieces:
                                                                move.append(move_position)
                                                        break
                        if empty:
                                move.append(move_position)
        return move
def bishop_moves(piece):
                move=[]
                empty=True
                x,y=piecePosition[piece]
                move_position=[]
                i=1
                while i<=x and i<=y:
                        move_position=[x-i,y-i]
                        for key,value in piecePosition.items():
                                        if move_position == value:
                                                empty=False
                                                if piece in white_pieces:
                                                        if key in black_pieces:
                                                                move.append(move_position)
                                                        break
                                                if piece in black_pieces:
                                                        if key in white_pieces:
                                                                move.append(move_position)
                                                        break
                        if empty:
                                move.append(move_position)
                        else:
                                break
                        i+=1
                i=1
                empty=True
                while i<=7-x and i<=7-y:
                        move_position=[x+i,y+i]
                        for key,value in piecePosition.items():
                                        if move_position == value:
                                                empty=False
                                                if piece in white_pieces:
                                                        if key in black_pieces:
                                                                move.append(move_position)
                                                        break
                                                if piece in black_pieces:
                                                        if key in white_pieces:
                                                                move.append(move_position)
                                                        break
                        if empty:
                                move.append(move_position)
                        else:
                                break
                        i+=1
                i=1
                empty=True
                while i<=x and i<=7-y :
                        move_position=[x-i,y+i]
                        for key,value in piecePosition.items():
                                        if move_position == value:
                                                empty=False
                                                if piece in white_pieces:
                                                        if key in black_pieces:
                                                                move.append(move_position)
                                                        break
                                                if piece in black_pieces:
                                                        if key in white_pieces:
                                                                move.append(move_position)
                                                        break
                        if empty:
                                move.append(move_position)
                        else:
                                break
                        i+=1
                i=1
                empty=True
                while i<=7-x and i<=y:
                        move_position=[x+i,y-i]
                        for key,value in piecePosition.items():
                                        if move_position == value:
                                                empty=False
                                                if piece in white_pieces:
                                                        if key in black_pieces:
                                                                move.append(move_position)
                                                        break
                                                if piece in black_pieces:
                                                        if key in white_pieces:
                                                                move.append(move_position)
                                                        break
                        if empty:
                                move.append(move_position)
                        else:
                                break
                        i+=1
                return move


def get_moves(piece):
        if 'Rook' in piece:
                return rook_moves(piece)
        if 'Knight' in piece:
                return knight_moves(piece)
        if 'Bishop' in piece:
                return bishop_moves(piece)
        if 'Queen' in piece:
                return bishop_moves(piece)+rook_moves(piece)
        if 'King' in piece:
                pass
        if 'Pawn' in piece:
                return pawn_moves(piece)


#gameplay
clicked=[]
def show_moves(piece):
        back()
        moves=get_moves(piece)
        print(moves)
        x,y=piecePosition[piece]
        rects=[]
        current=rectangles[x][y]
        def maintain(event):
                board.itemconfig(current, outline ='blue4', width=6)
        board.tag_bind(current,'<Enter>',maintain)
        board.tag_bind(current,'<Leave>', maintain)
        board.tag_bind(piece,'<Enter>',maintain)
        board.tag_bind(piece,'<Leave>',maintain)
        
        rects.append(current)
        for move in moves:
                i,j=move
                rect=rectangles[i][j]
                rects.append(rect)
                board.itemconfig(rect, outline='royalblue1',width=4)
                board.tag_unbind(rect,'<Enter>')
                board.tag_unbind(rect,'<Leave>')
        clicked.append(rects)

def clicked_Piece(event,piece):
        show_moves(piece)


def whiteturn():
        for piece in white_pieces:
                board.tag_bind(white_pieces[piece], '<Button-1>',lambda event,p=piece: clicked_Piece(event,p))



whiteturn()

root.mainloop()