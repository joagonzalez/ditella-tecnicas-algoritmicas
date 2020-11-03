# Devuelve la probabilidad de que Laura gane el juego; es decir,
# la probabilidad de que la primera bolita roja salga en el primer
# turno, o en el tercero, o en el quinto, etc.
def prob_laura(r, v):
    ret = 0
    turno = 1
    while turno <= r+v:
        ret = ret + prob_primera_roja_en_turno(r, v, turno)
        turno = turno + 2
    return ret

# Dadas r bolitas rojas y v bolitas verdes, devuelve la probabilidad
# de que la primera bolita roja salga en el turno indicado; es decir, la
# probabilidad de que primero salgan (turno-1) verdes y luego una roja.
def prob_primera_roja_en_turno(r, v, turno):
    ret = 1
    i = 1
    while i < turno:
        ret = ret * prob_verde(r, v)
        v = v - 1
        i = i + 1
    ret = ret * prob_roja(r, v)
    return ret

# Dadas r bolitas rojas y v bolitas verdes,
# devuelve la probabilidad de sacar una bolita roja.
def prob_roja(r, v):
    if r == 0:
        ret = 0
    else:
        ret = r/(r+v)
    return ret

# Dadas r bolitas rojas y v bolitas verdes,
# devuelve la probabilidad de sacar una bolita verde.
def prob_verde(r, v):
    if v == 0:
        ret = 0
    else:
        ret = v/(r+v)
    return ret

def prob_laura_iter(r, v):
    pass


if __name__ == '__main__':
    ROJAS = 20
    VERDES = 3
    print('Probabilidad de que gane laura O(N2): ' + str(prob_laura(ROJAS, VERDES)))
    print('Probabilidad de que gane laura O(N): ' + str(prob_laura_iter(ROJAS, VERDES)))