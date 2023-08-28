import re

from ..models.exercise import OnelinerExercise
from ..models.lesson import Lesson
from .lesson_04_arithmetic_ops import lesson_04_arithmetic_ops


exercises_env = {'x': 4, 'y': 5}


class CompareX4(OnelinerExercise):
    instructions = ('A continuación se han declarado las variables "x = 4" y '
                    '"y = 5". Comprueba que x vale 4 utilizando el operador de '
                    'igualdad:')
    hints = [
        'Recuerda que para comparar se usan dos iguales (==) en lugar de uno.',
    ]
    env = exercises_env

    def test(self) -> bool:
        return bool(re.match(r'^x *?\=\= *?4', self.source))


class CompareY5(OnelinerExercise):
    instructions = 'Ahora compara si x tiene el mismo valor que y:'
    hints = [
        'Recuerda que para comparar se usan dos iguales (==) en lugar de uno.',
    ]
    env = exercises_env

    def test(self) -> bool:
        return bool(re.match(r'^x *?\=\= *?y', self.source))


class NotEqualOp(OnelinerExercise):
    instructions = ('Utiliza el operador de desigualdad entre las variables x '
                    'y y para observar el resultado:')
    env = exercises_env

    def test(self) -> bool:
        return bool(re.match(r'^x *?\!\= *?y', self.source))


class GreaterThan(OnelinerExercise):
    instructions = 'Utiliza el operador > para comprobar si x es mayor que y:'
    env = exercises_env

    def test(self) -> bool:
        return bool(re.match(r'^x *?\> *?y', self.source))


class LessThan(OnelinerExercise):
    instructions = 'Ahora comprueba si el valor de y es más pequeño que 10:'
    env = exercises_env

    def test(self) -> bool:
        return bool(re.match(r'^y *?\< *?10', self.source))


class LessOrEqualThan(OnelinerExercise):
    instructions = ('También existe el operador <=, que comprueba si un número '
                    'es menor o igual a otro. Intenta comparar las variables x '
                    'y y utilizando este operador, de modo que el resultado '
                    'True:')
    hints = [
        'Recuerda colocar el valor más pequeño del lado izquierdo.',
    ]
    env = exercises_env

    def test(self) -> bool:
        return bool(re.match(r'^x *?\<\= *?y', self.source))


lesson_05_relational_ops = Lesson(
    'operadores-relacionales',
    'Operadores relacionales',
    [
        'Otro tipo de operadores que de puede utilizar en Python son los '
        'relacionales. Estos sirven para realizar comparaciones entre dos '
        'valores y son útiles cuando se quiere determinar si se cumnple una '
        'condición en particular.',

        'Para comprobar si dos variables contienen el mismo valor se utiliza '
        'el operador de igualdad "==" entre ambos valores, por ejemplo: '
        'a == 3.',

        CompareX4(),

        CompareY5(),

        'Para comparar cuando dos valores son distintos, en lugar de utilizar '
        'el operador de igualdad se usa el operador de desigualdad que se '
        'escribe "!=".',

        NotEqualOp(),

        'Como puedes observar, este operador devuelve True porque los valores '
        'de x y de y son diferentes.',

        'También existen ocasiones en las que es necesario comprobar cuál '
        'valor es más grande o más pequeño que otro. Para estos casos existen '
        'los operadores < y >.',

        GreaterThan(),

        LessThan(),

        'El siguiente operador es el mayor o igual (>=), que devuelve True '
        'incluso cuando ambos valores son idénticos. Para ver su diferencia, '
        'observa el siguiente código:\n\n'
        '[default]>>> 5 > 5\n'
        'False\n'
        '>>> 5 >= 5\n'
        'True[/]',

        LessOrEqualThan(),
    ],
    lesson_04_arithmetic_ops
)
