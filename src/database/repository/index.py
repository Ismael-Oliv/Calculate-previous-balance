import os
from sqlite3 import connect


class dabaseRepository:

    def __init__(self):
        self.dataBasePath = os.path.join('..', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

    def createConection():
        
        dataBasePath = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')
        connection = connect(dataBasePath)

        return connection


    def DBConection():
        path = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')
        database = os.path.exists(path)
        conn = connect(path)
        return conn


    def createXMLTable(conn, CompanyName):

        DBCreated = os.path.exists(
            os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db'))
        
        if DBCreated:
            c = conn.cursor()
            try:

                c.execute(f"""CREATE TABLE _NFe{CompanyName} (
                    chv TEXT,
                    nNF TEXT,
                    dhEmi TEXT,
                    dhSaiEnt TEXT,
                    CNPJEmit TEXT,
                    IEEmit TEXT,
                    CNPJDest TEXT,
                    IEDest TEXT,              
                    sequencia TEXT,
                    cProd TEXT,
                    cEAN TEXT,
                    xProd TEXT,
                    CFOP TEXT,
                    uCom TEXT,
                    qCom TEXT,
                    vUnCom TEXT,
                    vProd TEXT,
                    cEANTrib TEXT,
                    uTrib TEXT,
                    qTrib TEXT,
                    vUnTrib TEXT,
                    orig TEXT,
                    CST TEXT,
                    TotalICMSProprio TEXT,
                    TotalICMSSt TEXT
                    )""")

                conn.commit()

                return True

            except Exception as ex:

                if ex.__str__() == f'table _NFe{CompanyName} already exists':
                    return True

                else:
                    print('Erro ao criar companyTable :', ex)
                    return False


        else:

            return False

    def createCompanyTable(conn):

        DBCreated = os.path.exists(
            os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db'))

        if DBCreated:
            c = conn.cursor()
            try:

                c.execute(f"""CREATE TABLE CompanyName (
                    cnpj TEXT,
                    razao_social TEXT
                    )""")

                conn.commit()

                return True

            except Exception as ex:

                if ex.__str__() == f'table CompanyName already exists':
                    return True

                else:
                    print('Erro ao criar companyTable :', ex)
                    return False

        else:

            return False

    def createDeParaTable(self, conn, CompanyName):

        DBCreated = os.path.exists(
            os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db'))

        if DBCreated:
            c = conn.cursor()
            try:

                c.execute(f"""CREATE TABLE Depara{CompanyName} (
                     cod_interno TEXT,
                     cnpj TEXT,
                     cod_fornecedor TEXT
                     )""")

                conn.commit()
                conn.close()

                return True

            except Exception as ex:

                if ex.__str__() == f'table Depara{CompanyName} already exists':
                    return True

                else:
                    return False

        else:

            return False


    def selection(self, conn, CompanyTable, chv, cProd):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            c = conn.cursor()
            try:
                arrDatas = c.execute(
                    f"SELECT * FROM _NFe{CompanyTable} WHERE chv = '{chv}' and cProd = '{cProd}'")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                mensagem = Ex
                return mensagem

        else:
            mensagem = 'BD not exist'
            return mensagem

    def selectionNF(conn, CompanyTable, EAN):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            c = conn.cursor()
            try:
                arrDatas = c.execute(
                    f"SELECT * FROM _NFe{CompanyTable} WHERE cEANTrib = '{EAN}'")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                print(Ex)

        else:
            mensagem = 'BD not exist'
            return mensagem

    def selectCodDepara(self, conn, CompanyTable, CNPJ, COD_Forn):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            c = conn.cursor()
            try:
                arrDatas = c.execute(
                    f"SELECT * FROM Depara{CompanyTable} WHERE cnpj = '{CNPJ}' AND cod_fornecedor = {COD_Forn}")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                mensagem = Ex
                return mensagem

        else:
            mensagem = 'BD not exist'
            return mensagem

    def selectionNFe(self, conn, CompanyTable, chv, seq):
        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            c = conn.cursor()
            try:
                arrDatas = c.execute(
                    f"SELECT * FROM _NFe{CompanyTable} WHERE chv = '{chv}' AND sequencia = '{seq}'")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                mensagem = Ex
                return mensagem

        else:
            mensagem = 'BD not exist'
            return mensagem

    def selectOneCompany(conn, CNPJ):

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

    def selectAllCompany(conn):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            c = conn.cursor()
            try:
                arrDatas = c.execute(
                    f"SELECT * FROM companyName")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                mensagem = Ex
                return mensagem

        else:
            mensagem = 'BD not exist'
            return mensagem

    def selectionDepara(self, conn, CompanyName, cod_interno, cnpj):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            c = conn.cursor()
            try:
                arrDatas = c.execute(
                    f"SELECT * FROM Depara{CompanyName} WHERE cod_interno = '{cod_interno}' AND cnpj = '{cnpj}'")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                mensagem = Ex
                return mensagem

        else:
            mensagem = 'BD not exist'
            return mensagem

    def selectionDeparaAll(self, conn, CompanyName):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            c = conn.cursor()
            try:
                arrDatas = c.execute(
                    f"SELECT * FROM Depara{CompanyName} ASC")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                mensagem = Ex
                return mensagem

        else:
            mensagem = 'BD not exist'
            return mensagem

    def ListCompany(self, conn):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:
            c = conn.cursor()
            try:
                arrDatas = c.execute(
                    f"SELECT * FROM companyName")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                mensagem = Ex
                return mensagem

        else:
            mensagem = 'BD not exist'
            return mensagem

    def save(self, conn, companyName, infoProduto):

        try:

            c = conn.cursor()
            c.execute(
                f'INSERT INTO _NFe{companyName} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                infoProduto)

            conn.commit()

        except Exception as Ex:
            mensagem = Ex
            return mensagem

    def saveCompany(conn, infoProduto):

        try:

            c = conn.cursor()
            c.execute(f'INSERT INTO companyName VALUES (?, ?)', infoProduto)
            conn.commit()

        except Exception as Ex:
            mensagem = Ex
            return mensagem

    def saveDepara(self, conn, CompanyName, infoCod):

        try:

            c = conn.cursor()
            c.execute(f'INSERT INTO Depara{CompanyName} VALUES (?, ?, ?)', infoCod)
            conn.commit()

        except Exception as Ex:
            mensagem = Ex
            return mensagem
