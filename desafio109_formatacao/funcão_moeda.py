

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
    return f'{moeda}{n:.2f}'.replace('.', ',')





