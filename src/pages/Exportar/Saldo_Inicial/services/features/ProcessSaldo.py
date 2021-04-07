from src.pages.Exportar.Saldo_Inicial.respository.index import DBRepository
from src.pages.Exportar.Saldo_Inicial.services.features.ReturnXMLFile import returnXMLFile

def ProcessarSaldo(params):

    CFOP_Industria = [
        5401,
        5403,
        6401,
        6403,
        5402,
        6402
    ]

    CFOP_Comercio = [
        5405,
        6405
    ]

    Produtos = []

    Connection = params['Connection']
    CompanyName = params['CompanyName']
    XMLInC170 = params['XMLInC170']
    EAN = params['EAN']

    Item = params['Item'][0]

    Estado = 0
    ICMS_Proprio = 0
    ICMS_ST = 0

    ItemQuant = Item['QTD']
    necessario = Item['QTD']

    if ',' in necessario:

        arrquant = necessario.split(',')
        convertedNecessario = float(arrquant[0] + '.' + arrquant[1])
        necessario = float(convertedNecessario)
    else:

        necessario = float(Item['QTD'])

    for XMLInSPED in XMLInC170:

        if type(XMLInSPED['QTD']) == str:
            
            if ',' in XMLInSPED['QTD']:

                arrquant = XMLInSPED['QTD'].split(',')
                converterdQuantity = float(arrquant[0] + '.' + arrquant[1])
                XMLInSPED.update({'QTD':float(converterdQuantity)})

        chv = XMLInSPED['chv']

        codInt, cnpj, codForn= DBRepository.ReturnCodRelation(
                            conn=Connection,
                            companyName=CompanyName,
                            Item=XMLInSPED['Cod_Item'])[0]
        
        FileXML = returnXMLFile(Connection, CompanyName, codForn.strip(), chv)

        if len(FileXML) > 0:
            FileXML = FileXML[0]

            if FileXML['isProductST']:
                
                cfop = int(FileXML['CFOP'])
                
                soma = float(XMLInSPED['QTD']) + Estado

                if cfop in CFOP_Industria:
                    
                    if Estado < necessario:
                        soma = float(XMLInSPED['QTD']) + Estado
                    
                    if soma <= necessario:   

                        Estado += float(XMLInSPED['QTD'])

                        ICMS_Proprio += float(FileXML['TotalICMSProprio'])
                        ICMS_ST += float(FileXML['TotalICMSSt'])
                            
                        Produtos.append({
                            "ICMS_Proprio":ICMS_Proprio,
                            "ICMS_ST":ICMS_ST,
                            "isST": True,
                            'wasFound': True
                            })
                    
                    if soma > necessario:

                        diferenca = necessario - Estado

                        Estado += diferenca

                        qtd_unit_ICMS_proprio = float(FileXML['TotalICMSProprio']) / float(XMLInSPED['QTD'])
                        qtd_unit_ICMS_ST = float(FileXML['TotalICMSSt']) / float(XMLInSPED['QTD'])

                        ICMS_Proprio += qtd_unit_ICMS_proprio * diferenca
                        ICMS_ST += qtd_unit_ICMS_ST * diferenca


                        Produtos.append({
                            "ICMS_Proprio":ICMS_Proprio,
                            "ICMS_ST":ICMS_ST,
                            "isST": True,
                            'wasFound': True
                            })

                
                if cfop in CFOP_Comercio:
                    
                    if Estado < necessario:

                        soma = float(XMLInSPED['QTD']) + Estado

                        if soma <= necessario:

                            Estado = Estado + float(XMLInSPED['QTD'])

                            ICMS_Proprio += float(FileXML['TotalICMSProprio'])
                            ICMS_ST += float(FileXML['TotalICMSSt'])

                            Produtos.append({
                                "ICMS_Proprio":ICMS_Proprio,
                                "ICMS_ST":ICMS_ST,
                                "isST": True,
                                'wasFound': True
                                })

                        if soma > necessario:

                            diferenca = necessario - Estado

                            Estado += diferenca

                            qtd_unit_ICMS_proprio = float(FileXML['TotalICMSProprio']) / float(XMLInSPED['QTD'])
                            qtd_unit_ICMS_ST = float(FileXML['TotalICMSSt']) / float(XMLInSPED['QTD'])


                            ICMS_Proprio += qtd_unit_ICMS_proprio * diferenca
                            ICMS_ST += qtd_unit_ICMS_ST * diferenca


                            Produtos.append({
                                "ICMS_Proprio":ICMS_Proprio,
                                "ICMS_ST":ICMS_ST,
                                "isST": True,
                                'wasFound': True
                                })

                    else:

                        break
            
            else:

                Produtos.append({
                    "ICMS_Proprio": 0,
                    "ICMS_ST": 0,
                    "isST": False,
                    'wasFound': True
                })
        else:
            
            Produtos.append({
                "ICMS_Proprio": 0,
                "ICMS_ST": 0,
                "isST": False,
                'wasFound': False
            })

            return Produtos

    return Produtos

        

