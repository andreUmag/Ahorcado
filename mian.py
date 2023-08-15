from tkinter import *
from random import randint
from tkinter.messagebox import *

letrasUsadas = []
vidas = 7
letrasAcertadas = 0


def colocarLetras():
    x = 50
    y = 150
    contador = 0
    Label(canvas, text="Letras sin usar").place(x=75, y=110)
    for i in range(26):
        contador += 1
        letrasLabel[i].place(x=x, y=y)
        x += 30
        if contador == 5:
            y += 35
            contador = 0
            x = 50


def probarLetraFuncion():
    global vidas
    global letrasAcertadas
    letrasUsadas.append(letraObtenida.get())
    print(letrasUsadas)
    letrasLabel[ord(letraObtenida.get()) - 97].config(text="")


    if letraObtenida.get() in palabra:
        if palabra.count(letraObtenida.get()) > 1:
            letrasAcertadas += palabra.count(letraObtenida.get())
            for s in range(len(palabra)):
                if palabra[s] == letraObtenida.get():
                    guiones[s].config(text="" + letraObtenida.get())
        else:
            letrasAcertadas += 1
            guiones[palabra.index(letraObtenida.get())].config(text="" + letraObtenida.get())
            if letrasAcertadas == len(palabra):
                showwarning(title="GANASTE", message="FELICIDADES, GANASTE")
                exit()
    else:
        vidas -= 1
        canvas.itemconfig(imagen_id, image=imagenes[vidas - 1])
        if vidas == 0:
            showwarning(title="Perdiste", message="Sin vidas")  #
            exit()


raiz = Tk()
archivo = open("palabras.txt", "r")
conjuntoPalabras = list(archivo.read().split("\n"))
palabra = conjuntoPalabras[randint(0, len(conjuntoPalabras) - 1)].lower()
letraObtenida = StringVar()

raiz.config(width=1000, height=600, bg="beige", relief="groove", bd=10)
raiz.geometry("1000x600")
canvas = Canvas(raiz, width=1000, height=600)
canvas.pack(expand=True, fill="both")

imagenes = [
    PhotoImage(file="1.png"),
    PhotoImage(file="2.png"),
    PhotoImage(file="3.png"),
    PhotoImage(file="4.png"),
    PhotoImage(file="5.png"),
    PhotoImage(file="6.png"),
    PhotoImage(file="7.png"),
]
imagen_id = canvas.create_image(750, 300, image=imagenes[6])

Label(canvas, text="Ingresa una letra", font=("verdana", 24)).grid(row=0, column=0, padx=10, pady=10)
letra = Entry(canvas, width=1, font=("verdana", 24), textvariable=letraObtenida).grid(row=0, column=1, padx=10, pady=10)
probarLetra = Button(canvas, text="Ingresar", bg="gray", command=probarLetraFuncion).grid(row=1, column=0, pady=10)

letrasLabel = [Label(canvas, text=chr(j + 97), font=("verdana", 20)) for j in range(26)]
colocarLetras()

guiones = [Label(canvas, text="_", font=("verdana", 30)) for _ in palabra]
inicialx = 200
for i in range(len(palabra)):
    guiones[i].place(x=inicialx, y=400)
    inicialx += 50

raiz.mainloop()
