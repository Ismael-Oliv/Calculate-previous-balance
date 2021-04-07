def TratamentoInfoProduto(chv,Ident, Emitent, Destinat, InfoProdutos, Imposto):

    Produtos = []

    nNF, dhEmi, dhSaiEnt = Ident
    CNPJEmit, IEEmit = Emitent
    CNPJDest, IEDest = Destinat

    for index, infoProduto in enumerate(InfoProdutos):
        orig = Imposto[index][0]
        CST = Imposto[index][1]
        TotalICMSProprio = Imposto[index][2]
        TotalICMSSt = Imposto[index][3]

        sequencia = infoProduto[0]
        cProd = infoProduto[1].strip('0')
        cEAN = infoProduto[2]
        xProd = infoProduto[3]
        CFOP = infoProduto[4]
        uCom = infoProduto[5]
        qCom = infoProduto[6]
        vUnCom = infoProduto[7]
        vProd = infoProduto[8]
        cEANTrib = infoProduto[9]
        uTrib = infoProduto[10]
        qTrib = infoProduto[11]
        vUnTrib = infoProduto[12]

        info = [chv, nNF, dhEmi, dhSaiEnt, CNPJEmit, IEEmit, CNPJDest, IEDest,
                sequencia, cProd, cEAN, xProd, CFOP, uCom, qCom, vUnCom, vProd, cEANTrib, uTrib,
                qTrib, vUnTrib, orig, CST, TotalICMSProprio, TotalICMSSt]
        Produtos.append(info)

    return Produtos