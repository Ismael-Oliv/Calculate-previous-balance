import os
from src.database.repository.index import dabaseRepository


def Adicionar0220Feature(params):

    connection = params['conn']
    origem = params['origem']
    destino = params['destino']
    cnpj = params['cnpj']
    Barra_Progesso = params['barra']
    ComapanyName = params['ComapanyName']

    arrUniade = [
        'UN',
        'KG',
        'PC',
        'FD',
        'CX'
    ]

    Arquivos = os.listdir(origem)

    ArrC170 = []

    total0200 = 0
    for SPED in Arquivos:

        with open(os.path.join(origem, SPED), mode='r', encoding='utf-8') as fd:

            for line in fd:

                arrLine = line.split('|')

                if arrLine[1] == '0200':
                    total0200 += 1

                if arrLine[1] == 'C100':
                    CHV_Acesso = arrLine[9]

                if arrLine[1] == 'C170':

                    COD_Int_SPED = arrLine[3]
                    QUANT_Int_SPED = arrLine[5]
                    UNIT_Int_SPED = arrLine[6]

                    tx = [CHV_Acesso, COD_Int_SPED, QUANT_Int_SPED, UNIT_Int_SPED]
                    ArrC170.append(tx)

        with open(os.path.join(origem, SPED), mode='r', encoding='utf-8') as File:
            
            quant0200 = 0
            for line in File:

                arrLine = line.split('|')

                if arrLine[1] == '0200':
                    EAN_0200 = arrLine[4]
                    UNI_0200 = arrLine[6]
                    COD_0200 = arrLine[2]

                    ARRXML = dabaseRepository.selectionNF(connection, ComapanyName, EAN_0200)

                    if len(ARRXML) > 0:

                        for NFe in ARRXML:
                            ArrUnidade = []
                            XML = NFe

                            CHV_XML = XML[0]
                            COD_XML = XML[9]
                            CNPJ_XML = XML[4]
                            UN_XML = XML[13]

                            if UN_XML.upper() == 'UD':
                                UN_XML = 'PC'

                            elif UN_XML.upper() == 'FDO':
                                UN_XML = 'FD'

                            elif UN_XML.upper() == 'PZA':
                                UN_XML = 'PC'

                            QUANT_XML = XML[14]

                            Fator = 0
                            UNI_C170 = ''
                            QTD_C170 = ''

                            for NFe_C170 in ArrC170:

                                if f'NFe{NFe_C170[0]}' == CHV_XML and NFe_C170[1] == COD_0200:
                                    QTD_C170 = NFe_C170[2]

                                    Fator = int(float(QTD_C170) / float(QUANT_XML))
                                    break

                            if UN_XML not in ArrUnidade:
                                
                                ArrUnidade.append(UN_XML)
                                with open(os.path.join(destino, f'SPED_COM_0220{ComapanyName}.txt'), mode='a',  encoding='utf-8') as SPEDFILE:
                                    SPEDFILE.write(f'{line}')

                                    SPEDFILE.write(f'|0220|{UN_XML}|{Fator}|\n')

                    else:

                        with open(os.path.join(destino, f'SPED_COM_0220{ComapanyName}.txt'), mode='a',  encoding='utf-8') as SPEDFILE:
                            SPEDFILE.write(f'{line}')

                else:

                    with open(os.path.join(destino, f'SPED_COM_0220{ComapanyName}.txt'), mode='a',  encoding='utf-8') as SPEDFILE:
                        SPEDFILE.write(f'{line}')


                quant0200 += 1
                
                Barra_Progesso.setValue( (quant0200 / total0200) * 100)

    return True