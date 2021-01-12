class litPerson:

    def listt(self):
        import sqlite3
        self.nameDb = input('Por favor digite el nombre de la base de datos  ') + ".db"
        self.table = input('Por favor digite el nombre de la tabla  ')
        #print (self.nameDb)
        #print(self.table)
        self.rowss = "SELECT * FROM {}".format(self.table)
        print(self.rowss)
        try:
            self.con = sqlite3.connect(self.nameDb)
            self.cursor = self.con.cursor()
            self.cursor.execute(self.rowss)
            self.rows = self.cursor.fetchall()
            for r in self.rows:
                print(r)
        except Exception:
            print("Errorerror", Exception)



liP = litPerson()
liP.listt()