from colorama import Fore, Back, Style, init
init()

from rich.console import Console
console = Console()

import pyfiglet
from pyfiglet import Figlet
fig = Figlet()

print(fig.renderText('Jogo da Velha'))

console.print("Bem-vindo ao [bold]Jogo da Velha! [/bold] \n")

tabuleiro = [
        ['-','-','-'],
        ['-','-','-'],
        ['-','-','-']
    ]
def imprimir_tabuleiro(tabuleiro):

    for linha in tabuleiro:
        for valor in linha:
            print(f":{valor}:", end='')
        print(Fore.RESET)

print("")

while True:
    imprimir_tabuleiro(tabuleiro)

    jogar = int(input(Fore.BLUE + "P/ iniciar o jogo digite 1 \n"
                                            "P/ reiniciar digite 2 \n"
                                            "P/ encerrar digite 0:"))

    if jogar == 0:
        console.print("[i] Obrigado por jogar! [/i]", style="i blue")
        break

    elif jogar == 2:
        tabuleiro = [
            ['-','-','-'],
            ['-','-','-'],
            ['-','-','-']
        ]
        console.print("Jogo reiniciado!", style="bold green")
        print("")
        continue

       # jogador 1

    elif jogar == 1:
        jogador1_linha = int(input(Fore.CYAN + "jogador 1 digite a linha (0-2): "))
        jogador1_coluna = int(input(Fore.CYAN + "jogador 1 digite a coluna (0-2): "))

        if jogador1_linha ==0 or jogador1_linha ==1 or jogador1_linha==2:
            if tabuleiro[jogador1_linha][jogador1_coluna] == '-':
                tabuleiro[jogador1_linha][jogador1_coluna] = 'X'
            else:
                print("Posição já ocupada! Tente novamente.")
        else:
            print("Linha ou coluna inválida!")

        imprimir_tabuleiro(tabuleiro)

        print("")

        # jogador 2
        jogador2_linha = int(input(Fore.RED +"jogador 2 digite a linha (0-2): "))
        jogador2_coluna = int(input(Fore.RED +"jogador 2 digite a coluna (0-2): "))

        if jogador2_linha ==0 or jogador2_linha ==1 or jogador2_linha==2:
            if tabuleiro[jogador2_linha][jogador2_coluna] == '-':
                tabuleiro[jogador2_linha][jogador2_coluna] = 'O'
            else:
                print("Posição já ocupada! Tente novamente.")
        else:
            print("Linha ou coluna inválida!")

        imprimir_tabuleiro(tabuleiro)
        print("")
