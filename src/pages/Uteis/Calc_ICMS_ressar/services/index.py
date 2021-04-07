import os
from src.database.repository.index import dabaseRepository


def CalcularICMSRessarcimento(params):

    connection = params['conn']
    origem = params['origem']
    destino = params['destino']
    Barra_Progesso = params['Barra_Progesso']
    CompanyName = params['CompanyName']

    arrUniade = [
        'UN',
        'KG',
        'PC',
        'FD',
        'CX'
    ]
   
    with open(os.path.join(origem), mode='r', encoding='utf-8') as Funct:
        Total = len(Funct.readlines())


    with open(os.path.join(origem), mode='r', encoding='utf-8') as File:
        linha = 0
        linha_1050 = 0

        for line in File:
            
            arrLine = line.split('|')

            if arrLine[0] == '1050':
                
                REG = arrLine[0]
                COD_ITEM = arrLine[1]
                QTD_INI = arrLine[2]
                ICMS_TOT_INI = arrLine[3]
                QTD_FIM = arrLine[4]
                ICMS_TOT_FIM = arrLine[5]
                txt = f"{REG}|{COD_ITEM}|{QTD_INI}|{ICMS_TOT_INI}|{QTD_FIM}|{ICMS_TOT_FIM}"

                with open(os.path.join(destino, f"{CompanyName} Total - ICMS Ressarcimento.txt"), mode='a') as Func:
                    
                    if linha_1050 == 0:
                        
                        Func.write(f"REG|COD_ITEM|QTD_INI|ICMS_TOT_INI|QTD_FIM|ICMS_TOT_FIM\n")
                        linha_1050 += 1  
                    else:
                        Func.write(f"{txt}")

            linha += 1
            Barra_Progesso.setValue( (linha/Total) * 100 )
            


    return True