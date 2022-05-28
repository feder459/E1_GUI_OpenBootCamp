from tkinter import*

#Funcion resetear
def reset():
    selec.set(None)
#Defino una ventana con Tk, le doy geometría y un título a la ventana
ventana=Tk()
ventana.geometry("700x300+0+0")
ventana.title("Ejemplo de Radiobutton")
#Creo una variable para que las opciones aparezcan deseleccionadas de entrada
selec=StringVar()
selec.set(None)

#Colocamos una instrucción para el usuario
etiqueta=Label(ventana, text="Elija su sexo").place(x=100, y=70)

#Creamos los RadioButton(se llama así porque en las radios viejas se usaba
#un botón para seleccionar una determinada frecuencia de radio
rdBMasculino=Radiobutton(ventana, text="Masculino", value=1, variable=selec).place(x=100, y=100)
rdBFemenino=Radiobutton(ventana, text="Femenino", value=2, variable=selec).place(x=100, y=120)

#Hago un boton de reinicio
Button(ventana, text="Reiniciar", command=reset).pack()

ventana.mainloop()