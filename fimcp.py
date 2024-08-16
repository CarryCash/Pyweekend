import random as rd
import climage
import time
from climage import color_to_flags, color_types, convert
import fict

def jugar_ahorcado(nombre_psj, puntaje_anterior):
    # Mostrar imágenes iniciales
    print("Capítulo 3: FIMCP - El Desafío del Ahorcado")
    time.sleep(3)
    print("Tras resolver el enigma en FADCOM, te diriges a la Facultad de Mecánica y Ciencias de la Producción (FIMCP). Este lugar está lleno de maquinaria, planos y modelos en 3D, reflejando el enfoque práctico y técnico de la facultad. Aquí, te enfrentarás a un desafío único que pondrá a prueba tus conocimientos sobre las carreras que se ofrecen en esta facultad.")
    time.sleep(3)
    print("Al ingresar a FIMCP, te recibes con un ambiente de trabajo activo y enérgico. Los laboratorios están repletos de prototipos, herramientas y maquetas. De repente, una pantalla grande se enciende y muestra un juego de ahorcado, diseñado para evaluar tus conocimientos sobre las carreras ofrecidas en la facultad.")
    time.sleep(3)
    print(convert('img/fimcp.jpg', is_unicode=True, **color_to_flags(color_types.truecolor)))
    time.sleep(3)
    print("Un holograma aparece y te dice: Bienvenido a FIMCP. Para avanzar, debes demostrar tu conocimiento sobre las carreras que definen nuestra facultad. Participa en un juego de ahorcado con una serie de palabras clave relacionadas con nuestras carreras. Cada palabra correcta te acercará a descubrir un fragmento del misterio que buscas.")
    time.sleep(3)
    print("En la pantalla aparece una serie de palabras incompletas, cada una representando una carrera de FIMCP. Tu tarea es adivinar las letras para completar las palabras. Aquí están las palabras del juego de ahorcado:")
    time.sleep(4)
    print(convert('img/desafio_fimcp.jpg', is_unicode=True, **color_to_flags(color_types.truecolor)))

    # Lista de palabras para el juego
    palabras = ["MECANICA", "ALIMENTOS", "INGENIERIA INDUSTRIAL", "MATERIALES", "MECATRONICA"]
    palabra = rd.choice(palabras)
    lista_palabra = list(palabra)

    # Variables del juego
    intentos = 3
    puntos = 0
    errores = 0
    intentos_letra = 0

    # Muñequitos del ahorcado
    dibujos = [
        """ ------
        |    |
        |
        |
        |
        |
        -------- """,
        """ ------
        |    |
        |    O
        |
        |
        |
        -------- """,
        """ ------
        |    |
        |    O
        |    |
        |
        |
        -------- """,
        """ ------
        |    |
        |    O
        |   /|\
        |
        |
        -------- """,
        """ ------
        |    |
        |    O
        |   /|\
        |   / \
        |
        -------- """
    ]

    # Mostrar mensaje de bienvenida y palabra a adivinar
    print("Bienvenido al juego del ahorcado")
    print("Palabra a adivinar")
    lista_jugador = ["_" for _ in lista_palabra]
    print(" ".join(lista_jugador))

    while lista_jugador != lista_palabra and errores < intentos:
        letra = input("Ingrese una letra: ").upper()
        intentos_letra += 1

        if letra in lista_palabra:
            for i in range(len(lista_palabra)):
                if lista_palabra[i] == letra:
                    lista_jugador[i] = letra
            if intentos_letra == 1:
                puntos += 2
            elif intentos_letra == 2:
                puntos += 1
        else:
            print(f"La letra {letra} no se encuentra en la palabra")
            errores += 1
            print(dibujos[errores])

        print(" ".join(lista_jugador))
        intentos_letra = 0

    if lista_jugador == lista_palabra:
        print(f"¡Felicidades! Adivinaste la palabra: {palabra}")
        puntos += 5  # Puntos por ganar el juego
    else:
        print(f"Lo siento, has perdido. La palabra era: {palabra}")

    print(f"Tu puntaje en este nivel es: {puntos}")

    # Actualizar el puntaje total
    puntaje_total = puntaje_anterior + puntos
    time.sleep(3)
    print("¡Impresionante! Has demostrado un profundo conocimiento de las carreras que definen nuestra facultad. Al resolver el desafío, has desbloqueado un secreto vital: el engranaje central de nuestro reloj mecánico se ilumina, revelando un mensaje oculto que te dirige hacia la siguiente etapa de tu aventura. La pasión por la mecánica y la producción te ha llevado un paso más cerca de descubrir el enigma final. Prepárate para lo que viene, ya que el próximo capítulo te llevará a nuevos horizontes.")
    time.sleep(3)
    print("El engranaje del reloj mecánico gira y se abre un pasaje secreto en la facultad. A medida que te adentras en el pasaje, la luz revela el camino hacia la siguiente facultad, señalando el avance en tu búsqueda.")
    time.sleep(3)
    print("Continúa tu viaje, explorador. El conocimiento te espera.")
    time.sleep(2)
    print(f"Felicidades {nombre_psj}! Has ganado el juego.")
    
    print(f"Tu puntaje final es: {puntaje_total}")
    
    # Llamar a la función main en fict con los nuevos valores
    fict.main(puntaje_total)


def main_fimcp(nombre_psj, puntaje_global):
    # Llamar a la función de juego y pasar los parámetros necesarios
    return jugar_ahorcado(nombre_psj, puntaje_global)
