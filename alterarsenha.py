from lib import tk

import StartPage, informacoes

class alterarsenha(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lb2 = tk.Label(self, text="Nova Senha ")
        lb2.place(x=10, y=50)

        senha = tk.Entry(self, width = 30)
        senha.place(x=10, y=70)

        lb3 = tk.Label(self, text="Confirmar senha")
        lb3.place(x=10, y=100)

        confsenha = tk.Entry(self, width = 30)
        confsenha.place(x=10, y=120)

        btentrar2 = tk.Button(self, text="confirmar", command=lambda: controller.show_frame(informacoes))
        btentrar2.place(x=10, y=200) 
  
        btgravasenha2 = tk.Button(self, text="Voltar", command=lambda: controller.show_frame(StartPage))
        btgravasenha2.place(x=160, y=200)
        