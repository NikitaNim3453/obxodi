import os 
import tkinter



root = tkinter.Tk()
root.title("Obxodi")
root.geometry("500x500") 
root.config(bg="DimGrey")



def dis():
    os.startfile('C:\obxodi\prog\discord.bat') 

def ytb():
    os.startfile('C:\obxodi\prog\discord_youtube.bat') 




ds = tkinter.Button(width=22, height=2, text="Discord", font="Arial 30", command=dis, bg="Grey") 
ds.place(x=8, y=370) 



ytds = tkinter.Button(width=22, height=2, text="YouTube + Discord", font="Arial 30", command=ytb, bg="Grey") 
ytds.place(x=8, y=240) 


txt_one = tkinter.Label(text="Добрый день сер", font="Arial 30", bg="DimGrey")
txt_one.place(x=100, y= 40)

txt_tw = tkinter.Label(text="Чем займёмся?", font="Arial 30", bg="DimGrey")
txt_tw.place(x=100, y= 100)







root.mainloop()