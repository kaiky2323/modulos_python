def ajuda_moeda():
    '''
    O diretorio moeda é usado para calcular o
    dobro, a metade, o aumento de x porcento e
    a redução em x porcento.
    A Função moeda é usada para formatar a impressão, encurtando o programa principal, ela
    foi aplicada em todas as funções.
    A função tabela mostra um resumo dos valores
    '''


def metade(n=0,formato=False):
    res = n/2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def aumentando(n=0, porc=0, formato=False):
    res = n + (porc/100)*n
    return res if formato is False else moeda(res)


def diminuindo(n, porc=0, formato=False):
    res = n - (porc/100)*n
    return res if formato is False else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def tabela(preco=0, porc=0, porcm =0):
    print('-'*30)
    print('RESUMO VALOR'.center(30))
    print('-'*30)
    print(f'Valor analisado: \tR${preco:.2f}')
    print(f'Dobro do preço:  \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}', )
    print(f'{porc}% de Aumento: \t{aumentando(preco, porc, True)}')
    print(f'{porcm}% de redução: \t{diminuindo(preco, porcm, True)}')



