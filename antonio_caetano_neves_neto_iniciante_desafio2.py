import random

nome_jogador = input('Seu nome: ')  # Definindo o nome do jogador
vetor_jogadas = ['Pedra', 'Papel', 'Tesoura']  # Definindo uma lista de jogadas, que será usado pela máquina
'''
    O conceito do programa será bem simples. Um "while true", com um for
    de 5 repetições dentro. No final do while, terá a pergunta se o jogador deseja jogar,
    se sim, continua o while, se não, é encerrado e dado a pontuação final
'''

# Inicializando as variáveis de pontuação
pontuacao_jogador = 0
pontuacao_computador = 0
while True:
    for x in range(1, 6):  # Será 5 rodadas diretas, assim sendo usado o for para contagem
        escolha_jogador = input('Qual a sua jogada(Pedra, Papel, Tesoura): ')  # Pegando a escolha do jogador
        escolha_jogador = escolha_jogador.strip() # Caso seja escrito com espaços desnecessários
        num_aleatorio = random.randrange(0, 3)  # Definindo um número aleatório pra jogada do computador
        jogada_computador = vetor_jogadas[num_aleatorio]  # Jogada do computador

        '''
            Para verificar quem ganhou, é feito uma lista de if's para cada opção de jogadas,
            ordenadas "jogada do player" vs "jogada computador"
        '''
        # Jogadas iguais, ou seja, será empate
        if escolha_jogador == jogada_computador:
            print(f'{nome_jogador} {escolha_jogador} X {jogada_computador} Computador \n Empate!')

         # Verificando casos em que não será empate
        elif escolha_jogador == 'Pedra' and jogada_computador == 'Papel':
            print(f'{nome_jogador} {escolha_jogador} X {jogada_computador} Computador \n Você Perdeu!')
            pontuacao_computador = pontuacao_computador + 1

        elif escolha_jogador == 'Pedra' and jogada_computador == 'Tesoura':
            print(f'{nome_jogador} {escolha_jogador} X {jogada_computador} Computador \n Você Venceu!')
            pontuacao_jogador = pontuacao_jogador + 1

        elif escolha_jogador == 'Papel' and jogada_computador == 'Tesoura':
            print(f'{nome_jogador} {escolha_jogador} X {jogada_computador} Computador \n Você Perdeu!')
            pontuacao_computador = pontuacao_computador + 1

        elif escolha_jogador == 'Papel' and jogada_computador == 'Pedra':
            print(f'{nome_jogador} {escolha_jogador} X {jogada_computador} Computador \n Você Venceu!')
            pontuacao_jogador = pontuacao_jogador + 1

        elif escolha_jogador == 'Tesoura' and jogada_computador == 'Papel':
            print(f'{nome_jogador} {escolha_jogador} X {jogada_computador} Computador \n Você Venceu!')
            pontuacao_jogador = pontuacao_jogador + 1

        elif escolha_jogador == 'Tesoura' and jogada_computador == 'Pedra':
            print(f'{nome_jogador} {escolha_jogador} X {jogada_computador} Computador \n Você Perdeu!')
            pontuacao_computador = pontuacao_computador + 1

    resposta = input('Você deseja continuar jogando (S/N): ')  # Pegando a resposta do jogador da continuidade
    if resposta == 'N':  # Caso a resposta seja não, é impresso o resultado
        print(f'{nome_jogador} {pontuacao_jogador} X {pontuacao_computador} Computador')
        break  # Finalizando o ciclo
