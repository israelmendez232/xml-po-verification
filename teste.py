
dictadasd = [
    ["Código do Fornecedor", 1, "Cod. Fornecedor"],
    ["Quantidade", 2, "Qt.Saldo"],
    ["Valor Unitário do Produto", 3, "Vl.Unit.Ped."],
    ["Valor Unitário do Saldo", 4, "Vl.Saldo"]
]

for area in dictadasd:

    case = {
        "Código do Fornecedor": 1,
        "Quantidade": 2,
        "Valor Unitário do Produto": 3,
        "Valor Unitário do Saldo": 4
    }

    print(case[area[0]])