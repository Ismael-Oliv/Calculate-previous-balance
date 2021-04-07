import os
from src.database.repository.index import dabaseRepository
from src.pages.Exportar.Saldo_Inicial.respository.index import DBRepository
from src.pages.Exportar.Saldo_Inicial.services.features.ProcessSaldo import ProcessarSaldo
from src.pages.Exportar.Saldo_Inicial.services.features.ReturnRegistroH010 import ReadRegistroH010
from src.pages.Exportar.Saldo_Inicial.services.features.ReturnCadastroProdutos import ReturnCadastroProdutos
from src.pages.Exportar.Saldo_Inicial.services.features.ReturnItemInH010 import ReturnItemInH010
from src.pages.Exportar.Saldo_Inicial.services.features.ReturnRegistroC170 import ReturnRegistroC170


def ProcessarSaldoInicial(params):

    origem = params['Origem']
    Destino = params['Destino']
    Barra_Progresso = params['Barra_Progresso']
    CompanyName = params['CompanyName']

    Params_registroH010 = {
        "Origem":origem,
        "Destino":Destino,
        "Barra_Progresso":Barra_Progresso,
        "CompanyName": CompanyName
    }

    
    Connection = dabaseRepository.createConection()
    produtos = ReturnCadastroProdutos(params)

    for produto in produtos:
        
        ItemInH010 = ReturnItemInH010(Connection, CompanyName, produto['COD_ITEM'])

        if ItemInH010:

            XMLInC170 = ReturnRegistroC170(Connection, CompanyName, produto['COD_ITEM'])

            if XMLInC170:

                dados = {
                    'Connection':Connection,
                    'CompanyName':CompanyName,
                    'XMLInC170':XMLInC170,
                    'EAN': produto['COD_BARRA'],
                    'Item':ItemInH010
                }

                productsWithStOrNot = ProcessarSaldo(dados)               
                
                print(productsWithStOrNot)

                if productsWithStOrNot[0]['wasFound']:
                    
                    if productsWithStOrNot[0]['isST']:

                        # Corrigir
                        produto.update({"QTD":ItemInH010[0]['QTD']})
                        produto.update(productsWithStOrNot[0])
                        print(produto)
                        with open(os.path.join(Destino, f"{CompanyName}-Buscar NFs anteriores"), mode='a') as FWork:
                            FWork.write(f"{produto}\n")

                    else:
                        print('Produto não e ST')
                        FileName = f"{CompanyName}- Itens não st"
                        txt = f"{produto['COD_ITEM']}|{produto['DESCR_ITEM']}|{produto['COD_BARRA']}|{produto['CEST']}"
                        with open(
                            os.path.join(
                                Destino, FileName), mode='a') as FWork:
                            FWork.write(f"{txt}\n")

                else:

                    FileName = f"{CompanyName}-Nenhum Arquivo XML de entrada encontrado"
                    txt = f"{produto['COD_ITEM']}|{produto['DESCR_ITEM']}|{produto['COD_BARRA']}|{produto['CEST']}"
                    with open(
                        os.path.join(
                            Destino, FileName), mode='a') as FWork:
                        FWork.write(f"{txt}\n")

            else:
                
                FileName = f"{CompanyName}-Nenhum RegistroC170 foi encontrado"
                txt = f"{produto['COD_ITEM']}|{produto['DESCR_ITEM']}|{produto['COD_BARRA']}|{produto['CEST']}"
                with open(
                    os.path.join(
                        Destino, FileName), mode='a') as FWork:
                    FWork.write(f"{txt}\n")

        else:
            print('Produto não encontrado')

    return True
