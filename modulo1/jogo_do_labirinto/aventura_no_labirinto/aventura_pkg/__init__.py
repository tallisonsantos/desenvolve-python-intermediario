"""
Pacote aventura_pkg
Contém módulos para controlar o jogo Aventura no Labirinto:
- jogador: movimentação e pontuação do jogador
- labirinto: criação e impressão do labirinto
- utils: funções auxiliares como menu, instruções e tela final
"""

# Importa os módulos internos
from .jogador import *
from .labirinto import *
from .utils import *

# Opcional: define o que será exportado quando alguém fizer 'from aventura_pkg import *'
__all__ = [
    "iniciar_jogador",
    "mover",
    "pontuar",
    "criar_labirinto",
    "imprimir_labirinto",
    "contar_estrelas",
    "imprimir_menu",
    "imprimir_instrucoes",
    "tela_final",
    "resolver_labirinto"
]
