def leiaint(num = 0):
    validado = False
    valor = 0
    while not validado:
        try:
            inteiro = int(input(num).strip())
            valor = inteiro

        except KeyboardInterrupt:
            print(f'\n\033[31mO Usuario optou por não digitar nenhum numero\033[m')
            return 0

        except:
            print(f'\033[31mERRO! Digite um numero inteiro valido\33[m')

        else:
            validado = True

    return valor



def leiareal(num = 0):
    validado = False
    valor = 0
    while not validado:
        try:
            real = float(input(num).strip().replace(',', '.'))
            valor = real

        except KeyboardInterrupt:
            print(f'\n\033[31mO Usuario optou por não digitar nenhum numero\033[m')
            return 0

        except:
            print(f'\033[31mERRO! Digite um numero real valido\33[m')

        else:
            validado = True

    return float(f'{valor:.2f}')

