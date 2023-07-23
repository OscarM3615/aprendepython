from typing import Optional, Sequence
from rich.console import Console

console = Console(style='blue', width=80)


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
    console.print(f'[white]{title}[/]\n')

    for i, opt in enumerate(options, start=1):
        console.print(f'[white]{i}: {opt}[/]')

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
