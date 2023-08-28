import re

from ..models.exercise import OnelinerExercise
from ..models.lesson import Lesson
from .lesson_05_relational_ops import lesson_05_relational_ops


class NotOperator(OnelinerExercise):
    instructions = ('Como ejercicio, comprueba que los números 4 y 5 son '
                    'diferentes sin utilizar el operador !=:')
    hints = [
        'Recuerda hacer uso del operador "not".',
        'En lugar de utilizar != puedes negar el resultado de usar ==.',
    ]

    def test(self) -> bool:
        return bool(re.match(r'^not *?4 *?\=\= *?5', self.source))


class OrOperator(OnelinerExercise):
    instructions = ('Se han definido las variables a = True, b = False y c = '
                    'False. Observa qué sucede si evalúas "a or b":')
    env = {'a': True, 'b': False, 'c': True}

    def test(self) -> bool:
        return bool(re.match(r'^a *?or *?b', self.source))


class OrOperator2(OnelinerExercise):
    instructions = 'Por otro lado, observa qué sucede al evaluar "b or c":'
    env = {'a': True, 'b': False, 'c': True}

    def test(self) -> bool:
        return bool(re.match(r'^b *?or *?c', self.source))


lesson_06_logical_ops = Lesson(
    'operadores-logicos',
    'Operadores lógicos',
    [
        'Generalmente, es necesario comparar más de una condición al mismo '
        'tiempo para construir una condición aún más grande.',

        'El primer caso es cuando se quiere obtener el resultado opuesto a una '
        'condición, para esto se utiliza el operador "not". Su funcionamiento '
        'es devolver False cuando la condición se evalúa como verdadera y '
        'devuelve True cuando la condición es falsa. Por ejemplo:\n\n'
        '[default]>>> not True\n'
        'False[/]',

        'Como se observa, la condición True al ser negada se convierte en '
        'False, lo mismo sucede en el caso inverso:\n\n'
        '[default]>>> not False\n'
        'True[/]',

        NotOperator(),

        'Un caso bastante común es querer verificar que se cumple cierto '
        'conjunto de condiciones. Al utilizar el operador "and" se comprueba '
        'que todas las condiciones sean verdaderas para que el resultado final '
        'sea True. Si una condición no se cumple automáticamente la expresión '
        'entera será False:\n\n'
        '[default]>>> \'ejemplo\' == \'ejemplo\' and 3 < 5\n'
        'True[/]',

        'En el caso anterior, la expresión completa es verdadera porque se '
        'cumplen las dos condiciones unidas por el operador "and". En cambio, '
        'si una de las condiciones no se cumple, el resultado es distinto:\n\n'
        '[default]>>> \'ejemplo\' == \'EJEMPLO\' and 3 < 5\n'
        'False[/]\n\n'
        'Esta vez el resultado es False porque la primera condición no se ha '
        'cumplido.',

        'Por otro lado, cuando solamente es necesario que se cumpla como '
        'mínimo una condición se utiliza el operador "or". Este hará que la '
        'expresión sea verdadera si al menos una de las condiciones se cumple '
        'y solo devolverá False si ninguna condición se cumple.',

        OrOperator(),

        'A pesar de que solo a es verdadera, la expresión entera es True.',

        OrOperator2(),

        'Como se puede notar, en este caso la expresión ha sido False, dado '
        'que ni b ni c son verdaderas.',

        'En caso de querer evaluar condiciones más complejas se puede hacer '
        'una combinación de estos operadores. Por ejemplo:\n\n'
        '[default]>>> a and (b or c)[/]\n\n'
        'Esta expresión requiere que a siempre sea verdadera y que al menos '
        'una de las letras b o c sea también verdadera para devolver True. Si '
        'una de las condiciones no se cumple, se devolverá False.',
    ],
    lesson_05_relational_ops
)
