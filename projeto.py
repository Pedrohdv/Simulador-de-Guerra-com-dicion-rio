from random import *

atributos_unidades = {
    "unit_1": {"classe": "dinossauro", "vida": 500, "vidamax": 500, "ataque": 200, "defesa": 100,
               "agilidade": 1, "distancia_preferida": "perto"},
    "unit_2": {"classe": "galinha", "vida": 50, "vidamax": 50, "ataque": 10, "defesa": 20,
               "agilidade": 8, "distancia_preferida": "perto"},
    "unit_3": {"classe": "arqueiro", "vida": 200, "vidamax": 200, "ataque": 100, "defesa": 40,
               "agilidade": 5, "distancia_preferida": "longe"},
    "unit_4": {"classe": "lobo", "vida": 250, "vidamax": 250, "ataque": 75, "defesa": 50,
               "agilidade": 7, "distancia_preferida": "perto"},
    "unit_5": {"classe": "águia", "vida": 100, "vidamax": 100, "ataque": 100, "defesa": 30,
               "agilidade": 10, "distancia_preferida": "perto"},
    "unit_6": {"classe": "estilingue", "vida": 200, "vidamax": 200, "ataque": 50, "defesa": 30,
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
    if atacante == "unit_5" or alvo == "unit_5":
        return atacante["ataque"] * vantagem_classe * multiplicador_distancia
    else:
        return atacante["ataque"] * vantagem_terreno * vantagem_classe * multiplicador_distancia


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
    elif (distancia_atacante["perto"] and atacante["vida"] == atacante["vidamax"]) or (
            distancia_atacante["longe"] and alvo["vida"] != alvo["vidamax"]):
        return 1.2
    else:
        return 0.8
