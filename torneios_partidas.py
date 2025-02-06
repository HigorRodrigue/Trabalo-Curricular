

class Torneio:
    def __init__(self, nome, data_inicio):
        self.nome = nome
        self.data_inicio = data_inicio
        self.times_participantes = []
        self.tabela_resultados = []

    def adicionar_time(self, time):
        self.times_participantes.append(time)

def cadastrar_torneio(nome, data_inicio):
    return Torneio(nome, data_inicio)

def atualizar_torneio(torneio, novo_nome=None, nova_data=None):
    if novo_nome:
        torneio.nome = novo_nome
    if nova_data:
        torneio.data_inicio = nova_data
    return torneio

class Partida:
    def __init__(self, time1, time2, data, placar=None):
        self.time1 = time1
        self.time2 = time2
        self.data = data
        self.placar = placar
        self.estatisticas = {}

def agendar_partida(time1, time2, data):
    return Partida(time1, time2, data)

def registrar_placar(partida, placar):
    partida.placar = placar
    return partida
