import random
import copy
import sys

sys.setrecursionlimit(10**6)

atributos_unidades = {

    "unit_1": {"classe": "dinossauro", "vida": 500, "vidamax": 500, "ataque": 200, "defesa": 45,
               "agilidade": 1, "distancia_preferida": "perto"},
    "unit_2": {"classe": "galinha", "vida": 50, "vidamax": 50, "ataque": 5, "defesa": 10,
               "agilidade": 8, "distancia_preferida": "perto"},
    "unit_3": {"classe": "arqueiro", "vida": 200, "vidamax": 200, "ataque": 100, "defesa": 20,
               "agilidade": 6, "distancia_preferida": "longe"},
    "unit_4": {"classe": "lobo", "vida": 250, "vidamax": 250, "ataque": 75, "defesa": 25,
               "agilidade": 7, "distancia_preferida": "perto"},
    "unit_5": {"classe": "águia", "vida": 100, "vidamax": 100, "ataque": 100, "defesa": 15,
               "agilidade": 10, "distancia_preferida": "perto"},
    "unit_6": {"classe": "estilingue", "vida": 200, "vidamax": 200, "ataque": 75, "defesa": 15,
               "agilidade": 7, "distancia_preferida": "longe"}

}
#define atributos

vantagens_de_classe = {
    "águia": {"dinossauro": 1.2, "lobo": 1.2},
    "arqueiro": {"águia": 1.2, "galinha": 1.2},
    "hobbit": {"águia": 1.2, "galinha": 1.2},
    "lobo": {"arqueiro": 1.2, "hobbit": 1.2}
}
#define multiplicadores de vantagem que uma classe tem em outra




def calculo_ataque(atacante, alvo, vantagem_terreno, vantagem_classe, multiplicador_distancia):
    a = atacante["ataque"]
    if atacante["classe"] == "águia" or alvo["classe"] == "águia":
        return a * vantagem_classe * multiplicador_distancia
    else:
        return a * vantagem_terreno * vantagem_classe * multiplicador_distancia
#calcula o dano de ataque

def calculo_defesa(alvo, atacante, vantagem_terreno, vantagem_classe, multiplicador_distancia):
    if alvo == "unit_5" or atacante == "unit_5":
        return alvo["defesa"] * vantagem_classe * multiplicador_distancia
    else:
        return alvo["defesa"] * vantagem_terreno * vantagem_classe * multiplicador_distancia
#calcula o dano diminuido pela defesa

def calculo_multiplicador_distancia(atacante, alvo):
    distancia_atacante = atacante["distancia_preferida"]
    distancia_alvo = alvo["distancia_preferida"]
    if distancia_atacante == distancia_alvo:
        return 1
    elif ((distancia_atacante == "perto" and atacante["vida"] == atacante["vidamax"])
          or (distancia_atacante == "longe" and alvo["vida"] != alvo["vidamax"])):
        return 1.2
    else:
        return 0.8
#calcula a vantegem que a distância da a certas classes contra outras

def luta(atacante, alvo, vantagem_terreno_atq, vantagem_terreno_def, esquiva):

    mutiplicador_distancia = calculo_multiplicador_distancia(atacante, alvo)

    vantagem_classe = 1
    if atacante["classe"] in vantagens_de_classe and alvo["classe"] in vantagens_de_classe[atacante["classe"]]:
        vantagem_classe = vantagens_de_classe[atacante["classe"]][alvo["classe"]]

    dano_atq = calculo_ataque(atacante, alvo, vantagem_terreno_atq, vantagem_classe, mutiplicador_distancia)
    defesa = calculo_defesa(alvo, atacante, vantagem_terreno_def, vantagem_classe, mutiplicador_distancia)

    if atacante["classe"] != "galinha":
        dano_rec = dano_atq - defesa
    else:
        dano_rec = dano_atq

    if esquiva < alvo["agilidade"] and dano_rec > alvo["vidamax"]/2:
        dano_rec = alvo["vidamax"]/2
    if dano_rec < 1:
        dano_rec = 0

    alvo["vida"] -= dano_rec

    return alvo["vida"] <= 0.0
#calcula o dano que o ataque de um atacante dará ao defensor(considera os multiplicadores e atributos)

a1 = int(input("quant ex1 dino:"))
a2 = int(input("quant ex1 galinha:"))
a3 = int(input("quant ex1 arqueiro:"))
a4 = int(input("quant ex1 lobo:"))
a5 = int(input("quant ex1 águia:"))
a6 = int(input("quant ex1 estilingue:"))
#inputs para a quantidade de tropas do ex_1

EX_1 = {
    "dinossauro": {"quant": a1, "atr": atributos_unidades["unit_1"], "exercito" : "exército 1"},
    "galinha": {"quant": a2, "atr": atributos_unidades["unit_2"], "exercito" : "exército 1"},
    "arqueiro": {"quant": a3, "atr": atributos_unidades["unit_3"], "exercito" : "exército 1"},
    "lobo": {"quant": a4, "atr": atributos_unidades["unit_4"], "exercito" : "exército 1"},
    "águia": {"quant": a5, "atr": atributos_unidades["unit_5"], "exercito" : "exército 1"},
    "estilingue": {"quant": a6, "atr": atributos_unidades["unit_6"], "exercito" : "exército 1"}

}
#exercito 1

b1 = int(input("quant ex2 dino:"))
b2 = int(input("quant ex2 galinha:"))
b3 = int(input("quant ex2 arqueiro:"))
b4 = int(input("quant ex2 lobo:"))
b5 = int(input("quant ex2 águia:"))
b6 = int(input("quant ex2 estilingue:"))
#inputs para a quantidade de tropas do ex_2

EX_2 = {
    "dinossauro": {"quant": b1, "atr": atributos_unidades["unit_1"], "exercito" : "exército 2"},
    "galinha": {"quant": b2, "atr": atributos_unidades["unit_2"], "exercito" : "exército 2"},
    "arqueiro": {"quant": b3, "atr": atributos_unidades["unit_3"], "exercito" : "exército 2"},
    "lobo": {"quant": b4, "atr": atributos_unidades["unit_4"], "exercito" : "exército 2"},
    "águia": {"quant": b5, "atr": atributos_unidades["unit_5"], "exercito" : "exército 2"},
    "estilingue": {"quant": b6, "atr": atributos_unidades["unit_6"], "exercito" : "exército 2"}
}
#exercito 2


def confronto(b, atqex, atqexin, a, alvoex, alvoexin, vantagem_terreno_atq, vantagem_terreno_def, esquiva):
    result = luta(b, a, vantagem_terreno_atq, vantagem_terreno_def, esquiva)
    if result:
        alvoex[a["classe"]]["quant"] -= 1
        alvoexin.pop(a["classe"])
        print("{} do {} matou {} do {}".format(b["classe"], atqex[b["classe"]]["exercito"], a["classe"], alvoex[a["classe"]]["exercito"]))
    else:
        confronto(a, alvoex, alvoexin, b, atqex, atqexin, vantagem_terreno_atq, vantagem_terreno_def, esquiva)
#define o confronto direto entre 2 tropas
#primeiro um ataca e outro defende, caso o alvo não morra chama a função de novo com papeis invertidos
        

ex1in = dict()
ex2in = dict()
#exercitos de tropas em confrontos

while True:
    atacante = random.choice(list(EX_1.keys()))
    alvo = random.choice(list(EX_2.keys()))
    #define as tropas que vão se confrontar

    if atacante in ex1in:
        atacante = ex1in[atacante]
    else:
        ex1in[atacante] = copy.deepcopy(EX_1[atacante]["atr"])
        atacante = ex1in[atacante]

    if alvo in ex2in:
        alvo = ex2in[alvo]
    else:
        ex2in[alvo] = copy.deepcopy(EX_2[alvo]["atr"])
        alvo = ex2in[alvo]
    #coloca as tropas nos exércitos de tropas em confrontos

    e = random.randint(0, 30)
    co = random.randint(0, 1)
    vantagens_de_terreno = [0.8, 1, 1.2]
    vta = vantagens_de_terreno[random.randint(0, 2)]
    vtd = vantagens_de_terreno[random.randint(0, 2)]
    #variáveis que define multipricadores e outros fatores de batalha
    

    if co == 1:
        confronto(atacante, EX_1, ex1in, alvo, EX_2, ex2in, vta, vtd, e)
    else:
        confronto(alvo, EX_2, ex2in, atacante, EX_1, ex1in, vtd, vta, e)
    #define quem começa atacando
        
    if EX_1[atacante["classe"]]["quant"] <= 0:
        EX_1.pop(atacante["classe"])   
    if EX_2[alvo["classe"]]["quant"] <= 0:
        EX_2.pop(alvo["classe"])
    #remove tropas mortas
    
    if EX_1 == {}:
        print("EXERCITO DOIS GANHOU")
        break

    if EX_2 == {}:
        print("EXERCITO UM GANHO")
        break
    #mostra o resultado


print("No ex1 sobraram:")
for d in atributos_unidades.values():
    if d["classe"] not in EX_1:
        print(0, d["classe"]+"s")
    else:
        print(EX_1[d["classe"]]["quant"], d["classe"]+"s")

print("No ex2 sobraram:")
for d in atributos_unidades.values():
    if d["classe"] not in EX_2:
        print(0, d["classe"]+"s")
    else:
        print(EX_2[d["classe"]]["quant"], d["classe"]+"s")
#mostra os sobreviventes
