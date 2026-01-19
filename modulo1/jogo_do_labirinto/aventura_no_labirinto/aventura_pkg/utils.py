"""
Módulo utilitário do jogo Aventura no Labirinto.

Responsável por:
- Exibir menus
- Mostrar instruções
- Mostrar tela final com Rich
- Resolver o labirinto automaticamente usando RECURSÃO
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Console principal do Rich para impressão estilizada no terminal
console = Console()


def imprimir_menu(nome_jogador: str) -> str:
    """
    Exibe o menu principal do jogo e retorna a opção escolhida.

    Args:
        nome_jogador (str): Nome do jogador.

    Returns:
        str: Opção digitada pelo usuário.
    """
    console.clear()

    console.print(
        Panel.fit(
            f"[bold cyan]Aventura no Labirinto[/bold cyan]\n\n"
            f"Bem-vindo(a), [bold yellow]{nome_jogador}[/bold yellow]!\n\n"
            "[bold green]1[/bold green] - Instruções\n"
            "[bold green]2[/bold green] - Jogar\n"
            "[bold red]O[/bold red] - Sair",
            title="Menu Principal",
            border_style="cyan",
        )
    )

    return input("Escolha uma opção: ").lower()


def imprimir_instrucoes() -> None:
    """
    Mostra as instruções do jogo para o jogador.
    """
    console.clear()

    console.print(
        Panel.fit(
            "[bold]Como jogar:[/bold]\n\n"
            "- Use as teclas [bold]W A S D[/bold] para se mover\n"
            "- Digite a tecla e pressione [bold]ENTER[/bold]\n"
            "- Colete ⭐ para ganhar pontos\n"
            "- Evite as paredes (#)\n"
            "- Digite [bold red]O[/bold red] para sair do jogo\n",
            title="Instruções",
            border_style="green",
        )
    )

    input("\nPressione ENTER para voltar ao menu...")


def tela_final(jogador: dict) -> None:
    """
    Exibe a tela final do jogo com resumo da partida.

    Args:
        jogador (dict): Dicionário contendo dados do jogador
                        (nome, pontuacao, estrelas).
    """
    console.clear()

    # Cria uma tabela estilizada com Rich
    table = Table(
        title="🏆 Resultado Final 🏆",
        show_header=True,
        header_style="bold magenta",
    )

    table.add_column("Item", style="cyan")
    table.add_column("Valor", style="green")

    table.add_row("Jogador", jogador["nome"])
    table.add_row("⭐ Estrelas coletadas", str(jogador["estrelas"]))
    table.add_row("Pontuação final", str(jogador["pontuacao"]))

    console.print(Panel.fit(table, border_style="yellow"))
    console.print("\nObrigado por jogar! 🚀\n", style="bold blue")


def resolver_labirinto(labirinto: list, x: int, y: int, visitado=None, caminho=None):
    """
    Função RECURSIVA que tenta encontrar uma saída no labirinto.

    A função utiliza backtracking:
    - testa movimentos possíveis
    - marca posições visitadas
    - retorna o caminho se encontrar a saída

    Args:
        labirinto (list): Matriz representando o labirinto.
        x (int): Linha atual.
        y (int): Coluna atual.
        visitado (set): Conjunto de posições já visitadas.
        caminho (list): Lista de movimentos realizados.

    Returns:
        list | None: Lista de comandos ('w', 'a', 's', 'd') ou None se não houver saída.
    """

    # Inicializa estruturas na primeira chamada
    if visitado is None:
        visitado = set()

    if caminho is None:
        caminho = []

    # Verifica limites, paredes ou posições já visitadas
    if (
        x < 0 or x >= len(labirinto)
        or y < 0 or y >= len(labirinto[0])
        or labirinto[x][y] == "#"
        or (x, y) in visitado
    ):
        return None

    # Condição de saída: chegou à borda do labirinto
    if x == 0 or y == 0 or x == len(labirinto) - 1 or y == len(labirinto[0]) - 1:
        return caminho

    # Marca posição como visitada
    visitado.add((x, y))

    # Movimentos possíveis: cima, baixo, esquerda, direita
    movimentos = [
        (-1, 0, "w"),
        (1, 0, "s"),
        (0, -1, "a"),
        (0, 1, "d"),
    ]

    # Explora recursivamente cada movimento
    for dx, dy, comando in movimentos:
        resultado = resolver_labirinto(
            labirinto,
            x + dx,
            y + dy,
            visitado,
            caminho + [comando]
        )

        if resultado is not None:
            return resultado

    # Se nenhum caminho funcionar, retorna None (backtracking)
    return None