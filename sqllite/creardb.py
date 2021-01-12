class databsee:

    def __init__(self):
        self.nameBd = input("Digite el nombre de la base de datos:  ")
        self.nameBd = self.nameBd+'.db'
        #print(self.nameBd)

    def create_db (self):
        import sqlite3
        self.connect = sqlite3.connect(self.nameBd)
        #cursor ejecuta sentencias sql en py
        self.cursor = self.connect.cursor()
        #connect.commit()
        self.connect.close()

#dt = databsee()

