from desafio109_formatação import funcão_moeda
from funcão_moeda import moeda
import desafio108_formatação
n = float(input('Digite um valor: R$').replace(',','.'))
print(f'O dobro de {moeda(n)} é {funcão_moeda.dobro(n, True)}')
print(f'A Metade de {moeda(n)} é {funcão_moeda.metade(n, True)}')
print(f'Aumentand0 10% de {moeda(n)} temos R${funcão_moeda.aumentando(n, True)}')
print(f'Diminuindo 13% de {moeda(n)} temos {funcão_moeda.diminuindo(n, True)}')