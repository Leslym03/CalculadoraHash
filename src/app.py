from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
from function import *

root = Tk()
root.geometry('500x650') 
root.title("Calculadora de funciones Hash")
#root.resizable(0,0)
#root.configure(bg = 'beige')

#frame = Frame(root, width=450, height=500)
#frame.pack()
#frame.config(cursor="plus", bg="beige", bd=25)


entrada = Label(root, text="Ingrese el texto a cifrar", font=("Arial", 12))
entrada.grid(row=0, column=0, pady=10)

box_entrada = scrolledtext.ScrolledText(root,width=57,height=10)
box_entrada.grid(row=1,column=0, sticky=W+E, padx=10, pady=10)



tipo = Label(root, text="Seleccione el tipo de algoritmo", font=("Arial", 12))
tipo.grid(row=2, column=0, sticky=W, padx=30)

combo = Combobox(root)
combo['values']= ("MD4", "MD5", "SHA1", "SHA256", "HMAC")
combo.current(1) #set the selected item
combo.grid(row=3, column=0, sticky=W, padx=30, pady=10)

def cifrar():
    opcion = combo.get()
    print(opcion)
    texto = box_entrada.get("1.0", END)
    print(texto)

    if opcion == "MD5":
        resultado = MD5(texto)
    elif opcion == "MD4":
        resultado = MD4(texto)
    elif opcion == "SHA1":
        resultado = SHA1(texto)
    elif opcion == "SHA256":
        resultado = SHA256(texto)

    print(SHA1("hola"))
    print(resultado)



    salida = Label(root, text="Texto cifrado", font=("Arial", 12))
    salida.grid(row=5, column=0, pady=10)

    box_salida = scrolledtext.ScrolledText(root,width=57,height=10)
    box_salida.grid(row=6,column=0, sticky=W+E, padx=10, pady=10)

    box_salida.insert(INSERT,resultado)






btn = Button(root, text="Cifrar", command=cifrar)
btn.grid(row=3, column=0, sticky=E, padx=30, pady=10)



root.mainloop()