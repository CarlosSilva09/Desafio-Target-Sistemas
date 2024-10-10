# Questão 4
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcular o faturamento total dos estados 
faturamento_total = sum(faturamento_estados.values())

# Calcular o percentual de cada estados
percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()}

print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
