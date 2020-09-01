from tkinter import *

window = Tk()
window.title("ggg")

canvas = Canvas(window,width=500,height=500,bg="white")
canvas.create_rectangle(150,150,250,250,fill="green")
canvas.pack()
window.mainloop()

window = Tk()
canvas = Canvas(window,width=500,height=500,bg="white")
canvas.create_rectangle(0,0,500,500,fill="blue")
canvas.pack()
window.mainloop()

window = Tk()
canvas = Canvas(window,width=500,height=500,bg="white")
canvas.create_rectangle(0,0,250,250,fill="red")
canvas.pack()
window.mainloop()

window = Tk()
canvas = Canvas(window,width=500,height=500,bg="white")
canvas.create_rectangle(0,0,250,250,fill="purple")
canvas.create_rectangle(250,250,500,500,fill="brown")
canvas.pack()
window.mainloop()


window = Tk()
canvas = Canvas(window,width=500,height=500,bg="white")
canvas.create_line([250,0],[250,500],width=3,fil="blue")
canvas.pack()
window.mainloop()

window = Tk()
canvas = Canvas(window,width=500,height=500,bg="white")
canvas.create_line([0,250],[500,250],width=3,fil="blue")
canvas.pack()
window.mainloop()

window = Tk()
canvas = Canvas(window,width=500,height=500,bg="white")
canvas.create_line([0,0],[500,500],width=3,fil="blue")
canvas.pack()
window.mainloop()

window = Tk()
canvas = Canvas(window,width=500,height=500,bg="white")
canvas.create_line([0,0],[500,500],width=3,fil="blue")
canvas.create_line([0,500],[500,0],width=3,fil="black")
canvas.pack()
window.mainloop()

window = Tk()
canvas = Canvas(window,width=500,height=500,bg="white")
canvas.create_oval(100,100,200,200,width=3,outline="red")
canvas.create_oval(180,100,280,200,width=3,outline="green")
canvas.create_oval(260,100,360,200,width=3,outline="blue")

canvas.create_oval(130,160,230,260,width=3,outline="yellow")
canvas.create_oval(230,160,330,260,width=3,outline="black")

canvas.pack()
window.mainloop()

window = Tk()
canvas = Canvas(window,width=500,height=500,bg="white")
canvas.create_line([0,0],[500,500],width=3,fil="blue")
canvas.create_line([0,500],[500,0],width=3,fil="black")
canvas.pack()
window.mainloop()


window = Tk()
canvas = Canvas(window,width=500,height=500,bg="white")
canvas.create_oval(100,100,400,400,width=3,outline="black")
canvas.create_oval(140,140,360,360,width=3,outline="black")
canvas.create_oval(180,180,320,320,width=3,outline="black")
canvas.create_oval(220,220,280,280,width=3,outline="black")
canvas.create_oval(260,260,240,240,width=3,outline="black")
canvas.create_oval(300,300,200,200,width=3,outline="black")
canvas.create_oval(340,340,160,160,width=3,outline="black")
canvas.create_oval(380,380,120,120,width=3,outline="black")
canvas.create_oval(420,420,80,80,width=3,outline="black")
canvas.create_oval(460,460,40,40,width=3,outline="black")

canvas.pack()
window.mainloop()

window = Tk()
canvas = Canvas(window,width=500,height=120,bg="white")
canvas.create_polygon([10,10],[30,50],[80,50],[100,10],fill="red",width=2)
canvas.create_polygon([120,40],[160,10],[200,40],[180,80],[140,80],fill="yellow",width=2)
canvas.create_polygon([230,30],[250,30],[250,10],[270,10],[270,30],[290,30],[290,50],[270,50],[270,70],[250,70],[250,50],[230,50],fill="green",width=2)

canvas.pack()
window.mainloop()


window = Tk()
window.title("ggg")

canvas = Canvas(window,width=300,height=200,bg="white",
          cursor="pencil")

canvas.create_rectangle(0,50,100,75,fill="white",width=1)
canvas.create_rectangle(0,75,100,100,fill="red",width=1)
canvas.create_rectangle(0,100,100,125,fill="blue",width=1)

canvas.create_rectangle(100,50,75,125,fill="blue",width=1)
canvas.create_rectangle(125,50,100,125,fill="white",width=1)
canvas.create_rectangle(150,50,125,125,fill="red",width=1)

canvas.create_rectangle(150,50,250,75,fill="black",width=1)
canvas.create_rectangle(150,75,250,100,fill="red",width=1)
canvas.create_rectangle(150,100,250,125,fill="yellow",width=1)

canvas.pack()
window.mainloop()


window = Tk()
window.title("ggg")

canvas = Canvas(window,width=1000,height=1000,bg="white",
          cursor="pencil")

canvas.create_oval(100,100,200,200,width=2)

canvas.create_oval(100,150,110,155,width=1,fil="red")
canvas.create_oval(140,150,150,155,width=1,fil="red")

canvas.create_line([110,170],[130,180],width=4)
canvas.create_line([130,180],[150,170],width=4)

canvas.create_oval(50,200,250,400,width=2)
canvas.create_oval(20,400,300,650,width=2)

canvas.create_polygon([100,20],[200,20],[220,120],[80,120],fill="gray",width=2)

canvas.create_line([230,300],[360,350],width=3)
canvas.create_line([360,270],[300,650],width=3)

canvas.create_line([360,270],[350,190],width=3)
canvas.create_line([360,270],[370,190],width=3)
canvas.create_line([360,270],[390,190],width=3)

canvas.create_line([60,290],[30,400],width=3)
canvas.create_line([30,400],[120,350],width=3)

canvas.create_line([120,350],[130,380],width=3)
canvas.create_line([120,350],[140,370],width=3)
canvas.create_line([120,350],[150,360],width=3)
canvas.pack()
window.mainloop()

window = Tk()
window.title("ggg")

canvas = Canvas(window,width=1000,height=1000,bg="white",
          cursor="pencil")
 # орбита
canvas.create_oval(-180,640,380,1200,width=2, fil="yellow")
canvas.create_oval(-195,550,490,1230,width=2)
canvas.create_oval(-220,450,630,1300,width=2)
canvas.create_oval(-220,360,750,1320,width=2)
canvas.create_oval(-195,260,850,1320,width=2)
canvas.create_oval(-260,170,960,1390,width=2)
canvas.create_oval(-220,80,1050,1437,width=2)
canvas.create_oval(-348,6,1234,1690,width=2)
canvas.create_oval(-348,-80,1280,1670,width=2)
# плане
canvas.create_oval(440,810,510,880,width=2, fil="gray")
canvas.create_oval(570,780,660,874,width=2, fil="yellow")
canvas.create_oval(652,610,790,760,width=2, fil="blue")
canvas.create_oval(770,560,840,630,width=2, fil="red")
canvas.create_oval(580,170,860,460,width=2, fil="orange")
canvas.create_oval(42,-19,310,280,width=2, fil="orange")
canvas.create_oval(680,12,760,100,width=2, fil="blue")
canvas.create_oval(880,18,978,134,width=2, fil="blue")
# спут
canvas.create_oval(660,550,610,500,width=2, fil="gray")
canvas.create_oval(330,82,400,150,width=2, fil="gray")
canvas.create_oval(860,590,890,620,width=2, fil="gray")
# наз
canvas.create_text(158,870,text="Cолнце",font="Verdana 14",justify=CENTER,fill="black")
canvas.create_text(480,850,text="Меркурий",font="Verdana 14",justify=CENTER,fill="black")
canvas.create_text(610,820,text=" Венера",font="Verdana 14",justify=CENTER,fill="black")
canvas.create_text(720,680,text="Земля",font="Verdana 14",justify=CENTER,fill="black")
canvas.create_text(800,590,text="Марс",font="Verdana 14",justify=CENTER,fill="black")
canvas.create_text(720,310,text="Юпитер",font="Verdana 14",justify=CENTER,fill="black")
canvas.create_text(180,130,text="Сатурн",font="Verdana 14",justify=CENTER,fill="black")
canvas.create_text(720,50,text="Уран",font="Verdana 14",justify=CENTER,fill="black")
canvas.create_text(930,70,text="Нептун",font="Verdana 14",justify=CENTER,fill="black")
canvas.create_text(630,520,text="Луна",font="Verdana 14",justify=CENTER,fill="black")
canvas.create_text(365,110,text="Титан",font="Verdana 14",justify=CENTER,fill="black")
canvas.create_text(880,600,text="Фобос",font="Verdana 14",justify=CENTER,fill="black")

canvas.pack()
window.mainloop()


window = Tk()
window.title("ggg")

canvas = Canvas(window,width=700,height=700,bg="white",
          cursor="pencil")
canvas.create_polygon([170,400],[570,400],[530,500],[210,500],fill="burlywood3",width=2)


canvas.create_polygon([370,400],[370,10],[270,400],width=3,fill="azure2",outline="black")
canvas.create_polygon([370,400],[370,10],[470,400],width=3,fill="azure2",outline="black")

canvas.create_oval(450,425,500,475,width=4,fill="lightblue1",outline="white")
canvas.create_oval(350,425,400,475,width=4,fill="lightblue1",outline="white")
canvas.create_oval(250,425,300,475,width=4,fill="lightblue1",outline="white")

canvas.pack()
window.mainloop()


window = Tk()
canvas = Canvas(window,width=500,height=500,bg="white")
canvas.create_oval(10,10,240,240,width=3,outline="black")
canvas.create_rectangle(10,10,240,240,width=3,outline="black")

canvas.create_oval(230,230,490,490,width=3,outline="black")
canvas.create_rectangle(268,268,452,452,width=3,outline="black")

canvas.pack()
window.mainloop()

window = Tk()
window.geometry('350x350')
canvas = Canvas(window, bg='gray', width=350, height=350)
x = 225
y = 200
r = int(input("Введите радиус внутренней окружности: "))
r2 = int(input("Введите радиус внешней окружности: "))
canvas.create_oval(x - r2, y - r2, x + r2, y + r2, width=1, fill="black")
canvas.create_oval(x - r, y - r, x + r, y + r, width=1, fill="cyan2")
canvas.pack()
window.mainloop()

window = Tk()
window.title('lab2')
window.geometry('250x250')
canvas = Canvas(window, bg='black', width=250, height=250)
canvas.create_text(125, 125, fill="green", font=("Times New Roman",), text="I O S H A R A")
canvas.pack()
window.mainloop()

window = Tk()
window.title('lab3')
window.geometry('250x250')
canvas = Canvas(window, bg='white', width=250, height=320)
canvas.create_oval(85, 115, 170, 140, outline="black", fill="blue", width=3)
canvas.create_oval(115, 85, 140, 170, outline="black", fill="green", width=3)
canvas.pack()
window.mainloop()

window = Tk()
window.title('lab4')
window.geometry('250x150')
canvas = Canvas(window, bg='white', width=250, heigh=150)
canvas.create_polygon(125, 20, 168, 37, 185, 80, 168, 123, 125, 140, 82, 123, 65, 80, 82, 37, smooth=1, width=5,
                          outline="black", fill='plum1')
canvas.create_polygon(85, 5, 165, 5, 190, 5, 190, 30, 190, 40, 190, 75, 165, 75, 85, 75, 60, 75, 60, 50, 60, 30,
                          60, 5, smooth=1, width=5, outline="black", fill='gold')
canvas.pack()
window.mainloop()
