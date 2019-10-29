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
        Alert("CNPJ", CNPJ)

    for row in xml.iterrows():
        # 2. EAN
        EAN = row[1][1]

        try: 
            linha = po.loc[po['Ean'] == 7896447104592]
            print(linha)
        except: 
            Alert("EAN", EAN)
            
        # 3. Quantidade

        # 4. Valor Unitário do product

        # 5. Valor Total do Saldo


def Alert(element, value):
    print("{} apresentou problema: {}".format(element, value))

def main(uglyXML, uglyPO):
    po = prettyPO(uglyPO)
    CNPJ, xml = prettyXML(uglyXML)

    verification(po, xml, CNPJ)

main(uglyXML, uglyPO)
