# main.py

from jogadores import cadastrar_jogador, remover_jogador, gerar_relatorio_jogadores, Jogador
from times import cadastrar_time, atualizar_time, gerar_relatorio_times, Time
from torneios_partidas import cadastrar_torneio, atualizar_torneio, agendar_partida, registrar_placar, Torneio, Partida
from associar import associar_jogador_a_time

def menu():
    print("Menu:")
    print("1. Cadastrar Jogador")
    print("2. Remover Jogador")
    print("3. Cadastrar Time")
    print("4. Atualizar Time")
    print("5. Cadastrar Torneio")
    print("6. Atualizar Torneio")
    print("7. Agendar Partida")
    print("8. Registrar Placar")
    print("9. Gerar Relatório de Jogadores")
    print("10. Gerar Relatório de Times")
    print("11. Associar Jogador a Time")
    print("0. Sair")

    escolha = int(input("Escolha uma opção: "))
    return escolha

def main():
    jogadores = []
    times = []
    torneios = []

    while True:
        opcao = menu()

        if opcao == 1:
            # Cadastra um novo jogador
            nome = input("Nome do jogador: ")
            posicao = input("Posição: ")
            idade = int(input("Idade: "))
            jogadores.append(cadastrar_jogador(nome, posicao, idade))

        elif opcao == 2:
            # Remove um jogador existente
            nome = input("Nome do jogador a ser removido: ")
            jogadores = remover_jogador(jogadores, nome)

        elif opcao == 3:
            # Cadastra um novo time
            nome = input("Nome do time: ")
            tecnico = input("Nome do técnico: ")
            times.append(cadastrar_time(nome, tecnico))

        elif opcao == 4:
            # Atualiza informações de um time
            nome = input("Nome do time a ser atualizado: ")
            time = next((time for time in times if time.nome == nome), None)
            if time:
                novo_nome = input("Novo nome (deixe em branco para não alterar): ")
                novo_tecnico = input("Novo técnico (deixe em branco para não alterar): ")
                atualizar_time(time, novo_nome or None, novo_tecnico or None)

        elif opcao == 5:
            # Cadastra um novo torneio
            nome = input("Nome do torneio: ")
            data_inicio = input("Data de início: ")
            torneios.append(cadastrar_torneio(nome, data_inicio))

        elif opcao == 6:
            # Atualiza informações de um torneio
            nome = input("Nome do torneio a ser atualizado: ")
            torneio = next((torneio for torneio in torneios if torneio.nome == nome), None)
            if torneio:
                novo_nome = input("Novo nome (deixe em branco para não alterar): ")
                nova_data = input("Nova data (deixe em branco para não alterar): ")
                atualizar_torneio(torneio, novo_nome or None, nova_data or None)

        elif opcao == 7:
            # Agenda uma nova partida
            time1_nome = input("Nome do primeiro time: ")
            time2_nome = input("Nome do segundo time: ")
            data = input("Data da partida: ")
            time1 = next((time for time in times if time.nome == time1_nome), None)
            time2 = next((time for time in times if time.nome == time2_nome), None)
            if time1 and time2:
                partida = agendar_partida(time1, time2, data)
                time1.historico_partidas.append(partida)
                time2.historico_partidas.append(partida)

        elif opcao == 8:
            # Registra o placar de uma partida
            time1_nome = input("Nome do primeiro time: ")
            time2_nome = input("Nome do segundo time: ")
            time1 = next((time for time in times if time.nome == time1_nome), None)
            time2 = next((time for time in times if time.nome == time2_nome), None)
            if time1 and time2:
                partida = next((partida for partida in time1.historico_partidas if partida.time2 == time2), None)
                if partida:
                    placar = input("Placar da partida: ")
                    registrar_placar(partida, placar)

        elif opcao == 9:
            # Gera relatório de jogadores
            gerar_relatorio_jogadores(jogadores)

        elif opcao == 10:
            # Gera relatório de times
            gerar_relatorio_times(times)

        elif opcao == 11:
            # Associa um jogador a um time
            associar_jogador_a_time(jogadores, times)

        elif opcao == 0:
            # Encerra o programa
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
