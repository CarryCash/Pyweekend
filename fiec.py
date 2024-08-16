import random
import threading
import time
import climage
from climage import color_to_flags, color_types, convert
from colorama import Fore, Back, Style, init
from rich.console import Console
from rich.text import Text
from termcolor import colored

# Inicializar colorama
init()

# Crear una instancia de Rich Console
console = Console()

# Definir constantes
HACKER_CONSOLE_TITLE = "== HACKER CONSOLE =="
TERMINAL_MESSAGE = "Welcome to the Terminal of Doom!"
SECURE_ENVIRONMENT_MESSAGE = "You are in a secure environment."

# Estilos de texto y colores con colorama
def estilo_hacker_colorama():
    print(Fore.GREEN + Back.BLACK + Style.BRIGHT + HACKER_CONSOLE_TITLE + Style.RESET_ALL)
    print(Fore.GREEN + TERMINAL_MESSAGE + Style.RESET_ALL)
    print(Fore.GREEN + SECURE_ENVIRONMENT_MESSAGE + Style.RESET_ALL)
    

# Estilos de texto y colores con rich
def estilo_hacker_rich():
    console.print(Text(HACKER_CONSOLE_TITLE, style="bold green on black"))
    console.print(TERMINAL_MESSAGE, style="bold green")
    console.print(SECURE_ENVIRONMENT_MESSAGE, style="bold green")

# Estilos de texto y colores con termcolor
def estilo_hacker_termcolor():
    print(colored(HACKER_CONSOLE_TITLE, 'green', 'on_black', attrs=['bold']))
    print(colored(TERMINAL_MESSAGE, 'green'))
    print(colored(SECURE_ENVIRONMENT_MESSAGE, 'green'))

# Llamar a las funciones para mostrar los estilos
if __name__ == "__main__":
    estilo_hacker_colorama()

# Funciones para la Parte 1: Hackeo

def mostrar_menu():
    print(Fore.GREEN + "\n--- Operación Hacker - Parte 1 ---")
    print("1. Problema de Código en Python")
    print("2. Desafío de Seguridad SQL")
    print("3. Desafío de Seguridad CSRF")
    print("4. Salir")
    return input("Selecciona una opción: ")

def problema_codigo():
    print(Fore.GREEN + "\n--- Problema de Código en Python ---")
    print("El sistema de seguridad de la base de datos tiene un problema en su función de autenticación. Corrige la línea de código para que funcione correctamente.")
    print("\nCódigo Original:")
    print("""
def autenticar(usuario, password):
    if usuario = 'admin' and password == '1234':  # <-- Error aquí
        return True
    else:
        return False

resultado = autenticar('admin', '1234')
if resultado:
    print("Autenticación exitosa")
else:
    print("Autenticación fallida")
    """)
    print("Ingresa la línea corregida de código.")

    while True:
        linea_corregida = input("Línea corregida: ").strip()
        if linea_corregida == "if usuario == 'admin' and password == '1234':":
            print("\n¡Correcto! Has arreglado el problema de autenticación.")
            print("""
Autenticación exitosa
""")
            return True
        else:
            print("  File \"<stdin>\", line {}".format(2))
            print(f"    {linea_corregida}")
            print("       ^")
            print("SyntaxError: invalid syntax")

def mostrar_tabla_sql():
    print(Fore.GREEN + "\n--- Tabla 'codigos_seguridad' ---")
    print("id | codigo       | descripción               | estado")
    print("---|--------------|---------------------------|---------")
    print("1  | A1B2C3D4     | Acceso a la sala de datos  | Usado")
    print("2  | E5F6G7H8     | Acceso al servidor principal | Disponible")
    print("3  | I9J0K1L2     | Acceso a la sala de servidores | Usado")
    print("4  | M3N4O5P6     | Acceso a la sala de archivos  | Disponible")

def verificar_sql(consulta):
    consulta_correcta = "select descripcion from codigos_seguridad where id = 2;"
    
    if consulta.lower() == consulta_correcta:
        return "¡Correcto! Has explotado la vulnerabilidad SQL."
    
    if "select" not in consulta.lower():
        return "Error: Sintaxis incorrecta. Falta 'SELECT'."
    if "descripcion" not in consulta.lower():
        return "Error: La columna 'descripcion' no existe."
    if "from" not in consulta.lower():
        return "Error: Sintaxis incorrecta. Falta 'FROM'."
    if "codigos_seguridad" not in consulta.lower():
        return "Error: La tabla 'codigos_seguridad' no existe."
    if "where" not in consulta.lower():
        return "Error: Sintaxis incorrecta. Falta 'WHERE'."
    if "id = 2" not in consulta.lower():
        return "Error: Condición 'WHERE' incorrecta."
    
    return "Error: Consulta incorrecta. Intenta de nuevo."

def desafio_sql():
    print("\n--- Desafío de Seguridad SQL ---")
    print("La aplicación tiene una vulnerabilidad SQL. ¿Puedes explotarla?")
    mostrar_tabla_sql()
    print("Ingresa una consulta SQL para obtener la descripción del código con id = 2.")
    
    intentos_maximos = 3  # Número máximo de intentos permitidos
    for intento in range(intentos_maximos):
        consulta = input("Consulta SQL: ").strip()
        mensaje = verificar_sql(consulta)
        print(mensaje)
        if mensaje.startswith("¡Correcto!"):
            return True
        elif intento < intentos_maximos - 1:
            print(f"Te quedan {intentos_maximos - intento - 1} intentos.")
    print("Has agotado todos los intentos. Fin del desafío.")
    return False


def mostrar_tabla_usuarios():
    print(Fore.GREEN + "\n--- Tabla 'usuarios' ---")
    print("id | usuario   | email               | token_csrf")
    print("---|-----------|---------------------|------------------")
    print("1  | admin     | admin@example.com    | csrf-token-1234")
    print("2  | usuario1  | user1@example.com    | csrf-token-5678")
    print("3  | usuario2  | user2@example.com    | csrf-token-9101")
    print("4  | usuario3  | user3@example.com    | csrf-token-1121")

def desafio_csrf():
    print(Fore.GREEN + "\n--- Desafío de Seguridad CSRF ---")
    print("La aplicación tiene una vulnerabilidad CSRF. ¿Puedes explotarla?")
    print("El formulario de cambio de contraseña no valida el origen de la solicitud.")
    print("Para cambiar la contraseña del usuario 'admin', necesitas obtener y utilizar el token CSRF correcto.")
    mostrar_tabla_usuarios()
    print("Ingresa el token CSRF correcto para cambiar la contraseña del usuario 'admin'.")
    
    token = input(Fore.GREEN + "Token CSRF: ").strip()
    if token == "csrf-token-1234":
        print(Fore.GREEN + "¡Correcto! Has explotado la vulnerabilidad CSRF.")
        return True
    else:
        print(Fore.RED + "Token incorrecto. Intenta de nuevo.")
        return False
    
    
def parte_1():
    puntuacion = 0
    print(Fore.GREEN + "Comenzando la Parte 1: Hackeo")
    
    if problema_codigo():
        puntuacion += 10
        print(f"\nPuntuación actual: {puntuacion}")
        
        if desafio_sql():
            puntuacion += 15
            print(f"\nPuntuación actual: {puntuacion}")
            
            if desafio_csrf():
                puntuacion += 20
                print(f"\n¡Parte 1 completada! Tu puntuación final es: {puntuacion}")
                return puntuacion
            else:
                print("Fallaste en el Desafío de Seguridad CSRF. Fin de la Parte 1.")
                return puntuacion
        else:
            print("Fallaste en el Desafío de Seguridad SQL. Fin de la Parte 1.")
            return puntuacion
    else:
        print("Fallaste en el Problema de Código en Python. Fin de la Parte 1.")
        return puntuacion


class Timer(threading.Thread):
    def __init__(self, timeout, stop_event):
        super().__init__()
        self.timeout = timeout
        self.stop_event = stop_event

    def run(self):
        start_time = time.time()
        while time.time() - start_time < self.timeout:
            if self.stop_event.is_set():
                return
            time.sleep(1)
        self.stop_event.set()

def generar_preguntas_respuestas():
    preguntas = [
        {"pregunta": "¿Cuál es el primer nombre del famoso físico que desarrolló la teoría de la relatividad?", "respuesta": "einstein"},
        {"pregunta": "¿En qué continente se encuentra el desierto del Sahara?", "respuesta": "africa"},
        {"pregunta": "¿Cuál es el nombre del libro escrito por George Orwell que se desarrolla en una sociedad distópica?", "respuesta": "1984"},
        {"pregunta": "¿Qué elemento químico tiene el símbolo 'O' en la tabla periódica?", "respuesta": "oxigeno"},
        {"pregunta": "¿Cuál es la capital de Francia?", "respuesta": "paris"},
        {"pregunta": "¿Qué instrumento musical tiene 88 teclas y se toca con las manos?", "respuesta": "piano"}
    ]
    random.shuffle(preguntas)
    return preguntas

def descifrar_contrasena(respuestas):
    clave = "ESPOL1"  # Contraseña inicial
    for respuesta in respuestas:
        if respuesta[0] in clave:
            clave = clave.replace(respuesta[0], "", 1)
    return clave

def mostrar_proceso():
    print("\nDescribiendo la contraseña final...")
    time.sleep(1)  # Pausa de 1 segundo

    print("Iniciando proceso de desciframiento...")
    time.sleep(1)

    print("root@bt:~# cracking_password_tool --start")
    time.sleep(2)  # Pausa de 2 segundos

    print("[*] Analizando hash...")
    time.sleep(2)

    print("[*] Escaneando secuencias...")
    time.sleep(2)

    print("root@bt:~# pwdump /etc/passwd")
    time.sleep(1)

    print("root:x:0:0:root:/root:/bin/bash")
    time.sleep(1)

    print("daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin")
    time.sleep(1)

    print("...")
    time.sleep(1)

    print("[*] Verificando integridad de datos...")
    time.sleep(2)

    print("root@bt:~# hashcat -m 0 -a 0 /path/to/hashfile /path/to/wordlist")
    time.sleep(2)

    print("root@bt:~# hashcat --status")
    time.sleep(1)

    print("[*] Desciframiento en progreso...")
    time.sleep(2)

    print("root@bt:~# crackstatus")
    time.sleep(1)

    print("Status: Running")
    time.sleep(1)

    print("...")
    time.sleep(2)

    print("[*] Generando resultado final...")
    time.sleep(2)

    print("root@bt:~# crackresult")
    time.sleep(1)

    print("Contraseña descifrada: ESPOL1")

def parte_2():
    print("\n--- Operación Hacker - Parte 2 ---")
    print("Responde correctamente las siguientes preguntas para obtener la contraseña de acceso. Tienes 1 minuto.")
    
    preguntas = generar_preguntas_respuestas()
    respuestas_usuario = []
    
    stop_event = threading.Event()
    timer = Timer(timeout=60, stop_event=stop_event)
    timer.start()
    
    for i, pregunta in enumerate(preguntas):
        if stop_event.is_set():
            print("¡Tiempo agotado! Has perdido la oportunidad de descifrar la contraseña.")
            return
        
        respuesta = input(f"Pregunta {i+1}: {pregunta['pregunta']} ").strip().lower()
        if respuesta == pregunta['respuesta']:
            print("¡Correcto!")
            respuestas_usuario.append(respuesta)
        else:
            print("Respuesta incorrecta.")
    
    stop_event.set()
    
    # Mensajes simulando el desciframiento de contraseñas
    mostrar_proceso()

    
    clave_descifrada = "ESPOL1"
    print(f"La contraseña descifrada es: {clave_descifrada}")
    
    time.sleep(3)
    print(convert('img/img_3.jpg', is_unicode=True, **color_to_flags(color_types.truecolor)))
    
    
    print("\n--- DIPLOMA DE LOGRO ---\n")
    print("¡Felicidades!")
    print("El verdadero propósito del conocimiento no es solo acumular información, sino aplicar lo aprendido para resolver problemas y mejorar el mundo.")
    print("Has demostrado que el conocimiento es una herramienta poderosa cuando se usa con sabiduría y creatividad.")
    print("\nTu habilidad para superar el desafío del ahorcado en la Facultad de Mecánica y Ciencias de la Producción (FIMCP) ha demostrado tu comprensión profunda de las carreras y conceptos técnicos.")
    print("\nCon este logro, has desbloqueado un nuevo camino en tu aventura. Sigue explorando y enfrentando nuevos desafíos. El conocimiento te llevará a grandes alturas.")
    print("\n¡Sigue adelante, explorador!")
    


def juego():
    print(Fore.GREEN + "Bienvenido a Operación Hacker")
    
    puntuacion = parte_1()
    if puntuacion > 0:
        parte_2()
    else:
        print("No completaste la Parte 1, así que no puedes avanzar a la Parte 2.")
    


if __name__ == "__main__":
    
    juego()
