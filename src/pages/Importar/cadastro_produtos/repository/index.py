import os
from sqlite3 import connect

class Repository:

    def createConection():

        dataBasePath = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')
        connection = connect(dataBasePath)

        return connection

    def FindOne(conn, item, CompanyName):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:

            connection = conn.cursor()
            try:
                arrDatas = connection.execute(
                    f"SELECT * FROM _produto{CompanyName} WHERE COD_ITEM ='{item}'")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                print(Ex)

        else:
            mensagem = 'BD not exist'
            return mensagem
    
    def save(conn, companyName, info):
        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            conection = conn.cursor()

            try:
                c = conn.cursor()
                c.execute(
                    f'INSERT INTO _produto{companyName} VALUES (?, ?, ?, ?, ?, ?, ?)', info)

                conn.commit()

                return True

            except Exception as Ex:
                print(Ex)
                return False

        else:
            print('BD not exist')
            return False