"""
Module providing introductory functionality for the course.

This module includes the 'introduction()' function, which provides a tutorial
on how to navigate through the course.
"""

from .config import config
from .utils import console, selection


def introduction():
    """
    Displays an introduction to the lessons and guides the user through the
    setup before starting. It marks the introduction as completed in the
    configuration.
    """

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
        'En algunos ejercicios será necesario que escribas comprobar() para '
        'poder evaluar la respuesta, por lo general será en ejercicios que '
        'requieran que escribas varias líneas de código. Cuando los ejercicios '
        'se resuelvan en una sola línea este se evaluará de inmediato.\n'
    )
    console.input('...\n\n')
    console.print(
        'Si en algún momento deseas salir del curso puedes pulsar Ctrl+C '
        'durante una lectura o escribir exit() si te encuentras en el prompt '
        'de Python (>>>), puedes elegir si guardar o no el progreso actual.\n'
    )
    console.print('¡Comencemos con las lecciones!\n')
    console.input('...\n\n')

    config['intro_completed'] = True
    config.save()
