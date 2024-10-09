# try:
#     n = int(input('Informe um numero :'))
# except:
#     print('Erro!')



# try:
#     n = int(input('Informe um numero :'))
# except (ValueError,KeyboardInterrupt) as e:
#     print(f'Erro: {e}')
# # except KeyboardInterrupt:
# #     print('\nO Usuário cancelou a operacao')
    
# try:
#     txt = input('Informe um nome: ')[0]
# except IndexError as e:
#     print("Voce precisa digitar algum nome")
# else:
#     print('Acertou!')
# finally:
#     print('Sempre executado')


try:
    resp =input('Informe (S/N): ').lower()

    if resp == '':
        raise EOFError('Voce não digitou nada')
    if resp.isdigit():
        raise ValueError('Não informe Números')
except EOFError as e:
    print(f'{e}')
except ValueError as e:
    print(f'{e}')