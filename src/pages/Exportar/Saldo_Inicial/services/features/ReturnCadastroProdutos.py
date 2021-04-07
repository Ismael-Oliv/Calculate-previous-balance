
from src.pages.Exportar.Saldo_Inicial.respository.index import DBRepository
from src.database.repository.index import dabaseRepository


def ReturnCadastroProdutos(params):

    Barra_Progesso = params['Barra_Progresso']
    CompanyName = params['CompanyName']
   
    Cadastro_Produtos = []

    connection = dabaseRepository.createConection()
    produtos = DBRepository.FindCadastroProdutos(connection, CompanyName)

    if type(produtos)== list:

        for produto in produtos:
            
            if produto[6] != "":

                Cadastro_Produtos.append({
                    "COD_ITEM": produto[0],
                    "DESCR_ITEM":produto[1],
                    "COD_BARRA":produto[2],
                    "UNID_INV":produto[3],
                    "COD_NCM":produto[4],
                    "ALIQ_ICMS":produto[5],
                    "CEST":produto[6],
                })
                        
    return Cadastro_Produtos

