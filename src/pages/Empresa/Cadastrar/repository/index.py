import os

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


def createXMLC170Table(conn, CompanyName):

        DBCreated = os.path.exists(
            os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db'))

        if DBCreated:
            c = conn.cursor()
            try:

                c.execute(f"""CREATE TABLE _NFeC170{CompanyName} (
                    chv TEXT,
                    Dt_Emissao TIME,
                    Dt_Entrada TIME,
                    Num_Item TEXT,
                    Cod_Item TEXT,
                    Descricao TEXT,
                    Quant TEXT,
                    Unidade TEXT,
                    Vl_Item TEXT,
                    Vl_Desc TEXT,
                    Cst TEXT,
                    Cfop TEXT
                    )""")

                conn.commit()

                return True

            except Exception as ex:

                if ex.__str__() == f'table _NFeC170{CompanyName} already exists':
                    return True

                else:
                    print('Erro ao criar companyTable :', ex)
                    return True


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

def createRelationCode(conn, CompanyName):

    DBCreated = os.path.exists(
        os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db'))

    if DBCreated:
        c = conn.cursor()
        try:

            c.execute(f"""CREATE TABLE _codigoRelacionamento{CompanyName} (
                Cod_Item TEXT,
                cnpj TEXT,
                Cod_Forn TEXT
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

def createProductTable(conn, companyName):

    DBCreated = os.path.exists(
        os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db'))

    if DBCreated:
        c = conn.cursor()
        try:

            c.execute(f"""CREATE TABLE _produto{companyName} (
                COD_ITEM TEXT,
                DESCR_ITEM TEXT,
                COD_BARRA TEXT,
                UNID_INV TEXT,
                COD_NCM TEXT,
                ALIQ_ICMS TEXT,
                CEST TEXT
                )""")

            conn.commit()

            return True

        except Exception as ex:

            if ex.__str__() == f'table _produto{companyName} already exists':
                return True

            else:
                print('Erro ao criar companyTable :', ex)
                return False

    else:

        return False

def createH010Table(conn, companyName):

    DBCreated = os.path.exists(
        os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db'))

    if DBCreated:
        c = conn.cursor()
        try:

            c.execute(f"""CREATE TABLE _H010{companyName} (
                COD_ITEM TEXT,
                UNID TEXT,
                QTD TEXT,
                VL_UNIT TEXT,
                VL_ITEM TEXT,
                DATA TIME
                )""")

            conn.commit()

            return True

        except Exception as ex:

            if ex.__str__() == f'table _produto{companyName} already exists':
                return True

            else:
                print('Erro ao criar companyTable :', ex)
                return False

    else:

        return False

def selectOneCompany(conn, CNPJ):

    DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')
    print(CNPJ)
    if DBCreated:
        c = conn.cursor()
        try:
            arrDatas = c.execute(
                f"SELECT * FROM CompanyName WHERE cnpj = '{CNPJ}'")
            conn.commit()
            return arrDatas.fetchall()

        except Exception as Ex:

            print(Ex)
            return

    else:
        mensagem = 'BD not exist'
        print(mensagem)

def saveCompany(conn, infoProduto):

    try:

        c = conn.cursor()
        c.execute(f'INSERT INTO companyName VALUES (?, ?)', infoProduto)
        conn.commit()

    except Exception as Ex:
        print(Ex)
        return False
