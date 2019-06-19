from lib import tk, LARGE_FONT

from url import StartPage

class Sobre(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Game Maniacos",font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        label1 = tk.Label(self, text="SOBRE", font=LARGE_FONT)
        label1.pack()

        label2 = tk.Label(self, text="Objetivo: Criar 1 programa que" )
        label2.pack()

        label3 = tk.Label(self, text="consiga facilitar a busca" )
        label3.pack()

        label4 = tk.Label(self, text="por informações relacionadas a jogos" )
        label4.pack()

        label5 = tk.Label(self)
        label5.pack(pady=5)

        label6 = tk.Label(self, text="Autor: Gutembergues Gomes de Araujo" )
        label6.pack()

        label7 = tk.Label(self, text="RA:2840481623018")
        label7.pack()

        button1 = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10)
