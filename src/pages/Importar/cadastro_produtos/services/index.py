import os
from src.pages.Importar.cadastro_produtos.repository.index import Repository
from datetime import date


def ImportCadastroProduto(params):


    origem = params['Origem']
    Barra_Progesso = params['Barra_Progesso']
    CompanyName = params['CompanyName'].text()

    Arquivos = os.listdir(origem)

    connection = Repository.createConection()

    for SPED in Arquivos:

        with open(os.path.join(origem, SPED), mode='r', encoding='utf-8') as F:

            totalLinhas = len(F.readlines())
        linha = 0

        with open(os.path.join(origem, SPED), mode='r', encoding='utf-8') as File:

            for lineItem in File:

                arrLine = lineItem.split('|')

                if arrLine[1] == '0200':

                    COD_ITEM = arrLine[2].strip('0')
                    DESCR_ITEM = arrLine[3]
                    COD_BARRA = arrLine[4]
                    UNID_INV = arrLine[6]
                    COD_NCM = arrLine[8]
                    ALIQ_ICMS = arrLine[12]
                    CEST = arrLine[13]

                    findOneItem = Repository.FindOne(connection, COD_ITEM, CompanyName)

                    if not findOneItem:
                        txt = [COD_ITEM, DESCR_ITEM, COD_BARRA, UNID_INV, COD_NCM, ALIQ_ICMS, CEST]

                        Repository.save(connection, CompanyName, txt)


                linha += 1
                valor = ( linha / totalLinhas ) * 100
                
                Barra_Progesso.setValue(valor)