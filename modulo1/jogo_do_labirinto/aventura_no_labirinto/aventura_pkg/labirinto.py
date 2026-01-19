"""
Módulo responsável pela criação e exibição do labirinto do jogo
Aventura no Labirinto.

Este módulo contém funções para:
- Gerar um labirinto aleatório
- Exibir o labirinto no terminal usando Rich
- Contar estrelas existentes no mapa
"""

import random
from rich.console import Console

# Console do Rich para impressão estilizada
console = Console()


def criar_labirinto(linhas: int, colunas: int) -> list:
    """
    Cria um labirinto aleatório representado por uma matriz (lista de listas).

    Regras:
    - '#' representa paredes
    - '.' representa caminhos livres
    - '⭐' representa itens coletáveis
    - As bordas do labirinto são sempre paredes
    - A posição inicial (1, 1) é garantida como caminho livre

    Args:
        linhas (int): Número de linhas do labirinto.
        colunas (int): Número de colunas do labirinto.

    Returns:
        list: Matriz representando o labirinto.
    """
    labirinto = []

    for i in range(linhas):
        linha = []
        for j in range(colunas):

            # Bordas sempre são paredes
            if i == 0 or j == 0 or i == linhas - 1 or j == colunas - 1:
                linha.append("#")
            else:
                # Geração aleatória do conteúdo interno
                chance = random.random()

                if chance < 0.20:
                    linha.append("#")      # 20% de chance de parede
                elif chance < 0.25:
                    linha.append("⭐")     # 5% de chance de estrela
                else:
                    linha.append(".")      # Caminho livre

        labirinto.append(linha)

    # Garante que a posição inicial do jogador seja livre
    labirinto[1][1] = "."

    return labirinto


def imprimir_labirinto(labirinto: list, jogador: dict) -> None:
    """
    Imprime o labirinto no terminal, desenhando o jogador na posição atual.

    Observação:
    - O jogador NÃO é armazenado dentro da matriz do labirinto.
    - Ele é desenhado apenas visualmente no momento da impressão.

    Args:
        labirinto (list): Matriz do labirinto.
        jogador (dict): Dicionário contendo a posição atual do jogador.
    """
    console.clear()

    x_jogador, y_jogador = jogador["posicao"]

    for i, linha in enumerate(labirinto):
        linha_impressa = ""

        for j, celula in enumerate(linha):
            if i == x_jogador and j == y_jogador:
                linha_impressa += "P "
            else:
                linha_impressa += f"{celula} "

        console.print(linha_impressa)