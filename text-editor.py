from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
from tkinter.simpledialog import askstring
import configs


class Editor_Texto:
    filename = None
    font_list = ['Arial', 'Times New Roman', 'Impact', 'Georgia', 'Comfortaa']
    def __init__(self, root):
        self.root = root
    def nuevoFile(self):
        global filename
        filename = 'untitled'
        text.delete(0.0, END)

    def guardaFile(self):
        global filename
        t = text.get(0.0, END)
        f = open(filename, 'w')
        f.write(t)
        f.close()
    def guardarFIlecomo(self):
        f = asksaveasfile(defaultextension= '.txt')
        t = text.get("1.0", "end-1c")
        try:
            f.write(t.rstrip())
        except:
            messagebox.showerror(title="Error!", message="No se pudo guardar el archivo de texto!")

    def abrirFile(self):
        global filename
        file = askopenfile(parent=root,title='Select a File')
        filename = file.name
        t = file.read()
        text.delete(0.0, END)
        text.insert(0.0, t)
        file.close()

    #write a function that lets me search for a word in the file
    def BuscarPalabra(self):
        word = askstring(title="buscar", prompt="Ingrese texto")
        text.tag_remove("match", 1.0, END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text.search(word, start_pos, END, nocase=True)
                if not start_pos: 
                    break
                end_pos = f"{start_pos} + {len(word)}c"
                text.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text.tag_config('match', foreground='black', background='white')
    
    def CambiarFuente(self):
        print(self.font_list)
        top = Toplevel() # use Toplevel() instead of Tk()
        top.geometry('300x100')
        Label(top, text='Select your value', font=20).pack(pady=10)
        variable = StringVar()
        combo = ttk.Combobox(top, textvariable=variable, values=self.font_list)
        combo.bind('<<ComboboxSelected>>', lambda _: top.destroy())
        combo.pack()
        top.grab_set()
        top.wait_window(top)  # wait for itself destroyed, so like a modal dialog
        text.configure(font=variable.get())
    
if __name__ == "__main__":
    root = Tk()
    editor = Editor_Texto(root)
    root.tk.call('source', 'forest-dark.tcl')
    ttk.Style().theme_use('forest-dark')
    configs.Configs(root)

    scroll = Scrollbar(root)
    scroll.pack(side=RIGHT, fill=Y)

    text = Text(root, width=400, height=400, yscrollcommand=scroll.set)
    text.configure(font = 'Helvetica')
    text.pack()
    scroll.config(command=text.yview)

    menubar = Menu(root)
    root.config(menu=menubar)

    filemenu = Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Archivo", menu=filemenu)
    menubar.add_command(label="Buscar", command=editor.BuscarPalabra)
    menubar.add_command(label="Cambiar fuente", command=editor.CambiarFuente)
    filemenu.add_command(label="Nuevo", command=editor.nuevoFile)
    filemenu.add_command(label="Abrir", command=editor.abrirFile)
    filemenu.add_command(label="Guardar", command=editor.guardaFile)
    filemenu.add_command(label="Guardar Como", command=editor.guardarFIlecomo)
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=root.quit)

    root.mainloop()