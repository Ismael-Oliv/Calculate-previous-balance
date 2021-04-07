from src.pages.Exportar.Saldo_Inicial.respository.index import DBRepository

def returnXMLFile(Connection, CompanyName, CodItem, chv):
    XMLFile = []
    
    XMLs = DBRepository.FindOneXMLFileByEANAndChv(Connection, CompanyName, CodItem, chv)

    for XML in XMLs:
        
        isProductST = True

        CFOP = XML[12]
        if CFOP == '5403':
            print(XML)
            
        if CFOP[1:2] != '4': 
            isProductST = False

        XMLFile.append({
            'chv': XML[0],
            'nNF': XML[1],
            'dhEmi': XML[2],
            'dhSaiEnt': XML[3],
            'CNPJEmit': XML[4],
            'IEEmit': XML[5],
            'CNPJDest': XML[6],
            'IEDest': XML[7],
            'sequencia': XML[8],
            'cProd': XML[9],
            'cEAN': XML[10],
            'xProd': XML[11],
            'CFOP': XML[12],
            'uCom': XML[13],
            'qCom': XML[14],
            'vUnCom': XML[15],
            'vProd': XML[16],
            'cEANTrib': XML[17],
            'uTrib': XML[18],
            'qTrib': XML[19],
            'vUnTrib': XML[20],
            'orig': XML[21],
            'CST': XML[22],
            'TotalICMSProprio': XML[23],
            'TotalICMSSt': XML[24],
            'isProductST':isProductST
        })
    
    return XMLFile