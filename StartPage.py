from lib import tk, LARGE_FONT

from url import SeaofBTCapp, Jogos, Consoles, Produtoras, Acessorio, informacoes, Sobre, alterarsenha

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Game Maniacos", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Jogos", width=20,
                            command=lambda: controller.show_frame(Jogos))
        button.pack(pady=2,padx=10)

        button2 = tk.Button(self, text="Consoles", width=20,
                            command=lambda: controller.show_frame(Consoles))
        button2.pack(pady=2,padx=10)

        button3 = tk.Button(self, text="Produtoras", width=20,
                            command=lambda: controller.show_frame(Produtoras))
        button3.pack(pady=2,padx=10)

        button4 = tk.Button(self, text="Acessorio", width=20,
                            command=lambda: controller.show_frame(Acessorio))
        button4.pack(pady=2,padx=10)

        button5 = tk.Button(self, text="Informações", width=20,
                            command= lambda: controller.show_frame(informacoes))
        button5.pack(pady=2,padx=10)

        button6 = tk.Button(self, text="Sobre", width=5,
                            command=lambda: controller.show_frame(Sobre))
        button6.pack(pady=2,padx=10)

            

        