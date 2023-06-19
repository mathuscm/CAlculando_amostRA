# solicitar o estado o qual será realizado a pesquisa
def menu_regiao():
    while True:
        menu = {
            '1': 'Norte',
            '2': 'Nordeste',
            '3': 'Centro-Oeste',
            '4': 'Sul',
            '5': 'Sudeste'
        }
        
        # percorrendo as opções 
        for chave, valor in menu.items():
            print(f' {chave} : {valor}')

        opcao = input('Selecione em qual REGIÃO a pesquisa está sendo realizada: ')
        regiao_selec = menu.get(opcao)

        if regiao_selec:
            print('A região é: ', regiao_selec)
            break
        else:
            print('Digite uma opção válida')
        
            if regiao_selec == 1:
                
                norte = {
                            '1': 'AC - Acre',
                            '2': 'AP - Amapá',
                            '3': 'AM - Amazonas',
                            '4': 'RR - Roraima',
                            '5': 'PA - Pará',
                            '6': 'RO - Rondônia',
                            '7': 'TO - Tocantins'
                }

                for chave, valor in norte.items():
                    print(f'{chave} : {valor}')

                opcao2 = input('Digite o estado em que a pesquisa está sendo realizada: ')
                estado_selec = norte.get(opcao2)

                if estado_selec:
                    print(f'A pesquisa está sendo realizada na região: {regiao_selec}, no estado de {estado_selec}')
                    break
                else:
                    print('Digite uma opção válida')

            if regiao_selec == 2:
                nordeste = {
                            '1': 'AL - Alagoas',
                            '2': 'BA - Bahia',
                            '3': 'CE - Ceará',
                            '4': 'MA - Maranhão',
                            '5': 'PB - Paraíba',
                            '6': 'PE - Pernambuco',
                            '7': 'PI - Piauí',
                            '8': 'RN - Rio Grande do Norte',
                            '9': 'SE - Sergipe'
                                }

                for chave, valor in nordeste.items():
                    print(f'{chave} : {valor}')

                opcao3 = input('Digite o estado em que a pesquisa está sendo realizada: ')
                estado_selec1 = nordeste.get(opcao3)

                if estado_selec1:
                    print(f'A pesquisa está sendo realizada na região: {regiao_selec}, no estado {estado_selec1}')
                    break
                else:
                    print('Digite uma opção válida')

            if regiao_selec == 3:
                centro_oeste = {
                            '1': 'DF - Distrito Federal',
                            '2': 'GO - Goiás',
                            '3': 'MT - Mato Grosso',
                            '4': 'MS - Mato Grosso do Sul'
                                    } 
                
                for chave, valor in centro_oeste.items():
                    print(f'{chave} : {valor}')

                opcao4 = input('Digite em qual estado a pesquisa está sendo realizada: ')
                estado_selec2 = centro_oeste.get(opcao4)

                if estado_selec2:
                    print(f'A pesquisa está sendo realizada na região: {regiao_selec}, no estado {estado_selec2}')
                    break
                else:
                    print('Digite uma opção válida')

            if regiao_selec == 4:
                sul = {
                            '1': 'PR - Curitiba',
                            '2': 'RS - Rio Grande do Sul',
                            '3': 'SC - Santa Catarina'
                    }

                for chave, valor in sul.items():
                    print(f'{chave} : {valor}')

                    opcao5 = input('Digite em qual estado a pesquisa está sendo realizada: ')
                    estado_selec3 = sul.get(opcao5)

                if estado_selec3:
                    print(f'A pesquisa está sendo realizada na região: {regiao_selec}, no estado {estado_selec3}')
                    break
                else:
                    print('Digite uma opção válida')

            if regiao_selec == 5:
                sudeste = {
                            '1': 'ES - Espírito Santo',
                            '2': 'MG - Minas Gerais',
                            '3': 'RJ - Rio de Janeiro',
                            '4': 'SP - São Paulo'
                    }
                  
                for chave, valor in sudeste.items():
                    print(f'{chave} : {valor}')

                    opcao6 = input('Digite em qual estado a pesquisa está sendo realizada: ')
                    estado_selec4 = sudeste.get(opcao6)

                if estado_selec4:
                    print(f'A pesquisa está sendo realizada na região: {regiao_selec}, no estado {estado_selec4}')
                    break
                else:
                    print('Digite uma opção válida')
                    

# solicitar dados para calcular adesão/evasão da pesquisa
def calculando_dados():
    populacao = float(input('Informe o número de habitantes no seu Estado: '))
    participantes = float(input('Informe quantas pessoas responderam à pesquisa: '))

    #calculando porcentagem de adesão
    resultado = (participantes * 100) / populacao
    print('O total de participantes da pesquisa foi de: %.2f' % resultado,'%')

    # calculando porcentagem de diferença
    diferenca = populacao - participantes
    resultado2 = (diferenca * 100) / populacao
    print('A porcentagem que não participou da pesquisa foi de; %.2f' % resultado2, '%')

    return resultado, resultado2


# execução das funções
regiao = menu_regiao()
dados = calculando_dados()


    
