import re

from ..models.exercise import OnelinerExercise
from ..models.lesson import Lesson
from .lesson_02_strings import lesson_02_strings


class DeclareBoolVariable(OnelinerExercise):
    instructions = ('A continuación declara una variable llamada "soy_mayor" '
                    'con una valor True o False, dependiendo de si eres mayor '
                    'de edad o no.')
    hints = [
        'Recuerda asignar el nombre correcto a la variable.',
        'Los valores lógicos solo pueden ser True o False.'
    ]

    def test(self) -> bool:
        return bool(re.match(r'^soy_mayor *?= *?(True|False)', self.source))


lesson_03_booleans = Lesson(
    'tipo-de-dato-logico',
    'Tipo de dato lógico',
    [
        'Además de variables numéricas y de texto, el lenguaje Python cuenta '
        'el tipo de variable lógico. Este tipo de variable acepta solamente '
        'dos valores: True y False.\n\n'
        'Este tipo de dato se puede utilizar cuando solamente se tienen '
        'opciones binarias, por ejemplo: encendido/apagado, '
        'activado/desactivado, permitido/prohibido, etc.',

        'En este ejemplo se muestra la declaración de variables lógicas:\n\n'
        '[default]>>> curso_de_python = True\n'
        '>>> python_es_dificil = False[/]',

        DeclareBoolVariable(),
    ],
    lesson_02_strings
)
