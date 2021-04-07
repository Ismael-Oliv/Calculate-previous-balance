import shutil
import os
from time import time
from src.pages.Analises.XMLemSPED.repository.index import EditarRepository


def VerificarXMLInSped(params):
    origem = params['origem']
    destino = params['destino']
    CompanyName = params['CompanyName']
    connection = params['conn']
    Barra_Progesso = params['Barra_Progesso']

    Arquivos = os.listdir(origem)

    QuantLinhas = 0
    linha = 0

    message = ''

    for SPED in Arquivos:

        with open(os.path.join(f'{origem}', SPED), mode='r', encoding='utf-8') as f:
            QuantLinhas = len(f.readlines())

        with open(os.path.join(f'{origem}', SPED), mode='r', encoding='utf-8') as fd:

            for line in fd:

                arrLine = line.split('|')

                if arrLine[1] == '0000':
                    cnpj = arrLine[7]

                    if cnpj != CompanyName:
                        message = 'Arquivo SPED não pertence a empresa ativa'
                        return message

                if arrLine[1] == 'C100':
                    chv = f'NFe{arrLine[9]}'

                    NFe = EditarRepository.findOne(connection, CompanyName, chv)

                    if len(NFe) <= 0:
                       with open(os.path.join(destino, f'{CompanyName}-{time()}'), mode='a', encoding='utf-8') as function:
                           function.write(f'{chv}\n')

                linha += 1
                Barra_Progesso.setValue((linha / QuantLinhas) * 100)

    message = 'Processo concluido'
    return message