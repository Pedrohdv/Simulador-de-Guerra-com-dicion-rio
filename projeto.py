import random


atributos_unidades = {
    "unit_1": {"classe": "dinossauro", "vida": 500, "vidamax": 500, "ataque": 200, "defesa": 50,
               "agilidade": -1, "distancia_preferida": "perto"},
    "unit_2": {"classe": "galinha", "vida": 50, "vidamax": 50, "ataque": 10, "defesa": 10,
               "agilidade": 8, "distancia_preferida": "perto"},
    "unit_3": {"classe": "arqueiro", "vida": 200, "vidamax": 200, "ataque": 100, "defesa": 20,
               "agilidade": 6, "distancia_preferida": "longe"},
    "unit_4": {"classe": "lobo", "vida": 250, "vidamax": 250, "ataque": 75, "defesa": 25,
               "agilidade": 7, "distancia_preferida": "perto"},
    "unit_5": {"classe": "águia", "vida": 100, "vidamax": 100, "ataque": 100, "defesa": 15,
               "agilidade": 10, "distancia_preferida": "perto"},
    "unit_6": {"classe": "estilingue", "vida": 200, "vidamax": 200, "ataque": 50, "defesa": 15,
               "agilidade": 7, "distancia_preferida": "longe"}
}

vantagens_de_classe = {
    "águia": {"dinossauro": 1.2, "lobo": 1.2},
    "arqueiro": {"águia": 1.2, "galinha": 1.2},
    "estilingue": {"águia": 1.2, "galinha": 1.2},
    "lobo": {"arqueiro": 1.2, "estilingue": 1.2}
}

vantagens_de_terreno = {
    "vantagem_de_altura": {"ataque": 1.2, "defesa": 1.2},
    "desvantagem_de_altura": {"ataque": 0.8, "defesa": 0.8}
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


def luta(atacante, alvo, vantagem_terreno, esquiva):
    if esquiva <= alvo["agilidade"]:
        return False

    mutiplicador_distancia = calculo_multiplicador_distancia(atacante, alvo)

    vantagem_classe = 1
    if atacante["classe"] in vantagens_de_classe and alvo["classe"] in vantagens_de_classe[atacante["classe"]]:
        vantagem_classe = vantagens_de_classe[atacante["classe"]][alvo["classe"]]

    dano_atq = calculo_ataque(atacante, alvo, vantagem_terreno, vantagem_classe, mutiplicador_distancia)
    defesa = calculo_defesa(alvo, atacante, vantagem_terreno, vantagem_classe, mutiplicador_distancia)

    dano_rec = dano_atq - defesa

    if dano_rec < 0:
        dano_rec = 0

    alvo["vida"] -= dano_rec

    return alvo["vida"] <= 0


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


def confronto(atacante, atqex, alvo, alvoex, vantagem_terreno, esquiva):
    result = luta(atacante, alvo, vantagem_terreno, esquiva)
    if result:
        alvoex[alvo["classe"]]["quant"] = alvoex[alvo["classe"]]["quant"] - 1
    else:
        confronto(alvo,alvoex,atacante,atqex,vantagem_terreno, e)

while True:
    atacante = random.choice(list(EX_1.values()))["atr"]
    atqex = EX_1
    alvo = random.choice(list(EX_2.values()))["atr"]
    alvoex = EX_2

    e = random.randint(20,30)

    confronto(atacante, atqex, alvo, alvoex, 1, e)

    if atqex[atacante["classe"]]["quant"] <= 0:
        del atqex[atacante["classe"]]

    if alvoex[alvo["classe"]]["quant"] <= 0:
        del alvoex[alvo["classe"]]
    print(EX_1)
    print(EX_2)
    if atqex == {}:
        print("EXERCITO DOIS DEU GREMIO")
        break

    if alvoex == {}:
        print("EXERCITO UM DEU GREMIO")
        break


print(EX_1, EX_2)