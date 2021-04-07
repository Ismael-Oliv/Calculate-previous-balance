def Impostos(Itens):

    arrImpostos = []

    for ICMS in Itens:

        if type(ICMS) == str:
            arrTipoImposto = []
            if ICMS == 'imposto':
                
                arrTagImp = []
                for TagImp in Itens['imposto']:
                    arrTagImp.append(TagImp)

                if 'ICMS' in arrTagImp:

                    for tag in Itens[ICMS]['ICMS']:
                        tag = tag

                    ImpostoICMS = Itens[ICMS]['ICMS'][tag]

                    for tag in ImpostoICMS:
                        arrTipoImposto.append(tag)

                    orig = ImpostoICMS['orig']

                    if 'CST' in arrTipoImposto:
                        CST = ImpostoICMS['CST']
                    else:

                        if 'CSOSN' in arrTipoImposto:
                            CST = ImpostoICMS['CSOSN']

                        if 'CSOSN101' in arrTipoImposto:
                            CST = ImpostoICMS['CSOSN101']

                    if 'vBC' in arrTipoImposto:
                        vBC = float(ImpostoICMS['vBC'])
                    else:
                        vBC = 0

                    if 'vICMS' in arrTipoImposto:
                        vICMS = float(ImpostoICMS['vICMS'])
                    else:
                        vICMS = 0

                    if 'vBCST' in arrTipoImposto:
                        vBCST = float(ImpostoICMS['vBCST'])
                    else:
                        vBCST = 0

                    if 'vICMSST' in arrTipoImposto:
                        vICMSST = float(ImpostoICMS['vICMSST'])
                    else:
                        vICMSST = 0

                    TotalICMSProprio = vICMS
                    TotalICMSSt = float(vICMSST)

                    infoImpostos = [orig, CST, TotalICMSProprio, TotalICMSSt]
                    arrImpostos.append(infoImpostos)

        if type(ICMS) != str:

            arrTipoImposto = []
            arrTagImp = []

            for tagImp in ICMS['imposto']:
                arrTagImp.append(tagImp)

            if 'ICMS' in arrTagImp:

                ImpostoICMS = ICMS['imposto']['ICMS']
                for tag in ImpostoICMS:
                    tag = tag

                for tipo in ImpostoICMS[tag]:
                    arrTipoImposto.append(tipo)

                orig = ImpostoICMS[tag]['orig']

                if 'CST' in arrTipoImposto:
                    CST = ImpostoICMS[tag]['CST']
                else:

                    if'CSOSN' in arrTipoImposto:
                        CST = ImpostoICMS[tag]['CSOSN']

                    if'CSOSN101' in arrTipoImposto:
                        CST = ImpostoICMS[tag]['CSOSN101']

                if 'vBC' in arrTipoImposto:
                    vBC = float(ImpostoICMS[tag]['vBC'])
                else:
                    vBC = 0

                if 'vICMS' in arrTipoImposto:
                    vICMS = float(ImpostoICMS[tag]['vICMS'])
                else:
                    vICMS = 0

                if 'vBCST' in arrTipoImposto:
                    vBCST = float(ImpostoICMS[tag]['vBCST'])
                else:
                    vBCST = 0

                if 'vICMSST' in arrTipoImposto:
                    vICMSST = float(ImpostoICMS[tag]['vICMSST'])
                else:
                    vICMSST = 0

                TotalICMSProprio = vICMS
                TotalICMSSt = vICMSST

                infoImpostos = [orig, CST, TotalICMSProprio, TotalICMSSt]
                arrImpostos.append(infoImpostos)

    return arrImpostos
