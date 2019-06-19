import psycopg2

class conexao():

    def getConnection(self):
        return self.connection
     
    def ConectarPadrao(self):
        try:
            self.connection = psycopg2.connect(  user = "postgres",
                                            password = "12345",
                                            host = "127.0.0.1",
                                            port = "5432", #no PC 5432 Notebok 5433
                                            database = "postgres")

            self.Cursor = self.connection.cursor()
            
        except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PostgreSQL", error)
                       

    def getCursor(self):
        if self.Cursor == None:
            self.ConectarPadrao()
        return self.Cursor
    def Cursor_Execute(self, query):
        try:
            self.Cursor = self.getCursor()
            self.Cursor.execute(query)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PostgreSQL", error)
    def Cursor_Return(self, query):
        try:
            self.Cursor = self.getCursor()
            self.Cursor.execute(query)
            retorno = self.Cursor.fetchone()
            
            return retorno
        except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PostgreSQL", error)

    def __init__(self):
        self.ConectarPadrao()

    def FecharCursor(self):
        if(self.Cursor.close() != None):
            self.Cursor.close()

    def FecharConexao(self):
        if(self.connection):
            self.FecharCursor()
            self.connection.close()
            print("PostgreSQL connection is closed")

