import tkinter as tk

root=tk.Tk()
root.geometry("400x500")
root.title("Chess")

Header=tk.Frame(root,bg='gray',height=50)
Header.pack(fill='x')
Header2=tk.Frame(root,bg='gray',height=50)
Header2.pack(side='bottom',fill='x')

board=tk.Canvas(root,width=600,height=600)
board.pack(expand=False,fill='both')

 

i=0
j=0
n=50
x1=0
x2=n
y1=0
y2=n
while i<=8:
    while j<=8:
        if (i+j)%2==0:
            colour='lightgreen'
        else:
            colour='black'
        board.create_rectangle(x1,y1,x2,y2,fill=colour)
        x2=x1
        x1=n*(j+1)
        j+=1
    y2=y1
    y1=n*(i+1)
    x1=0
    j=0
    i+=1    

root.mainloop()