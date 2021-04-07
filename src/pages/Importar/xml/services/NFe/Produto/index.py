def Produto(Itens):
    global sequencia
    arrProdutos = []
    for iten in Itens:

        if type(iten) == str:

            if iten == '@nItem':
                sequencia = Itens[iten]

            if iten == 'prod':
                arrTag = []
                for tag in Itens['prod']:
                    arrTag.append(tag)

                cProd = Itens[iten]['cProd']

                if 'cEAN' in arrTag:
                    cEAN = Itens[iten]['cEAN']
                else:
                    cEAN = '0'

                xProd = Itens[iten]['xProd']
                CFOP = Itens[iten]['CFOP']
                uCom = Itens[iten]['uCom']
                qCom = Itens[iten]['qCom']
                vUnCom = Itens[iten]['vUnCom']
                vProd = Itens[iten]['vProd']

                if 'cEANTrib' in arrTag:
                    cEANTrib = Itens[iten]['cEANTrib']
                else:
                    cEANTrib = '0'

                uTrib = Itens[iten]['uTrib']
                qTrib = Itens[iten]['qTrib']
                vUnTrib = Itens[iten]['vUnTrib']

                infoProd = [sequencia, cProd, cEAN, xProd, CFOP, uCom, qCom, vUnCom, vProd, cEANTrib, uTrib, qTrib, vUnTrib]
                arrProdutos.append(infoProd)

        if type(iten) != str:

            arrTag = []
            for tag in iten['prod']:
                arrTag.append(tag)

            sequencia = iten['@nItem']
            cProd = iten['prod']['cProd']

            if 'cEAN' in arrTag:
                cEAN = iten['prod']['cEAN']
            else:
                cEAN = '0'

            xProd = iten['prod']['xProd']
            CFOP = iten['prod']['CFOP']
            uCom = iten['prod']['uCom']
            qCom = iten['prod']['qCom']
            vUnCom = iten['prod']['vUnCom']
            vProd = iten['prod']['vProd']

            if 'cEANTrib' in arrTag:
                cEANTrib = iten['prod']['cEANTrib']
            else:
                cEANTrib = '0'

            uTrib = iten['prod']['uTrib']
            qTrib = iten['prod']['qTrib']
            vUnTrib = iten['prod']['vUnTrib']

            infoProd = [sequencia, cProd, cEAN, xProd, CFOP, uCom, qCom, vUnCom, vProd, cEANTrib, uTrib, qTrib, vUnTrib]
            arrProdutos.append(infoProd)

    return arrProdutos
