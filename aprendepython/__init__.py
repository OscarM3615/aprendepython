from .intro import introduction
from .config import config
from .menu import Menu
from .utils import console


def comenzar():
    console.print('¡Bienvenido a [bold green]aprendepython[/]!\n')

    if not config['intro_completed']:
        introduction()

    menu = Menu()
    menu.show()


config.load()

console.print(
    '¡Hola! Escribe aprendepython.comenzar() cuando desees comenzar.')
