class createTable:

    def __init__(self):
        self.keys_values = dict()
        self.pkk =         dict()
        self.nameDb = input('Por favor digite el nombre de la base de datos');
        self.nameTable = input('Por favor digite el nombre de la tabla');


    def build_table(self):
        print("Crear tabla, primero debe facilitar el nombre del campo y el tipo de dato del mismo!")
        self.isPk = input("Esta tabla tiene llave primaria responda si o no").lower()
        if(self.isPk == "si"):
            print("por defecto este programa convierte el primer campo que ingrese como llave primaria")
            self.cantidad_campos = int (input("Digite la cantidad de campos de la bd"))
            self.i=0
            while self.i <=self.cantidad_campos:
                self.clave = input("por favor digite el nombre del campo ")
                self.valor = input("por favor digite el valor del campo ")
                if(self.i == 0):
                    self.uppk = self.valor + "  PRIMARY KEY"
                    self.pkk.setdefault(self.clave,self.uppk);
                    self.keys_values.update(self.pkk)
                else:
                    self.keys_values.setdefault(self.clave,self.valor)
                self.i +=1
        elif (self.isPk == "no"):
             try:
                    self.cantidad_campos = int (input("Digite la cantidad de campos de la bd"))
                    self.i=0
                    while self.i <=self.cantidad_campos:
                        self.clave = input("por favor digite el nombre del campo ")
                        self.valor = input("por favor digite el valor del campo ")
                        self.keys_values.setdefault(self.clave,self.valor)
                        self.i +=1
             except ValueError:
                print ("por favor digite un número")
             except:
                print ("Por favor verifique que esta digitando un número")


    def show_dict(self):
        for k,v in self.keys_values.items():
            print (k,v)

    def send_table(self):
        import sqlite3
        # convert to dictionary in string
        """self.table= self.table+'.db'
        self.field = str(self.keys_values).replace(':', ' ').replace("'", "").replace('}', ')').replace('{', '(');
        
        self.my_query = "CREATE TABLE " + self.table + " {}".format(self.field)
        self.cursor = self.con.cursor()
        self.cursor.execute(self.my_query)
        self.con.commit()
        self.con.close()"""
        self.field = str(self.keys_values).replace(':', ' ').replace("'", "").replace('}', ')').replace('{', '(');
        self.my_query = "CREATE TABLE " + self.nameTable + " {}".format(self.field)
        try:
            self.con = sqlite3.connect(self.nameDb+".db")
            self.cursor = self.con.cursor()
            self.cursor.execute(self.my_query)
            self.con.commit()
            self.con.close()
        except Exception:
            print("Errorerror", Exception)

"""
createT = createTable()
createT.build_table()
createT.show_dict()
createT.send_table()
"""