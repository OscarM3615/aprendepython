"""
A module for user interaction and console utilities.

This module provides utility functions to print styled messages and handle
user interaction such as option selection and safely exit the program.
"""

from typing import Optional, Sequence

from rich.console import Console

from .config import config

console = Console(style='blue', width=80)


class CheckExercise(SystemExit):
    """
    Custom exception for controlling program flow during exercise checking.

    This exception is raised when the program flow needs to be interrupted to
    check the user's exercise solution. It inherits from the built-in SystemExit
    exception, which allows InteractiveConsole to be closed gracefully.
    """

    ...


class QuitLesson(SystemExit):
    """
    Custom exception for controlling program flow when quitting a lesson.

    This exception is raised when the user decides to quit the current lesson.
    It inherits from the built-in SystemExit exception, allowing the program to
    exit the lesson gracefully.
    """

    ...


def exercise_check():
    """
    This function raises a 'CheckExercise' exception, which is caught at an
    appropriate level in the program's control flow to initiate the exercise
    checking process.
    """

    raise CheckExercise


def exercise_exit():
    """
    This function raises a 'QuitLesson' exception, which is caught at an
    appropriate level in the program's control flow to handle the process of
    quitting the current lesson.
    """

    raise QuitLesson


def selection(options: Sequence[str], *, title: Optional[str] = None) -> int:
    """
    Generate a styled menu with the provided options and return the selected
    option as an int.

    Args:
        options (Sequence[str]): The options to include in the menu.
        title (Optional[str]): An optional, customised title.

    Returns:
        int: The index of the selected option (starting in 1).
    """

    if not title:
        title = 'Selecciona el número de la opción y presiona Enter.'
    console.print(f'[default]{title}[/]\n')

    for i, opt in enumerate(options, start=1):
        console.print(f'[default]{i}: {opt}[/]')

    # Repeat the input until the answer is a number.
    while True:
        try:
            answer = int(console.input('\n[default]Selección: [/]'))
            if answer not in range(len(options) + 1):
                raise IndexError()
        except (KeyboardInterrupt, EOFError):
            console.print('[yellow]Por favor elige una opción.[/]')
        except ValueError:
            console.print(
                '[red]La selección debe ser un número. Por favor intenta de '
                'nuevo.[/]'
            )
        except IndexError:
            console.print(
                '[red]La selección debe estar entre las opciones. Por favor '
                'intenta de nuevo.[/]'
            )
        else:
            break
    print()

    return answer


def safe_exit():
    """
    Ask the user to save progress into the config file, then exit the interpreter.
    """

    try:
        option = selection(
            ['Guardar y salir', 'Salir sin guardar'],
            title='¿Deseas guardar tu progreso antes de salir?'
        )
        if option == 1:
            config.save()
            console.print('[green]Cambios guardados.[/]')
    except (KeyboardInterrupt, EOFError):
        ...

    console.print('¡Hasta la próxima!\n')
    exit()


def confirm_quit_lesson() -> bool:
    """
    Ask the user to confirm quitting the current lesson.
    """

    try:
        option = selection(
            ['Terminar la lección', 'Continuar estudiando'],
            title='¿Deseas terminar la lección? El progreso no será guardado.'
        )
    except (KeyboardInterrupt, EOFError):
        option = 1

    return option == 1
