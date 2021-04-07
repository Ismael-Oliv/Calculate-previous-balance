from src.pages.Exportar.Saldo_Inicial.respository.index import DBRepository

Registros = []

def ReturnRegistroC170(Connection, CompanyName, Cod_Item_H010):
    
    RegistrosC170 = DBRepository.FindXMLInRegistroC170(
                Connection, CompanyName, Cod_Item_H010)

    for RegistroC170 in RegistrosC170:
        
        [   
            chv,
            dt_Emissao,
            dt_Entrada,
            Num_Item,
            Cod_Item,
            Descricao,
            Quant,
            Unidade,
            Vl_Item,
            Vl_Desc,
            Cst,
            Cfop,

        ] = RegistroC170
        
        Registros.append({
            "chv":chv,
            "dt_Emissao":dt_Emissao,
            "dt_Entrada":dt_Entrada,
            "Sequencia": Num_Item,
            "Cod_Item": Cod_Item,
            "Descricao": Descricao,
            "QTD": Quant,
            "Unidade": Unidade,
            "Vl_Item": Vl_Item,
            "Vl_Desconto": Vl_Desc,
            "CST": Cst,
            "CFOP": Cfop
        })

    return Registros
