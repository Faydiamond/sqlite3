class insertBd:
    def __init__(self):
        self.nameDb = input('Por favor digite el nombre de la base de datos  ')+".db"
        self.table  = input('Por favor digite el nombre de la tabla  ')
        self.id = input('por favor digite el id  ')
        self.name = input('por favor digite el nombre  ')
        self.age = input('por favor digite la edad  ')

    def ins_table(self):
        import sqlite3
        #insert into database= yeronnnn.db and table person
        #self.existdDb = 'SELECT * from sqlite_master where type= "table" and ' + "name='{}'".format(self.table)
        #print("exist" + self.existdDb)
        self.insPerson= "insert into {} ('id','name','age') values ({},'{}',{})".format(self.table,self.id,self.name,self.age)
        print(self.insPerson)
        try:
            self.con = sqlite3.connect( self.nameDb )
            self.cursor = self.con.cursor()
            self.cursor.execute(self.insPerson)
            self.con.commit()
            self.con.close()
        except Exception:
            print("Errorerror", Exception)


#insBd = insertBd()
#insBd.ins_table()