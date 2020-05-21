"""
    O segredo do código vai estar em um "while" em que vai verificar se o
    módulo de todos os números recebidos pelo input é igual a zero, se não,
    ele soma um ao valor da variável e repete até achar o MMC.

    Para o MDC, eu acho o maior números dos recebidos pelo input e atribuio na
    variável MDC, verifico se o módulo de todos os números em relaçao ao valor
    da variável MDC, se não der, diminuo o valor da variável e repete até achar
    o MDC
"""
# Definindo minha lista de números pegados pelos inputs
numeros = [input('Primeiro número: '),
           input('Segundo número: '),
           input('Terceiro número: '),
           input('Quarto número: '),
           input('Quinto número: ')]

'''
    Começando as verificações propostas. Faz a verificação
    se todos são números naturais, para isso, usando a verificação "num_x.isdigit()" 
    para todos os números. Se passar, quer dizer que são naturais. Se não, emite
    a mensagem avisando. Para saber se é maior que 10000, faz um IF com as 
    condicionais de todos os números < 10000, se for maior, o programa não é realizado
'''

limite = 10000  # Definindo o limite dos números, como foi proposto, será 10000
definidores = True  # Variável que definirá se o program irá executar as operações,
# isso caso obedecer as condições presentes
x = 0 # Variável de indice do vetor atual
for num in numeros:  # Rodando o vetor de números
    if num.isdigit():  # Verifica se é natural
        if int(num) <= limite:  # Verifica se está abaixo do limite ou igual
            numeros[x] = int(num)  # Se tiver, transforma a string do index do vetor em inteiro
        else:
            print("O meu programa não é obrigado a calcular isso")  # Mensagem de erro
            definidores = False  # O programa não será mais executado
    else:
        print("Não é possível calcular m.m.c e m.d.c com os números fornecidos")  # Mensagem de erro
        definidores = False  # O programa não será mais executado
    x = x + 1
if definidores:
    '''
        Para saber se um número é primo ou não, irei realizar um 
        "for x in range(2, num-1)", e verificando se o modulo do num sobre o x
        é igual a zero, se sim, ele não é primo. O range é dessa forma para
        evitar o 1 e o próprio número
    '''
    for num in numeros:
        primo = True  # Variável de verificação de número primo
        for x in range(2, num-1):
            if num % x == 0:  # Se o resultado do módulo for verdadeiro, quer dizer que o número não é primo
                primo = False
        if primo:
            print(f'O número {num} é primo')

    # Achando o Minimo multiplo comum
    min_mult_comum = 1
    while True:  # Vai ficar repetindo até a função "break" ser ativada
        if min_mult_comum % numeros[0] == 0 and min_mult_comum % numeros[1] == 0 and min_mult_comum % numeros[2] == 0 and min_mult_comum % numeros[3] == 0 and min_mult_comum % numeros[4] == 0:
            break  # Caso o módulo de todas as operações for igual a zero, quer dizer que o MMC foi achado
        min_mult_comum = min_mult_comum + 1  # Como esse não é o mmc , tente novamente com o seu sucessor

    print(f'O mínimo multiplo comum é {min_mult_comum}')

    # Achando o Máximo divisor comum
    max_div_comum = max(numeros[0], numeros[1], numeros[2], numeros[3], numeros[4])
    while True:  # Vai ficar repetindo até a função "break" ser ativada
        if numeros[0] % max_div_comum == 0 and numeros[1] % max_div_comum == 0 and numeros[2] % max_div_comum == 0 and numeros[3] % max_div_comum == 0 and numeros[4] % max_div_comum == 0:
            break  # Caso o módulo de todas as operações for igual a zero, quer dizer que o MDC foi achado
        max_div_comum = max_div_comum - 1  # Como esse não é o MDC, tente novamente com o seu antecessor

    print(f'O máximo divisor comum é {max_div_comum}')
