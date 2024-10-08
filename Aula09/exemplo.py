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
    
try:
    txt = input('Informe um nome: ')[0]
except IndexError as e:
    print("Voce precisa digitar algum nome")
else:
    print('Acertou!')
finally:
    print('Sempre executado')
