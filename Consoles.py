from lib import tk

import StartPage

class Consoles(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        prodlist=['Sony','Nintendo','Sega','MicroSoft','Naught Dog','Capcom','Squase Enix', 'Konami']
        consolist=['Nintendo', 'Nintendo 64', 'PlayStation', 'PlayStation 2', 'PlayStation 3','PlayStation 4',
                        'Xbox','Xbox 360', 'Xbox One', 'PC']
        

        label = tk.Label(self, text="Produtora")
        label.place(x=10,y=10)

        spinbox = tk.Spinbox (self, fg="blue", font=12, values=prodlist)
        spinbox.place(x=10,y=30)


        label1 = tk.Label(self, text="Console")
        label1.place(x=10,y=50)

        spinbox1 = tk.Spinbox (self, fg="blue", font=12, values=consolist)
        spinbox1.place(x=10,y=70)

        label3 = tk.Label(self, text="Tipo de Pesquisa")
        label3.place(x=10,y=110)

        #radio= tk.Radiobutton(self, text="Simples",value = 1 ,variable = 'gr1').place(x=10,y=130)
        #radio1= tk.Radiobutton(self, text="Completa",value = 2 ,variable = 'gr1').place(x=80,y=130)

        
        CheckVar1 = tk.IntVar()
        C1 = tk.Checkbutton(self, text = "Mostrar Todos os Consoles", variable = CheckVar1,
                            onvalue = 1, offvalue = 0) 
                        
        C1.place(x=10,y=160)
        


        button1 = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=10,y=200)

        button2 = tk.Button(self, text="Procurar",
                            command=lambda: controller.show_frame(StartPage))
        button2.place(x=70,y=200)
