def leiadinheiro(preco):
    validacao = False
    while not validacao:
        numero = str(input(preco)).replace(',', '.')
        if numero.isalpha() or numero.strip() == '':
            print(f'ERRO \"{numero}\" é um preço invalido')
        else:
            validacao = True
            return float(numero)
