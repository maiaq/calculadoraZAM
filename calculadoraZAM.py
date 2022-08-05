from tkinter import *
from functools import partial 
from menu import Aplicacion
boton = ""



def digito(num):
    global boton
    boton = boton + str(num)
    calculo.set(boton)

def igual():
    try:
        global boton
        total = str(eval(boton))
        calculo.set(total)
        boton = ""
    except:
        calculo.set(" error ")

def limpiar():
    global boton
    boton = ""
    calculo.set("")
    
def prueba(label):
    print(label)

def ventanachica(label):
    ventana.geometry("640x480")
    


if __name__ == "__main__":
    menu = Aplicacion()
    ventana = menu.ventana1
#     ventana.configure(background="light pink")
    ventana.title("Calculadora ZAM")
#     ventana.geometry("285x190")
    ventana.resizable(width=False, height=False)
    print("creando Calcu")
    calculo = menu.calculo
    datos = Entry(ventana, font=("Seven Segment",12), textvariable=calculo, justify="right")
    datos.grid(columnspan=10, ipadx=32)
    i = 0
    for fila in range(2,5):
        for columna in range(0,3):
            i += 1
            bot = Button(ventana, text=' ' + str(i) + ' ', fg='black', bg='white',
                           command=partial(digito, i), height=2, width=5)
            bot.grid(row=fila, column=columna)
    digitos = ['+', '-', '*', '/']

    boton0 = Button(ventana, text=' 0 ', fg='black', bg='white',
                     command=lambda: digito(0), height=2, width=5)
    boton0.grid(row=5, column=0)
    
    for fil in range(2,6):
        operador = Button(ventana, text=' ' + digitos[fil-2] + ' ', fg='black', bg='white',
                     command=partial(digito, digitos[fil-2]), height=2, width=5)
        operador.grid(row=fil, column=3)
   
    resultado = Button(ventana, text=' = ', fg='black', bg='white',
                   command=igual, height=2, width=5)
    resultado.grid(row=5, column=2)
    limpiar = Button(ventana, text='borrar', fg='red', bg='white',
                   command=limpiar, height=2, width=5)
    limpiar.grid(row=5, column='1')

    ventana.mainloop()