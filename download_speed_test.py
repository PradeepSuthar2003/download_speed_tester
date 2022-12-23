from tkinter import *
import speedtest


def check_speed():
    spd = speedtest.Speedtest()
    down_spd = str(round(spd.download()/10**6, 3)) + " Mbps"
    up_spd = str(round(spd.upload()/10**6, 3)) + " Mbps"
    up_num_spd.config(text=up_spd)
    dn_num_spd.config(text=down_spd)


wn = Tk()
wn.title("Internet Speed Tester")
wn.geometry('500x500')
wn.config(bg='black')

title = Label(text="Internet Speed Test", fg='yellow',
              bg='black', font=('none', 30, 'bold'))
title.place(x=40, y=20)

down_spd = Label(text="Download Speed : ", fg='yellow',
                 bg='black', font=('none', 20, 'bold'))
down_spd.place(x=60, y=150)


dn_num_spd = Label(text="00", fg='yellow',
                   bg='black', font=('none', 25, 'bold'))
dn_num_spd.place(x=80, y=200)

up_spd = Label(text="Upload Speed : ", fg='yellow',
               bg='black', font=('none', 20, 'bold'))
up_spd.place(x=60, y=250)

up_num_spd = Label(text="00", fg='yellow',
                   bg='black', font=('none', 25, 'bold'))
up_num_spd.place(x=80, y=300)

chk_spd_btn = Button(text='Check Speed', fg='black',
                     bg='yellow', activebackground='green', border=1, command=check_speed)
chk_spd_btn.place(x=80, y=400)

wn.mainloop()
