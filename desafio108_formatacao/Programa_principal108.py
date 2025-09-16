from funcao_moeda import funcao_moeda
from funcao_moeda import funcao_moeda
n = float(input('Digite um valor: R$').replace(',','.'))
print(f'O dobro de {funcao_moeda.moeda(n)} é R${funcao_moeda.moeda((funcao_moeda.dobro(n)))}')
print(f'A Metade de {funcao_moeda.moeda(n)} é R${funcao_moeda.moeda(funcao_moeda.metade(n))}')
print(f'Aumentand0 10% de {funcao_moeda.moeda(n)} temos R${funcao_moeda.moeda(funcao_moeda.aumentando(n))}')
