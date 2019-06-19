
from lib import tk

import StartPage

class Acessorio(tk.Frame):
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        prodlist=['Sony','Nintendo','Sega','MicroSoft','Naught Dog','Capcom','Squase Enix', 'Konami']
        aceslist=['Guitarra','Tambor', 'Volante', 'PSMove', 'Kinect', 'Luva']
        
        label = tk.Label(self, text="Produtora")
        label.place(x=10,y=10)

        spinbox = tk.Spinbox (self, fg="blue", font=12, values=prodlist)
        spinbox.place(x=10,y=30)

        label1 = tk.Label(self, text="Produtora")
        label1.place(x=10,y=50)

        spinbox1= tk.Spinbox (self, fg="blue", font=12, values=aceslist)
        spinbox1.place(x=10,y=70)


        label3 = tk.Label(self, text="Tipo de Pesquisa")
        label3.place(x=10,y=100)

        #radio= tk.Radiobutton(self, text="Simples",value = 1 ,variable = 'gr1').place(x=10,y=120)
        #radio1= tk.Radiobutton(self, text="Completa", value = 0 ,variable = 'gr1').place(x=80,y=120)

        
        CheckVar1 = tk.IntVar()
        C1 = tk.Checkbutton(self, text = "Mostrar Todos os Consoles", variable = CheckVar1,
                            onvalue = 1, offvalue = 0)                
        C1.place(x=10,y=150)
        

        button1 = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=10,y=180)

        button2 = tk.Button(self, text="Procurar",
                            command=lambda: controller.show_frame(StartPage))
        button2.place(x=70,y=180)
