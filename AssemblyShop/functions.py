from random import randint

LONGITUD_CODIGO = 10

def generarLetra():
    l = randint(0,5)
    if l == 0:
        return 'a'
    if l == 1:
        return 'b'
    if l == 2:
        return 'c'
    if l == 3:
        return 'd'
    if l == 4:
        return 'e'
    if l == 5:
        return 'f'

def generarCodigoToken():
    codigo = ''
    i=0
    while i<LONGITUD_CODIGO:
        if randint(1,2) == 1:
            codigo += str(randint(0,9))
        else:
            codigo += generarLetra()
        i += 1
    return codigo

def crearCodigoToken():
    codigo = generarCodigoToken()
    return codigo

