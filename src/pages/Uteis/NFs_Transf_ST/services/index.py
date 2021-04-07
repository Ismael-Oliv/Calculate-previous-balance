import os
import shutil
import xmltodict


def FindXMlWithoutSt(Params):

    connection = Params['conn']
    Origem = Params['origem']
    Destino = Params['destino']
    Barra_Progesso = Params['Barra_Progesso']
    CompanyName = Params['CompanyName']

    total = len(os.listdir(Origem))
    quantLinha = 0
    ValoProduto = 0

    for xml in os.listdir(Origem):

        with open(os.path.join(Origem,xml), mode='r', encoding='utf-8') as fd:
            doc = xmltodict.parse(fd.read())

            arrTag = []
            for tag in doc:
                arrTag.append(tag)

            if 'enviNFe' in arrTag:
                startWith = doc['enviNFe']['NFe']['infNFe']

            if 'nfeProc' in arrTag:
                startWith = doc['nfeProc']['infNFe']

            if 'CFe' in arrTag:
                startWith = doc['CFe']['infCFe']

            if startWith:

                # ide = startWith['ide']
                chv = startWith['@Id']
                # emit = startWith['emit']
                # dest = startWith['dest']
                # det = startWith['det']
                Itens = startWith['det']

                total = startWith['total']['vNF']

                for produto in Itens:

                    if type(produto) == str:

                        if produto == 'prod':
                            cProd = Itens[produto]['cProd']
                            xProd = Itens[produto]['xProd']
                            CFOP = Itens[produto]['CFOP']
                            vProd = Itens[produto]['vProd']

                        if produto == 'imposto':

                            if CFOP == '5409':
                                Impostos = Itens[produto]['ICMS']
                                for ICMSTag in Impostos:
                                    txt = f"{cProd}|{xProd}|{CFOP}|{vProd}|{ICMSTag}|{chv}\n"
                                    with open(os.path.join(Destino,f'{CompanyName}-Relatorio-NFe-Transf-S-ST.txt'),
                                        mode='a', encoding='utf-8') as fs:
                                        fs.write(txt)


                    if type(produto) != str:
                        cProd = produto['prod']['cProd']
                        xProd = produto['prod']['xProd']
                        CFOP = produto['prod']['CFOP']
                        vProd = produto['prod']['vProd']
                        if CFOP == '5409':

                            Impostos = produto['imposto']['ICMS']
                            for ICMSTag in Impostos:
                                txt = f"{cProd}|{xProd}|{CFOP}|{vProd}|{ICMSTag}|{chv}\n"
                                with open(os.path.join(Destino,f'{CompanyName}-Relatorio-NFe-Transf-S-ST.txt'),
                                    mode='a', encoding='utf-8') as fs:
                                    fs.write(txt)


        quantLinha =+ 1

        Barra_Progesso.setValue((quantLinha / total) * 100)

    print('Concluido')
