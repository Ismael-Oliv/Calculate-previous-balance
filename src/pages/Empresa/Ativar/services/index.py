from src.database.repository.index import dabaseRepository

class AtivarServices:
    
    def selectAll():

        try:
            conection = dabaseRepository.DBConection()
            AllCompany = dabaseRepository.selectAllCompany(conection)
            
            conection.close()

            return AllCompany
        except Exception as EX:
            return False
    
    def selectOne(CNPJ):
        conection = dabaseRepository.DBConection()        
        Company = dabaseRepository.selectOneCompany(conection, CNPJ)
        return Company