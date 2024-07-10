# Importando módulos úteis ############################################################
import os
import sys
import random
import time
from colorama import Fore, Back, Style, init
init()
# Função: Limpar tela #################################################################
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função: Imprimir separador para menus ###############################################
def separador(cor = Fore.LIGHTGREEN_EX):
    print(cor + '======================================' + Style.RESET_ALL)

# Função: Cria um loading falso ######################################################
def loading(segundos, pontos, repeticoes,cor = Fore.YELLOW):
    clear_screen()
    loads = 0
    reticencias = ['.']
    while repeticoes > loads:
        for ponto in range(pontos):
            reticencias.append('.')
            loads += 1
            print(cor + 'Carregando' + ''.join(reticencias), end='\r')
            time.sleep(segundos)
            clear_screen()
            if len(reticencias) > pontos:
                reticencias = ['.']


# Função: Printar boas vindas #########################################################
def boas_vindas():
    separador()
    print(Fore.LIGHTGREEN_EX + '===== BEM-VINDO AO JOGO DA FORCA =====' + Style.RESET_ALL)
    separador()

# Função: Nomear o jogador ############################################################
def jogador():
    global nome
    boas_vindas()
    print(Fore.LIGHTGREEN_EX + '========== INSIRA SEU NOME: ==========' + Style.RESET_ALL)
    separador()
    print(Fore.LIGHTGREEN_EX + 'Seu nome será usado no placar.')
    nome = input(Fore.LIGHTGREEN_EX + 'Eu sou... ')

# Função: Mostrar algumas informações sobre o jogo, como pontos e erros ##############
def header():
    print(Fore.LIGHTGREEN_EX + 'Pontuação: ' + Fore.LIGHTRED_EX + str(pontos) + Fore.LIGHTGREEN_EX + ' /// Dificuldade: ' + Fore.LIGHTRED_EX + dificuldade.capitalize() + Style.RESET_ALL)
    separador()
    if modo == 'singleplayer':
        print(Fore.LIGHTGREEN_EX + 'Categoria: ' + Fore.LIGHTRED_EX + categoria.capitalize() + Fore.LIGHTGREEN_EX + ' /// Número de erros: ' + Fore.LIGHTRED_EX + str(erros) + '/' + str(strike) + Style.RESET_ALL)
    else:
        print(Fore.LIGHTGREEN_EX + 'Número de erros: ' + str(erros) + '/' + str(strike) + Style.RESET_ALL)
    separador()
    if dicasswitch == 'on':
        print(Fore.LIGHTGREEN_EX + 'Dica: ' + dica + Style.RESET_ALL)
    elif dicasswitch == 'false':
        print(Fore.LIGHTRED_EX + 'Não há dicas no modo difícil.' + Style.RESET_ALL)
    elif dicasswitch == 'perguntar':
        print(Fore.LIGHTCYAN_EX + 'Para obter uma dica, digite "!dica"' + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + 'Multiplicador: ' + Fore.LIGHTRED_EX + str(seq) + 'x' + Style.RESET_ALL)

# Função: Definir o modo de jogo #####################################################
def modo_de_jogo():
    global modo
    boas_vindas()
    print(Fore.LIGHTGREEN_EX + '====== SELECIONE O MODO DE JOGO ======' + Style.RESET_ALL)
    separador()
    modo = input(Fore.LIGHTGREEN_EX + '- singleplayer = Forca padrão\n- multiplayer = Um jogador escolhe a palavra secreta e o outro adivinha\n')
    clear_screen()

# Função: Definir a palavra secreta ##################################################
def criar_palavra_secreta():
    global palavra_secreta, letras_acertadas, dica, categoria
    if modo == 'multiplayer':
        boas_vindas()
        print(Fore.LIGHTGREEN_EX + '====== SELECIONE O MODO DE JOGO ======' + Style.RESET_ALL)
        separador()
        palavra_secreta = input(Fore.LIGHTGREEN_EX + 'A palavra secreta é... ')
        clear_screen()
        boas_vindas()
        print(Fore.LIGHTGREEN_EX + '====== SELECIONE O MODO DE JOGO ======' + Style.RESET_ALL)
        separador()
        dica = input(Fore.LIGHTGREEN_EX + 'A dica da palavra secreta é... ')
        clear_screen()
    elif modo == 'singleplayer':
        boas_vindas()
        print(Fore.LIGHTGREEN_EX + '=== SELECIONE A CATEGORIA DESEJADA ===' + Style.RESET_ALL)
        separador()
        palavras = {
                'frutas': ['banana', 'maçã', 'manga', 'uva', 'laranja', 'abacaxi', 'melancia'],
                'animais': ['tigre', 'leão', 'urso', 'cachorro', 'gato', 'papagaio', 'elefante'],
                'paises': ['brasil', 'estados unidos', 'alemanha', 'japão', 'china', 'portugal', 'frança'],
                'verbos': ['dormir', 'estudar', 'correr', 'levantar', 'comer', 'acabar', 'começar']
                }
        categoria = input(Fore.LIGHTGREEN_EX + 'Lista de categorias existentes:\n- frutas\n- animais\n- paises\n- verbos\n')
        clear_screen()
        if categoria not in palavras:
            print(Fore.RED + 'ERRO: A categoria inserida é inválida' + Style.RESET_ALL)
            sys.exit()
        palavra_secreta = random.choice(palavras[categoria])
    else:
        print(Fore.RED + 'ERRO: O modo de jogo inserido é inválido.' + Style.RESET_ALL)
        sys.exit()
    letras_acertadas = ['_' for _ in palavra_secreta]

# Função: Define a dificuldade ########################################################
def definir_dificuldade():
    global dificuldade
    clear_screen()
    boas_vindas()
    print(Fore.LIGHTGREEN_EX + '== SELECIONE A DIFICULDADE DESEJADA ==' + Style.RESET_ALL)
    separador()
    dificuldade = input(Fore.LIGHTGREEN_EX + 'Insira a dificuldade:\n- Para fácil = facil\n- Para médio = medio\n- Para difícil = dificil\n')
    clear_screen()

# Função: Define a dica baseada na palavra secreta ####################################
def definir_dica():
    global dicas, dica
    dicas = {
            'banana': 'Macaco', 'maçã': 'Isaac Newton', 'manga': 'Caroço', 'uva': 'Vinho', 'laranja': 'Cor',
            'abacaxi': 'Coroa', 'melancia': 'Sementes',
            'tigre': 'Listras', 'leão': 'Rei', 'urso': 'Mel', 'cachorro': 'Caramelo', 'gato': 'Egito',
            'papagaio': 'Repetitivo', 'elefante': 'Pesado',
            'brasil': '5 estrelas', 'estados unidos': 'Maior potência', 'alemanha': 'Muro', 'japão': 'Anime',
            'china': 'Muralha', 'portugal': 'CR', 'frança': 'Torre',
            'dormir': 'Cama', 'estudar': 'Escola', 'correr': 'Maratona', 'levantar': 'Cair', 'comer': 'Fome',
            'acabar': 'Final', 'começar': 'Partida'
             }
    if modo == 'singleplayer':
        dica = dicas[palavra_secreta]

# Função: Define variáveis globais e importantes para o jogo ###########################
def inicializar_variaveis():
    global enforcou, acertou, erros, pontos, strike, dificuldade, dicasswitch, vogais, sequencia, seq
    enforcou = False
    acertou = False
    erros = 0
    pontos = 0
    vogais = ['a','e','i','o','u']
    sequencia = 0
    seq = 0
    if dificuldade == 'facil':
        strike = 8
        dicasswitch = 'on'
    elif dificuldade == 'medio':
        strike = 6
        dicasswitch = 'perguntar'
    elif dificuldade == 'dificil':
        strike = 4
        dicasswitch = 'false'
    else: 
        print(Fore.RED + 'ERRO: A dificuldade inserida é inválida' + Style.RESET_ALL)
        sys.exit()

# Função: Recebe o chute de uma letra ou uma palavra ##################################
def chutar(letras_acertadas):
    global dicasswitch
    printar_forca()
    print(Fore.LIGHTGREEN_EX + str(letras_acertadas))
    global chute
    chute = input("Qual letra? ")

# Função: Imprime o gráfico da forca ##################################################
def printar_forca():
    pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n", 
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n", 
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n"]
    try:
        print(Fore.LIGHTGREEN_EX + pics[erros] + Style.RESET_ALL)
    except IndexError:
        print(Fore.LIGHTGREEN_EX + pics[6] + Style.RESET_ALL)


# Criação do placar vazio #############################################################
placar = []
# Função: Criar o placar de líderes ###################################################
def podio():
    global placar
    placar.append((nome, pontos))
    print(Fore.LIGHTBLUE_EX + '=============== PLACAR ===============' + Style.RESET_ALL)
    separador(Fore.LIGHTBLUE_EX)
    for jogador_nome, jogador_pontos in placar:
        print(Fore.LIGHTBLUE_EX + f'{jogador_nome} = {jogador_pontos} pontos.')

# Função: Processamento principal do jogo #############################################
def fluxo():
    global enforcou, acertou, erros, pontos, dicasswitch, sequencia, seq, strike, poststrike, letras_acertadas
    chutar(letras_acertadas)
    if chute == palavra_secreta:
        pontos += 250
        acertou = True
    elif(chute.upper() in palavra_secreta.upper()):
        for posicao, letra in enumerate(palavra_secreta):
            if(chute.upper() == letra.upper()) and chute not in letras_acertadas:
                letras_acertadas = [letra if letra.upper() == chute.upper() else acerto for letra, acerto in zip(palavra_secreta, letras_acertadas)]
                pontos += 120
                sequencia += 1
                if chute in vogais:
                    strike += 1
                if sequencia >= 2 and sequencia <= 3:
                    pontos += 60
                    seq = 1.5
                elif sequencia >= 4 and sequencia <= 5:
                    seq = 2
                    pontos += 120
    elif chute == '!dica':
        dicasswitch = 'on'
    else:
        erros += 1
        sequencia = 0
        seq = 0
        pontos -= 100
    enforcou = erros == strike
    acertou = '_' not in letras_acertadas or chute == palavra_secreta
    clear_screen()


# Função: Imprime um sumário ao final do jogo ########################################
def sumario():
    print(Fore.LIGHTBLUE_EX + '============== SUMÁRIO: ==============' + Style.RESET_ALL)
    separador(Fore.LIGHTBLUE_EX)
    print(Fore.LIGHTBLUE_EX + f'Palavra secreta: {palavra_secreta}')
    separador(Fore.LIGHTBLUE_EX)
    print(Fore.LIGHTBLUE_EX + 'Erros:', erros, '/', strike)
    separador(Fore.LIGHTBLUE_EX)
    print(Fore.LIGHTBLUE_EX + 'Dificuldade:', dificuldade.capitalize() + Style.RESET_ALL)
    separador(Fore.LIGHTBLUE_EX)
    podio()
    separador(Fore.LIGHTBLUE_EX)
    replay()

# Função: Convidar a jogar novamente #################################################
def replay():
    time.sleep(3)
    print(Fore.LIGHTBLUE_EX + '========= JOGAR NOVAMENTE? ==========' + Style.RESET_ALL)
    separador(Fore.LIGHTBLUE_EX)
    retry = input(Fore.LIGHTBLUE_EX + '[   ] Sim      [   ] Não\n')
    if retry.lower() == 'sim':
        jogar()
    else:
        clear_screen()
        separador(Fore.LIGHTBLUE_EX)
        print(Fore.LIGHTBLUE_EX + '======== OBRIGADO POR JOGAR!! ========' + Style.RESET_ALL)
        separador(Fore.LIGHTBLUE_EX)
        for i in range(8):
            print('\n')

# Função: Confere se o jogo terminou #################################################
def fim_do_jogo():
    if acertou:
        separador()
        print(Fore.GREEN + '======== VOCÊ VENCEU A FORCA! ========' + Style.RESET_ALL)
        separador()
    elif erros == strike:
        separador(Fore.LIGHTRED_EX)
        print(Fore.LIGHTRED_EX + '======== VOCÊ PERDEU A FORCA! ========' + Style.RESET_ALL)
        separador(Fore.LIGHTRED_EX)
    sumario()

# Função: Junta todas as funções em uma só função ####################################
def jogar():
    global acertou, dificuldade, categoria, modo
    clear_screen()
    jogador()
    definir_dificuldade()
    modo_de_jogo()
    criar_palavra_secreta()
    inicializar_variaveis()
    definir_dica()
    while not enforcou and not acertou:
        boas_vindas()
        header()
        fluxo()
    fim_do_jogo()

# Tela de entrada ####################################################################
def entrada():
    print(Fore.YELLOW + '============================' + Style.RESET_ALL)
    print(Fore.YELLOW + 'Trabalho avaliativo de F.L.A' + Style.RESET_ALL)
    print(Fore.YELLOW + 'IFRN - Campus Pau dos Ferros' + Style.RESET_ALL)
    print(Fore.YELLOW + '============================' + Style.RESET_ALL)
    print(Fore.YELLOW + 'Caio Enzo Bessa de Oliviera' + Style.RESET_ALL)
    print(Fore.YELLOW + 'Tawan Wesllen Moura de Aquino' + Style.RESET_ALL)
    print(Fore.YELLOW + '============================' + Style.RESET_ALL)
    resp = input(Fore.YELLOW + 'Digite "jogar" para iniciar o jogo.\n' + Fore.YELLOW +'->' + Style.RESET_ALL)
    if resp == 'jogar':
        loading(0.5, 2, 6)
        jogar()
    else:
        clear_screen()
        entrada()
clear_screen()
entrada()