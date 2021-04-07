def Identificador(ide):

    arrTag = []
    for tag in ide:
        arrTag.append(tag)

    nNF = ide['nNF']

    if 'dhEmi' in arrTag:
        dhEmi = ide['dhEmi']
    else:
        dhEmi = '0'

    if 'dhSaiEnt' in arrTag:
        dhSaiEnt = ide['dhSaiEnt']
    else:
        dhSaiEnt = '0'

    Ide = [nNF, dhEmi, dhSaiEnt]

    return Ide
