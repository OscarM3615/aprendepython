from typing import Sequence
from rich.console import Console

console = Console(style='blue', width=80)


def selection(options: Sequence[str]) -> int:
    console.print(
        '[white]Selecciona el número de la opción y presiona Enter.[/]\n'
    )
    for i, opt in enumerate(options, start=1):
        console.print(f'[white]{i}. {opt}[/]')

    # Repeat the input until the answer is a number.
    while True:
        try:
            answer = int(console.input('\n[white]Selección: [/]'))
        except ValueError:
            console.print(
                '[red]La selección debe ser un número. Por favor intenta de '
                'nuevo.[/]'
            )
        else:
            break
    print()

    return answer
