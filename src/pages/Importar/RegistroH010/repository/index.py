import os
from sqlite3 import connect

class Repository:

    def createConection():

        dataBasePath = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')
        connection = connect(dataBasePath)

        return connection
    
    def Save(conn, companyName, infoProduto):
        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            conection = conn.cursor()

            try:
                c = conn.cursor()
                c.execute(
                    f'INSERT INTO _H010{companyName} VALUES (?, ?, ?, ?, ?, ?)', infoProduto)

                conn.commit()

                return True

            except Exception as Ex:
                print(Ex)
                return False

        else:
            print('BD not exist')
            return False

    def FindItemInH010(conn, date_Emissao, Cod_item, CompanyTable):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            c = conn.cursor()
            try:
                arrDatas = c.execute(
                    f"""
                    SELECT * FROM _H010{CompanyTable} 
                    WHERE DATA = '{date_Emissao}' AND COD_ITEM = '{Cod_item}'
                    """)
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                print(Ex)
                return False

        else:
            print('BD not exist')
            return False