# solicitar o estado o qual será realizado a pesquisa
def menu_estado():
    estado = input('Em qual estado esta pesquisa está sendo realizada? (Digite apenas a sigla, por exemplo: MG): '.upper())
        
    return estado

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
estado = menu_estado()
dados = calculando_dados()


    
