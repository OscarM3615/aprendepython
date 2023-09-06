from .config import config
from .content import lessons
from .intro import introduction
from .menu import Menu
from .utils import console


def comenzar():
    console.print('¡Bienvenido a [bold green]aprendepython[/]!\n')

    if not config['intro_completed']:
        try:
            introduction()
        except (KeyboardInterrupt, EOFError):
            console.print(
                '[yellow]Saliendo de [bold green]aprendepython[/]...[/]')
            exit()

    menu = Menu(lessons)
    menu.show()


config.load()

console.print(
    '¡Hola! Escribe aprendepython.comenzar() cuando desees comenzar.')
