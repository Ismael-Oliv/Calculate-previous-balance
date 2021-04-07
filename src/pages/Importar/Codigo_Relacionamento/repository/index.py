import os
from sqlite3 import connect

class Repository:

    def FindOne(conn, companyName, Item, CNPJ):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:

            connection = conn.cursor()
            try:
                arrDatas = connection.execute(f"""SELECT * FROM _codigoRelacionamento{companyName} WHERE
                                                Cod_Item ='{Item}' AND cnpj ='{CNPJ}'""")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                print(Ex)

        else:
            mensagem = 'BD not exist'
            return mensagem
    
    def Save(conn, companyName, relation):
        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            conection = conn.cursor()

            try:
                c = conn.cursor()
                c.execute(
                    f'INSERT INTO _codigoRelacionamento{companyName} VALUES (?, ?, ?)', relation)

                conn.commit()

                return True

            except Exception as Ex:
                print(Ex)
                return False

        else:
            print('BD not exist')
            return False

