import tkinter  as tk
from tkinter import messagebox as msg
import time
import sys
from functools import partial
import psycopg2
from conexao import conexao

import os

import json

from uuid import getnode as get_mac



LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Jogos, Consoles, Produtoras, Acessorio, informacoes, Sobre, alterarsenha):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def Logout(self):
        conect = conexao()
        mac = get_mac()
        conect.Cursor_Execute(f"Delete from sessao where mac_adress = {mac}")
        conect.FecharConexao()
        
        
        self.destroy()

        main()
        
            

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

        button7 = tk.Button(self, text="Logout", width=5,
                            command=lambda: controller.Logout())
        button7.pack(pady=2,padx=10)
        

          


class Jogos(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        prodlist=['Sony','Nintendo','Sega','MicroSoft','Naught Dog','Capcom','Squase Enix', 'Konami']
        consolist=['Nintendo', 'Nintendo 64', 'PlayStation', 'PlayStation 2', 'PlayStation 3','PlayStation 4',
                        'Xbox','Xbox 360', 'Xbox One', 'PC']
        joglist=['Mario', 'Sonic', 'Zelda','The King of Fighters', 'Dnkey Kong', 'Devil May Cry','The Last of Us',
                        'The Whitcher', 'Uncharted', 'Mortal Kombat', 'Whatch Dogs']

        label = tk.Label(self, text="Produtora")
        label.place(x=10,y=10)

        spinbox = tk.Spinbox (self, fg="blue", font=12, values=prodlist)
        spinbox.place(x=10,y=30)


        label1 = tk.Label(self, text="Console")
        label1.place(x=10,y=50)

        spinbox1 = tk.Spinbox (self, fg="blue", font=12, values=consolist)
        spinbox1.place(x=10,y=70)


        label2 = tk.Label(self, text="Jogos")
        label2.place(x=10,y=90)

        spinbox2 = tk.Spinbox (self, fg="blue", font=12, values=joglist)
        spinbox2.place(x=10,y=110)


        label3 = tk.Label(self, text="Tipo de Pesquisa")
        label3.place(x=10,y=150)

        radio = tk.Radiobutton(self, text="Simples",value = 1 ,variable = 'gr1')
        radio.place(x=10,y=170)
        radio1= tk.Radiobutton(self, text="Completa",value = 2 ,variable = 'gr1')
        radio1.place(x=80,y=170)


        button1 = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=10,y=200)

        button2 = tk.Button(self, text="Procurar",
                            command=lambda: controller.show_frame(StartPage))
        button2.place(x=70,y=200)


      

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

        radio= tk.Radiobutton(self, text="Simples",value = 1 ,variable = 'gr1')
        radio.place(x=10,y=130)
        radio1= tk.Radiobutton(self, text="Completa",value = 2 ,variable = 'gr1')
        radio1.place(x=80,y=130)

        
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



class Produtoras(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        prodlist=['Sony','Nintendo','Sega','MicroSoft','Naught Dog','Capcom','Squase Enix', 'Konami']
        
        label = tk.Label(self, text="Produtora")
        label.place(x=10,y=10)

        spinbox = tk.Spinbox (self, fg="blue", font=12, values=prodlist)
        spinbox.place(x=10,y=30)


        label3 = tk.Label(self, text="Tipo de Pesquisa")
        label3.place(x=10,y=60)

        radio= tk.Radiobutton(self, text="Simples",value = 1 ,variable = 'gr1')
        radio.place(x=10,y=80)
        radio1= tk.Radiobutton(self, text="Completa",value = 2 ,variable = 'gr1')
        radio1.place(x=80,y=80)

        
        CheckVar1 = tk.IntVar()
        C1 = tk.Checkbutton(self, text = "Mostrar Todos os Consoles", variable = CheckVar1,
                            onvalue = 1, offvalue = 0)                
        C1.place(x=10,y=120)
        

        button1 = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=10,y=150)

        button2 = tk.Button(self, text="Procurar",
                            command=lambda: controller.show_frame(StartPage))
        button2.place(x=70,y=150)


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

        radio= tk.Radiobutton(self, text="Simples",value = 1 ,variable = 'gr1')
        radio.place(x=10,y=120)
        radio1= tk.Radiobutton(self, text="Completa", value = 0 ,variable = 'gr1')
        radio1.place(x=80,y=120)

        
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

        label8 = tk.Label(self, text="Autor: Emerson Souza da Silva" )
        label8.pack()

        label9 = tk.Label(self, text="RA:2840481623012")
        label9.pack()

        button1 = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10)

class informacoes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        

        try:
            conect = conexao()
            mac = get_mac()
            
            user = conect.Cursor_Return(f"SELECT *  FROM pessoa  WHERE id = ( SELECT max(usuario) FROM sessao where mac_adress = {mac});")
            

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
                if(conect.connection):
                   conect.FecharConexao()

        lb1 = tk.Label(self, text="Nome Completo")
        lb1.place(x=10, y=0)

        nome = tk.Label(self, text= user[1])
        nome.place(x=10, y=20)

        lb2 = tk.Label(self, text="Senha")
        lb2.place(x=10, y=50)

        senha = tk.Label(self, text='[Senha oculta]')
        senha.place(x=10, y=70)
        

        lb4 = tk.Label(self, text="Email")
        lb4.place(x=10, y=100)

        email = tk.Label(self, text=user[3])
        email.place(x=10, y=120)

        lb5 = tk.Label(self, text="Endereco")
        lb5.place(x=10, y=150)

        ende = tk.Label(self, text=user[4])
        ende.place(x=10, y=170)

        lb6 = tk.Label(self, text="Cidade")
        lb6.place(x=10, y=200)

        cid = tk.Label(self, text=user[5])
        cid.place(x=10, y=220)

        lb7 = tk.Label(self, text="Bairro")
        lb7.place(x=10, y=250)

        bair = tk.Label(self, text=user[6])
        bair.place(x=10, y=270)

        lb8 = tk.Label(self, text="CEP")
        lb8.place(x=10, y=300)
        
        cep = tk.Label(self, text=user[7])
        cep.place(x=10, y=320)

        btentrar2 = tk.Button(self, text="Alterar Senha", command=lambda: controller.show_frame(alterarsenha))
        btentrar2.place(x=10, y=360) 
  
        btgravasenha2 = tk.Button(self, text="Voltar", command=lambda: controller.show_frame(StartPage))
        btgravasenha2.place(x=110, y=360)

        btgexportarjson = tk.Button(self, text="Exporta Usuario .JSON", command=lambda: self.exportarjson())
        btgexportarjson.place(x=170, y=360)

        lb15 = tk.Label(self, text="")
        lb15.place(x=10, y=450)

    def exportarjson(self):
        sessa = sessao()
        user = sessa.getuser()

        data = dict({"ID":"","NOME":"","SENHA":"","EMAIL":"","ENDERECO":"", "CIDADE":"", "BAIRRO":"","CEP":""})

        data["ID"]       = user[0]
        data["NOME"]     = user[1]
        data["SENHA"]    = user[2]
        data["EMAIL"]    = user[3]
        data["ENDERECO"] = user[4]
        data["CIDADE"]   = user[5]
        data["BAIRRO"]   = user[6]
        data["CEP"]      = user[7]

        f = open(f"usuario_{user[1]}.json","w")
        json.dump(data, f, sort_keys=False, indent=4)
        f.close()
        msg.showinfo('Sucesso', f"o arquivo usuario_{user[1]}.json foi gerado com sucesso")

       
    
class alterarsenha(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lb3 = tk.Label(self, text="Senha Atual ")
        lb3.place(x=10, y=50)
        self.count = 0

        self.senhaatual = tk.Entry(self, width = 30)
        self.senhaatual.place(x=10, y=70)
        self.senhaatual.config(show="*")

        btvalidarsenha = tk.Button(self, text="Validar", command=lambda: self.validasenhaatual())
        btvalidarsenha.place(x=190, y=65)

        lb2 = tk.Label(self, text="Nova Senha ")
        lb2.place(x=10, y=100)

        self.senha = tk.Entry(self, width = 30)
        self.senha.place(x=10, y=120)
        self.senha.config(show="*")
        self.senha.configure(state='disabled')

        lb3 = tk.Label(self, text="Confirmar senha")
        lb3.place(x=10, y=150)

        self.confsenha = tk.Entry(self, width = 30)
        self.confsenha.place(x=10, y=170)
        self.confsenha.config(show="*")
        self.confsenha.configure(state='disabled')
        

        self.btentrar2 = tk.Button(self, text="confirmar", command=lambda: self.validarsenhaigual(controller))
        self.btentrar2.place(x=10, y=210)
        self.btentrar2.configure(state='disabled' )
  
        btgravasenha2 = tk.Button(self, text="Voltar", command=lambda: controller.show_frame(informacoes))
        btgravasenha2.place(x=160, y=210)
    
    def updatepassword(self):
        try:
            sessa = sessao()
            user = sessa.getuser()

            conect = conexao()
            conect.Cursor.execute("update pessoa set senha = %s where id = %s",(self.senha.get(),user[0]))
            conect.connection.commit()

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
                if(conect.connection):
                   conect.FecharConexao()

    def validarsenhaigual(self, controller):
        if self.senha.get() == self.confsenha.get():
            self.updatepassword()
            msg.showinfo('Sucesso','Senha atualizada com sucesso!')
            self.senhaatual.delete(0,'end')
            
            self.senha.delete(0, 'end')
            self.senha.configure(state='disabled')
            self.confsenha.delete(0,'end')
            self.confsenha.configure(state='disabled')
            self.btentrar2.configure(state ='disabled')
            self.count = 0
            controller.show_frame(informacoes)

        else:
            msg.showinfo('Atenção', 'Digite a mesma senha para continuar.')

    def getcount(self):
        return self.count

    def setcount(self,count):
        self.count = count

    def validasenhaatual(self):
        self.count += 1
        if self.count < 3:
            sessa = sessao()
            user = sessa.getuser()
            if self.senhaatual.get() == user[2]:
                self.confsenha.configure(state='normal')
                self.senha.configure(state='normal')
                self.btentrar2.configure(state='normal')
                
            else:
                msg.showwarning('Atenção', 'senha não confere com atual!')
                
        else:
            msg.showwarning('Atenção', 'Numero de tentativa acabou, refaça seu login!')
            self.destroy()

class sessao:

    def __init__(self):

        try:
            conect = conexao()
            self.mac = get_mac()
            self.user = conect.Cursor_Return(f"SELECT *  FROM pessoa  WHERE id = ( SELECT max(usuario) FROM sessao where mac_adress = {self.mac});")
            
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
                if(conect.connection):
                    conect.FecharConexao()
    def getuser(self):
        return self.user

    def getiduser(self):
        return self.user[0]    
            
        
#Tela de Login
#===============================================================



def bt_cadastro():
    cadastro1 = tk.Tk()
    cadastro1.title("Cadastro")

    def bt_sair():
        cadastro1.destroy()

    """def importarjson(self):
        from tkFileDialog import askopenfilename


        
        f = open("arduino_SENSOR.json","r")
        dadoss = json.load(f)"""

    def bt_salvar12(val):
              
        if ((senha.get() and confsenha.get()) != ("") ):
            lb15["text"] = "Senha não igual"
            if((senha.get())== confsenha.get()):
                lb15["text"] = "Cadastro efetuado"
                try:
                    conect = conexao()

                    test = conect.Cursor_Return("SELECT MAX(id) FROM pessoa;")
                    test1, = test
                    if test1 == None:
                        test1 = 1
                    else:
                        test1 += 1

                    conect.Cursor.execute("INSERT INTO pessoa (id, nome, senha, email, endereco, cidade, bairro, cep) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)",(str(test1), nome.get(), senha.get(), email.get(), ende.get(), cid.get(), bair.get(), cep.get()))
                    conect.connection.commit()
                    #conect.Cursor_Execute(f"INSERT INTO pessoa (id, nome, senha, endereco, cidade, bairro, cep) VALUES ({test1}, {nome.get()}, {senha.get()}, {ende.get()}, {cid.get()}, {bair.get()}, {cep.get()})") 
   
                except (Exception, psycopg2.Error) as error :
                    print ("Error while connecting to PostgreSQL", error)
                finally:
                    #closing database connection.
                        if(conect.connection):
                            conect.FecharConexao()
                            print("PostgreSQL connection is closed")

                            
                            time.sleep(2)
                            cadastro1.destroy()
         
        else:
            lb15["text"] = "Preencha corretamente"
    
    


    lb1 = tk.Label(cadastro1, text="Nome Completo")
    lb1.place(x=10, y=0)

    nome = tk.Entry(cadastro1, width = 49)
    nome.place(x=10, y=20)

    lb2 = tk.Label(cadastro1, text="Senha")
    lb2.place(x=10, y=50)

    senha = tk.Entry(cadastro1, width = 49)
    senha.place(x=10, y=70)
    senha.config(show="*")

    lb3 = tk.Label(cadastro1, text="Confirmar senha")
    lb3.place(x=10, y=100)

    confsenha = tk.Entry(cadastro1, width = 49)
    confsenha.place(x=10, y=120)
    confsenha.config(show="*")
    

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

    cep = tk.Entry(cadastro1, width = 14)
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

    


def main ():
    jpas = tk.Tk()
    jpas.title("Login")

    
    def bt_entrar(val2):

        try:
            
            conect = conexao()

            logintest = login.get()
            senhatest = confpas.get()
            #print(teste)

            validacao = conect.Cursor_Return(f"SELECT id FROM pessoa WHERE nome = '{logintest}' and senha = '{senhatest}' ;")
                        

            if validacao != None:
                mac = get_mac()
                cursos = conect.Cursor
                teste = f"INSERT INTO sessao (id, usuario, mac_adress) VALUES (nextval('s_idsessao'), {validacao[0]}, {mac})"
                cursos.execute(teste)
                conect.connection.commit()

                #time.sleep(2)
                jpas.destroy()
                app = SeaofBTCapp()
                app.title("Game Maniacos")
                app.geometry("300x400+100+100")

                

                app.mainloop()
            else:
                msg.showerror('Erro','Não foi encontrar este usuário/senha')
                login.delete(0,'end')
                login.focus()
                confpas.delete(0,'end')

    
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
                if(conect.connection):
                    conect.FecharConexao()
                    print("PostgreSQL connection is closed")
    
    

    lb1 = tk.Label(jpas, text="Login")
    lb1.place(x=10, y=0)

    login = tk.Entry(jpas, width = 49)
    login.place(x=10, y=20)
    login.focus()


    lb2 = tk.Label(jpas, text="Senha")
    lb2.place(x=10, y=50)

    confpas = tk.Entry(jpas, width = 49)
    confpas.place(x=10, y=70)
    confpas.config(show="*")
    confpas.bind("<Return>",bt_entrar)

    btentrar = tk.Button(jpas, text="ENTRAR", width=20)
    btentrar.place(x=10, y=90)
    btentrar["command"] = partial(bt_entrar, btentrar)
    


    btgravasenha = tk.Button(jpas, text="Cadastro", width=20, command=bt_cadastro)
    btgravasenha.place(x=160, y=90)

    jpas.geometry("350x150+100+100")
    

    #def valida_sessao(self):
    try:
        conect = conexao()
        mac = get_mac()
        
        user = conect.Cursor_Return(f"SELECT *  FROM pessoa  WHERE id = ( SELECT max(usuario) FROM sessao where mac_adress = {mac});")
        
        if user != None:
            jpas.destroy()

            app = SeaofBTCapp()
            app.title("Game Maniacos")
            app.geometry("300x400+100+100")
            app.mainloop()
            
        else:
            jpas.mainloop()

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(conect.connection):
                conect.FecharConexao()
    


main()