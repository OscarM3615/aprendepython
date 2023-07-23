from .config import config
from .utils import console, selection


def introduction():
    console.print(
        'Antes de comenzar con las lecciones, es necesario cubrir algunos '
        'aspectos sobre cómo utilizar la librería. Primero, necesitas saber '
        'que cuando aparezca "..." significa que debes presionar Enter al '
        'terminar de leer para continuar con la lección.\n'
    )
    console.input(
        '... <- Esta es la señal para que pulses Enter para continuar.\n\n'
    )
    console.print(
        'Además, cuando la consola diga "Respuesta:", aparezca el prompt de '
        'Python (>>>) o se te pida seleccionar una opción de una lista, '
        'significa que necesitas ingresar tu respuesta y presionar Enter.\n'
    )
    selection(['Continuar', 'Seguir', 'Entendido'])
    console.print(
        'Si en algún momento deseas salir del curso puedes pulsar Ctrl+C '
        'durante una lectura o escribir exit() si te encuentras en el prompt '
        'de Python (>>>), puedes elegir si guardar o no el progreso actual.\n'
    )
    console.print('¡Comencemos con las lecciones!\n')
    console.input('...\n\n')

    config['intro_completed'] = True
    config.save()
