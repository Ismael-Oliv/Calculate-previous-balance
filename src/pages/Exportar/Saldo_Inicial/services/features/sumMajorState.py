# import os
# from src.database.repository.index import dabaseRepository
# from src.pages.Exportar.Saldo_Inicial.services.features.sumMajorState import CFOPIndustry

# def Adicionar0220Feature(params):

#     connection = params['conn']
#     origem = params['origem']
#     destino = params['destino']
#     cnpj = params['cnpj']
#     Barra_Progesso = params['barra']
#     ComapanyName = params['ComapanyName']

#     CFOP_Industria = [
#         5401,
#         5403,
#         6401,
#         6403,
#         5402,
#         6402
#     ]

#     CFOP_Comercio = [
#         5405,
#         6405
#     ]

#     Arquivos = os.listdir(origem)

#     ArrC170 = []

#     total0200 = 0
#     for SPED in Arquivos:

#         with open(os.path.join(origem, SPED), mode='r', encoding='utf-8') as File:
            
#             quant0200 = 0

#             for lineItem in File:

#                 arrLine = lineItem.split('|')

#                 if arrLine[1] == '0200':

#                     EAN_0200 = arrLine[4]
#                     UNI_0200 = arrLine[6]
#                     COD_0200 = arrLine[2]

#                     if UNI_0200 == 'KG' or UNI_0200 == 'kg':
#                         foundKG = UNI_0200.split('.')

#                         if foundKG > 1:
#                             necessario = float(foundKG[0] + '.' + foundKG[1])
#                         else:
#                             necessario = float(UNI_0200)

#                     findPrevXMl = dabaseRepository.selectionNF(connection, ComapanyName, EAN_0200)

#                     if len(findPrevXMl) > 0:
                        
#                         estado = 0
#                         ICMS_Proprio = 0
#                         ICMS_ST = 0
#                         ICMS_ST_FCPST = 0

#                         for XMLFileFound in findPrevXMl:

#                             chave_acesso = XMLFileFound[0]
#                             sequencia = XMLFileFound[0]

#                             findXMLInSped = dabaseRepository.selectionNF(connection, ComapanyName, EAN_0200)

#                             if findXMLInSped:

#                                 QuantInSPEDxml = float(findXMLInSped[12])
#                                 CFOP = findPrevXMl[2]

#                                 if CFOP in CFOP_Industria:

#                                     if Quantidade < necessario:
#                                         soma = Quantidade + estado

#                                     if soma <= necessario:

#                                         estado += Quantidade

#                                         ICMS_Proprio += arrXML['vICMS']
#                                         ICMS_ST += arrXML['vICMSST']
#                                         ICMS_ST_FCPST += arrNFe['vFCPST']

#                                         arrXML.append([

#                                             arrNFe[xml].chv,
#                                             arrNFe[xml].dhEmi,
#                                             arrNFe[xml].dhSaiEnt,
#                                             arrNFe[xml].seq,
#                                             arrNFe[xml].cProd,
#                                             arrNFe[xml].xProd

#                                         ])


#                                         if soma > necessario:

#                                             diferenca = necessario - estado

#                                             estado = estado + diferenca

#                                             qtd_unit_ICMS_proprio = arrNFe['vICMS'] / Quantidade
#                                             qtd_unit_ICMS_ST = arrNFe['vICMSST'] / Quantidade
#                                             qtd_unit_ICMS_ST_FCPST = arrNFe['vFCPST'] / Quantidade

#                                             ICMS_Proprio = ICMS_Proprio + qtd_unit_ICMS_proprio * diferenca
#                                             ICMS_ST = ICMS_ST + qtd_unit_ICMS_ST * diferenca
#                                             ICMS_ST_FCPST += (qtd_unit_ICMS_ST_FCPST * diferenca)

#                                             arrXML.push([

#                                                 arrNFe[chv]
#                                                 arrNFe[dhEmi]
#                                                 arrNFe[dhSaiEnt]
#                                                 arrNFe[seq]
#                                                 arrNFe[cProd]
#                                                 arrNFe[xProd]
#                                             ])

#                                     else:

#                                         break

#                                 if CFOP in CFOP_Comercio:

#                                     if estado < necessario:

#                                         soma = QuantInSPEDxml + estado
#                                         if soma <= necessario:
                                        
#                                             estado = estado + QuantInSPEDxml
#                                         ICMS_Proprio += arrNFe[vICMSEfet]
#                                         ICMS_ST += arrNFe[vICMSSTRet]
#                                         ICMS_ST_FCPST += arrNFe[vFCPST]

#                                         arrXML.append([

#                                             arrNFe[chv],
#                                             arrNFe[dhEmi],
#                                             arrNFe[dhSaiEnt],
#                                             arrNFe[seq],
#                                             arrNFe[cProd],
#                                             arrNFe[xProd],

#                                         ])

#                                         if soma > necessario:

#                                             diferenca = necessario - estado
#                                             estado += diferenca
                                        
#                                             qtd_unit_ICMS_proprio = arrNFe[xml].vICMS / NFe[0].QUANTIDADE
#                                             qtd_unit_ICMS_ST = arrNFe[xml].vICMSST / NFe[0].QUANTIDADE
#                                             qtd_unit_ICMS_ST_FCPST = arrNFe[xml].vFCPST / NFe[0].QUANTIDADE

#                                             ICMS_Proprio = ICMS_Proprio + qtd_unit_ICMS_proprio * diferenca
#                                             ICMS_ST = ICMS_ST + qtd_unit_ICMS_ST * diferenca
#                                             ICMS_ST_FCPST =
#                                             ICMS_ST_FCPST + qtd_unit_ICMS_ST_FCPST * diferenca

#                                             arrXML.append([

#                                                 arrNFe[chv],
#                                                 arrNFe[dhEmi],
#                                                 arrNFe[dhSaiEnt],
#                                                 arrNFe[seq],
#                                                 arrNFe[cProd],
#                                                 arrNFe[xProd]

#                                             ])

#                                     else:
#                                         break

#                             else:
#                                 message = 'XML não encontrado no SPED'
                    
#                     else:
#                         message = 'Arquivo XML não importado'

#                 quant0200 += 1
                
#                 Barra_Progesso.setValue( (quant0200 / total0200) * 100)

#     return True