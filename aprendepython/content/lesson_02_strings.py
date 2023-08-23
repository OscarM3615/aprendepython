from ..models.lesson import Lesson
from .lesson_01_numerics import lesson_01_numerics

lesson_02_strings = Lesson(
    'cadenas-de-texto',
    'Cadenas de texto',
    [
        'Las cadenas de texto se declaran utilizando comillas simples o '
        'dobles, su única diferencia es que las comillas dobles facilitan la '
        'aparición de apóstrofes en el valor de la variable:\n\n'
        '[default]>>> cadena = \'este es un ejemplo\'\n'
        '>>> cadena = "este es un \'ejemplo\'"[/]',

        'Otra notación para declarar variables es la palabra clave str, que '
        'tiene como principal utilidad convertir variables de otros tipos de '
        'dato en cadenas de texto. En el siguiente ejemplo se utiliza un '
        'número entero:\n\n'
        '[default]>>> num = str(3)\n'
        '>>> num\n'
        '\'3\'[/]',

        'Como se puede observar, el valor de num se muestra entre comillas, '
        'lo que indica que se ha convertido en una cadena de texto.'
    ],
    lesson_01_numerics
)
