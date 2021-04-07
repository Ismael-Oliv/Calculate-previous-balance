from src.database.repository.index import dabaseRepository
from src.pages.Exportar.Saldo_Inicial.respository.index import DBRepository

def ReturnItemInH010(Connection, CompanyName, item):
    ItensH010 = []

    for item in DBRepository.FindItemInH010(Connection, CompanyName, item):
        
        ItensH010.append({
            "COD_ITEM":item[0],
            "UNID":item[1],
            "QTD":item[2],
            "VL_UNIT":item[3],
            "VL_ITEM":item[4]
        })

    return ItensH010