while True:
    try:
        num = int(input('Informe um número: '))
    except (ValueError) as e:
        print(f'{e} Valor informado não é valido') 
    except KeyboardInterrupt as e:
        print(f'{e} Entrada interrompida pelo usuario')
        break
    else:
        print(f'Numero {num} informado com sucesso')
        break