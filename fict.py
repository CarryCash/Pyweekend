import numpy as np
import fcnm
import climage
import time

from climage import color_to_flags, color_types, convert




# Parámetros del laberinto
ANCHO = 20
ALTO = 10

# Caracteres para el laberinto
PARED_HORIZONTAL = '-'
PARED_VERTICAL = '|'
ESQUINA = '+'
VACIO = ' '
JUGADOR = '👤'
HABILIDAD = '🎓'
SALIDA = '🚪'

def crear_laberinto(ancho, alto):
    laberinto = np.full((alto, ancho), VACIO, dtype=str)
    
    # Dibujar las paredes exteriores
    laberinto[0, :] = PARED_HORIZONTAL
    laberinto[-1, :] = PARED_HORIZONTAL
    laberinto[:, 0] = PARED_VERTICAL
    laberinto[:, -1] = PARED_VERTICAL
    laberinto[0, 0] = ESQUINA
    laberinto[0, -1] = ESQUINA
    laberinto[-1, 0] = ESQUINA
    laberinto[-1, -1] = ESQUINA
    
    # Añadir paredes internas para crear un laberinto más complejo
    laberinto[2, 2:8] = PARED_HORIZONTAL
    laberinto[4, 2:8] = PARED_HORIZONTAL
    laberinto[6, 2:8] = PARED_HORIZONTAL
    laberinto[2:8, 4] = PARED_VERTICAL
    laberinto[2:6, 6] = PARED_VERTICAL
    
    # Añadir habilidad y salida
    laberinto[5, 3] = HABILIDAD  # Nueva posición de la habilidad
    laberinto[8, 18] = SALIDA    # Salida en la posición (8, 18)

    return laberinto

def imprimir_laberinto(laberinto, pos_jugador, tiene_habilidad):
    laberinto_con_jugador = laberinto.copy()
    y, x = pos_jugador
    laberinto_con_jugador[y, x] = JUGADOR
    
    if tiene_habilidad:
        laberinto_con_jugador[5, 3] = VACIO  # La habilidad desaparece después de recogerla
    
    for fila in laberinto_con_jugador:
        print("".join(fila))
    print()  # Línea en blanco para separar cada impresión

def mover_jugador(posicion, direccion, laberinto):
    y, x = posicion
    if direccion == 'w' and laberinto[y - 1, x] != PARED_HORIZONTAL:
        y -= 1
    elif direccion == 's' and laberinto[y + 1, x] != PARED_HORIZONTAL:
        y += 1
    elif direccion == 'a' and laberinto[y, x - 1] != PARED_VERTICAL:
        x -= 1
    elif direccion == 'd' and laberinto[y, x + 1] != PARED_VERTICAL:
        x += 1
    return (y, x)


def main(puntaje_anterior):
    laberinto = crear_laberinto(ANCHO, ALTO)
    pos_jugador = (1, 1)  # Posición inicial del jugador
    tiene_habilidad = False  # El jugador empieza sin habilidad
    puntos = 0  # Puntuación obtenida en el nivel actual
    
    print("Capítulo 4: FICT - El Laberinto de la Tierra")
    print("\n")

    time.sleep(3)
    print("Después de superar el desafío en FIMCP, se adentra en la Facultad de Ingenierías en Ciencia de la Tierra (FICT). Esta facultad, llena de modelos geológicos, mapas topográficos y simulaciones de procesos naturales, es el próximo escenario de tu aventura. Aquí, enfrentarás un desafío que pondrá a prueba tu habilidad para orientarte y tu ingenio.")
    print("\n")

    time.sleep(3)
    print("Al ingresar a FICT, te encuentras en un entorno que simula un vasto paisaje subterráneo, con túneles y cavernas que se extienden en todas direcciones. Una pantalla holográfica se activa y muestra un laberinto tridimensional que representa el desafío que debes enfrentar.")
    
    time.sleep(3)
    print("Un holograma de un geólogo aparece y te dice:")
    time.sleep(3)
    print("Bienvenido a la Facultad de Ingenierías en Ciencia de la Tierra. Para avanzar, debes atravesar nuestro laberinto subterráneo. Este laberinto está diseñado para simular los complejos sistemas geológicos que estudiamos aquí. Solo encontrando la salida podrás continuar con tu búsqueda.")
    time.sleep(3)
    
    print("Instrucciones:")
    print("w - Mover hacia arriba")
    print("a - Mover hacia la izquierda")
    print("s - Mover hacia abajo")
    print("d - Mover hacia la derecha")
    print("Encuentra la habilidad (⚡) y la salida (E) para ganar.\n")
    
    juego_en_progreso = True
    
    while juego_en_progreso:
        imprimir_laberinto(laberinto, pos_jugador, tiene_habilidad)
        movimiento = input("Mover (w/a/s/d): ").strip()
        
        if movimiento in ('w', 'a', 's', 'd'):
            pos_jugador = mover_jugador(pos_jugador, movimiento, laberinto)
            
            if pos_jugador == (5, 3) and not tiene_habilidad:
                tiene_habilidad = True
                print("¡Has recogido la habilidad!")
            
            if pos_jugador == (8, 18):
                if tiene_habilidad:
                    print("¡Excelente trabajo! Has demostrado tu capacidad para orientarte en los complejos sistemas geológicos. Al superar el laberinto, has desbloqueado un fragmento del enigma que estás buscando. La comprensión de la Tierra te ha llevado un paso más cerca de resolver el misterio final.")
                    print("\n")

                    time.sleep(3)
                    print("El laberinto se disuelve y revela una entrada secreta que te lleva a la siguiente facultad. Mientras avanzas hacia la salida, el holograma te da un último mensaje:")
                    print("\n")

                    time.sleep(3)
                    print("El camino hacia el conocimiento es a menudo complicado, pero con cada desafío superado, estás más cerca de desvelar los secretos que buscas. Prepárate para la próxima etapa de tu aventura.")
                    print("\n")

                    time.sleep(3)
                    print("Con el laberinto superado, te preparas para tu próximo destino, listo para enfrentar nuevos desafíos en tu viaje.")
                    print("\n")

                    time.sleep(2)
                    puntos += 30
                    puntaje_total = puntaje_anterior + puntos
                    print(f"Tu puntaje total acumulado: {puntaje_total}")
                    juego_en_progreso = False
                else:
                    print("Necesitas la habilidad para pasar al siguiente nivel.")
    
    # Llamar a la función principal de fcnm.py con el puntaje total acumulado
    fcnm.juego_calculo(puntaje_total)


if __name__ == "__main__":
    nombre_psj = "Jugador"  
    puntaje_anterior = 0  
    main(puntaje_anterior)
