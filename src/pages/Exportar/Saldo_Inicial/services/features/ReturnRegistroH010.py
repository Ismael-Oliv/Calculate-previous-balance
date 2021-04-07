import os
from src.database.repository.index import dabaseRepository


def ReadRegistroH010(params):

    origem = params['Origem']
    destino = params['Destino']
    Barra_Progesso = params['Barra_Progresso']
    ComapanyName = params['CompanyName']

    Arquivos = os.listdir(origem)
    
    RegistrosH010 = []
    Registros0200 = []
    
    for SPED in Arquivos:

        with open(os.path.join(origem, SPED), mode='r', encoding='utf-8') as File:
            
            for lineItem in File:

                arrLine = lineItem.split('|')
                
                if arrLine[1] == '0200':
                    Registros0200.append(arrLine)

                if arrLine[1] == 'H010':
      
                    [ 
                        vazio,
                        Reg,
                        Cod_item,
                        Unid,
                        Quant,
                        Vl_Unit,
                        Vl_Item,
                        Ind_Prop,
                        Cod_Part,
                        Txt_Compl,
                        Cod_Cta,
                        Vl_Item_Ir,
                        line

                    ] = arrLine
                   
                    if Unid == 'KG' or Unid == 'kg':
                        foundKG = Quant.split('.')

                        if len(foundKG) > 1:
                            Quant = float(foundKG[0] + '.' + foundKG[1])
                        else:
                            Quant = Quant
                    
                    Cod_EAN = ''

                    for registro0200 in Registros0200:

                        if registro0200[2] == Cod_item:
                            Cod_EAN = registro0200[4]
                            break

                    

                    RegistrosH010.append({
                        "Registro_H010": Reg,
                        "EAN_H010":Cod_EAN,
                        "Codigo_Item_H010":Cod_item,
                        "Unidade_H010":Unid,
                        "Quantidade_H010":Quant,
                        "Valor_Unitario_H010":Vl_Unit,
                        "Valor_Item_H010":Vl_Item,
                    })

    Registros0200 = ''                 
    return RegistrosH010

