def Emitente(emit):

    arrTag = []

    for tag in emit:
        arrTag.append(tag)

    if 'CNPJ' in arrTag:
        CNPJ = emit['CNPJ']
    else:
        CNPJ = '0'

    if 'IE' in arrTag:
        IE = emit['IE']
    else:
        IE = '0'

    Emit = [CNPJ, IE]
    return Emit
