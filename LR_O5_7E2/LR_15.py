from tkinter import *

window = Tk()
window.title("ggg")

canvas = Canvas(window,width=1000,height=1000,bg="white",
          cursor="pencil")

'''''
canvas.create_rectangle(0,100,300,200,fill="red")
canvas.create_rectangle(0,200,300,300,fill="blue")
canvas.create_rectangle(300,0,400,300,fill="blue")
canvas.create_rectangle(500,0,600,300,fill="red")
canvas.create_rectangle(600,0,900,100,fill="black")
canvas.create_rectangle(600,100,900,200,fill="red")
canvas.create_rectangle(600,200,900,300,fill="yellow")
'''''
'''''
canvas.create_oval(100,100,200,200,width=2)
canvas.create_oval(50,200,250,400,width=2)
canvas.create_oval(20,400,300,650,width=2)
canvas.create_polygon([100,20],[200,20],[220,120],[80,120],fill="gray",width=2)
canvas.create_line([230,300],[360,350],width=3)
canvas.create_line([360,270],[300,650],width=3)
canvas.create_line([360,270],[350,190],width=3)
canvas.create_line([360,270],[370,190],width=3)
canvas.create_line([360,270],[390,190],width=3)
'''''
'''''
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
'''''
''
canvas.create_line([170,400],[570,400],width=3)
canvas.create_line([210,500],[530,500],width=3)
canvas.create_line([170,400],[210,500],width=3)
canvas.create_line([570,400],[530,500],width=3)

canvas.create_line([370,400],[370,10],width=3)
canvas.create_line([270,400],[370,10],width=3)
canvas.create_line([470,400],[370,10],width=3)

canvas.create_oval(450,425,500,475,width=2,)
canvas.create_oval(350,425,400,475,width=2,)
canvas.create_oval(250,425,300,475,width=2,)
''


canvas.pack()
window.mainloop()