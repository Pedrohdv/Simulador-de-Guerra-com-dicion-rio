import random
import copy
import sys

sys.setrecursionlimit(10**6*2)

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

vantagens_de_classe = {
    "águia": {"dinossauro": 1.2, "lobo": 1.2},
    "arqueiro": {"águia": 1.2, "galinha": 1.2},
    "estilingue": {"águia": 1.2, "galinha": 1.2},
    "lobo": {"arqueiro": 1.2, "estilingue": 1.2}
}


#não vai se aplicar á aguia

def calculo_ataque(atacante, alvo, vantagem_terreno, vantagem_classe, multiplicador_distancia):
    a = atacante["ataque"]
    if atacante["classe"] == "águia" or alvo["classe"] == "águia":
        return a * vantagem_classe * multiplicador_distancia
    else:
        return a * vantagem_terreno * vantagem_classe * multiplicador_distancia


def calculo_defesa(alvo, atacante, vantagem_terreno, vantagem_classe, multiplicador_distancia):
    if alvo == "unit_5" or atacante == "unit_5":
        return alvo["defesa"] * vantagem_classe * multiplicador_distancia
    else:
        return alvo["defesa"] * vantagem_terreno * vantagem_classe * multiplicador_distancia


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


a1 = int(input("quant ex1 dino:"))
a2 = int(input("quant ex1 galinha:"))
a3 = int(input("quant ex1 arqueiro:"))
a4 = int(input("quant ex1 lobo:"))
a5 = int(input("quant ex1 águia:"))
a6 = int(input("quant ex1 estilingue:"))

EX_1 = {
    "dinossauro": {"quant": a1, "atr": atributos_unidades["unit_1"]},
    "galinha": {"quant": a2, "atr": atributos_unidades["unit_2"]},
    "arqueiro": {"quant": a3, "atr": atributos_unidades["unit_3"]},
    "lobo": {"quant": a4, "atr": atributos_unidades["unit_4"]},
    "águia": {"quant": a5, "atr": atributos_unidades["unit_5"]},
    "estilingue": {"quant": a6, "atr": atributos_unidades["unit_6"]}

}

b1 = int(input("quant ex2 dino:"))
b2 = int(input("quant ex2 galinha:"))
b3 = int(input("quant ex2 arqueiro:"))
b4 = int(input("quant ex2 lobo:"))
b5 = int(input("quant ex2 águia:"))
b6 = int(input("quant ex2 estilingue:"))

EX_2 = {
    "dinossauro": {"quant": b1, "atr": atributos_unidades["unit_1"]},
    "galinha": {"quant": b2, "atr": atributos_unidades["unit_2"]},
    "arqueiro": {"quant": b3, "atr": atributos_unidades["unit_3"]},
    "lobo": {"quant": b4, "atr": atributos_unidades["unit_4"]},
    "águia": {"quant": b5, "atr": atributos_unidades["unit_5"]},
    "estilingue": {"quant": b6, "atr": atributos_unidades["unit_6"]}
}


def confronto(b, atqex, atqexin, a, alvoex, alvoexin, vantagem_terreno_atq, vantagem_terreno_def, esquiva):
    result = luta(b, a, vantagem_terreno_atq, vantagem_terreno_def, esquiva)
    if result:
        alvoex[a["classe"]]["quant"] -= 1
        alvoexin.pop(a["classe"])
    else:
        confronto(a, alvoex, alvoexin, b, atqex, atqexin, vantagem_terreno_atq, vantagem_terreno_def, esquiva)


ex1in = dict()
ex2in = dict()

while True:
    atacante = random.choice(list(EX_1.keys()))
    alvo = random.choice(list(EX_2.keys()))

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

    e = random.randint(0, 30)
    co = random.randint(0, 1)
    vantagens_de_terreno = [0.8, 1, 1.2]
    vta = vantagens_de_terreno[random.randint(0, 2)]
    vtd = vantagens_de_terreno[random.randint(0, 2)]

    if co == 1:
        confronto(atacante, EX_1, ex1in, alvo, EX_2, ex2in, vta, vtd, e)
    else:
        confronto(alvo, EX_2, ex2in, atacante, EX_1, ex1in, vtd, vta, e)

    if EX_1[atacante["classe"]]["quant"] <= 0:
        EX_1.pop(atacante["classe"])

    if EX_2[alvo["classe"]]["quant"] <= 0:
        EX_2.pop(alvo["classe"])
    if EX_1 == {}:
        print("EXERCITO DOIS DEU GREMIO")
        break

    if EX_2 == {}:
        print("EXERCITO UM DEU GREMIO")
        break


print("No ex1 sobraram:")
print(EX_1["dinossauro"]["quant"], "dinossauros")
print(EX_1["galinha"]["quant"], "galinhas")
print(EX_1["arqueiro"]["quant"], "arqueiros")
print(EX_1["lobo"]["quant"], "lobos")
print(EX_1["águia"]["quant"], "águias")
print(EX_1["estilingue"]["quant"], "estilingues")

print("No ex2 sobraram:")
print(EX_2["dinossauro"]["quant"], "dinossauros")
print(EX_2["galinha"]["quant"], "galinhas")
print(EX_2["arqueiro"]["quant"], "arqueiros")
print(EX_2["lobo"]["quant"], "lobos")
print(EX_2["águia"]["quant"], "águias")
print(EX_2["estilingue"]["quant"], "estilingues")
