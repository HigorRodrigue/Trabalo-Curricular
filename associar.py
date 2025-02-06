# associar.py

def associar_jogador_a_time(jogadores, times):
    nome_jogador = input("Nome do jogador: ")
    nome_time = input("Nome do time: ")

    jogador = next((jogador for jogador in jogadores if jogador.nome == nome_jogador), None)
    time = next((time for time in times if time.nome == nome_time), None)

    if jogador and time:
        time.adicionar_jogador(jogador)
        print(f"Jogador {jogador.nome} foi associado ao time {time.nome}.")
    else:
        print("Jogador ou time não encontrado.")
