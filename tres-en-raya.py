##tres en raya con algoritmo MiniMax
#Inteligencia artificial y juegos
#uso de algoritmo MiniMax
import sys
MAX=1
MIN=-1
global jugada_maquina

def minimax(tablero, jugador):
    global jugada_maquina

    #hay ganador o empate? (nodo terminal)
    if  game_over(tablero):
        return [ganador(tablero), 0]
    
    #generar las posibles jugadas3
    movimientos = []
    for jugada in range(0,len(tablero)):
        if tablero[jugada] == 0:
            tableroaux = tablero[:]
            tableroaux[jugada] = jugador
            
            puntuacion = minimax(tableroaux, jugador*(-1))
            movimientos.append([puntuacion, jugada])
    if jugador==MAX:
        movimiento = max(movimientos)
        jugada_maquina = movimiento[1]
    else:
        movimiento=min(movimientos)
        
    return movimiento[0]

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
                
        if str(casilla) in '0123456789' and len(str(casilla)) ==1 \
            and tablero[casilla-1] ==0:
            tablero[casilla-1]=MIN
            ok=True
    return tablero

def juega_computador(tablero):
    global jugada_maquina
    punt = minimax(tablero[:], MAX)
    tablero[jugada_maquina]=MAX
    return tablero

if __name__ == '__main__':
    print("Introduce casilla o 0 para terminar: ")
    tablero = [0,0,0,0,0,0,0,0,0]    
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