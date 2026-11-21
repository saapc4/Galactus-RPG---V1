import random
from random import randint
from time import sleep
import os
margem_mult_dano = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
def recuperar(aiai):
    aiai["Vida"] = aiai["Vida_maxima"]
    aiai["Mana"] = aiai["Mana_maxima"]
def uparlevel(cara):
    cara["Dano"] *= 1.1
    cara["Vida_maxima"] *= 1.1
    cara["Vida"] = cara["Vida_maxima"]
    cara["Mana_maxima"] *= 1.1
    cara["Mana"] = cara["Mana_maxima"] 
    cara["Level"] += 1
    cara["Xp"] -= cara["Xp_maximo"]
    cara["Xp_maximo"] += 50
def escolher(opcoes, mensagem):
    while True:
        escolha = input(mensagem).capitalize()
        if escolha in opcoes:
            return escolha
        print('ESCOLHA UMA OPÇÃO VÁLIDA!')
morreu = []
def batalha(monstro_batalha):
    morreu.clear()
    turno = 1
    vida_monstro = monstro_batalha["vida"]
    vida_personagem = personagem["Vida"]
    mana_personagem = personagem["Mana"]
    while True:
        print(f'{personagem["Nome"]} vs {monstro_batalha["nome"]}')
        print(f'Turno: {turno}')
        print(f'Vida de {monstro_batalha["nome"]}: {vida_monstro:.2f}')
        print(f'Sua vida: {vida_personagem:.2f}')
        print(f'Sua mana: {mana_personagem:.2f}')
        acao = escolher(("1", "2", "3"), ("1- Atacar\n2- Fugir(60% de sucesso)\n3- Curar 20% da vida e 20 de mana\n"))

        if acao == "1":
            while True:
                print(f'Ataques disponíveis: ')
                for i in ataques.keys():
                    print(f'{i}')
                atk = str(input('Ataque escolhido: '))
                if atk in ataques.keys():
                    ataque = ataques[atk].copy()
                    if ataque["mana"] > mana_personagem:
                        print(f'Mana insuficiente para usar este ataque!')
                    break
            mult_dano_jogador = random.choice(margem_mult_dano)
            mult_dano_monstro = random.choice(margem_mult_dano)
            vida_monstro -= ((ataque["dano"] * personagem["Dano"]) * mult_dano_jogador)
            print(f'Causou {((ataque["dano"] * personagem["Dano"]) * mult_dano_jogador):.2f} de dano!')
            mana_personagem -= ataque["mana"]
            sleep(0.3)
        elif acao == "2":
            print(f'Tentando fugir...')
            fugiu = random.randint(0, 100) 
            print(fugiu)
            if fugiu > 60:
                print(f'FUGIU!')
                break
            print('FALHOU!')
            sleep(0.2)
        elif acao == "3":
            vida_personagem *= 1.2
            mana_personagem += 20
        if vida_monstro <= 0:
            print(f'Você matou {monstro_batalha["nome"]}')
            break
        print(f'{monstro_batalha["nome"]} vai te atacar!')
        sleep(0.1)
        vida_personagem -= (monstro_batalha["dano"] * mult_dano_monstro)
        print(f'Causou {(monstro_batalha["dano"] * mult_dano_monstro):.2f} de dano!')
        sleep(0.3)
        if vida_personagem <= 0:
            print('Você morreu!')
            morreu.append('Morreu')
            sleep(3)
            break
        turno += 1
        os.system("clear")
    personagem["Vida"] -= (personagem["Vida"] - vida_personagem)
    personagem["Mana"] -= (personagem["Mana"] - mana_personagem)
racas = {
    "Humano":{"vida":100, "mana":50, "dano":1.2},
    "Elfo":{"vida": 90, "mana":100, "dano":0.5},
    "Dracônico":{"vida": 110, "mana":40, "dano":1.3}
}
classes = {
    "Tank":{"multiplicador_de_vida": 1.2, "multiplicador_de_mana": 0.8, "multiplicador_de_dano": 1.2 },
    "Mago":{"multiplicador_de_vida": 0.95, "multiplicador_de_mana": 1.5, "multiplicador_de_dano": 0.5},
    "Espadachim":{"multiplicador_de_vida": 1.0, "multiplicador_de_mana": 0.7, "multiplicador_de_dano": 1.3}
}
ataques = {
    "Corte":{"dano":30, "mana": 0},
    "Raio":{"dano": 40, "mana":30}
}
monstros = {
    'Slime':{"nome": 'Slime', "vida":randint(25, 40), "dano":randint(8, 20), "xp":randint(30, 60)},
    'Lobo':{"nome": 'Lobo', "vida":randint(50, 70), "dano":randint(18, 30), "xp":randint(80, 110)},
    'Traunt':{"nome": 'Traunt', "vida":randint(80, 100), "dano":randint(35, 60), "xp":randint(130, 170)},
    "Dragão Sábio": {"nome": "O Grande Dragão Sábio", "vida": randint(450, 550),"dano": randint(50, 70),"xp":randint(450, 550)}
}

print('Bem vindo ao Galactus RPG')
nome = str(input('Qual seu nome? '))
print(f'Olá {nome}')
print(f'Crie seu personagem: ')

raca = escolher(("Humano", "Elfo", "Dracônico"), ("Escolha sua raça: (Humano, Elfo ou Dracônico)\n"))
classe = escolher(("Tank", "Mago", "Espadachim"), ("Escolha sua classe: (Tank, Mago ou Espadachim)\n"))

personagem = {
    "Nome": nome,
    "Raça": raca,
    "Classe": classe,
    "Vida": (racas[raca]["vida"] * classes[classe]["multiplicador_de_vida"]),
    "Vida_maxima": (racas[raca]["vida"] * classes[classe]["multiplicador_de_vida"]),
    "Mana": (racas[raca]["mana"] * classes[classe]["multiplicador_de_mana"]),
    "Mana_maxima": (racas[raca]["mana"] * classes[classe]["multiplicador_de_mana"]),
    "Dano": (racas[raca]["dano"] * classes[classe]["multiplicador_de_dano"]),
    "Level": 1,
    "Xp": 0,
    "Xp_maximo": 100,
    "Ataques": ataques
}


print(f'\nSeus ataques iniciais são: ')
for i, c in ataques.items():
    print(f'{i}, {c}')
print('\n')
input('Pressione ENTER para continuar...')
os.system("clear")

dias_restantes = 5
while True:
    print(f'Herói: {personagem["Nome"]}')
    print(f'Level: {personagem["Level"]}')
    print(f'Xp: {personagem["Xp"]}/{personagem["Xp_maximo"]}')
    print(f'Vida: {personagem["Vida"]:.2f}/{personagem["Vida_maxima"]:.2f}')
    print(f'Mana: {personagem["Mana"]:.2f}/{personagem["Mana_maxima"]:.2f}')
    print(f'Daqui a {dias_restantes} dias você terá que lutar contra o "Grande Dragão Sábio"!\n')
    print('Opções: ')
    print('1- Caçar e upar seu level\n2- Nada (passa um dia)\n3- Descansar (passa um dia descansando para recuperar a vida e mana)')
    
    while True:
        evento = input('O que deseja fazer? ')
        if evento in '123':
            break
        print(f'Escolha uma opção!')

    if evento == "1":
        batalhas = 1
        while True:
            monstrosss = ["Slime", "Traunt", "Lobo"]
            monstro_sorteado = random.choice(monstrosss)
            print(f'Você vai para a floresta e encontra um {monstro_sorteado}!')
            sleep(1)
            os.system("clear")
            batalha(monstros[monstro_sorteado])
            if personagem["Vida"] <= 0:
                print('Você misteriosamente acorda em sua cama...')
                personagem["Vida"] += (personagem["Vida"] * -1) + 10
                sleep(1.3)
                break
            
            print(f'Você ganhou {monstros[monstro_sorteado]["xp"]} de xp!')
            personagem["Xp"] += monstros[monstro_sorteado]["xp"]
            if personagem["Xp"] >= personagem["Xp_maximo"]:
                while personagem["Xp"] >= personagem["Xp_maximo"]:
                    uparlevel(personagem)
                print(f'Você upou para o level {personagem["Level"]}!')
                print('Sua vida e mana foram restauradas!')
                if personagem["Level"] == 5:
                    print('Você upou para o level 5!!! Ataques desbloquados: Investida, Tornado')
                    ataques["Investida"] = {"dano": 50,"mana": 10}
                    ataques["Tornado"] = {"dano": 60,"mana": 40}
            if batalhas == 3:
                print('Você se sente cansado e decide ir embora...')
                sleep(2)
                break        
            cont = str(input('Quer continuar caçando?'))
            if cont in 'Nn':
                break
            batalhas += 1
    elif evento == '2':
        print('PÉSSIMA ESCOLHA! MAS OK...')
        sleep(0.2)
    elif evento == '3':
        recuperar(personagem)
        print('Você descansa o dia inteiro e tem sua vida e mana restauradas.')
    dias_restantes -= 1
    if dias_restantes == 0:
        print(f'\nVocê irá batalhar com {monstros["Dragão Sábio"]["nome"]}!')
        sleep(5)
        os.system("clear")
        while True:
            recuperar(personagem)
            batalha(monstros["Dragão Sábio"])
            if len(morreu) == 0:
                os.system("clear")
                print('Parabéns!!! Você zerou o Galactus RPG!')
                sleep(5)
                os.system("sl")
                break
            else:
                print('Que pena!!! Tente de novo!')
                sleep(4)
                recuperar(personagem)
            os.system("clear")
        break
    os.system("clear")
os.system("clear")
