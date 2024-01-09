#  copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

novos_produtos = [
    {**p, 'preco': round(p['preco']*1.1, 2)} for p in copy.deepcopy(produtos)
]

produtos_em_ordem_por_valor_crescente = sorted(novos_produtos, key = lambda preco_asc: preco_asc['preco'])
produtos_em_ordem_por_valor_decrescente = sorted(novos_produtos, key = lambda preco_desc: preco_desc['preco'], reverse=True)
produtos_em_ordem_por_nome_crescente = sorted(novos_produtos, key = lambda preco_desc: preco_desc['nome'])
produtos_em_ordem_por_nome_decrescente = sorted(novos_produtos, key = lambda preco_desc: preco_desc['nome'], reverse=True)

print(*produtos,sep='\n')
print()
print(*novos_produtos,sep='\n')
print()
print(*produtos_em_ordem_por_valor_crescente,sep='\n')
print()
print(*produtos_em_ordem_por_valor_decrescente,sep='\n')
print()
print(*produtos_em_ordem_por_nome_crescente,sep='\n')
print()
print(*produtos_em_ordem_por_nome_decrescente,sep='\n')