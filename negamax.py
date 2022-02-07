##tres en raya con algoritmo negamax
#Inteligencia artificial y juegos
#uso de algoritmo negamax
import sys
MAX=1
MIN=-1
INF = sys.maxsize-1

def negamax(tablero, jugador, profundidad, alfa, beta):
    max_puntuacion = -INF
    alfa_local = alfa

    for jugada in range(0,len(tablero)):
        #columna totalmente llena?
        if tablero[jugada] == 0:
            tableroaux = tablero.copy()
            tableroaux[jugada] = jugador
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

def evalua_jugada(tablero,jugador):
    n2=comprueba_linea(tablero, 2 ,jugador)[1]
    n3=comprueba_linea(tablero, 3, jugador)[1]
    valor_jugada= n2 + 10*n3
    return valor_jugada

def comprueba_linea(table, n, jugador):
    #comprueba si hay una linea en n filas
    tablero = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila += [table[i*3+j]]
        tablero += [fila]

    ganador = 0
    num_lineas = 0
    lineas_posibles = 4-n

    #busca linea horizontal
    for i in range(3):
        for j in range(lineas_posibles):
            cuaterna=tablero[i][j:j+n]
            if cuaterna==[tablero[i][j]]*n and tablero[i][j]!=0:
                ganador=tablero[i][j]
                if ganador==jugador:
                    num_lineas=num_lineas+1
    
    #buscar linea vertical
    for i in range(3):
        for j in range(lineas_posibles):
            cuaterna=[]
            for k in range(n):
                cuaterna.append(tablero[j+k][i])
            if cuaterna==[tablero[j][i]]*n and tablero[j][i]!=0:
                ganador = tablero[j][i]
                if ganador==jugador:
                    num_lineas=num_lineas+1
    
    #buscar linea diagonal
    for j in range(lineas_posibles-i):
        cuaterna1=[]
        cuaterna2=[]
        cuaterna3=[]
        cuaterna4=[]
        for k in range(n):
            cuaterna1.append(tablero[i+j+k][j+k])
            cuaterna2.append(tablero[j+k][i+j+k])
            cuaterna3.append(tablero[j+k][2-(j+k)])
            cuaterna4.append(tablero[j+k][2-(i+j+k)])

        if cuaterna1==[cuaterna1[0]]*n and tablero[i+j][j]!=0:
            ganador = tablero[i+j][j]
            if ganador==jugador:
                num_lineas=num_lineas+1
        elif cuaterna2==[cuaterna2[0]]*n and tablero[j][i+j]!=0:
            ganador = tablero[j][i+j]
            if ganador==jugador:
                num_lineas=num_lineas+1
        elif cuaterna3==[cuaterna3[0]]*n and tablero[i+j][2-j]!=0:
            ganador = tablero[i+j][2-j]
            if ganador==jugador:
                num_lineas=num_lineas+1
        elif cuaterna4==[cuaterna4[0]]*n and tablero[j][2-(i+j)]!=0:
            ganador = tablero[j][2-(i+j)]
            if ganador==jugador:
                num_lineas=num_lineas+1
    return (ganador, num_lineas)

def game_over(tablero):
    #hay empate?
    no_hay_emplate=False
    for i in range(0,len(tablero)):
        if tablero[i]==0:
            no_hay_emplate=True
            break
    #hay ganador?
    if ganador(tablero)==0 and no_hay_emplate:
        return False
    else:
        return True

#Verifica si hay ganador entre (-1 y 1) en caso contrario retorna 0
def ganador(tablero):
    lineas=[[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    ganador=0
    for linea in lineas:
        if tablero[linea[0]]==tablero[linea[1]] and \
        tablero[linea[0]]==tablero[linea[2]] and tablero[linea[0]] != 0:
            ganador=tablero[linea[0]]
    return ganador

def ver_tablero(tablero):
    for i in range(0,3):
        fila = ''
        for j in range(0,3):
            if tablero[i*3+j]==MAX:
                fila += ' X '
            elif tablero[i*3+j]==MIN:
                fila += ' O '
            else:
                fila += ' . '
        print(fila)

def juega_humano(tablero):
    ok=False
    while not ok:
        casilla: int = int(input("Casilla (1-9) o 0 (Terminar)?: "))

        if casilla == 0:
            ok = True
            print("Terminó el programa!")
            sys.exit()
                
        if str(casilla) in '123456789' and len(str(casilla)) ==1 \
            and tablero[casilla-1] ==0:
            tablero[casilla-1]=MIN
            ok=True
    return tablero

def juega_computador(tablero):
    punt,jugada = negamax(tablero[:], MAX, MAX_PROFUNDIDAD, -INF, INF)
    tablero[jugada]=MAX
    return tablero

if __name__ == '__main__':
    tablero = [0,0,0,0,0,0,0,0,0]    
    print("Introduce casilla o 0 para terminar: ")
    
    ok=False
    profundidades=[1, 2, 4]
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
    g = ganador(tablero)
    if g == 0:
        gana = '¡Empate!'
    elif g == MIN:
        gana = '¡Ganó Jugador!'
    else:
        gana = '¡Ganó el Computador!'

    print("Resultado: "+gana)