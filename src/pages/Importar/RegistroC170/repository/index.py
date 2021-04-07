import os
from sqlite3 import connect

class RegistroC170Repository:

    def createConection():

        dataBasePath = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')
        connection = connect(dataBasePath)

        return connection

    def FindOne(conn):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:

            connection = conn.cursor()
            try:
                arrDatas = connection.execute(f"SELECT * FROM companyName")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                print(Ex)

        else:
            mensagem = 'BD not exist'
            return mensagem
    
    def Save(conn, companyName, infoProduto):
        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            conection = conn.cursor()

            try:
                c = conn.cursor()
                c.execute(
                    f'INSERT INTO _NFeC170{companyName} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', infoProduto)

                conn.commit()

                return True

            except Exception as Ex:
                print(Ex)
                return False

        else:
            print('BD not exist')
            return False

    def FindOneXMLInC170(conn, chv, Cod_item, CompanyTable):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            c = conn.cursor()
            try:
                arrDatas = c.execute(
                    f"""
                    SELECT * FROM _NFeC170{CompanyTable} 
                    WHERE chv = '{chv}' AND Cod_item = '{Cod_item}'
                    """)
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                print(Ex)
                return False

        else:
            print('BD not exist')
            return False