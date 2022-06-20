'''
Instituto Federal da Bahia - IFBA
Curso: Análise e Desenvolvimento de Sistemas - ADS
Aluno: Ives dos Anjos Seixas Rodrigues
Professor: Domingos Mainart
Data: 09/12/2021
Disciplina: Python - INF032D 2021.2
Avaliação: Projeto final - Jogo de Adivinhação
'''

import random   # Importando biblioteca para números aleatórios


def secreto(inicio, fim):  # Função para determinar número aleatório secreto
    ini_num_aleatorio = inicio
    fim_num_aleatorio = fim
    comeco = int(ini_num_aleatorio)
    final = int(fim_num_aleatorio)
    num_sec = random.randint(comeco, final)
    #return num_sec


def repeticao(x):
    repito = x
    while repito == 1:
        jogo_adivinhacao()
        repito = int(input('\nDeseja jogar de novo?\n(1)Sim ou (2)Não:'))

    if repito == 2:
        print('Até mais!!!')


def jogo_adivinhacao():  # Função para execução e configurações iniciais do jogo
    ponto = 100
    tentativas, ponto_fracao, ponto_certo = 0, 0, 0

    print('\nVamos definir um intervalo?')
    ini_num_aleatorio = input('Digite o início do intervalo:')
    fim_num_aleatorio = input('Digite o final do intervalo:')

    if ini_num_aleatorio.isnumeric() == False or fim_num_aleatorio.isnumeric() == False:
        print('\n\033[0;31mDigite um número, por favor.\033[m')
        jogo_adivinhacao()

    num_secreto = secreto(ini_num_aleatorio, fim_num_aleatorio)
    print(num_secreto)
    nivel = input('Digite a dificuldade do jogo:\n(1) Fácil\n(2) Médio\n(3) Difícil:')

    # Definindo nível do jogo
    if nivel.isnumeric() == True:
        nivel = int(nivel)
        if nivel == 1:
            tentativas = 10
            ponto_fracao = ponto / tentativas
        elif nivel == 2:
            tentativas = 5
            ponto_fracao = ponto / tentativas
        else:
            tentativas = 3
            ponto_fracao = ponto / tentativas
    else:
        print('\n\033[0;31mDefina um nível digitando um número válido, por favor.\033[m')
        jogo_adivinhacao()

    # Verificação dos número ante o número secreto
    chute = 0
    for i in range(0, tentativas):  # Loop definido pelo número de tentativas
        if chute != num_secreto and i <= tentativas:
            # Compara se o chute é diferente do número secreto
            # Compara e controla se a rodada é menor ou igual ao número de tentativaas
            i = i + 1
            print(f'\nEssa é sua tentativa {i} de {tentativas}:')
            chute = input('Qual será o número secreto? Dê seu chute:')

            if chute.isnumeric() == True:  # Função verifica se a entrada é número ou não como booleano (true ou False)
                chute = int(chute)
                if int(ini_num_aleatorio) > chute or chute > int(fim_num_aleatorio):
                    print('\n\033[0;31mVocê digitou um número fora do intervalo estabelecido.\033[m\n')
                else:
                    if chute == num_secreto:
                        print('\n\033[0;32mVocê ACERTOU!!!\033[m')
                        if i == 1:
                            print('Parabéns, você conseguiu!!! Sua pontuação foi:', ponto)
                            break
                        elif i == 5:  # Definição das pontuações
                            ponto_certo = round((ponto / i) / 5, 2)
                        elif i == 3:
                            ponto_certo = round((ponto / i) / 3, 2)
                        else:
                            ponto_certo = round(ponto - (ponto_fracao * i), 2)

                        print(f'Parabéns, você conseguiu!!! Sua pontuação foi: {abs(ponto_certo)}pts.')
                        break
                    elif chute > num_secreto:
                        print('\n\033[0;31mVocê errou, o número foi maior do que o secreto, tente de novo!!!\033[m\n')
                    elif chute < num_secreto:
                        print('\n\033[0;31mVocê errou, o número foi menor do que o secreto, tente de novo!!!\033[m\n')
                if i == tentativas:
                    print('O número secreto era:', num_secreto)
                    ponto_errado = round(ponto - (ponto_fracao * i), 2)
                    print(f'Que pena!!! Sua pontuação foi: {abs(ponto_errado)}pts.')
            else:
                if i == tentativas:
                    print('\n\033[0;31mOps! Na próxima, digite um número, por favor...\033[m')
                else:
                    print('\n\033[0;31mOps, digite um número, por favor...\033[m')


print('***********************')
print('* JOGO DE ADIVINHAÇÃO *')
print('***********************\n')

print('''
Bem vindo ao jogo!\n
Instruções:
Para começar você deve definir o intervalo dos números que deseja adivinhar;
Depois, defina a dificuldade dizendo o nível de dificuldade.
Boa sorte!!!''')

jogo_adivinhacao()

repetir = int(input('\nDeseja jogar de novo?\n(1)Sim ou (2)Não:'))

repeticao(repetir)