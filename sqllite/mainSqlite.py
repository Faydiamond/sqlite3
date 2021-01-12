class createtable:

    def __init__(self):
        #nombre tabla
        self.mainn()

    def mainn (self):
        self.msgOpt= """

1- Crear base de datos.
2- Crear tabla de la base de datos.
3- Inseratr registro en la tabla person
4- Listar tabla persona 
"""
        print(self.msgOpt)
        self.Option = int (input("Digite el numero de la opció que desee   "))
        ##Options
        if (self.Option == 1):
            print("crear base de datos")
            import creardb
            self.cre_db = creardb.databsee()
            self.cre_db.create_db()
        elif (self.Option == 2):
            import creTable
            self.crtTable = creTable.createTable()
            self.crtTable.build_table()
            self.crtTable.send_table()
        elif (self.Option == 3):
            import insert
            self.insert = insert.insertBd()
            self.insert.ins_table()
        else:
            print("Por favor digite una opción valida del menu")

        #cursor ejecuta sentencias sql en py


c = createtable()
#c.show_table()
#c.add_campesTable()
#c.show_campes()
#c.parameters_send()