import xmltodict
import os

from src.database.repository.index import dabaseRepository
from src.pages.Importar.xml.services.NFe.Identificador.index import Identificador
from src.pages.Importar.xml.services.NFe.Emitente.Index import Emitente
from src.pages.Importar.xml.services.NFe.Destinatario.index import Destinatario
from src.pages.Importar.xml.services.NFe.Produto.index import Produto
from src.pages.Importar.xml.services.NFe.Imposto.index import Impostos
from src.pages.Importar.xml.services.TratamentoInfoProduto.index import TratamentoInfoProduto

from sqlite3 import connect

TipoNF = ['enviNFe', 'nfeProc']


def saveXML(Params):

    conn = Params['conn']
    pathSrc = Params['caminho']
    companyName = Params['cnpj'].text()
    Barra_Progesso = Params['barra']
    Tela = Params['Screen']
    
    arrXML = os.listdir(pathSrc)
    XMLTotal = len(arrXML)

    arrDesconhecido = []

    ProdutosCadastradas = 0

    for xml in arrXML:

        with open(os.path.join(pathSrc, xml), mode='r', encoding='utf-8') as fd:
            doc = xmltodict.parse(fd.read())

            for tipo in doc:
                if tipo in TipoNF:
                    tag = tipo
            try:

                if doc[tag]:

                    ide = doc[tag]['NFe']['infNFe']['ide']
                    Ident = Identificador(ide)

                    chv = doc[tag]['NFe']['infNFe']['@Id']

                    emit = doc[tag]['NFe']['infNFe']['emit']
                    Emitent = Emitente(emit)

                    dest = doc[tag]['NFe']['infNFe']['dest']
                    destinat = Destinatario(dest)

                    det = doc[tag]['NFe']['infNFe']['det']
                    InfoProdutos = Produto(det)

                    arrImpostos = doc[tag]['NFe']['infNFe']['det']
                    Imposto = Impostos(arrImpostos)
                    
                    if len(Imposto) > 0:

                        ProdutosTratados = TratamentoInfoProduto(chv, Ident, Emitent, destinat, InfoProdutos, Imposto)

                        CFOP = ProdutosTratados[0][12]

                        if ProdutosTratados[0][4] == companyName or ProdutosTratados[0][6] == companyName:

                            # if CFOP[1:2] == '4':

                            for ProdutoInfo in ProdutosTratados:

                                chvAcesso = ProdutoInfo[0]
                                cProd = ProdutoInfo[9]

                                xmlFound = dabaseRepository.selection(cProd, conn, companyName, chvAcesso, cProd)
                            
                                if len(xmlFound) == 0:

                                    response = dabaseRepository.save(cProd, conn, companyName, ProdutoInfo)
                                    
                        else:
                            arrDesconhecido.append(xml)
                            print('XML Não é da empresa')
                            
            except:

                print('Erro com o xml', xml)
        ProdutosCadastradas = ProdutosCadastradas + 1
        Barra_Progesso.setValue(
            (ProdutosCadastradas / XMLTotal) * 100
            )

    return { 
        "XMLImportados":ProdutosCadastradas,
        "XMLDesconhecido": arrDesconhecido
        }