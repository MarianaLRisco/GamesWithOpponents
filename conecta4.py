#conecta 4 con poda alfa-beta
import sys
import copy
MAX = 1
MIN = -1
MAX_PROFUNDIDAD = 4

def negamax(tablero, jugador, profundidad, alfa, beta):
    max_puntuacion = -sys.maxsize-1 #poniendo limite
    alfa_local = alfa
    for jugada in range(7):
        #columna totalmente llena?
        if tablero[0][jugada] == 0:
            tableroaux=copy.deepcopy(tablero)
            insertar_ficha(tableroaux, jugada, jugador)
            if game_over(tableroaux) or profundidad == 0:
                return [evalua_jugada(tableroaux, jugador), jugada]
            else:
                puntuacion = -negamax(tableroaux, jugador*(-1), profundidad-1, -beta, -alfa_local)[0]
                
            if puntuacion > max_puntuacion:
                max_puntuacion = puntuacion
                jugada_max = jugada

            #poda alfa-beta
            if max_puntuacion >= beta:
                break
            if max_puntuacion > alfa_local:
                alfa_local = max_puntuacion
                
    return [max_puntuacion, jugada_max]

def evalua_jugada(tablero, jugador):
    n2=comprueba_linea(tablero, 2 ,jugador)[1]
    n3=comprueba_linea(tablero, 3, jugador)[1]
    n4=comprueba_linea(tablero, 4, jugador)[1]
    valor_jugada=4*n2+9*n3+1000*n4
    return valor_jugada

def game_over(tablero):
    #hay empate?
    no_hay_empate = False
    for i in range(7):
        for j in range(7):
            if tablero[i][j] == 0:
                no_hay_empate = True
                break
        if no_hay_empate:
            break
    #hay ganador?
    if ganador(tablero)[0] == 0 and no_hay_empate:
        return False
    else:
        return True

def comprueba_linea(tablero, n, jugador):
    #comprueba si hay una linea en n filas
    ganador = 0
    num_lineas = 0
    lineas_posibles = 8-n

    #busca linea horizontal
    for i in range(7):
        for j in range(lineas_posibles):
            cuaterna=tablero[i][j:j+n]
            if cuaterna==[tablero[i][j]]*n and tablero[i][j]!=0:
                ganador=tablero[i][j]
                if ganador==jugador:
                    num_lineas=num_lineas+1;
    
    #buscar linea vertical
    for i in range(7):
        for j in range(lineas_posibles):
            cuaterna=[]
            for k in range(n):
                cuaterna.append(tablero[j+k][i])
            if cuaterna==[tablero[j][i]]*n and tablero[j][i]!=0:
                ganador = tablero[j][i]
                if ganador==jugador:
                    num_lineas=num_lineas+1;
    
    #buscar linea diagonal
    for i in range(4):
        for j in range(lineas_posibles-i):
            cuaterna1=[]
            cuaterna2=[]
            cuaterna3=[]
            cuaterna4=[]
            for k in range(n):
                cuaterna1.append(tablero[i+j+k][j+k])
                cuaterna2.append(tablero[j+k][i+j+k])
                cuaterna3.append(tablero[i+j+k][6-(j+k)])
                cuaterna4.append(tablero[j+k][6-(i+j+k)])

            if cuaterna1==[cuaterna1[0]]*n and tablero[i+j][j]!=0:
                ganador = tablero[i+j][j]
                if ganador==jugador:
                    num_lineas=num_lineas+1;
            elif cuaterna2==[cuaterna2[0]]*n and tablero[j][i+j]!=0:
                ganador = tablero[j][i+j]
                if ganador==jugador:
                    num_lineas=num_lineas+1;
            elif cuaterna3==[cuaterna3[0]]*n and tablero[i+j][6-j]!=0:
                ganador = tablero[i+j][6-j]
                if ganador==jugador:
                    num_lineas=num_lineas+1;
            elif cuaterna4==[cuaterna4[0]]*n and tablero[j][6-(i+j)]!=0:
                ganador = tablero[j][6-(i+j)]
                if ganador==jugador:
                    num_lineas=num_lineas+1;
    return (ganador, num_lineas)

def ganador(tablero):
    return comprueba_linea(tablero, 4, 0)

def ver_tablero(tablero):
    for i in range(7):
        for j in range(7):            
            if tablero[i][j]==MAX:
                print('X', end=" ")
            elif tablero[i][j]==MIN:
                print('O', end=" ")                
            else:
                print('.', end=" ")
        print("")
    print('- - - - - - -')
    print('1 2 3 4 5 6 7')

def insertar_ficha(tablero, columna, jugador):
    #encontrar la primera casilla libre en la columna
    #y colocar la ficha
    ok=False
    for i in range(6, -1, -1): #(inicio, hasta -1 osea agarrando 0,como va disminuyendo -1)
        if (tablero[i][columna] == 0):
            tablero[i][columna] = jugador
            ok=True
            break
    return ok

def juega_humano(tablero):
    ok=False
    while not ok:
        col: int = int(input("Columna (1-7) o 0 (salir)?: "))
        
        if col==0:
            ok = True
            print("Terminó el programa!")
            sys.exit(0)        
        
        if str(col) in '01234567' and len(str(col))==1:
            ok=insertar_ficha(tablero, col-1, MIN)
        if ok == False:
            print("Movimiento Ilegal")
            
    return tablero

def juega_computador(tablero):
    tablerotmp=copy.deepcopy(tablero)
    punt, jugada = \
    negamax(tablerotmp, MAX, MAX_PROFUNDIDAD,-sys.maxsize-1, sys.maxsize)
    insertar_ficha(tablero, jugada, MAX)
    return tablero

if __name__ == '__main__':
    #tablero 7x7
    tablero=[[0 for j in range(7)] for i in range(7)]

    ok=False
    profundidades=[3, 4, 6]

    while not ok:
        dificultad: int = int(input("Dificultad (1=Facil, 2=Medio, 3=Dificil): "))
        if str(dificultad) in '123' and len(str(dificultad)) == 1:
            MAX_PROFUNDIDAD=profundidades[dificultad-1]
            ok=True

    while True:
        ver_tablero(tablero)
        tablero = juega_humano(tablero)
        if game_over(tablero):
            break

        tablero = juega_computador(tablero)
        if game_over(tablero):
            break

    ver_tablero(tablero)
    g=ganador(tablero)[0]
    if g==0:
        gana= '¡Empate!'
    elif g==MIN:
        gana= '¡Ganó Jugador!'
    else:
        gana= '¡Ganó el Computador!'

    print('Resultado: '+gana)