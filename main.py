
import tkinter as tk

root=tk.Tk()
root.geometry("1280x700")
root.title("Chess")

header=tk.Frame(root, bg='black',height=30)
header.pack(fill='x')

turn_label = tk.Label(header, text="Turn: White", bg='black', fg='white', font=('Arial', 14, 'bold'))
turn_label.pack(side='left', padx=20, pady=10)

game_status_label = tk.Label(header, text="Game Status: Active", bg='black', fg='white', font=('Arial', 14))
game_status_label.pack(side='right', padx=20, pady=10)

leftFrame=tk.Frame(root,bg='gray',width=200,height=650)
leftFrame.pack(side='left',fill='y')
leftFrame.pack_propagate(False)

white_title = tk.Label(leftFrame, text="WHITE PLAYER", bg='lightgray', fg='black', font=('Arial', 16, 'bold'))
white_title.pack(pady=(10, 5))

white_captures_frame = tk.LabelFrame(leftFrame, text="Captured Pieces", bg='lightgray', fg='black', font=('Arial', 12, 'bold'))
white_captures_frame.pack(fill='x', padx=10, pady=5)

white_captures_content = tk.Frame(white_captures_frame, bg='lightgray')
white_captures_content.pack(fill='x', padx=5, pady=5)

white_promotion_frame = tk.LabelFrame(leftFrame, text="Promotion Options", bg='lightgray', fg='black', font=('Arial', 12, 'bold'))
white_promotion_frame.pack(fill='x', padx=10, pady=5)

controls_frame = tk.LabelFrame(leftFrame, text="Game Controls", bg='lightgray', fg='black', font=('Arial', 12, 'bold'))
controls_frame.pack(fill='x', padx=10, pady=5)

rightFrame=tk.Frame(root,bg='gray',width=200,height=650)
rightFrame.pack(side='right',fill='y')
rightFrame.pack_propagate(False)

black_title = tk.Label(rightFrame, text="BLACK PLAYER", bg='darkgray', fg='white', font=('Arial', 16, 'bold'))
black_title.pack(pady=(10, 5))

black_captures_frame = tk.LabelFrame(rightFrame, text="Captured Pieces", bg='darkgray', fg='white', font=('Arial', 12, 'bold'))
black_captures_frame.pack(fill='x', padx=10, pady=5)

black_captures_content = tk.Frame(black_captures_frame, bg='darkgray')
black_captures_content.pack(fill='x', padx=5, pady=5)

black_promotion_frame = tk.LabelFrame(rightFrame, text="Promotion Options", bg='darkgray', fg='white', font=('Arial', 12, 'bold'))
black_promotion_frame.pack(fill='x', padx=10, pady=5)

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
unicode_pieces = {
    'whiteRook1': '♖',
    'whiteRook2': '♖',
    'whiteKnight1': '♘',
    'whiteKnight2': '♘',
    'whiteBishop1': '♗',
    'whiteBishop2': '♗',
    'whiteQueen': '♕',
    'whiteKing': '♔',
    'whitePawn1': '♙',
    'whitePawn2': '♙',
    'whitePawn3': '♙',
    'whitePawn4': '♙',
    'whitePawn5': '♙',
    'whitePawn6': '♙',
    'whitePawn7': '♙',
    'whitePawn8': '♙',

    'blackRook1': '♜',
    'blackRook2': '♜',
    'blackKnight1': '♞',
    'blackKnight2': '♞',
    'blackBishop1': '♝',
    'blackBishop2': '♝',
    'blackQueen': '♛',
    'blackKing': '♚',
    'blackPawn1': '♟',
    'blackPawn2': '♟',
    'blackPawn3': '♟',
    'blackPawn4': '♟',
    'blackPawn5': '♟',
    'blackPawn6': '♟',
    'blackPawn7': '♟',
    'blackPawn8': '♟',
}
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
                    piecePosition['blackRook1']=[7,j]
            if j==7:
                    blackRook2=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackRook)
                    piecePosition['blackRook2']=[7,j]
            if j==1:
                    blackKnight1=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackKnight)
                    piecePosition['blackKnight1']=[7,j]
            if j==6:
                    blackKnight2=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackKnight)
                    piecePosition['blackKnight2']=[7,j]
            if j==2:
                    blackBishop1=board.create_image(boardPositions[7][j]['x'],boardPositions[7][j]['y'], image=blackBishop)
                    piecePosition['blackBishop1']=[7,j]
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
for name,piece in all_pieces.items():
    x,y=piecePosition[name]
    j = y
    i= x

    board.tag_bind(piece, '<Enter>', lambda event,rect=rectangles[i][j]: on_Enter_rect(event,rect))
    board.tag_bind(piece, '<Leave>', lambda event,rect=rectangles[i][j]: on_Leave_rect(event,rect))

def on_Enter_rect(event,rect):
        board.itemconfig(rect, outline='black',width=6)
def on_Leave_rect(event,rect):
        board.itemconfig(rect, outline='black',width=1)

def back():
      if len(clicked_moves)>0:  
        for rects in clicked_moves[-1]:
                board.itemconfig(rects,width=0)
                board.tag_bind(rects,'<Enter>',lambda event,rect=rects: on_Enter_rect(event,rect))
                board.tag_bind(rects,'<Leave>',lambda event,rect=rects: on_Leave_rect(event,rect))
                board.tag_unbind(rects,'<Button-1>')
def backButtons(moves,isWhite):
        for move in moves:
                x,y=move
                board.tag_unbind(rectangles[x][y],'<Button-1>')
        if isWhite:
                for piece in white_pieces:
                        board.tag_unbind(white_pieces[piece], '<Button-1>')
        else :
                for piece in black_pieces:
                        board.tag_unbind(black_pieces[piece], '<Button-1>')
def promotion (piece):
        selected=tk.StringVar()
        x,y=piecePosition[piece]
        if 'white' in piece:
                def choose(option):
                        selected.set(option)
                b1=tk.Button(leftFrame, text="Queen", command=lambda: choose("Q"))
                b1.pack(side='right')
                b2=tk.Button(leftFrame, text="Knight", command=lambda: choose("K"))
                b2.pack(side='right')
                b3=tk.Button(leftFrame, text="Rook", command=lambda: choose("R"))
                b3.pack(side='right')
                b4=tk.Button(leftFrame, text="Bishop", command=lambda: choose("B"))
                b4.pack(side='right')
                root.wait_variable(selected)
                if selected.get()=='Q':
                        whiteQueen2=board.create_image(boardPositions[x][y]['x'],boardPositions[x][y]['y'], image=whiteQueeni)
                        board.delete(all_pieces[piece])
                        piecePosition['whiteQueen2']=piecePosition[piece]
                        all_pieces['whiteQueen2']=whiteQueen2
                        white_pieces['whiteQueen2']=whiteQueen2
                        piecePosition.pop(piece)
                        all_pieces.pop(piece)
                        white_pieces.pop(piece)
                elif selected.get()=='K':
                        whiteKnight3=board.create_image(boardPositions[x][y]['x'],boardPositions[x][y]['y'], image=whiteKnight)
                        board.delete(all_pieces[piece])
                        piecePosition['whiteKnight3']=piecePosition[piece]
                        all_pieces['whiteKnight3']=whiteKnight3
                        white_pieces['whiteKnight3']=whiteKnight3
                        piecePosition.pop(piece)
                        all_pieces.pop(piece)
                        white_pieces.pop(piece)
                elif selected.get()=='R':
                        whiteRook3=board.create_image(boardPositions[x][y]['x'],boardPositions[x][y]['y'], image=whiteRook)
                        board.delete(all_pieces[piece])
                        piecePosition['whiteRook3']=piecePosition[piece]
                        all_pieces['whiteRook3']=whiteRook3
                        white_pieces['whiteRook3']=whiteRook3
                        piecePosition.pop(piece)
                        all_pieces.pop(piece)
                        white_pieces.pop(piece)
                if selected.get()=='B':
                        whiteBishop3=board.create_image(boardPositions[x][y]['x'],boardPositions[x][y]['y'], image=whiteBishop)
                        board.delete(all_pieces[piece])
                        piecePosition['whiteBishop3']=piecePosition[piece]
                        all_pieces['whiteBishop3']=whiteBishop3
                        white_pieces['whiteBishop3']=whiteBishop3
                        piecePosition.pop(piece)
                        all_pieces.pop(piece)
                        white_pieces.pop(piece)
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
        if 'black' in piece:
                def choose(option):
                        selected.set(option)
                b1=tk.Button(rightFrame, text="Queen", command=lambda: choose("Q"))
                b1.pack(side='right')
                b2=tk.Button(rightFrame, text="Knight", command=lambda: choose("K"))
                b2.pack(side='right')
                b3=tk.Button(rightFrame, text="Rook", command=lambda: choose("R"))
                b3.pack(side='right')
                b4=tk.Button(rightFrame, text="Bishop", command=lambda: choose("B"))
                b4.pack(side='right')
                root.wait_variable(selected)
                if selected.get()=='Q':
                        blackQueen2=board.create_image(boardPositions[x][y]['x'],boardPositions[x][y]['y'], image=blackQueeni)
                        board.delete(all_pieces[piece])
                        piecePosition['blackQueen2']=piecePosition[piece]
                        all_pieces['blackQueen2']=blackQueen2
                        black_pieces['blackQueen2']=blackQueen2
                        piecePosition.pop(piece)
                        all_pieces.pop(piece)
                        black_pieces.pop(piece)
                elif selected.get()=='K':
                        blackKnight3=board.create_image(boardPositions[x][y]['x'],boardPositions[x][y]['y'], image=blackKnight)
                        board.delete(all_pieces[piece])
                        piecePosition['blackKnight3']=piecePosition[piece]
                        all_pieces['blackKnight3']=blackKnight3
                        black_pieces['blackKnight3']=blackKnight3
                        piecePosition.pop(piece)
                        all_pieces.pop(piece)
                        black_pieces.pop(piece)
                elif selected.get()=='R':
                        blackRook3=board.create_image(boardPositions[x][y]['x'],boardPositions[x][y]['y'], image=blackRook)
                        board.delete(all_pieces[piece])
                        piecePosition['blackRook3']=piecePosition[piece]
                        all_pieces['blackRook3']=blackRook3
                        black_pieces['blackRook3']=blackRook3
                        piecePosition.pop(piece)
                        all_pieces.pop(piece)
                        black_pieces.pop(piece)
                if selected.get()=='B':
                        blackBishop3=board.create_image(boardPositions[x][y]['x'],boardPositions[x][y]['y'], image=blackBishop)
                        board.delete(all_pieces[piece])
                        piecePosition['blackBishop3']=piecePosition[piece]
                        all_pieces['blackBishop3']=blackBishop3
                        black_pieces['blackBishop3']=blackBishop3
                        piecePosition.pop(piece)
                        all_pieces.pop(piece)
                        black_pieces.pop(piece)
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
        
def check(position,piece):
        moves=[]
        if 'white' in piece:
                for attacker in black_pieces:
                        if attacker != 'blackKing':
                                moves.extend(get_moves(attacker))
                        else :
                                moves.extend(king_moves_wo_check('blackKing'))
        elif 'black' in piece:
                for attacker in white_pieces:
                        if attacker != 'whiteKing':
                                moves.extend(get_moves(attacker))
                        else :
                                moves.extend(king_moves_wo_check('whiteKing'))
        for move in moves:
                if move==position:
                        return True
        return False
                

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
                        for key,value in piecePosition.items():
                                if move_position == value and key in white_pieces:
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
def king_moves(piece):
        empty=True
        move=[]
        x,y=piecePosition[piece]
        move_position=()
        kingMoves=[
        (1, 0), (0, 1),
        ( -1, 0), (0, -1),
        (-1, -1), (-1, +1),
        (+1, -1), (+1, +1)]
        for i,j in kingMoves:
                move_position=[x+i,y+j]
                if 0 <= x+i <= 7 and 0<= y+j <=7:
                        if not check(move_position,piece):
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
def king_moves_wo_check(piece):
        empty=True
        move=[]
        x,y=piecePosition[piece]
        move_position=()
        kingMoves=knight_moves =[
        (1, 0), (0, 1),
        ( -1, 0), (0, -1),
        (-1, -1), (-1, +1),
        (+1, -1), (+1, +1)]
        for i,j in kingMoves:
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
                return king_moves(piece)
        if 'Pawn' in piece:
                return pawn_moves(piece)

def on_check_moves(piece):
        moves=[]
        if 'white' in piece:
                for defender in white_pieces:
                        moves.extend(defender)

def end_game():
        pass
#gameplay
clicked_moves=[]

def show_moves(piece):
        back()
        moves=get_moves(piece)
        if moves!=None:
                x,y=piecePosition[piece]
                rects=[]
                current=rectangles[x][y]

                board.tag_unbind(current,'<Enter>')
                board.tag_unbind(current,'<Leave>')
                board.tag_unbind(piece,'<Enter>')
                board.tag_unbind(piece,'<Leave>')
                board.itemconfig(current, outline ='blue4', width=6)
                
                def maintain_selected(event):
                        board.itemconfig(current, outline='blue4', width=6)
                board.tag_bind(current, '<Enter>', maintain_selected)
                board.tag_bind(current, '<Leave>', maintain_selected)
                board.tag_bind(piece, '<Enter>', maintain_selected)
                board.tag_bind(piece, '<Leave>', maintain_selected)
                rects.append(current)
                for move in moves:
                        i,j=move
                        rect=rectangles[i][j]
                        rects.append(rect)
                        board.itemconfig(rect, outline='royalblue1',width=4)
                        board.tag_unbind(rect,'<Enter>')
                        board.tag_unbind(rect,'<Leave>')
                clicked_moves.append(rects)
        return moves

def get_piece(rect):
    pos = None
    for i in range(8):
        for j in range(8):
            if rectangles[i][j] == rect:
                pos = [i, j]
                break
        if pos:
            break
    for piece_name, position in piecePosition.items():
        if position == pos:
            return piece_name
        
    return None

def get_pos(rect):
    pos = None
    for i in range(8):
        for j in range(8):
            if rectangles[i][j] == rect:
                pos = [i, j]
                return pos
        
    return pos

def selected_move(event,piece,rect,moves):
        x,y=get_pos(rect)
        if(get_piece(rect)):
                target_name=get_piece(rect)
                if target_name in black_pieces:
                        captured=tk.Label(leftFrame,text=unicode_pieces[target_name],font=('Arial',20))
                        captured.pack(side='top')
                        black_pieces.pop(target_name)
                elif target_name in white_pieces:
                        captured=tk.Label(rightFrame,text=unicode_pieces[target_name],font=('Arial',20))
                        white_pieces.pop(target_name)
                        captured.pack(side='top')
                target=all_pieces[target_name]
                board.delete(target)
                all_pieces.pop(target_name)
                piecePosition.pop(target_name)
        back()
        backButtons(moves,'white' in piece)
        piecePosition[piece]=get_pos(rect)
        piece_id=all_pieces[piece]
        board.coords(piece_id,boardPositions[x][y]['x'],boardPositions[x][y]['y'])
        board.tag_bind(piece,'<Enter>','')
        if 'Pawn' in piece:
                if 'white' in piece and x==7:
                        promotion(piece)
                if 'black' in piece and x==0:
                        promotion(piece)
        result= play()
        if result:
                label=tk.Label(rightFrame,text=result)
                label.pack(fill='x')
                end_game()

def clicked_piece_moves(event,piece):
        moves=show_moves(piece)
        for move in moves:
                i,j=move
                if not get_piece(rectangles[i][j]):
                        board.tag_bind(rectangles[i][j],'<Button-1>',lambda event,rect=rectangles[i][j]: selected_move(event,piece,rect,moves))
                else:
                        board.tag_bind(all_pieces[get_piece(rectangles[i][j])],'<Button-1>',lambda event,rect=rectangles[i][j]:selected_move(event,piece,rect,moves))

def whiteturn():
        if not check(piecePosition['whiteKing'],'whiteKing'):
                for piece in white_pieces:
                        board.tag_bind(white_pieces[piece], '<Button-1>',lambda event,p=piece: clicked_piece_moves(event,p))
        else:
                if get_moves('whiteKing') :
                        board.tag_bind(whiteKing, '<Button-1>',lambda event: clicked_piece_moves(event,'whiteKing'))
                else:
                        print('Black Won')
                        return 'Black won'
        return ''

def blackturn():
        if not check(piecePosition['blackKing'],'blackKing'):
                for piece in black_pieces:
                        board.tag_bind(black_pieces[piece], '<Button-1>',lambda event,p=piece: clicked_piece_moves(event,p))
        else :
                if get_moves('blackKing') :
                        board.tag_bind(blackKing, '<Button-1>',lambda event: clicked_piece_moves(event,'blackKing'))
                else:   
                        print('White_won')
                        return 'White won'
        return ''

i=0
def play():
        global i
        if i%2==0:
                print("whiteTurn")
                i+=1
                return whiteturn()
        else:
                i+=1
                print("blackTurn")
                return blackturn()
        

bt =tk.Button(leftFrame,text="Start",command=play)
bt.pack(side='right',fill='x')
root.mainloop()

#Problems:
#Outlining Errors
#Promotion
#King move to capture and in check
#Stalemate

