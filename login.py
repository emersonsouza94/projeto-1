from lib import tk, LARGE_FONT, time, partial, conexao

# import SeaofBTCapp, StartPage, Jogos, Consoles, Produtoras, Acessorio, informacoes, Sobre, alterarsenha
from Trabalho_Python import SeaofBTCapp

class sessao():

    def setidset(self, idset):
        self.idset = idset

    def getidset(self):
        return self.idset

    def __init__(self, idset):
        self.idset = idset


#Tela de Login
#===============================================================
jpas = tk.Tk()
jpas.title("Login")





def main ():
    def bt_entrar(val2):

        try:
            conect = conexao.conexao()
            
            connection = conect.connection

            cursor = connection.cursor()

            logintest = login.get()
            senhatest = confpas.get()
            #print(teste)

            cursor.execute(f"SELECT id FROM pessoa WHERE nome = '{logintest}' and senha = '{senhatest}' ;")
            test = cursor.fetchone()

            

            if test != None:
                time.sleep(2)
                jpas.destroy()
                app = SeaofBTCapp()
                app.title("Game Maniacos")
                app.geometry("300x400+100+100")

               # cursor.execute("INSERT INTO sessao (id, usuario) VALUES (nextval('s_idsessao'),%s)",(test))
                #connection.commit()

                app.mainloop()
    
        except (Exception, conexao.psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")
    
    

    lb1 = tk.Label(jpas, text="Login")
    lb1.place(x=10, y=0)

    login = tk.Entry(jpas, width = 49)
    login.place(x=10, y=20)


    lb2 = tk.Label(jpas, text="Senha")
    lb2.place(x=10, y=50)

    confpas = tk.Entry(jpas, width = 49)
    confpas.place(x=10, y=70)

    btentrar = tk.Button(jpas, text="ENTRAR", width=20)
    btentrar.place(x=10, y=90)
    btentrar["command"] = partial(bt_entrar, btentrar)


    btgravasenha = tk.Button(jpas, text="Cadastro", width=20, command=bt_cadastro)
    btgravasenha.place(x=160, y=90)

    jpas.geometry("350x150+100+100")
    jpas.mainloop()

main()