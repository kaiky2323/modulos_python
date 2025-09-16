import funcão_moeda

n = float(input('Digite um valor: R$'))
print(f'O dobro de R${n:.2f} é R${funcão_moeda.dobro(n)}')
print(f'A Metade de R${n:.2f} é R${funcão_moeda.metade(n)}')
print(f'Aumentand0 10% de R${n:.2f} temos R${funcão_moeda.aumentando(n)}')
print(f'Diminuindo 13% de R${n:.2f} temos R${funcão_moeda.diminuindo(n)}')