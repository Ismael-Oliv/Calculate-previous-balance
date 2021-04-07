import os
from sqlite3 import connect
from typing import Dict, TypedDict

class DBRepository:

    def ReturnCodRelation(conn, companyName, Item):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:

            connection = conn.cursor()
            try:
                arrDatas = connection.execute(f"""SELECT * FROM _codigoRelacionamento{companyName} WHERE
                                                Cod_Item ='{Item}'""")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                print(Ex)

        else:
            mensagem = 'BD not exist'
            return mensagem

    def FindAllXMLFile(conn, CompanyName, Item):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

        if DBCreated:

            connection = conn.cursor()
            try:
                arrDatas = connection.execute(f"SELECT * FROM _NF{CompanyName} WHERE cod='{Item}'")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                print(Ex)

        else:
            mensagem = 'BD not exist'
            return mensagem


    def FindOneXMLFileByEANAndChv(conn, CompanyName, CodItem, CHV):

        DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')
        
        if DBCreated:

            connection = conn.cursor()
            try:
                arrDatas = connection.execute(f"""SELECT * FROM _NFe{CompanyName}
                                                WHERE  chv='NFe{CHV}' 
                                                AND cProd='{CodItem}'""")
                conn.commit()
                return arrDatas.fetchall()

            except Exception as Ex:
                print(Ex)

        else:
            mensagem = 'BD not exist'
            return mensagem


    def FindXMLInRegistroC170(conn, CompanyName, Item):

            DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

            if DBCreated:

                connection = conn.cursor()
                try:
                    arrDatas = connection.execute(f"""
                                SELECT * FROM 
                                _NFeC170{CompanyName} 
                                WHERE Cod_item='{Item}' ORDER BY Dt_Entrada DESC""")
                                
                    conn.commit()
                    return arrDatas.fetchall()

                except Exception as Ex:
                    print(Ex)

            else:
                mensagem = 'BD not exist'
                return mensagem   

    
    def FindCadastroProdutos(conn, CompanyName):

            DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')
            
            if DBCreated:

                connection = conn.cursor()
                try:
                    arrDatas = connection.execute(f"SELECT * FROM _produto{CompanyName}")
                    conn.commit()
                    return arrDatas.fetchall()

                except Exception as Ex:
                    print(Ex)

            else:
                mensagem = 'BD not exist'
                return mensagem 

    def FindItemInH010(conn, CompanyName, Item):

            DBCreated = os.path.join(os.getcwd(), 'src', 'database', 'file', 'Banco_Dados_Ressarcimento_Icms.db')

            if DBCreated:

                connection = conn.cursor()
                try:
                    # Não é para ser _produto
                    arrDatas = connection.execute(
                        f"SELECT * FROM _H010{CompanyName} WHERE COD_ITEM='{Item}'")
                    conn.commit()
                    return arrDatas.fetchall()

                except Exception as Ex:
                    print(Ex)

            else:
                mensagem = 'BD not exist'
                return mensagem 