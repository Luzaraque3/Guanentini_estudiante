from tkinter import *
from tkinter import messagebox
from tkinter import messagebox, ttk

# abrir toplevel centigrados
def edad():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Edad")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("300x200")
    toplevel_centigrados.config(bg="white")

# abrir toplevel centigrados
def Libros():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Centigrados")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("300x200")
    toplevel_centigrados.config(bg="white")
# Mujer
def Mujer():
    messagebox.showinfo("Estudiante", "Eres mujer confirma")

# Hombre
def Hombre():
    messagebox.showinfo("Estudiante", "Eres hombre confirma")

# Borrar
def borrar():
    messagebox.showinfo("Nombre = ", "El nombre del estudiante sera borrado")
# salir
def salir():
    messagebox.showinfo("Informacion del Estudiante", "La app se va a cerrar")
    ventana_principal.destroy()

#----------------------------------
# Ventana principal
#----------------------------------
# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Datos del estudiante")

# tamaño de la ventana
ventana_principal.geometry("600x600")

# ventana
ventana_principal.title("Angelica Araque")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="coral")

#--------------------------------
# frame entrada datos
#--------------------------------
Frame_entrada = Frame(ventana_principal)
Frame_entrada.config(bg="white", width=580, height=580)
Frame_entrada.place(x=10, y=10)

#-------------------------
# variables globales
#-------------------------
x = StringVar()
y = StringVar()

# titulo de la app
titulo = Label(Frame_entrada, text="Datos del Estudiante")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.place(x=220,y=10)

# etiqueta para valor de x
Nombre = Label(Frame_entrada, text= "Nombre= ")
Nombre.config(bg = "white", fg ="green", font=("Helventica", 18))
Nombre.place(x=200, y=60)
# caja de texto para valor x
Nombre =Entry(Frame_entrada, textvariable=x)
Nombre.config(bg="white", fg="blue", font=("Times New Roman",18), widt=15)
Nombre.focus_set()
Nombre.place(x=320, y=60)

# logo de la app
logo1 = PhotoImage(file="img/colegio.png")
lb_logo1 = Label(Frame_entrada, image=logo1, bg="white")
lb_logo1.place(x=0,y=40)

#-----------------------
# Edad del estudiante
#-----------------------
Edad = Label(Frame_entrada, text= "Edad= ")
Edad.config(bg = "white", fg ="green", font=("Helventica", 17))
Edad.place(x=200, y=110)

combo = ttk.Combobox(Frame_entrada,state="readonly")
combo.place(x=280, y=120)
combo["values"] = ("12", "13","14", "15", "16", "17", "18")
combo.current(0)

# etiqueta para valor de x
grado = Label(Frame_entrada, text= "Grado= ")
grado.config(bg = "white", fg ="green", font=("Helventica", 18))
grado.place(x=200, y=150)

# caja de texto para valor x
grado =Entry(Frame_entrada, textvariable=y)
grado.config(bg="white", fg="blue", font=("Times New Roman",18), widt=13)
grado.focus_set()
grado.place(x=310, y=150)

logo2 = PhotoImage(file="img/libro.png")
lb_logo2 = Label(Frame_entrada, image=logo2, bg="white")
lb_logo2.place(x=70,y=270)
bt_piedra = Button(Frame_entrada,image=img_libro.png, command=Libros)
bt_piedra.place(x=45, y=10, width=100, height=100)


#---------------------------
# barra menu
#---------------------------
barra_menu = Menu()
ventana_principal.config(menu=barra_menu)

menu_convertir = Menu(tearoff=0)
menu_convertir.add_command(label="Menu", command=Menu)
menu_convertir.add_separator()
menu_convertir.add_command(label="Mujer", command=Mujer)
menu_convertir.add_command(label="Hombre", command=Hombre)

menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", command=salir)

menu_borrar = Menu(tearoff=0)
menu_borrar.add_command(label="Borrar", command=borrar)

barra_menu.add_cascade(label="Menú", menu=menu_convertir)
barra_menu.add_cascade(label="Salir", menu=menu_salir)

barra_menu.add_cascade(label="Borrar", menu=menu_borrar)

# logo de la app


#rum 
ventana_principal.mainloop()