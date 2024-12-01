from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

def juegoNuevo():
    global la_palabra_conEspacios
    global numeroDeIntentos
    numeroDeIntentos=0

    la_palabra = random.choice(lista_palabras)
    la_palabra_conEspacios = " ".join(la_palabra)
    etiquetaPalabra.set(' '.join("_"*len(la_palabra)))
    imgEtiqueta.config(image=fotos[0])

    n=0
    for c in ascii_uppercase:
        try:
            ventana.nametowidget("."+c.lower()).destroy()
        except:
            print("Already deleted")
        Button(ventana,name=c.lower(),text=c,command=lambda c=c: adivinar(c),font=('Helvetica 18'),width=4).grid(row=1+n//9,column=n%9)
        n+=1

def adivinar(letra):
    global numeroDeIntentos
    if numeroDeIntentos<11:
        texto = list(la_palabra_conEspacios)
        adivinado = list(etiquetaPalabra.get())
        if la_palabra_conEspacios.count(letra)>0:
            for c in range(len(texto)):
                if texto[c]==letra:
                    adivinado[c]=letra
                    try:
                        ventana.nametowidget("."+letra.lower()).destroy()
                    except:
                        print("Already deleted")
                etiquetaPalabra.set("".join(adivinado))
                if etiquetaPalabra.get()==la_palabra_conEspacios:
                    messagebox.showinfo("Ahorcado","Ganaste! =)")
                    break
        else:
            numeroDeIntentos += 1
            imgEtiqueta.config(image=fotos[numeroDeIntentos])
            if numeroDeIntentos == 11:
                messagebox.showwarning("Ahorcado","Perdiste =(")
        
ventana = Tk()
ventana.title("Ahorcado")

lista_palabras = ['PUNTARENAS','SANJOSE','LIMON','ALAJUELA','HEREDIA','GUANCASTE']
fotos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

imgEtiqueta=Label(ventana)
imgEtiqueta.grid(row=0,column=0,columnspan=3,padx=10,pady=40)

etiquetaPalabra = StringVar()
Label(ventana,textvariable=etiquetaPalabra,font=('consolas 24 bold')).grid(row=0,column=3,columnspan=3,padx=10)

Button(ventana,text="Juego\nnuevo",command=lambda:juegoNuevo(),font=("Helvetica 10 bold")).grid(row=3,column=8)

juegoNuevo()
ventana.mainloop()