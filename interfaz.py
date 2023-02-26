import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x300")

cajauseretiqueta = tkinter.Label(ventana, text= "Usuario")
cajauseretiqueta.pack(side= tkinter.TOP)
cajausuario = tkinter.Entry(ventana, font= "Helvetica 14")
cajausuario.pack()


cajapassetiqueta = tkinter.Label(ventana, text= "Contraseña")
cajapassetiqueta.pack(side= tkinter.TOP)
cajacontrasena = tkinter.Entry(ventana, font= "Helvetica 14")
cajacontrasena.pack()



def Get_user():
    cajausuario.get()
    cajacontrasena.get()

boton = tkinter.Button(ventana, text= "Jugar", command= cajausuario and cajacontrasena)
boton.pack()

ventana.mainloop()
