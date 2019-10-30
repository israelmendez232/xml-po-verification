import os 
import pandas as pd
import xml.etree.ElementTree as ET


uglyXML = 'Pedidos e Notas/XML/CARDEAL - NFe 151434.xml'
uglyPO = 'Pedidos e Notas/PO/Pedido 26877 Cardeal (Nota 151434).xlsx'

def prettyPO(uglyPO): 
    return pd.read_excel(uglyPO)

def prettyXML(uglyXML):
    tree = ET.parse(uglyXML)
    root = tree.getroot()

    CNPJ = int(root[0][0][1][0].text)

    arrayTotal = []
    # Encontrando os products:
    for element in root[0][0]:

        # Se for product, continua no Loop específico:
        if 'det' in str(element.tag):
            products = element[0]
            array = []

            # Insere os detalhes do product na DF:
            for product in products:
                i = 0
                array.insert(i, product.text)
                i+=1
            
            arrayTotal.append(array)

    return CNPJ, pd.DataFrame(arrayTotal, columns = [
        'cProd', 
        'EAN', 
        'Nome do Produto',
        'NCM',
        'CEST',
        'CFOP',
        'uCom',
        'qCom',
        'vUnCom',
        'vProd',
        'cEANTrib',
        'uTrib',
        'qTrib',
        'vUnTrib',
        'indTot'
    ])

def verification(po, xml, CNPJ): # Etapas da Verificação:
    # 1. CNPJ
    if CNPJ != po.iloc[0][0]:
        Alert(False, "CNPJ", CNPJ)
    else: 
        Alert(True, "CNPJ", CNPJ)
    
    areas = [
        ["Código do Fornecedor", "Cod. Fornecedor"],
        ["Quantidade", "Qt.Saldo"],
        ["Valor Unitário do Produto", "Vl.Unit.Ped."],
        ["Valor Unitário do Saldo", "Vl.Saldo"]
    ]
    
    for area in areas:
        for row in xml.iterrows():
            # 2. EAN
            EAN = row[1][4]

            try: 
                linha = po.loc[po['Ean'] == int(EAN)]
            except: 
                Alert(False, "EAN", EAN)

            area = area[0]
            try: 
                valorNota = float(area[1])

                case = {
                    "Código do Fornecedor": row[1][0],
                    "Quantidade": row[1][7],
                    "Valor Unitário do Produto": row[1][8],
                    "Valor Unitário do Saldo": row[1][5]
                }

                valorXML = float(linha[case[area[0]]].values)
            
                if valorNota != valorXML:
                    detailedAlert(area, row[1][12], EAN, valorNota, valorXML)
            except Exception as e: 
                print(e)

        Alert(True, "EAN", 1)
        Alert(True, "Quantidade", 1)
        Alert(True, "Valor Unitário do Produto", 1)
        Alert(True, "Valor Total do Produto", 1)


def Alert(success, element, value):
    if success:
        print("{} seguiu com sucesso: ✓ ".format(element))
    else:
        print("{} apresentou problema: {}".format(element, value))

def detailedAlert(element, product, ean, poValue, xmlValue):
    print("\n{} está divergente.".format(element))
    print("Produto: {}. EAN: {}. (Nota) {} ≠ {} (XML) \n".format(product, ean, poValue, xmlValue))


def main(uglyXML, uglyPO):
    po = prettyPO(uglyPO)
    CNPJ, xml = prettyXML(uglyXML)

    verification(po, xml, CNPJ)

main(uglyXML, uglyPO)
