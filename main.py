#
# CHATBOT PARA REALIZAÇÃO DE PEDIDOS E ESCLARECIMENTO DE DÚVIDAS
#

import re
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

global flag
flag     = 0

# DICIONÁRIO ONDE É REALIZADA A LISTAGEM DOS SABORES
sabores = [
    {'[0] -': 'Balãozinho de Presunto e Queijo'},
    {'[1] -': 'Bolinha de Queijo'},
    {'[2] -': 'Coxinha de Carne'},
    {'[3] -': 'Coxinha de Frango'},
    {'[4] -': 'Enroladinho de Calabresa'},
    {'[5] -': 'Enroladinho de Salsicha'},
    {'[6] -': 'Quibe'}
]

# FUNÇÃO UTILIZADA PARA FAZER A LISTAGEM DOS SABORES NO DICIONÁRIO
def lista_sabores():
    for sabor in sabores:
        for numero, descricao in sabor.items():
            print(numero, descricao)
    
    print('')

# FUNÇÃO QUE REALIZA A SOLICITAÇÃO DOS PEDIDOS
def solicita_pedido():
    
    global sabores_replace
    global qtd_sabores
    global flag
    
    flag            = 0
    escolha_sabores = []
    sabores_replace = []
    qtd_sabores     = []
    index_sabores   = ['primeiro', 'segundo', 'terceiro']
    
    lista_sabores()

    # SOLICITA A ESCOLHA DOS SABORES E QUANTIDADE DE SALGADOS
    index = 0
    while index < 3:
        
        sabores_user = input(f'Escolha o {index_sabores[index]} sabor (Até 3 sabores diferentes): ')        

            # VALIDA SE O VALOR INFORMADO PELO USUÁRIO É NUMERICO
        if sabores_user.isdigit():
            sabores_user_int = int(sabores_user)

            # BLOQUEIO CASO O VALOR INFORMADO FOR MAIR QUE 6
            if sabores_user_int > 6:
                print('Opção selecionada invalida! Por gentileza informar numeração de 0 a 6.')                

            else:
                # REALIZA O PROCEDIMENTO DA COLETA DOS SABORES E QUANTIDADE
                escolha_sabores.append(sabores[sabores_user_int])
                
                global escolha_sabores_str
                escolha_sabores_str = str(escolha_sabores[index]).replace('{','').replace('}','').replace("'","")\
                    .replace(':','').replace('[','').replace(']','').replace('-','').replace('0','').replace('1','')\
                    .replace('2','').replace('3','').replace('4','').replace('5','').replace('6','')
                sabores_replace.append(escolha_sabores_str)

                qtd_user = input('Agora escolha a quantidade: ')
                print('')
                qtd_user_int = int(qtd_user)
                qtd_sabores.append(qtd_user_int)

                index += 1

                global soma_qtd
                soma_qtd = sum(qtd_sabores)
            
        else:
            print('Valor informado não é um digito, por gentileza refaça a escolha! 😕')

    solicita_endereco()
    solicita_forma_pagamento()

    if entrada_pedido_int == 0:
        if soma_qtd < 100 or soma_qtd > 100:
            print('Quantidade total de salgados não é 100, refaça o pedido! 😕')
            print('')
            solicita_pedido()
            flag = 0

        else:
            confirma_escolha()
            flag = 10

    if entrada_pedido_int == 1:
        if soma_qtd < 50 or soma_qtd > 50:
            print('Quantidade total de salgados não é 50, refaça o pedido! 😕')
            print('')
            solicita_pedido()
            flag = 0
            
        else:
            confirma_escolha()
            flag = 10

# FUNÇÃO PARA SOLICITAR A FORMA DE PAGAMENTO
def solicita_forma_pagamento():

    global cartao
    global dinheiro
    global pix
    
    cartao   = False
    dinheiro = False
    pix      = False

    dinheiro_cliente_float = 0
    
    print('Formas de pagamento:')
    print('[0] - Cartão Débito/Crédito')
    print('[1] - Dinheiro')
    print('[2] - PIX')
    escolha_pagamento = input('Escolha uma das opções (0 a 2): ')

    if escolha_pagamento.isdigit():
        escolha_pagamento_int = int(escolha_pagamento)        
        
        if escolha_pagamento_int == 0:
            cartao = True
        
        elif escolha_pagamento_int == 1:
            dinheiro = True
            
            dinheiro_cliente = input('Por gentileza, informar o valor para calcularmos o troco: ')

            if dinheiro_cliente.isdigit():
                dinheiro_cliente_float = float(dinheiro_cliente)

                global troco_cliente

                if entrada_pedido_int == 0:
                    troco_cliente = dinheiro_cliente_float - 89.90

                elif entrada_pedido_int == 1:
                    troco_cliente = dinheiro_cliente_float - 44.90

            else:
                print('Valor informado não é numérico! 😕')
        
        elif escolha_pagamento_int == 2:
            pix = True

        else:
            print('Opção selecionada invalida! Por gentileza informar numeração de 0 a 2. 😕')
            solicita_forma_pagamento()

    else:
        print('Opção selecionada não numérica! 😕')
        solicita_forma_pagamento()

# FUNÇÃO PARA APRESENTAR A FORMA DE PAGAMENTO
def apresenta_pagamento():
    if cartao == True:
        print('Enviaremos a máquina de cartão de crédito/débito!')

    elif dinheiro == True and entrada_pedido_int == 0:
        print(f'Seu troco é: {troco_cliente:0.2f}')

    elif dinheiro == True and entrada_pedido_int == 1:
        print(f'Seu troco é: {troco_cliente:0.2f}')

    elif pix == True:
        print('Minha chave pix é XXX.XXX.XXX-XX, por gentileza enviar comprovante de transferência!')

# FUNÇÃO UTILIZADA PARA APRESENTAR OS SABORES E QUANTIDADES ESCOLHIDAS PELO USUÁRIO
def apresenta_escolha():    
    
    print('Sabores escolhidos e quantidades 📋')
    index = 0
    
    while index < 3:
        print(f'{sabores_replace[index]} - {qtd_sabores[index]}')
        index += 1
    
    print('Total de salgados:', soma_qtd)
    print('')
    
    flag = 10

# REALIZA A SOLICITAÇÃO DO ENDEREÇO DE ENTREGA DO CLIENTE
def solicita_endereco():
    
    global rua
    global numero_casa
    global cep
    
    rua         = input('Digite o nome da rua/avenida: ')
    numero_casa = input('Digite o número do endereço: ')
    cep         = input('Digite o CEP (Somente Números): ')
    print('')
    
    padrao_cep = r'^\d{5}\d{3}$'
    
    while True:

        if numero_casa.isdigit():            
        
            if re.match(padrao_cep, cep):                
                break
    
            else:
                print('CEP incorreto! 😕')
                solicita_endereco()
        
        else:
            print('Número informado invalido! 😕')
            solicita_endereco()
    
    global flag
    flag = 0

# APRESENTA O ENDEREÇO INFORMADO PELO CLIENTE
def apresenta_endereco():
    print('Endereço informado 📍')
    print('Rua/Avenida: ', rua)
    print('Número: ', numero_casa)
    print('CEP: ', cep)
    print('')

# CONFIRMA AS ESCOLHAS DO USUÁRIO
def confirma_escolha():    
    print('[0] - Sim')
    print('[1] - Não')    
    confirma_escolha_user = input('Informações estão corretas? 🤔: ')
    print('')

    if confirma_escolha_user.isdigit():
        confirma_escolha_int = int(confirma_escolha_user)
            
        if confirma_escolha_int == 0:
            print('Pedido gerado com sucesso! 😁\n')
            print('Dados do pedido:\n')
            apresenta_escolha()
            apresenta_endereco()
            apresenta_pagamento()
            
            flag = 10
    
        elif confirma_escolha_int == 1:
            solicita_pedido()            
            flag = 0
    
    else:
        print('Opção selecionada invalida! Por gentileza informar 0 ou 1.')

print('Olá, bem-vindo(a) a xxxxxxxxx! 😀\n')

print('Estamos muito contentes em recebê-lo(a) aqui. 😁\n\
Sou o assistente virtual da xxxxxxxxx e estou aqui para responder às suas perguntas,\
 fornecer informações sobre nossos deliciosos salgados e auxiliá-lo(a)\
 com qualquer dúvida que você possa ter.\n')

while True:
    print('O que gostaria de saber sobre nossos produtos?\n')
    print('[0] - Valor do cento(100) do salgado 💰')
    print('[1] - Valor do meio cento(50) do salgado 💰')
    print('[2] - Sabores disponíveis 😋')
    print('[3] - Realizar Pedido 📖')
    print('[4] - Sair ❌\n')
    user_option = input('Escolha uma das opções(0 a 4): ')
    print('')

    if user_option.isdigit():    
        
        option_int = int(user_option)

        # LISTA O VALOR DO CENTO
        if option_int == 0:
            print('O valor do cento(100) do salgado é R$ 89,90\n')
    
        # LISTA O VALOR DO MEIO CENTO
        elif option_int == 1:
            print('O valor do meio cento(50) do salgado é R$ 44,90\n')
    
        # LISTA SABORES
        elif option_int == 2:
            lista_sabores()        

        # REALIZA A INICIAÇÃO DA SOLICITAÇÃO DOS PEDIDOS
        elif option_int == 3:            
            
            while True:
                print('[0] - Fazer pedido de um cento(100 Salgados)')
                print('[1] - Fazer pedido de meio cento(50 Salgados)')
                print('[2] - Voltar\n')                
                entrada_pedido = input('Escolha uma das opções(0 a 2): ')
                print('')

                if entrada_pedido.isdigit():
                    entrada_pedido_int = int(entrada_pedido)

                    # SOLICITAÇÃO DE PEDIDO DO CENTO DE SALGADO
                    if entrada_pedido_int == 0:
                        solicita_pedido()
                        
                        if flag == 10:
                            break

                    # SOLICITAÇÃO DE PEDIDO DO MEIO CENTO DE SALGADO
                    elif entrada_pedido_int == 1:                        
                        solicita_pedido()

                        if flag == 10:
                            break

                    elif entrada_pedido_int == 2:
                        break

                    else:
                        print('Opção selecionada invalida! Por gentileza informar numeração de 0 a 2. 😕')
                
                else:
                    print('Opção selecionada não numérica! 😕')

        # REALIZA A SAIDA DO BOT
        elif option_int == 4:
            break
    
    else:
        print('Opção selecionada invalida! Por gentileza informar numeração de 0 a 4. 😕')

    if flag == 10:
        break