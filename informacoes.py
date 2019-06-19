from lib import tk, conexao

import StartPage, alterarsenha 

class informacoes(tk.Frame):
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        conect = conexao.conexao()
        cursor = conect.Cursor

        cursor.execute("SELECT usuario FROM sessao WHERE id = (SELECT MAX(id) FROM sessao);")
        test = cursor.fetchone()

        cursor.execute("SELECT * FROM pessoa WHERE id = %s;", (test))
        test1 = cursor.fetchone()

        lb1 = tk.Label(self, text="Nome Completo")
        lb1.place(x=10, y=0)

        nome = tk.Label(self, text= test1[1])
        nome.place(x=10, y=20)

        lb2 = tk.Label(self, text="Senha")
        lb2.place(x=10, y=50)

        senha = tk.Label(self, text=test1[2])
        senha.place(x=10, y=70)

        lb4 = tk.Label(self, text="Email")
        lb4.place(x=10, y=100)

        email = tk.Label(self, text="Email Usuario")
        email.place(x=10, y=120)

        lb5 = tk.Label(self, text="Endereco")
        lb5.place(x=10, y=150)

        ende = tk.Label(self, text="Endereço Usuario")
        ende.place(x=10, y=170)

        lb6 = tk.Label(self, text="Cidade")
        lb6.place(x=10, y=200)

        cid = tk.Label(self, text="Cidade Usuario")
        cid.place(x=10, y=220)

        lb7 = tk.Label(self, text="Bairro")
        lb7.place(x=10, y=250)

        bair = tk.Label(self, text="Bairro Usuario")
        bair.place(x=10, y=270)

        lb8 = tk.Label(self, text="CEP")
        lb8.place(x=10, y=300)

        cep = tk.Label(self, text="CEP Usuario")
        cep.place(x=10, y=320)

        btentrar2 = tk.Button(self, text="Alterar Senha", command=lambda: controller.show_frame(alterarsenha))
        btentrar2.place(x=10, y=360) 

        btgravasenha2 = tk.Button(self, text="Voltar", command=lambda: controller.show_frame(StartPage))
        btgravasenha2.place(x=160, y=360)

        lb15 = tk.Label(self, text="")
        lb15.place(x=10, y=450)