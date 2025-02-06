class Time:
    def __init__(self, nome, tecnico):
        self.nome = nome
        self.tecnico = tecnico
        self.jogadores = []
        self.historico_partidas = []
        
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        jogador.time = self

    def remover_jogador(self, nome_jogador):
        self.jogadores = [jogador for jogador in self.jogadores if jogador.nome != nome_jogador]

def cadastrar_time(nome, tecnico):
    return Time(nome, tecnico)

def atualizar_time(time, novo_nome=None, novo_tecnico=None):
    if novo_nome:
        time.nome = novo_nome
    if novo_tecnico:
        time.tecnico = novo_tecnico
    return time

def gerar_relatorio_times(times):
    for time in times:
        print(f"Time: {time.nome}, Técnico: {time.tecnico}")
        print("Jogadores:")
        for jogador in time.jogadores:
            print(f"  - {jogador.nome} ({jogador.posicao})")
