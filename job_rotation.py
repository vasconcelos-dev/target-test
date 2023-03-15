# 1
indice = 13
soma = k = 0

while k < indice:
    k += 1
    soma += k

print(soma) # 91

# 2
numero = int(input('Informe um número: '))
a = c = 0
b = 1

print(f'{a} {b}', end='')

while c < numero:

    c = a + b
    print(f' {c}', end='')
    a = b
    b = c

if c == numero:

    print(f'\nO número {numero} pertence a sequência de Fibonacci.')

elif c != numero:

    print(f'\nO número {numero} não pertence a sequência de Fibonacci.')

# 3
import json

with open("./dados.json") as arquivo:
    
    dados_json = json.load(arquivo)

valores = []

for dado in dados_json:
    
    if dado["valor"] > 0:
    
        valores.append(dado["valor"])

maior_faturamento = max(valores) # 48.924,2448
menor_faturamento = min(valores) # 373,7838
faturamento_medio = sum(valores) / len(valores) # 438.172,77349999995 / 21 = 20.865,370166666664
dias_acima_media = 0

for _ in valores:
        
    if _ > faturamento_medio:

        dias_acima_media += 1

print(f"O menor valor de faturamento ocorrido em um dia no mês, foi de R$ {menor_faturamento:.2f}.") # O menor valor de faturamento ocorrido em um dia no mês, foi de R$ 373.78.
print(f"O maior valor de faturamento ocorrido em um dia no mês, foi de R$ {maior_faturamento:.2f}.") # O maior valor de faturamento ocorrido em um dia no mês, foi de R$ 48924.25.
print(f"O faturamento ficou, durante {dias_acima_media} dias, acima da média mensal de R$ {faturamento_medio:.2f}.") # O faturamento ficou, durante 10 dias, acima da média mensal de R$ 20865.37.

# 4
estados = {"São Paulo": 67836.43,
            "Rio de Janeiro": 36678.66,
            "Minas Gerais": 29229.88,
            "Espírito Santo": 27165.48,
            "Outros": 19849.53}
faturamento_total = sum(estados.values())

for estado in estados:
    percentual = estados[estado] / faturamento_total * 100
    print(f'{estado}: {percentual:.2f}%.') # São Paulo: 37.53% Rio de Janeiro: 20.29% Minas Gerais: 16.17% Espírito Santo: 15.03% Outros: 10.98%

# 5
palavra = str(input("Qual é a palavra? "))

palavra_separada = palavra.strip()
palavra_invertida = palavra_separada[::-1]

print(palavra_invertida)
