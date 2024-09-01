from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
import configs

filename = None
def nuevoFile():
    global filename
    filename = 'untitled'
    text.delete(0.0, END)

def guardaFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()
def guardarFIlecomo():
    f = asksaveasfile(defaultextension= '.txt')
    t = text.get("1.0", "end-1c")
    try:
        f.write(t.rstrip())
    except:
        messagebox.showerror(title="Error!", message="No se pudo guardar el archivo de texto!")

def abrirFile():
    global filename
    file = askopenfile(parent=root,title='Select a File')
    filename = file.name
    t = file.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    file.close()

root = Tk()
root.tk.call('source', 'Forest-ttk-theme/forest-dark.tcl')
ttk.Style().theme_use('forest-dark')
configs.Configs(root)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="Nuevo", command=nuevoFile)
filemenu.add_command(label="Abrir", command=abrirFile)
filemenu.add_command(label="Guardar", command=guardaFile)
filemenu.add_command(label="Guardar Como", command=guardarFIlecomo)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)

root.config(menu=menubar)
root.mainloop()