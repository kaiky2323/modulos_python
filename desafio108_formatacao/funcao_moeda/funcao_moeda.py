def metade(n=0):
    res = n/2
    return res

def dobro(n=0):
    res = n * 2
    return res

def aumentando(n=0):
    res = n + (10/100)*n
    return res


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n}'.replace('.', ',')