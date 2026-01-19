"""
Arquivo principal do jogo Aventura no Labirinto.

Responsável por:
- processar argumentos da CLI
- exibir menu
- controlar o fluxo do jogo
- tocar música de fundo (opcional)
- checar vitória ao coletar todas as estrelas
"""

# ---------------- IMPORTS ----------------
import argparse        # Para ler argumentos da linha de comando
import os              # Para manipular caminhos de arquivos
import threading       # Para rodar a música em paralelo
from playsound import playsound  # Para tocar música de fundo

from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import iniciar_jogador, mover
from aventura_pkg.utils import imprimir_menu, imprimir_instrucoes, tela_final

# ---------------- FUNÇÃO DE MÚSICA ----------------
def tocar_musica():
    """
    Toca a música de fundo (musica_fundo.mp3) localizada na pasta 'assets'.
    Caso o arquivo não exista, desativa o som.
    """
    musica_path = os.path.join("assets", "musica_fundo.mp3")
    if os.path.exists(musica_path):
        playsound(musica_path)
    else:
        print("Arquivo de música não encontrado! Música desativada.")

# ---------------- FUNÇÃO PRINCIPAL ----------------
def main():
    # ---------------- ARGUMENTOS DA CLI ----------------
    parser = argparse.ArgumentParser(description="Jogo Aventura no Labirinto")
    parser.add_argument("--name", required=True, help="Nome do jogador")
    parser.add_argument(
        "--dificuldade",
        choices=["facil", "medio", "dificil"],
        default="facil",
        help="Dificuldade do labirinto"
    )
    parser.add_argument(
        "--disable-sound",
        action="store_true",
        help="Desativa sons do jogo"
    )
    args = parser.parse_args()

    # ---------------- MENU PRINCIPAL ----------------
    while True:
        opcao = imprimir_menu(args.name)  # Exibe menu e lê opção
        match opcao:
            case "1":
                imprimir_instrucoes()        # Mostra instruções
            case "2":
                break                        # Inicia o jogo
            case "o":
                print("Saindo do jogo...")
                return                        # Encerra o programa
            case _:
                print("Opção inválida. Digite novamente.")

    # ---------------- CONFIGURAÇÃO DA DIFICULDADE ----------------
    match args.dificuldade:
        case "facil":
            linhas, colunas = 10, 20
        case "medio":
            linhas, colunas = 12, 25
        case "dificil":
            linhas, colunas = 15, 30

    # ---------------- INICIALIZAÇÃO ----------------
    labirinto = criar_labirinto(linhas, colunas)  # Cria o labirinto aleatório
    jogador = iniciar_jogador(args.name)          # Inicializa jogador
    total_estrelas = sum(linha.count("⭐") for linha in labirinto)  # Conta todas as estrelas no labirinto

    # ---------------- MÚSICA DE FUNDO ----------------
    if not args.disable_sound:
        # Roda a música em uma thread separada para não travar o jogo
        thread_musica = threading.Thread(target=tocar_musica, daemon=True)
        thread_musica.start()

    # ---------------- LOOP PRINCIPAL DO JOGO ----------------
    while True:
        # Imprime o labirinto com jogador
        imprimir_labirinto(labirinto, jogador)

        # HUD: exibe informações do jogador
        print(
            f"Jogador: {jogador['nome']}  |  "
            f"Pontos: {jogador['pontuacao']}  |  "
            f"⭐ Estrelas: {jogador['estrelas']}/{total_estrelas}"
        )
        print("W/A/S/D para mover | O para sair")

        # Lê movimento do jogador
        movimento = input(">> ").lower()

        # Verifica se o jogador deseja sair
        if movimento == "o":
            print("\nVocê saiu do jogo!")
            break

        # Atualiza posição do jogador e pontuação
        mover(jogador, movimento, labirinto)

        # Checa se todas as estrelas foram coletadas
        if jogador["estrelas"] >= total_estrelas:
            print("\n🎉 Parabéns! Você coletou todas as estrelas! 🎉\n")
            break  # Encerra o loop principal

    # ---------------- TELA FINAL ----------------
    tela_final(jogador)  # Mostra resumo com Rich

# ---------------- PONTO DE ENTRADA ----------------
if __name__ == "__main__":
    main()
