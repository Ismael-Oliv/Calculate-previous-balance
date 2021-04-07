import os
from src.pages.Importar.RegistroH010.repository.index import Repository
from src.database.repository.index import dabaseRepository
from datetime import date

def SalvarRegistroH010(params):

    origem = params['Origem']
    Barra_Progesso = params['Barra_Progesso']
    CompanyName = params['CompanyName'].text()

    Arquivos = os.listdir(origem)

    connection = dabaseRepository.createConection()

    for SPED in Arquivos:

        with open(os.path.join(origem, SPED), mode='r', encoding='utf-8') as F:

            totalLinhas = len(F.readlines())
        linha = 0

        with open(os.path.join(origem, SPED), mode='r', encoding='utf-8') as File:

            for lineItem in File:

                arrLine = lineItem.split('|')
                if arrLine[1] == 'H010':
                    
                    COD_ITEM = arrLine[2]
                    UNID = arrLine[3]

                    if ',' in arrLine[4]:
                        arrQTD = arrLine[4].split(',')
                        convertedQTD = arrQTD[0] + '.' + arrQTD[1]
                        QTD = float(convertedQTD)

                    else:
                        
                        QTD = float(arrLine[4])


                    VL_UNIT = arrLine[5]
                    VL_ITEM = arrLine[6]

                    dt_Emissao = '31032019'

                    EDay = int(dt_Emissao[0:2])
                    EMout = int(dt_Emissao[2:4])
                    EYear = int(dt_Emissao[4:])

                    date_Emissao = date(EYear, EMout, EDay).isoformat()

                    ExistentRegister = Repository.FindItemInH010(
                        connection, COD_ITEM, date_Emissao, CompanyName)

                    if not ExistentRegister:

                        txt = [

                            COD_ITEM,
                            UNID,
                            QTD,
                            VL_UNIT,
                            VL_ITEM,
                            date_Emissao

                        ]


                        Response = Repository.Save(connection, CompanyName, txt)

        
                linha += 1
                valor = ( linha / totalLinhas ) * 100
                
                Barra_Progesso.setValue(valor)