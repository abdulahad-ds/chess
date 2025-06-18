import tkinter as tk

root=tk.Tk()
root.geometry("1280x700")
root.title("Chess")

Header=tk.Frame(root,bg='gray',height=25)
Header.pack(fill='x')
Header2=tk.Frame(root,bg='gray',height=25)
Header2.pack(side='bottom',fill='x')

board=tk.Canvas(root,width=600,height=750)
board.pack(expand=False,fill='both')

 

i=0
j=0
n=int(596/8)
x1=0
x2=n
y1=0
y2=n
img=tk.PhotoImage(file="white-pawn.png")
whitePawn1 = img.subsample(2, 2)
img=tk.PhotoImage(file="white-rook.png")
whiteRook=img.subsample(2,2)
img=tk.PhotoImage(file="white-knight.png")
whiteKnight=img.subsample(2,2)
img=tk.PhotoImage(file="white-bishop.png")
whiteBishop=img.subsample(2,2)
img=tk.PhotoImage(file="white-queen.png")
whiteQueen=img.subsample(2,2)
img=tk.PhotoImage(file="white-king.png")
whiteKing=img.subsample(2,2)

img=tk.PhotoImage(file="black-pawn.png")
blackPawn1 = img.subsample(2, 2)
img=tk.PhotoImage(file="black-rook.png")
blackRook=img.subsample(2,2)
img=tk.PhotoImage(file="black-knight.png")
blackKnight=img.subsample(2,2)
img=tk.PhotoImage(file="black-bishop.png")
blackBishop=img.subsample(2,2)
img=tk.PhotoImage(file="black-queen.png")
blackQueen=img.subsample(2,2)
img=tk.PhotoImage(file="black-king.png")
blackKing=img.subsample(2,2)

while i<=8:
    while j<=8:
        if (i+j)%2==0:
            colour='darkgrey'
            colour2='snow'
        else:
            colour='snow'
            colour2='darkgrey'
            
        blockNum=chr(j+96)+str(i)
        
        board.create_rectangle(x1,y1,x2,y2,fill=colour)
        board.create_text(x1-8, y1-8, text=blockNum, font=("Arial", int(n/8)),fill='black')
        #knight = board.create_text(int((x1+x2)/2),int( (y1+y2)/2), text="♘", font=("Arial", 36))
        if i==1:
            if j==1 or j==8:
                    board.create_image(int((x1+x2)/2),int( (y1+y2)/2), image=whiteRook)
            if j==2 or j==7:
                    board.create_image(int((x1+x2)/2),int( (y1+y2)/2), image=whiteKnight)
            if j==3 or j==6:
                    board.create_image(int((x1+x2)/2),int( (y1+y2)/2), image=whiteBishop)
            if j==4:
                    board.create_image(int((x1+x2)/2),int( (y1+y2)/2), image=whiteQueen)
            if j==5:
                    board.create_image(int((x1+x2)/2),int( (y1+y2)/2), image=whiteKing)
        if i==2:
            board.create_image(int((x1+x2)/2),int( (y1+y2)/2), image=whitePawn1)

        if i==8:
            if j==1 or j==8:
                    board.create_image(int((x1+x2)/2),int( (y1+y2)/2), image=blackRook)
            if j==2 or j==7:
                    board.create_image(int((x1+x2)/2),int( (y1+y2)/2), image=blackKnight)
            if j==3 or j==6:
                    board.create_image(int((x1+x2)/2),int( (y1+y2)/2), image=blackBishop)
            if j==4:
                    board.create_image(int((x1+x2)/2),int( (y1+y2)/2), image=blackQueen)
            if j==5:
                    board.create_image(int((x1+x2)/2),int( (y1+y2)/2), image=blackKing)

        if i==7:
            board.create_image(int((x1+x2)/2),int( (y1+y2)/2), image=blackPawn1)
        x2=x1
        x1=n*(j+1)
        j+=1
    y2=y1
    y1=n*(i+1)
    x1=0
    j=0
    i+=1    

root.mainloop()