"""
Módulo responsável pelo controle do jogador no jogo Aventura no Labirinto.

Aqui ficam as funções relacionadas a:
- criação do jogador
- movimentação
- pontuação
"""

def iniciar_jogador(nome: str, color: str = "cyan") -> dict:
    """
    Inicializa o jogador com nome, posição inicial e pontuação.

    Args:
        nome (str): nome do jogador
        color (str): cor usada para exibir o jogador (rich)

    Returns:
        dict: dicionário com o estado inicial do jogador
    """
    return {
        "nome": nome,
        "posicao": (1, 1),   # posição inicial (linha, coluna)
        "pontuacao": 0,      # pontos totais
        "estrelas": 0,       # quantidade de ⭐ coletadas
        "color": color       # cor do jogador
    }


def mover(jogador: dict, direcao: str, labirinto: list) -> None:
    """
    Move o jogador no labirinto de acordo com a direção informada.

    Args:
        jogador (dict): estado atual do jogador
        direcao (str): tecla pressionada (w, a, s, d)
        labirinto (list): matriz do labirinto
    """
    x, y = jogador["posicao"]

    # Mapeamento de direções (linha, coluna)
    movimentos = {
        "w": (-1, 0),  # cima
        "s": (1, 0),   # baixo
        "a": (0, -1),  # esquerda
        "d": (0, 1)    # direita
    }

    # Se a tecla não for válida, não faz nada
    if direcao not in movimentos:
        return

    dx, dy = movimentos[direcao]
    novo_x, novo_y = x + dx, y + dy

    # Verifica se não é parede
    if labirinto[novo_x][novo_y] != "#":

        # Se encontrou estrela, pontua
        if labirinto[novo_x][novo_y] == "⭐":
            pontuar(jogador)

        # Limpa posição anterior
        labirinto[x][y] = "."

        # Atualiza posição do jogador
        jogador["posicao"] = (novo_x, novo_y)

        # Desenha o jogador no labirinto
        labirinto[novo_x][novo_y] = "P"


def pontuar(jogador: dict) -> None:
    """
    Atualiza a pontuação do jogador ao coletar uma estrela.

    Args:
        jogador (dict): estado atual do jogador
    """
    jogador["pontuacao"] += 10
    jogador["estrelas"] += 1