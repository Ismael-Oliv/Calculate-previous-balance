import os
from src.pages.Importar.RegistroC170.repository.index import RegistroC170Repository
from datetime import date

def ReadRegistroH010(params):

    origem = params['Origem']
    Barra_Progesso = params['Barra_Progesso']
    CompanyName = params['CompanyName'].text()

    Arquivos = os.listdir(origem)

    connection = RegistroC170Repository.createConection()

    for SPED in Arquivos:

        with open(os.path.join(origem, SPED), mode='r', encoding='utf-8') as F:

            totalLinhas = len(F.readlines())
        linha = 0

        with open(os.path.join(origem, SPED), mode='r', encoding='utf-8') as File:

            for lineItem in File:

                arrLine = lineItem.split('|')

                if arrLine[1] == 'C100':
                    
                    chv = arrLine[9]
                    
                    dt_Emissao = arrLine[10]
                    if dt_Emissao:

                        EDay = int(dt_Emissao[0:2])
                        EMout = int(dt_Emissao[2:4])
                        EYear = int(dt_Emissao[4:])

                        date_Emissao = date(EYear, EMout, EDay).isoformat()


                    dt_Entrada = arrLine[11]
                    if dt_Entrada:
                        EnDay = int(dt_Entrada[0:2])
                        EnMout = int(dt_Entrada[2:4])
                        EnYear = int(dt_Entrada[4:])

                        date_Entrada = date(EnYear, EnMout, EnDay).isoformat()


                if arrLine[1] == 'C170':

                    descricao = arrLine[4]
                    Sequencia = arrLine[2]
                    Cod_item = arrLine[3]

                    if ',' in arrLine[5]:
                       arrQuant = arrLine[5].split(',')
                       convertedQuant = float(arrQuant[0] + '.' + arrQuant[1])
                       
                    else:
                        Quant = float(arrLine[5])

                    Unid = arrLine[6]
                    Vl_Unit = arrLine[7]
                    vl_Desc = arrLine[8]
                    cst = arrLine[10]
                    cfop = arrLine[11]


                    ExistentRegister = RegistroC170Repository.FindOneXMLInC170(connection, chv, Cod_item, CompanyName)

                    if not ExistentRegister:

                        txt = [

                            chv,
                            date_Emissao,
                            date_Entrada,
                            Sequencia,
                            Cod_item,
                            descricao,
                            Quant,
                            Unid,
                            Vl_Unit,
                            vl_Desc,
                            cst,
                            cfop

                        ]


                        Response = RegistroC170Repository.Save(connection, CompanyName, txt)

        
                linha += 1
                valor = ( linha / totalLinhas ) * 100
                
                Barra_Progesso.setValue(valor)