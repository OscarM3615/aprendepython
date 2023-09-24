import re

from ..models.exercise import OnelinerExercise
from ..models.lesson import Lesson


class UsePrintFunction(OnelinerExercise):
    instructions = ('Utiliza la instrucción print() para mostrar "Hola mundo" '
                    'en pantalla:')
    hints = [
        'Recuerda colocar el texto entre comillas',
        'Recuerda utilizar paréntesis en la instrucción',
        'Verifica que el texto sea "Hola mundo"',
    ]

    def test(self) -> bool:
        return bool(
            re.match(r'^print *?\( *?[\'\"]Hola mundo[\'\"] *?\)', self.source)
        )


lesson_00_intro = Lesson(
    'introduccion',
    'Introducción',
    [
        'Python es un lenguaje de programación que busca tener una sintaxis '
        'bastante sencilla. Actualmente existen dos versiones principales de '
        'Python: Python 2 y Python 3. Se prefiere el uso de la versión 3 por '
        'soportar características más modernas, por lo que este curso emplea '
        'la versión de Python 3.',

        'La instrucción más simple de Python es print, permite mostrar texto '
        'en pantalla incluyendo un salto de línea. Ejemplo:\n\n'
        '[default]>>> print(\'Este texto se mostrará en pantalla\')[/]',

        UsePrintFunction(),

        'Python usa indentación para agrupar bloques de código en '
        'lugar de emplear llaves como en otros lenguajes de programación. Esto '
        'significa que habrá código tabulado a la derecha como en el siguiente '
        'ejemplo:\n\n'
        '[default]>>> if 2 + 2 == 4:\n'
        '...     print(\'La suma es 4\')[/]\n\n'
        'El uso de indentación será visto en próximas lecciones.',
    ],
)
