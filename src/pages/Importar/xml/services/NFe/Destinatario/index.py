def Destinatario(dest):
    arrTag = []

    for tag in dest:
        arrTag.append(tag)

    if 'CNPJ' in arrTag:
        CNPJ = dest['CNPJ']
    else:
        CNPJ = '0'

    if 'IE' in arrTag:
        IE = dest['IE']
    else:
        IE = '0'

    Dest = [CNPJ, IE]
    return Dest
