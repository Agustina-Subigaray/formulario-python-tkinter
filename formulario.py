import tkinter as tk

# LADO CONSOLA

personas = []  # Lista para guardar los datos como diccionarios

def guardar():
    global personas  # Accedemos a la lista global

    nombre = caja_nombre.get()
    email = caja_email.get()
    edad = caja_edad.get()

    datos = {"nombre": nombre, "email": email, "edad": edad}
    personas.append(datos)  # Agregamos el diccionario a la lista

    print("Persona guardada:", datos)  # Mostramos en consola
    limpiar_campos()

def limpiar_campos():
    caja_nombre.delete(0, tk.END)
    caja_email.delete(0, tk.END)
    caja_edad.delete(0, tk.END)

# LADO GRÁFICO

ventana = tk.Tk()
ventana.title("Formulario de inscripción")
ventana.config(width=400, height=300)
ventana.resizable(False, False)

# Campo nombre
tk.Label(text="Nombre").place(x=20, y=30)
caja_nombre = tk.Entry()
caja_nombre.place(x=120, y=30, width=180, height=25)

# Campo edad
tk.Label(text="Edad").place(x=20, y=80)
caja_edad = tk.Entry()
caja_edad.place(x=120, y=80, width=180, height=25)

# Campo email
tk.Label(text="Email").place(x=20, y=130)
caja_email = tk.Entry()
caja_email.place(x=120, y=130, width=180, height=25)

# Botón
tk.Button(text="Guardar", command=guardar).place(x=140, y=200, width=100, height=40)

ventana.mainloop()
