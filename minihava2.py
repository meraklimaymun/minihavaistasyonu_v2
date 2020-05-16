#! /usr/bin/python3

import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
from tkinter import * 
import tkinter.font 
from PIL import Image, ImageTk

GPIO.setmode (GPIO.BCM)

win = tkinter.Tk() #win ile tk'yi cagirdigimizi belirttik.

win.attributes('-fullscreen', True) #Tam ekran moduna gecis.
win.configure(bg='black') #Arkaplan rengini siyah yapiyoruz.

       #ARKAPLAN RESMINI OLUSTURUYORUZ...
arkaplan_resim = Image.open("/home/pi/Desktop/NRF24L01/arkaplan.jpg")
arkaplan_resim= ImageTk.PhotoImage(arkaplan_resim)
canv = Canvas(win, width=800,height=480, background="black")   
canv.create_image(400, 240, image = arkaplan_resim)
canv.place(x=0,y=0)

pipes = [[0xE8, 0xE8, 0XF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 17)

radio.setPayloadSize(32)
radio.setChannel(0x76)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel (NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe(1, pipes[1])
radio.printDetails()
radio.startListening()


while True:
    while not radio.available(0):
        time.sleep(1/100)
    
    receivedMessage = []
    radio.read(receivedMessage, radio.getDynamicPayloadSize())
    string = ""
    
    for n in receivedMessage:
        if (n >= 32 and n <= 126):
            string += chr(n)
    print(string)
    olcum = (string.split())
    



    #SICAKLIK DEGERINE GORE GOSTERGE DEGISIMI...
    if int(olcum[1]) >-30 and int(olcum[1]) <=0:
       sicaklik_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye1.png")
       #sicaklik_resim = sicaklik_resim.resize((179,101), Image.ANTIALIAS)
       sicaklik_resim = ImageTk.PhotoImage(sicaklik_resim)
       canv.create_image(424, 123, image = sicaklik_resim)
       
    elif int(olcum[1]) >0 and int(olcum[1]) <=10:
       sicaklik_resim= Image.open("/home/pi/Desktop/NRF24L01/seviye2.png")
       #sicaklik_resim = sicaklik_resim.resize((179,101), Image.ANTIALIAS)
       sicaklik_resim = ImageTk.PhotoImage(sicaklik_resim)
       canv.create_image(424, 123, image = sicaklik_resim)

    elif int(olcum[1]) >10 and int(olcum[1]) <=20:
       sicaklik_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye3.png")
       #sicaklik_resim = sicaklik_resim.resize((179,101), Image.ANTIALIAS)
       sicaklik_resim = ImageTk.PhotoImage(sicaklik_resim)
       canv.create_image(424, 123, image = sicaklik_resim)

    elif int(olcum[1]) >20 and int(olcum[1]) <=30:
       sicaklik_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye4.png")
       #sicaklik_resim = sicaklik_resim.resize((179,101), Image.ANTIALIAS)
       sicaklik_resim = ImageTk.PhotoImage(sicaklik_resim)
       canv.create_image(424, 123, image = sicaklik_resim)
       
    elif int(olcum[1]) >30 and int(olcum[1]) <=40:
       sicaklik_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye5.png")
       #sicaklik_resim = sicaklik_resim.resize((179,96), Image.ANTIALIAS)
       sicaklik_resim = ImageTk.PhotoImage(sicaklik_resim)
       canv.create_image(424, 123, image = sicaklik_resim)

    elif int(olcum[1]) >40 and int(olcum[1]) <=50:
       sicaklik_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye6.png")
       #sicaklik_resim = sicaklik_resim.resize((179,96), Image.ANTIALIAS)
       sicaklik_resim = ImageTk.PhotoImage(sicaklik_resim)
       canv.create_image(424, 123, image = sicaklik_resim)


    #NEM DEGERINE GORE GOSTERGE DEGISIMI...
    if int(olcum[0]) >0 and int(olcum[0]) <=30:
       nem_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye1.png")
       #nem_resim = nem_resim.resize((179,96), Image.ANTIALIAS)
       nem_resim = ImageTk.PhotoImage(nem_resim)
       canv.create_image(683, 123, image = nem_resim)
    
    elif int(olcum[0]) >30 and int(olcum[0]) <=40:
       nem_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye2.png")
       #nem_resim = nem_resim.resize((179,96), Image.ANTIALIAS)
       nem_resim = ImageTk.PhotoImage(nem_resim)
       canv.create_image(683, 123, image = nem_resim)
       
    elif int(olcum[0]) >40 and int(olcum[0]) <=50:
       nem_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye3.png")
       #nem_resim = nem_resim.resize((179,96), Image.ANTIALIAS)
       nem_resim = ImageTk.PhotoImage(nem_resim)
       canv.create_image(683, 123, image = nem_resim)

    elif int(olcum[0]) >50 and int(olcum[0]) <=60:
       nem_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye4.png")
       #nem_resim = nem_resim.resize((179,96), Image.ANTIALIAS)
       nem_resim = ImageTk.PhotoImage(nem_resim)
       canv.create_image(683, 123, image = nem_resim)
       
    elif int(olcum[0]) >60 and int(olcum[0]) <=70:
       nem_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye5.png")
       #nem_resim = nem_resim.resize((179,96), Image.ANTIALIAS)
       nem_resim = ImageTk.PhotoImage(nem_resim)
       canv.create_image(683, 123, image = nem_resim)
       
    elif int(olcum[0]) >70 and int(olcum[0]) <=100:
       nem_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye6.png")
       #nem_resim = nem_resim.resize((179,96), Image.ANTIALIAS)
       nem_resim = ImageTk.PhotoImage(nem_resim)
       canv.create_image(683, 123, image = nem_resim)
    
    #RUZGAR DEGERLERINE GORE GOSTERGE DEGISIMI
    if int(olcum[3]) >=0 and int(olcum[3]) <=20:
       ruzgar_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye1.png")
       #ruzgar_resim = ruzgar_resim.resize((179,96), Image.ANTIALIAS)
       ruzgar_resim = ImageTk.PhotoImage(ruzgar_resim)
       canv.create_image(424, 323, image = ruzgar_resim)
       etiket4 = Label(win, text=("Sakin"),bg="white",fg="black", height=1, width=8,font = "Helvetica 14 bold italic")
       etiket4.place(x=405, y=385)
    
    elif int(olcum[3]) >20 and int(olcum[3]) <=100:
       ruzgar_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye2.png")
       #ruzgar_resim = ruzgar_resim.resize((179,96), Image.ANTIALIAS)
       ruzgar_resim = ImageTk.PhotoImage(ruzgar_resim)
       canv.create_image(424, 323, image = ruzgar_resim)
       etiket4 = Label(win, text=("Ruzgarli"),bg="white",fg="black", height=1, width=8,font = "Helvetica 14 bold italic")
       etiket4.place(x=405, y=385)
    
    elif int(olcum[3]) >100 and int(olcum[3]) <=250:
       ruzgar_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye3.png")
       #ruzgar_resim = ruzgar_resim.resize((179,96), Image.ANTIALIAS)
       ruzgar_resim = ImageTk.PhotoImage(ruzgar_resim)
       canv.create_image(424, 323, image = ruzgar_resim)
       etiket4 = Label(win, text=("Esintili"),bg="white",fg="black", height=1, width=8,font = "Helvetica 14 bold italic")
       etiket4.place(x=405, y=385)
    
    elif int(olcum[3]) >250 and int(olcum[3]) <=500:
       ruzgar_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye4.png")
       #ruzgar_resim = ruzgar_resim.resize((179,96), Image.ANTIALIAS)
       ruzgar_resim = ImageTk.PhotoImage(ruzgar_resim)
       canv.create_image(424, 323, image = ruzgar_resim)
       etiket4 = Label(win, text=("Esintili"),bg="white",fg="black", height=1, width=8,font = "Helvetica 14 bold italic")
       etiket4.place(x=405, y=385)
       
    elif int(olcum[3]) >500 and int(olcum[3]) <=750:
       ruzgar_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye5.png")
       #ruzgar_resim = ruzgar_resim.resize((179,96), Image.ANTIALIAS)
       ruzgar_resim = ImageTk.PhotoImage(ruzgar_resim)
       canv.create_image(424, 323, image = ruzgar_resim)
       etiket4 = Label(win, text=("Firtina"),bg="white",fg="black", height=1, width=8,font = "Helvetica 14 bold italic")
       etiket4.place(x=405, y=385)
       
    elif int(olcum[3]) >750 and int(olcum[3]) <=1000:
       ruzgar_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye6.png")
       #ruzgar_resim = ruzgar_resim.resize((179,96), Image.ANTIALIAS)
       ruzgar_resim = ImageTk.PhotoImage(ruzgar_resim)
       canv.create_image(424, 323, image = ruzgar_resim)
       etiket4 = Label(win, text=("Firtina"),bg="white",fg="black", height=1, width=8,font = "Helvetica 14 bold italic")
       etiket4.place(x=405, y=385)
       
       #BASINC DEGERINE GORE GOSTERGE DEGISIMI...
    if int(olcum[2]) >910 and int(olcum[2]) <=945:
       basinc_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye1.png")
       #basinc_resim = basinc_resim.resize((179,96), Image.ANTIALIAS)
       basinc_resim = ImageTk.PhotoImage(basinc_resim)
       canv.create_image(683, 323, image = basinc_resim)
       
    if int(olcum[2]) >945 and int(olcum[2]) <=970:
       basinc_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye2.png")
       #basinc_resim = basinc_resim.resize((179,96), Image.ANTIALIAS)
       basinc_resim = ImageTk.PhotoImage(basinc_resim)
       canv.create_image(683, 323, image = basinc_resim)

    if int(olcum[2]) >970 and int(olcum[2]) <=995:
       basinc_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye3.png")
       #basinc_resim = basinc_resim.resize((179,96), Image.ANTIALIAS)
       basinc_resim = ImageTk.PhotoImage(basinc_resim)
       canv.create_image(683, 323, image = basinc_resim)
       
    if int(olcum[2]) >995 and int(olcum[2]) <=1020:
       basinc_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye4.png")
       #basinc_resim = basinc_resim.resize((179,96), Image.ANTIALIAS)
       basinc_resim = ImageTk.PhotoImage(basinc_resim)
       canv.create_image(683, 323, image = basinc_resim)
       
    if int(olcum[2]) >1020 and int(olcum[2]) <=1045:
       basinc_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye5.png")
       #basinc_resim = basinc_resim.resize((179,96), Image.ANTIALIAS)
       basinc_resim = ImageTk.PhotoImage(basinc_resim)
       canv.create_image(683, 323, image = basinc_resim)
       
    if int(olcum[2]) >1045 and int(olcum[2]) <=1070:
       basinc_resim = Image.open("/home/pi/Desktop/NRF24L01/seviye5.png")
       #basinc_resim = basinc_resim.resize((179,96), Image.ANTIALIAS)
       basinc_resim = ImageTk.PhotoImage(basinc_resim)
       canv.create_image(683, 323, image = basinc_resim)
       
    etiket1 = Label(win, text=(olcum[1]+ chr(176)+"C"),bg="white",fg="black", height=1, width=5,font = "Helvetica 26 bold italic")
    etiket1.place(x=390, y=170)
    
    etiket2 = Label(win, text=("%"+ olcum[0]),bg="white",fg="black", height=1, width=4,font = "Helvetica 27 bold italic")
    etiket2.place(x=655, y=168)
    
    etiket3 = Label(win, text=(olcum[2] + "hPa"),bg="white",fg="black", height=1, width=7,font = "Helvetica 17 bold italic")
    etiket3.place(x=655, y=380)
    win.update()
    #time.sleep(300)

win.mainloop() #Penceremizi yaratiyoruz.
  
    


