import random
import fiec
import sympy as sp
import time

def generar_pregunta():
   

    x = sp.symbols('x')
    operaciones = ['integral', 'derivada', 'limite']
    operacion = random.choice(operaciones)
    
    # Definir una función aleatoria
    func = x**2 - 3*x + sp.sin(x) + sp.cos(x)
    
    if operacion == 'integral':
        # Calcular la integral
        resultado = sp.integrate(func, x)
        pregunta = f"¿Cuál es la integral de {func} con respecto a x?"
    elif operacion == 'derivada':
        # Calcular la derivada
        resultado = sp.diff(func, x)
        pregunta = f"¿Cuál es la derivada de {func} con respecto a x?"
    elif operacion == 'limite':
        # Calcular el límite
        resultado = sp.limit(func, x, 0)  # Puedes cambiar el valor del límite si lo prefieres
        pregunta = f"¿Cuál es el límite de {func} cuando x tiende a 0?"
    
    return pregunta, resultado

def juego_calculo(puntaje_total):
    puntaje = 0
    respuestas_correctas = 0
    
    print("Capítulo 5: FCNM - El Desafío Matemático\n")
    time.sleep(3)
    print("Tras superar el laberinto en FICT, llegas a la Facultad de Ciencias y Matemáticas (FCNM). Este lugar está lleno de gráficos, ecuaciones y simulaciones matemáticas, representando el corazón del análisis matemático en la universidad. Aquí, te enfrentarás a un desafío que pondrá a prueba tus habilidades en cálculo.")
    time.sleep(3)
    print("Al ingresar a FCNM, te rodea un ambiente de fórmulas y gráficos en 3D. Una pantalla grande muestra una serie de ejercicios matemáticos, cada uno relacionado con conceptos clave del cálculo: límites, derivadas e integrales. Un holograma de un matemático te da la bienvenida y te explica el desafío.")
    print("\n")
    time.sleep(2)
    print("Bienvenido a la Facultad de Ciencias y Matemáticas. Para avanzar, deberás demostrar tu competencia en cálculo resolviendo una serie de ejercicios. Cada ejercicio se centra en uno de los conceptos fundamentales del cálculo: límites, derivadas e integrales. Completa los ejercicios correctamente para desbloquear el siguiente paso en tu búsqueda.\n")
    
    
    for _ in range(3):  # Número de preguntas
        pregunta, respuesta = generar_pregunta()
        print("\n" + pregunta)
        
        respuesta_usuario = input("Tu respuesta: ").strip()
        try:
            respuesta_usuario_simb = sp.sympify(respuesta_usuario)
        except sp.SympifyError:
            respuesta_usuario_simb = None
        
        if respuesta_usuario_simb == respuesta:
            print("¡Correcto!")
            respuestas_correctas += 1
        else:
            print(f"Incorrecto. La respuesta correcta era {respuesta}.")
    
    # Asignar puntos basado en el número de respuestas correctas
    if respuestas_correctas == 3:
        puntaje = 30
    elif respuestas_correctas == 2:
        puntaje = 20
    elif respuestas_correctas == 1:
        puntaje = 10
    else:
        puntaje = 0
    
    puntaje_total += puntaje
    
    print(f"\nTu puntaje final en este juego es: {puntaje}/30")
    print(f"Tu puntaje total acumulado es: {puntaje_total}")
    
    print("¡Excelente trabajo! Has demostrado tu dominio de los conceptos fundamentales del cálculo. Al resolver estos ejercicios, has desbloqueado un fragmento crucial del enigma que buscas. La claridad matemática te ha llevado un paso más cerca de desvelar el misterio final.")
    time.sleep(3)
    print("Un panel en la pantalla muestra una clave secreta que te dirige a la siguiente facultad. A medida que avanzas hacia la salida, el holograma agrega:")
    time.sleep(3)
    print("El camino hacia el conocimiento está lleno de desafíos matemáticos y lógicos. Has hecho un gran progreso. Prepárate para enfrentar lo que viene en tu próxima etapa.")
    time.sleep(3)
    print("\n")

    print("Con el desafío matemático superado, te preparas para tu siguiente destino, listo para enfrentar nuevas pruebas en tu viaje.")
    
    if respuestas_correctas == 3:
        print("¡Excelente trabajo! ¡Eres un maestro del cálculo!")
    elif respuestas_correctas == 2:
        print("¡Buen trabajo! Solo un par de errores.")
    elif respuestas_correctas == 1:
        print("Has hecho un intento decente. ¡Sigue practicando!")
    else:
        print("No te desanimes. Inténtalo de nuevo para mejorar.")
    
    
    fiec.juego()
    

if __name__ == "__main__":
    puntaje_total = 0  # Este valor debe ser actualizado con el puntaje real antes de llamar a juego_calculo
    juego_calculo(puntaje_total)
