import os
from src.pages.Importar.Codigo_Relacionamento.repository.index import Repository
from src.database.repository.index import dabaseRepository
from datetime import date

def ReadCodigoRelacionamento(params):

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

                if len(lineItem) > 1:
                    
                    CodItem, CNPJ, CodForn = lineItem.split(';')

                    ExistentRegister = Repository.FindOne(
                                                    conn=connection,
                                                    companyName=CompanyName,
                                                    Item=CodItem,
                                                    CNPJ=CNPJ
                                                    )
                    if not ExistentRegister:
                        txt = [CodItem, CNPJ, CodForn.strip('0')]
                        print(txt)
                        Repository.Save(
                                        conn= connection,
                                        companyName= CompanyName,
                                        relation= txt
                                        )

        
                    linha += 1
                    valor = ( linha / totalLinhas ) * 100
                    
                    Barra_Progesso.setValue(valor)