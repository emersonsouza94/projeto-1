from lib import tk

import StartPage

class bt_cadastro(tk.Frame):
    
    def bt_sair():
        cadastro1.destroy()

    def bt_salvar12(val):
        
        
        if ((senha.get() and confsenha.get()) != ("") ):
            lb15["text"] = "Senha não igual"
            if((senha.get())== confsenha.get()):
                lb15["text"] = "Cadastro efetuado"
                try:

                    Conect = conexao.conexao()
                    cursor = Conect.Cursor
                    connection = Conect.connection

                    cursor.execute("SELECT MAX(id) FROM pessoa;")
                    test = cursor.fetchone()
                    test1 = test[0]
                    if test1 == None:
                        test1 = 1
                    else:
                        test1 += 1

                    cursor.execute("INSERT INTO pessoa (id, nome, senha) VALUES (%s, %s,%s)",(test1, nome.get(), senha.get()))
                    connection.commit()

    
                    cursor.execute("SELECT * FROM pessoa;")
                    test = cursor.fetchall()
                    print(test)
    
                except (Exception, conexao.psycopg2.Error) as error :
                    print ("Error while connecting to PostgreSQL", error)
                finally:
                    #closing database connection.
                        if(connection):
                            Conect.FecharConexao()
                            print("PostgreSQL connection is closed")

                            
                            time.sleep(2)
                            cadastro1.destroy()
                

                
                            
        else:
            lb15["text"] = "Preencha corretamente"
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        cadastro1 = tk.Tk()
    cadastro1.title("Cadastro")

        lb1 = tk.Label(cadastro1, text="Nome Completo")
        lb1.place(x=10, y=0)

        nome = tk.Entry(cadastro1, width = 49)
        nome.place(x=10, y=20)

        lb2 = tk.Label(cadastro1, text="Senha")
        lb2.place(x=10, y=50)

        senha = tk.Entry(cadastro1, width = 49)
        senha.place(x=10, y=70)

        lb3 = tk.Label(cadastro1, text="Confirmar senha")
        lb3.place(x=10, y=100)

        confsenha = tk.Entry(cadastro1, width = 49)
        confsenha.place(x=10, y=120)

        lb4 = tk.Label(cadastro1, text="Email")
        lb4.place(x=10, y=150)

        email = tk.Entry(cadastro1, width = 49)
        email.place(x=10, y=170)

        lb5 = tk.Label(cadastro1, text="Endereco")
        lb5.place(x=10, y=200)

        ende = tk.Entry(cadastro1, width = 49)
        ende.place(x=10, y=220)

        lb6 = tk.Label(cadastro1, text="Cidade")
        lb6.place(x=10, y=250)

        cid = tk.Entry(cadastro1, width = 49)
        cid.place(x=10, y=270)

        lb7 = tk.Label(cadastro1, text="Bairro")
        lb7.place(x=10, y=300)

        bair = tk.Entry(cadastro1, width = 49)
        bair.place(x=10, y=320)

        lb8 = tk.Label(cadastro1, text="CEP")
        lb8.place(x=10, y=350)

        cep = tk.Entry(cadastro1, width = 49)
        cep.place(x=10, y=370)

        btentrar2 = tk.Button(cadastro1, text="Salvar", width=20)
        btentrar2.place(x=10, y=400) 
        btentrar2["command"] = partial(bt_salvar12, btentrar2)

                
        btgravasenha2 = tk.Button(cadastro1, text="Sair", width=20, command=bt_sair)
        btgravasenha2.place(x=160, y=400)

        lb15 = tk.Label(cadastro1, text="")
        lb15.place(x=10, y=450)

        cadastro1.geometry("370x500+100+100")
        cadastro1.mainloop()