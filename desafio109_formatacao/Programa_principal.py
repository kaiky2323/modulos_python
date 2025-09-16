import funcão_moeda


n = float(input('Digite um valor: R$'))
print(f'O dobro de R${n:.2f} é {funcão_moeda.dobro(n, True)}')
print(f'A Metade de R${n:.2f} é {funcão_moeda.metade(n, True)}')
print(f'Aumentando 10% de R${n:.2f} temos {funcão_moeda.aumentando(n, 10,True)}')
print(f'Diminuindo 13% de R${n:.2f} temos {funcão_moeda.diminuindo(n, 13, True)}')