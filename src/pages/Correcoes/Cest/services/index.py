from src.database.repository.index import dabaseRepository
import os

def corrgirCest(Params):

    conn = Params['conn']
    origemPath = Params['origem']
    Destpath = Params['destino']
    companyName = Params['cnpj']
    Barra_Progesso = Params['barra']
    Tela = Params['Screen']

    Arquivos = os.listdir(origemPath)

    for SPED in Arquivos:

        n_linhas = 0
        nlinha = 1

        with open(os.path.join(origemPath, SPED), mode='r', encoding='utf-8') as fd:
            n_linhas = len(fd.readlines())

        with open(os.path.join(origemPath, SPED), mode='r', encoding='utf-8') as fd:

            for line in fd:

                arrLine = line.split('|')

                if arrLine[1] == '0200':
                    
                    EAN = arrLine[4]
                    CEST0200 = arrLine[12]
                    NFe = dabaseRepository.selectionNF(conn, companyName, EAN)

                    if len(NFe):

                        CESTXML = NFe[0][18]

                        if CESTXML and CEST0200 != CESTXML:
                            CEST = CESTXML
                        else :
                            CEST = CEST0200

                        REG = arrLine[0]
                        COD_ITEM = arrLine[1]
                        DESCR_ITEM = arrLine[2]
                        COD_BARRA = arrLine[3]
                        COD_ANT_ITEM = arrLine[4]
                        UNID_INV = arrLine[5]
                        TIPO_ITEM = arrLine[6]
                        COD_NCM = arrLine[7]
                        EX_IPI = arrLine[8]
                        COD_GEN = arrLine[9]
                        COD_LST = arrLine[10]
                        ALIQ_ICMS = arrLine[11]

                        txtLine = f"""|{REG}|{COD_ITEM}|{DESCR_ITEM}|
                                    {COD_BARRA}|{COD_ANT_ITEM}|{UNID_INV}|
                                    {TIPO_ITEM}|{COD_NCM}|{EX_IPI}|{COD_GEN}|
                                    {COD_LST}|{ALIQ_ICMS}|{CEST}|"""

                        with open(os.path.join(Destpath, f'SPED_COM_0220{companyName}.txt'), mode='a',  encoding='utf-8') as SPEDFILE:
                            SPEDFILE.write(f'{txtLine}')

                    else:
                        with open(os.path.join(Destpath, f'SPED_COM_0220{companyName}.txt'), mode='a',  encoding='utf-8') as SPEDFILE:
                            SPEDFILE.write(f'{line}')

                else:

                    with open(os.path.join(Destpath, f'SPED_COM_0220{companyName}.txt'), mode='a',  encoding='utf-8') as SPEDFILE:
                        SPEDFILE.write(f'{line}')                   

                Barra_Progesso.setValue((nlinha / n_linhas) * 100)
                nlinha += 1

    return True    
