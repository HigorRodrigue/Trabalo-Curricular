# jogadores.py

class Jogador:
    def __init__(self, nome, posicao, idade, time=None):
        self.nome = nome
        self.posicao = posicao
        self.idade = idade
        self.time = time

def cadastrar_jogador(nome, posicao, idade, time=None):
    return Jogador(nome, posicao, idade, time)

def remover_jogador(jogadores, nome):
    jogadores = [jogador for jogador in jogadores if jogador.nome != nome]
    return jogadores

def gerar_relatorio_jogadores(jogadores):
    for jogador in jogadores:
        print(f"Nome: {jogador.nome}, Posição: {jogador.posicao}, Idade: {jogador.idade}, Time: {jogador.time.nome if jogador.time else 'N/A'}")
