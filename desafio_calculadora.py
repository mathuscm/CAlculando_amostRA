print('='*102)
print('                    Relatório de estimativa de pessoas esperadas para a contribuição\n                    da pesquisa realizada pela ONG de preservação do meio ambiente.'.upper())
print('='*102)

estado = input('Em qual estado esta pesquisa está sendo realizada? (Digite apenas a sigla, por exemplo: MG): '.upper())
populacao = float(input('Informe o número de habitantes no seu Estado: '))
participantes = float(input('Informe quantas pessoas responderam à pesquisa: '))


# quantas pessoas precisam ser entrevistadas?
expectativa_minima = (0.50 * populacao)/ participantes
populacao_necessaria = 25%100  # z score
margem_erro = (0.05 * populacao_necessaria) / (participantes ** 0.5) # desvio padrão 

print('A expectativa é que a pesquisa atinja até 50% da população.\nO número necessário é de 25% da população.')

# calculo do resultado de adesão à pesquisa 
resultado = (participantes * 100)/ populacao
print(populacao_necessaria-resultado)
print('O total de participantes da pesquisa foi de: %.2f' % resultado,'%')
diferenca = populacao - participantes
print( '%.0f' %  diferenca, 'pessoas não participaram da pesquisa.')

# qual a margem de erro?

resultado2 = (diferenca * 100)/ populacao
print('A porcentagem que não participou da pesquisa foi de; %.2f' % resultado2, '%')
atingir = resultado - 25 
print('%.2f' % atingir)














'''def menu_estado():
    while True:
        estado = input('Selecione em qual REGIÃO a pesquisa está sendo realizada: ')
        menu = {
            '1': 'Norte',
            '2': 'Nordeste',
            '3': 'Centro-Oeste',
            '4': 'Sul',
            '5': 'Sudeste'
        }

        for chave, valor in menu:
            print(f' {chave} : {valor}')

        estado_selecionado = input('Opção: ')'''
''''1': 'AC',
        '2': 'AL',
        '3': 'AP',
        '4': 'AM',
        '5': 'BA',
        '6': 'CE',
        '7': 'DF',
        '8': 'ES',
        '9': 'GO',
        '10': 'MA',
        '11': 'MT',
        '12': 'MS',
        '13': 'MG',
        '14': 'PA',
        '15': 'PB',
        '16': 'PR','''
