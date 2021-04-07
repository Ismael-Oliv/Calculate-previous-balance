import os
from sqlite3 import connect

class EditarRepository:

    def AllCompany(conn):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'databaseFile', 'Banco_Dados_Ressarcimento_Icms.db')

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
    
    def Remove(conn, CompanyTable):
        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            conection = conn.cursor()

            try:
                conection.execute(f"DELETE FROM CompanyName WHERE cnpj ='{CompanyTable}'")
                conection.execute(f"DROP TABLE _NFe{CompanyTable}")

                conn.commit()
                return True

            except Exception as Ex:
                print(Ex)

        else:
            mensagem = 'BD not exist'
            return mensagem


    def updataCompany(conn, CNPJPrev, CNPJNew, CompanyName):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            c = conn.cursor()

            try:
                arrDatas = c.execute(f"""
                UPDATE CompanyName
                SET cnpj = '{CNPJNew}' AND razao_social = '{CompanyName}'
                WHERE cnpj = '{CNPJPrev}'
                """)

                conn.commit()

                return arrDatas.fetchall()

            except Exception as Ex:
                print(Ex)

        else:
            mensagem = 'BD not exist'
            print(mensagem)


    def OneCompany(conn, CNPJ):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')
        
        if DBCreated:
            c = conn.cursor()
            try:
                arrDatas = c.execute(
                    f"SELECT * FROM CompanyName WHERE cnpj = '{CNPJ}'")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                mensagem = Ex
                print(mensagem)

        else:
            mensagem = 'BD not exist'
            print(mensagem)