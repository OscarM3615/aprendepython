import re

from ..models.exercise import OnelinerExercise
from ..models.lesson import Lesson
from .lesson_00_intro import lesson_00_intro


class DeclareIntVariable(OnelinerExercise):
    instructions = ('A modo de práctica, declara una variable llamada x con el '
                    'valor de 10:')
    hints = [
        'Recuerda asignar correctamente el nombre de la variable.',
        'Revisa que el valor sea 10',
    ]

    def test(self) -> bool:
        return bool(re.match(r'^x *?= *?10', self.source))


class DeclareFloatVariable(OnelinerExercise):
    instructions = ('Para practicar el uso de los números de punto flotante, '
                    'declara una variable llamada "y" con el valor de 2.5:')
    hints = [
        'Recuerda utilizar el símbolo de punto.',
        'Recuerda asignar el nombre "y" a la variable.',
    ]

    def test(self) -> bool:
        return bool(re.match('^y *?= *?2.5', self.source))


lesson_01_numerics = Lesson(
    'tipos-de-datos-numericos',
    'Tipos de datos numéricos',
    [
        'Python es un lenguaje de tipado dinámico, no es necesario declarar '
        'las variables antes de utilizarlas ni especificar su tipo de dato. El '
        'primer tipo de dato a presentar serán los numéricos.',

        'El lenguaje soporta principalmente dos tipos de números: enteros '
        '(int) y de punto flotante (float).',

        'Los números enteros pueden ser positivos o negativos. Para declarar '
        'un número de tipo entero se utiliza la siguiente sintaxis:\n\n'
        '[default]>>> positivo = 5\n'
        '>>> negativo = -5\n\n[/]'
        'El ejemplo anterior declara dos variables enteras.',

        DeclareIntVariable(),

        'Para declarar variables de punto flotante se requiere incluir un '
        'en el valor, seguido de la parte decimal. El siguiente ejemplo lo '
        'demuestra:\n\n'
        '[default]>>> fnum = 6.5[/]',

        'Al igual que con los números enteros, las variables de punto flotante '
        'pueden ser positivas o negativas:\n\n'
        '[default]>>> neg_fnum = -3.2[/]',

        DeclareFloatVariable(),

        'También es posible declarar números utilizando las notaciones int y '
        'float, como se muestra a continuación:\n\n'
        '[default]>>> entero = int(5)\n'
        '>>> flotante = float(4.0)[/]',

        'La principal funcionalidad de esta notación es la conversión de la '
        'variablede un tipo de dato a otro, como convertir un entero a punto '
        'flotante y viceversa. Observa qué sucede al convertir un flotante a '
        'entero con la notación anterior:\n\n'
        '[default]>>> int(4.4)\n'
        '4[/]',

        'Como se puede observar, se pierde la parte decimal y se conserva '
        'solo la parte entera. Ahora observa qué sucede al convertir un entero '
        'a punto flotante:\n\n'
        '[default]>>> float(6)\n'
        '6.0[/]\n\n'
        'En este caso, solo se agrega la parte decimal, la cual equivale a 0.'
    ],
    lesson_00_intro
)
