import os
from sqlite3 import connect

class EditarRepository:

    def createConection():

        dataBasePath = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')
        connection = connect(dataBasePath)

        return connection

    def findOne(conn, companyName, chv):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'databaseFile', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:

            connection = conn.cursor()
            try:
                arrDatas = connection.execute(f"SELECT * FROM _NFe{companyName} WHERE chv ='{chv}'")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                print(Ex)

        else:
            mensagem = 'BD not exist'
            return mensagem
    
