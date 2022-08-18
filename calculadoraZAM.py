from tkinter import *
from functools import partial 
from menu import Aplicacion
boton = ""


class Calculadora:
    def __init__(self):
        menu = Aplicacion()
        ventana = menu.ventana1
    #     ventana.configure(background="light pink")
        ventana.title("Calculadora ZAM")
    #     ventana.geometry("285x190")
        ventana.resizable(width=False, height=False)
        print("creando Calcu")
        self.calculo = menu.calculo
        self.datos = Entry(ventana, font=("Seven Segment",12), textvariable=self.calculo, justify="center")
        self.datos.grid(columnspan=15, ipadx=32)
        i = 0
        boton0 = Button(ventana, text=' 0 ', fg='black', bg='white',
                         command=lambda: digito(0), height=2, width=5)
        boton0.grid(row=5, column=0)
        self.lista_botones = [boton0]
        for fila in range(2,5):
            for columna in range(0,3):
                i += 1
                bot = Button(ventana, text=' ' + str(i) + ' ', fg='black', bg='white',
                               command=partial(self.digito, i), height=2, width=5)
                bot.grid(row=fila, column=columna)
                self.lista_botones.append(bot)
        digitos = ['+', '-', '*', '/']

        
         
        
        for fil in range(2,6):
            operador = Button(ventana, text=' ' + digitos[fil-2] + ' ', fg='black', bg='white',
                         command=partial(self.digito, digitos[fil-2]), height=2, width=5)
            operador.grid(row=fil, column=3)
            self.lista_botones.append(operador)
       
        resultado = Button(ventana, text=' = ', fg='black', bg='white',
                       command=self.igual, height=2, width=5)
        resultado.grid(row=5, column=2)
        limpiar = Button(ventana, text='borrar', fg='red', bg='white',
                       command=self.limpiar, height=2, width=5)
        limpiar.grid(row=5, column='1')
        self.lista_botones.append(resultado)
        self.lista_botones.append(limpiar)
        menu.recibirCalculadora(self.lista_botones, self.datos)
        ventana.mainloop()
    
    def digito(self, num):
        global boton
        boton = boton + str(num)
        self.calculo.set(boton)

    def igual(self):
        try:
            global boton
            total = str(eval(boton))
            self.calculo.set(total)
            boton = ""
        except:
            self.calculo.set(" error ")

    def limpiar(self):
        global boton
        boton = ""
        self.calculo.set("")
        
    def prueba(self, label):
        print(label)

    def ventanachica(self, label):
        ventana.geometry("640x480")
    
if __name__ == "__main__":
    calcu = Calculadora()

    


    