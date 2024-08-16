import climage
import sys
import fadcom
from climage import color_to_flags, color_types, convert
import time

# Inicializar el puntaje global
puntaje = 0

def bienvenida():
    print("¡Bienvenido al 'Rastro de los Sabios'!")
    print("\n")

    continuar_juego = ""
    while continuar_juego.lower() not in ["si", "no"]:
        continuar_juego = input("¿Quieres continuar la aventura? (si/no)").lower()
        if continuar_juego not in ["si", "no"]:
            print("¡Inténtalo de nuevo!")

    if continuar_juego.lower() == "no":
        sys.exit()
    
    sexo = ""
    while sexo.lower() not in ["hombre", "mujer"]:
        sexo = input("Ingrese su género: ")
        if sexo.lower() not in ["hombre", "mujer"]:
            print("Opción no válida. ¡Inténtalo de nuevo!")

    nombre_usuario = ""
    while not nombre_usuario.isalpha() or len(nombre_usuario) > 11:
        nombre_usuario = input("Ingrese su nombre de usuario: ").capitalize()
        
        if not nombre_usuario.isalpha():
            print("El nombre de usuario debe contener solo letras. ¡Inténtalo de nuevo!")
        elif len(nombre_usuario) > 11:
            print("El nombre de usuario debe tener como máximo 11 letras. ¡Inténtalo de nuevo!")
        print("Estamos creando su personaje... ")
    time.sleep(5)
    if sexo.lower() == "hombre":
        nombre_psj = f"{nombre_usuario} Jotaro"
        print(convert('img/hombre_psj.png', is_unicode=True, **color_to_flags(color_types.truecolor)))
    else:
        nombre_psj = f"{nombre_usuario} Ayaka"
        print(convert('img/mujer_psj.png', is_unicode=True, **color_to_flags(color_types.truecolor)))
    print("Eres un estudiante apasionado y curioso que un día despierta con una gran motivación para descubrir el verdadero propósito detrás de tu vida académica en la prestigiosa Escuela Politécnica del Ecuador (ESPOL). En tu habitación, encuentras un viejo libro cubierto de polvo con el título El Rastro de los Sabios. El libro habla de una antigua leyenda sobre un conocimiento perdido escondido en los rincones más profundos de ESPOL. Al leer el libro, sientes una chispa de emoción y te preguntas si estás listo para la aventura que se avecina. Después de una breve reflexión, decides que es el momento de embarcarte en esta misión.")
    print(convert('img/libro.png', is_unicode=True, **color_to_flags(color_types.truecolor)))
    time.sleep(3)
    print("\n")

    print("Antes de comenzar tu aventura, te tomas un momento para prepararte. Organizas tus notas, revisas el mapa antiguo que encontraste y te aseguras de tener todo lo necesario para tu viaje. Con una mezcla de nerviosismo y emoción, te diriges a la puerta de tu habitación y te dices a ti mismo: Estoy listo para empezar. Con ese pensamiento en mente, te adentras en el campus, sabiendo que cada facultad te llevará más cerca de desentrañar el enigma que has decidido resolver.")

    return nombre_psj

def main():
    nombre_psj = bienvenida()
    
    # Llamada a fadcom con solo nombre_psj
    nombre_psj = fadcom.main_fadcom(nombre_psj)

if __name__ == "__main__":
    main()
