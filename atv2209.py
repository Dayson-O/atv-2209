compras = [
    {"produto": "Arroz", "preco": 20.0, "quantidade": 2},
    {"produto": "Feijão", "preco": 8.0, "quantidade": 1},
    {"produto": "Leite", "preco": 5.0, "quantidade": 3},
    {"produto": "Pão", "preco": 0.5, "quantidade": 10},
    {"produto": "Café", "preco": 12.0, "quantidade": 1}
]

print("\n")

for item in compras:
    print(f"Produto: {item['produto']} | Preço: {item['preco']} | Quantidade: {item['quantidade']}")

total = 0
maiscaro = compras[0]
maisquantidade = compras[0]

for item in compras:
    total += item['preco'] * item['quantidade']
    if item['preco'] > maiscaro['preco']:
        maiscaro = item
    if item['quantidade'] > maisquantidade['quantidade']:
        maisquantidade = item

print("\nResumo da Compra:")
print(f"Total de itens diferentes: {len(compras)}")
print(f"Total gasto: R$ {total}")
print(f"Produto mais caro: {maiscaro['produto']} | Preço: R$ {maiscaro['preco']}")
print(f"Produto com maior quantidade: {maisquantidade['produto']} | Quantidade: {maisquantidade['quantidade']}")
print(f"\n")