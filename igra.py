

from tkinter import *



class igra:
    def __init__(self, master):
        self.canvas = Canvas(master, width=700, height=600, bg = "pink")
        self.canvas.grid(row=1, column=1)
        menu = Menu(master)
        master.config(menu = menu)
        menu.add_command(label="Start", command=self.start)
        menu.add_command(label="Exit", command=master.destroy)
        self.canvas.bind("<Button-1>", self.klik)
        self.canvas.create_line([(600,0),(600,600)], width = 2)
        self.canvas.create_line([(500,0),(500,600)], width = 2)
        self.canvas.create_line([(400,0),(400,600)], width = 2)
        self.canvas.create_line([(300,0),(300,600)], width = 2)
        self.canvas.create_line([(200,0),(200,600)], width = 2)
        self.canvas.create_line([(100,0),(100,600)], width = 2)
        self.canvas.create_line([(0,100),(700,100)], width = 2)
        self.canvas.create_line([(0,200),(700,200)], width = 2)
        self.canvas.create_line([(0,300),(700,300)], width = 2)
        self.canvas.create_line([(0,400),(700,400)], width = 2)
        self.canvas.create_line([(0,500),(700,500)], width = 2)
        self.matrika = [[0 for i in range(7)] for i in range(6)]
        self.konec = False
        self.navrsti = 0
    def start(self):
        self.canvas.delete(ALL)
        self.canvas.create_line([(600,0),(600,600)], width = 2)
        self.canvas.create_line([(500,0),(500,600)], width = 2)
        self.canvas.create_line([(400,0),(400,600)], width = 2)
        self.canvas.create_line([(300,0),(300,600)], width = 2)
        self.canvas.create_line([(200,0),(200,600)], width = 2)
        self.canvas.create_line([(100,0),(100,600)], width = 2)
        self.canvas.create_line([(0,100),(700,100)], width = 2)
        self.canvas.create_line([(0,200),(700,200)], width = 2)
        self.canvas.create_line([(0,300),(700,300)], width = 2)
        self.canvas.create_line([(0,400),(700,400)], width = 2)
        self.canvas.create_line([(0,500),(700,500)], width = 2)
        self.matrika = [[0 for i in range(7)] for i in range(6)]
        self.navrsti = 0
        self.konec = False

    def klik(self, event):
        if not(self.konec):
            if self.navrsti == 0:
                x, y = event.x, event.y
                a=x//100
                b=5
                naredi = True
                while not(self.matrika[b][a]==0):
                    if b==0:
                        naredi = False
                    else:
                        b-=1
                if naredi:
                    self.matrika[b][a]=1
                    self.navrsti = 1
                    self.canvas.create_oval(100*(a+0.05),100*(b+0.05),100*(a+1-0.05),100*(b+1-0.05), fill = "white")
            
            else:
                x, y = event.x, event.y
                a=x//100
                b=5
                naredi = True
                while not(self.matrika[b][a]==0):
                    if b==0:
                        naredi = False
                    else:
                        b-=1
                if naredi:
                    self.matrika[b][a]=(-1)
                    self.navrsti = 0
                    self.canvas.create_oval(100*(a+0.05),100*(b+0.05),100*(a+1-0.05),100*(b+1-0.05), fill = "black")


            for i in range(4):
                if i==0:  #vodoravno
                    for z in range(6):
                        for q in range(4):
                            if not(self.matrika[z][q]==0):
                                if self.matrika[z][q] == self.matrika[z][q+1]:
                                    if self.matrika[z][q] == self.matrika[z][q+2]:
                                        if self.matrika[z][q] == self.matrika[z][q+3]:
                                            self.konec=True
                                            barva = "white" if self.navrsti == 0 else "black"
                                            
                                            self.canvas.create_line([(50 + 100*q,50 + 100*z),(50 + 100*(q+3),50 +100*z)], width = 3, fill = barva)
                elif i==1:  #desnadiagonala
                    
                    for z in range(3):
                        for q in range(4):
                            if not(self.matrika[z][q]==0):
                                if self.matrika[z][q] == self.matrika[z+1][q+1]:
                                    if self.matrika[z][q] == self.matrika[z+2][q+2]:
                                        if self.matrika[z][q] == self.matrika[z+3][q+3]:
                                            self.konec=True
                                            barva = "white" if self.navrsti == 0 else "black"
                                            
                                            self.canvas.create_line([(50 + 100*q,50 + 100*z),(50 + 100*(q+3),50 +100*(z+3))], width = 3, fill = barva)
                elif i==2:  #navpicno
                    for z in range(3):
                        for q in range(7):
                            if not(self.matrika[z][q]==0):
                                if self.matrika[z][q] == self.matrika[z+1][q]:
                                    if self.matrika[z][q] == self.matrika[z+2][q]:
                                        if self.matrika[z][q] == self.matrika[z+3][q]:
                                            self.konec=True
                                            barva = "white" if self.navrsti == 0 else "black"
                                            self.canvas.create_line([(50 + 100*q,50 + 100*z),(50 + 100*q,50 +100*(z+3))], width = 3, fill = barva)
                else:
                    for z in range(3,6):
                        for q in range(4):
                            if not(self.matrika[z][q]==0):
                                if self.matrika[z][q] == self.matrika[z-1][q+1]:
                                    if self.matrika[z][q] == self.matrika[z-2][q+2]:
                                        if self.matrika[z][q] == self.matrika[z-3][q+3]:
                                            self.konec=True
                                            barva = "white" if self.navrsti == 0 else "black"
                                            self.canvas.create_line([(50 + 100*q,50 + 100*z),(50 + 100*(q+3),50 +100*(z-3))], width = 3, fill = barva)

                                
            
        else:
            master = Tk()
            w = Message(master, text="Game Over", bg='pink',)
            w.pack()
            self.canvas.delete(ALL)
               





root = Tk()
aplikacije = igra(root)
root.mainloop()
