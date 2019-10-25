import os 
import pandas as pd
import xml.etree.ElementTree as et


uglyXML = 'Pedidos e Notas/XML/CARDEAL - NFe 151434.xml'
uglyPO = 'Pedidos e Notas/PO/Pedido 26877 Cardeal (Nota 151434).xlsx'

def prettyPO(uglyPO): 
    return pd.read_excel(uglyPO)

def prettyXML(uglyXML):
    etree = ET.fromstring(uglyXML)
    dfcols = ['id', 'name']
    df = pd.DataFrame(columns=dfcols)

    for i in etree.iter(tag='data'):
        df = df.append(
                pd.Series([i.get('id'), i.get('name')], index=dfcols),
                ignore_index=True
            )

    return df

def verification(uglyXML, uglyPO):
    po = prettyPO(uglyPO)
    xml = prettyXML(uglyXML)


def main(uglyXML, uglyPO):
    verification(uglyXML, uglyPO)

# main(uglyXML, uglyPO)

print(prettyPO(uglyPO))
# print(prettyXML(uglyXML))
