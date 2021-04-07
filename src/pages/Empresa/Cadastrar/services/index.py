from src.database.repository.index import dabaseRepository
from src.pages.Empresa.Cadastrar.repository.index import createXMLC170Table
from src.pages.Empresa.Cadastrar.repository.index import createXMLTable
from src.pages.Empresa.Cadastrar.repository.index import createCompanyTable
from src.pages.Empresa.Cadastrar.repository.index import selectOneCompany
from src.pages.Empresa.Cadastrar.repository.index import createProductTable
from src.pages.Empresa.Cadastrar.repository.index import createH010Table
from src.pages.Empresa.Cadastrar.repository.index import createRelationCode

class CadastrarServices:

    def __init__(self):
        self.mensagem = []

    def createTables(self, CNPJ, CompanyName):

        try:
            conection = dabaseRepository.DBConection()
            DBCreated = createCompanyTable(conection)

            if DBCreated:

                ExistCompany = selectOneCompany(conection, CNPJ)

                if len(ExistCompany) == 0:

                    info = [CNPJ, CompanyName]
                    result = dabaseRepository.saveCompany(conection, info)
                    XMLTable = createXMLTable(conection, CNPJ)
                    C170Table = createXMLC170Table(conection, CNPJ)
                    productTable = createProductTable(conection, CNPJ)
                    H010Table = createH010Table(conection, CNPJ)
                    RelationCode = createRelationCode(conection, CNPJ)

                    if not RelationCode:
                        self.mensagem.append(['RelationCode', RelationCode])

                    if not H010Table:
                        self.mensagem.append(['H010Table', H010Table])

                    if not XMLTable:
                        self.mensagem.append(['XMLTable', XMLTable])

                    if not productTable:
                        self.mensagem.append(['productTable', productTable])

                    if not C170Table:
                        self.mensagem.append([C170Table])

                    if result == None:
                        self.mensagem.append(['ExistCompany', result])

                else:

                    self.mensagem.append(['Empresa já cadastrada'])

                conection.close()

        except Exception as EX:

            self.mensagem.append(["Exception", EX])

        return self.mensagem
