import random
import climage
from climage import color_to_flags, color_types, convert
import fimcp
import time

puntaje_global = 0

def mostrar_opciones(opciones):
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")

def validar_respuesta(eleccion_fadcom, respuesta_fadcom, intentos_logica):
    if eleccion_fadcom == respuesta_fadcom + 1:
        return True
    else:
        intentos_logica += 1
        print(f"Incorrecto. Te quedan {3 - intentos_logica} intentos más.")
        return False

def obtener_eleccion():
    eleccion = input("Ingresa el número de la opción correcta: ")
    if eleccion.isdigit():
        return int(eleccion)
    else:
        print("Ingresa un número válido.")
        return None

def mostrar_acertijos(acertijos):
    for idx, (pregunta, _) in enumerate(acertijos):
        print(f"Acertijo {idx+1}: {pregunta}")

def obtener_respuesta_acertijo():
    return input("Ingresa tu respuesta: ").strip().lower()

def verificar_respuesta_acertijo(respuesta, respuesta_correcta):
    return respuesta == respuesta_correcta

def actualizar_puntaje(intentos_acertijos):
    global puntaje_global
    if intentos_acertijos == 0:
        puntaje_global += 3  
    elif intentos_acertijos == 1:
        puntaje_global += 1  
        

def logica_diseno_grafico(nombre_psj):
    global puntaje_global
    print(f"Después de descubrir el misterioso libro El Rastro de los Sabios, {nombre_psj} se dirige a FADCOM, la Facultad de Diseño y Comunicación Audiovisual, para enfrentar su primer desafío. Esta facultad es conocida por su creatividad y vibrante energía, y se dice que guarda un enigma oculto relacionado con su verdadero color representativo. Para desentrañar este enigma, debes resolver una serie de acertijos que revelarán cinco palabras clave. Cada palabra, al completar su primera letra, te llevará más cerca de descubrir el color que define a FADCOM y desbloquear la siguiente fase de tu aventura.")

    print("Desafío de lógica - Diseño Gráfico:")
    print("¿Cuál de estos colores representa a Fadcom?")
    opciones = ["azul", "rojo", "fuxia", "verde"]
    respuesta_fadcom = 2  # El color correcto es el fuxia
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")
    
    intentos_logica = 0
    
    while intentos_logica < 3:
        eleccion_fadcom = obtener_eleccion()
        if eleccion_fadcom is not None:
            if validar_respuesta(eleccion_fadcom, respuesta_fadcom, intentos_logica):
                puntaje_global += 3 if intentos_logica == 0 else 1
                print("¡Correcto!")
                
                return True
        intentos_logica += 1

    print(f"Has agotado tus intentos en el desafío de lógica, {nombre_psj}.")
    return False

def pl_acertijos(nombre_psj):
    global puntaje_global
    
    print("Desafío de memoria - Acertijos:")
    acertijos = [
        ("En el arte y el diseño, soy esencial para definir la estructura de los objetos y las figuras. Sin mí, las ideas quedan en caos. ¿Qué soy?", "forma"),
        ("En el cine y la fotografía, capturo momentos en el tiempo, inmortalizando imágenes para siempre. ¿Qué soy?", "angulo"),
        ("En el diseño gráfico, soy la clave para crear composiciones equilibradas, guiando la mirada del espectador. ¿Qué soy?", "dimension"),
        ("Soy la herramienta que da forma a las palabras, dando vida a las ideas en papel o pantalla. ¿Qué soy?", "composicion"),
        ("Soy el espacio entre las líneas y las formas, y sin mí, el diseño sería caótico y confuso. ¿Qué soy?", "orden"),
        ("En la edición de video, soy el proceso que transforma horas de grabación en una narrativa coherente y emocionante. ¿Qué soy?", "montaje")
    ]
    
    mostrar_acertijos(acertijos)
    
    for idx, (_, respuesta_correcta) in enumerate(acertijos):
        intentos_acertijos = 0
        acertijo_resuelto = False
        
        while intentos_acertijos < 3 and not acertijo_resuelto:
            respuesta = obtener_respuesta_acertijo()
            if verificar_respuesta_acertijo(respuesta, respuesta_correcta):
                print(f"La letra '{respuesta_correcta[0].upper()}' se ilumina.")
                actualizar_puntaje(intentos_acertijos)
                print(f"Puntaje actual: {puntaje_global} puntos")
                acertijo_resuelto = True
            else:
                intentos_acertijos += 1
                if intentos_acertijos < 3:
                    print(f"Incorrecto. Te quedan {3 - intentos_acertijos} intentos más.")
                else:
                    print(f"Has agotado tus intentos en el acertijo {idx + 1}, {nombre_psj}.")
                    return False
    
    print(f"\n¡Felicidades {nombre_psj}! Has completado todos los acertijos.")
    print("La palabra clave encontrada es: FADCOM")

    
    # Ingresar al siguiente nivel
    
    return True

def mini_juegofd(nombre_psj):
    global puntaje_global
    
    print("Capítulo 2: FADCOM - El Enigma del Color Perdido")
    time.sleep(3)
    print("\n")

    print("Al entrar en FADCOM, te encuentras rodeado de una explosión de colores y formas artísticas. Los muros están cubiertos de murales, los pasillos están llenos de pantallas que muestran obras de estudiantes, y en el aire se respira un ambiente de constante creatividad. Sin embargo, sientes que algo falta, como si un color esencial estuviera ausente.")
    time.sleep(2)
    print("\n")

    print("De repente, te das cuenta de que las paredes y pantallas comienzan a oscurecerse, dejando solo una paleta de tonos neutros. Aparece un holograma que te habla con una voz tranquila pero autoritaria:")
    time.sleep(2)
    print("\n")

    
    print("Bienvenido a FADCOM, donde el color es más que una simple percepción; es el alma de nuestra creatividad. Para avanzar, debes descubrir el color que nos representa. Para hacerlo, primero debes encontrar y resolver cinco acertijos. Cada acertijo te dará una palabra clave y la primera letra de cada palabra formará el nombre de nuestra facultad: FADCOM. Solo entonces el verdadero color será revelado.")
        
    print("\nEnemigo 1: Esteban, el maestro del engaño")
    
    if not logica_diseno_grafico(nombre_psj):
        print("Esteban ha ganado. Fin del juego.")
        return False
    
    print("\nEnemigo 2: Laura, la ilusionista")
    
    if not pl_acertijos(nombre_psj):
        print("Laura te ha superado. Fin del juego.")
        return False
    
    return True

def main_fadcom(nombre_psj):
    global puntaje_global
    puntaje_global = 0  # Reiniciar el puntaje global para el juego
    resultado = mini_juegofd(nombre_psj)
    
    if resultado:
        print(f"¡Buen intento {nombre_psj}! Tu puntaje final es {puntaje_global}.")
        print("\n")

        time.sleep(3)
        print("Con todas las letras de FADCOM iluminadas y los enemigos derrotados, los muros de la facultad se llenan nuevamente de colores vibrantes, pero ahora, un color sobresale entre todos: el verdadero color representativo de FADCOM. El holograma vuelve a aparecer y te felicita:")
        print("\n")

        time.sleep(3)
        print("Has desentrañado el enigma. Este color representa la esencia de nuestra facultad, donde la creatividad no tiene límites. Continúa tu búsqueda, nombre_jugador_aqui. El camino hacia el conocimiento solo acaba de comenzar.")
        print("\n")

        time.sleep(3)
        print("Con el enigma resuelto, el camino hacia la siguiente facultad se desbloquea, y tu aventura continúa.")
        print("\n")

        time.sleep(3)
        print(convert('img/img_4.jpg', is_unicode=True, **color_to_flags(color_types.truecolor)))

        nombre_psj = fimcp.main_fimcp(nombre_psj, puntaje_global)
        puntaje_total = fimcp.main_fimcp(nombre_psj, puntaje_global)
        return nombre_psj, puntaje_total
        
    else:
        print(f"\nEstuviste cerca {nombre_psj} !!.")
        return nombre_psj, puntaje_global
