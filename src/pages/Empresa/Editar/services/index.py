from src.pages.Empresa.Editar.repository.index import EditarRepository

def removeCampany(conection, cnpj):

    response = EditarRepository.Remove(conection, cnpj)

    if response:
        return True
    else:
        return False

def updataCompany(conection, cnpj):
    response = EditarRepository.updataCompany(conection, cnpj)

    if response:
        return True
    else:
        return False
        