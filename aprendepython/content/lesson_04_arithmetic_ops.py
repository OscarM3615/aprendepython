import re

from ..models.exercise import OnelinerExercise
from ..models.lesson import Lesson
from .lesson_03_booleans import lesson_03_booleans


class SumTwoNumbers(OnelinerExercise):
    instructions = ('Escribe la suma de 5 + 7, pulsa Enter y observa el '
                    'resultado:')
    hints = [
        'Recuerda utilizar números enteros.',
        'Utiliza el operador de suma para obtener el resultado.',
    ]

    def test(self) -> bool:
        return bool(re.match(r'^5 *?\+ *?7', self.source))


class StoreSumInVariable(OnelinerExercise):
    instructions = ('Suma de nuevo a + b, pero asigna el resultado a una '
                    'variable llamada c con la sintaxis de asignación: '
                    'c = a + b')
    hints = [
        'Recuerda usar el símbolo = para almacenar en una variable.',
        'Verifica que la variable declarada se llame "c".',
        'Usa los nombres "a" y "b" para realizar la suma.',
    ]
    env = {'a': 5, 'b': 7}

    def test(self) -> bool:
        return bool(re.match(r'^c *?= *?a *?\+ *?b', self.source))


class ShowCValue(OnelinerExercise):
    instructions = ('Ahora muestra el valor de "c" escribiendo "c" y pulsando '
                    'Enter:')
    env = {'a': 5, 'b': 7, 'c': 12}

    def test(self) -> bool:
        return bool(re.match(r'^c$', self.source))


class MakeSubstraction(OnelinerExercise):
    instructions = ('A continuación resta b - a en la consola para ver el '
                    'resultado:')
    hints = ['Utiliza los nombres de las variables para hacer la resta.']
    env = {'a': 5, 'b': 7}

    def test(self) -> bool:
        return bool(re.match(r'^b *?\- *?a', self.source))


class StoreSubstraction(OnelinerExercise):
    instructions = ('Ahora asigna el resultado de la resta en la variable c, '
                    'tal como se hizo con la suma:')
    hints = [
        'Utiliza los nombres de las variables para hacer la resta.',
        'Verifica que la variable declarada se llame "c".',
    ]
    env = {'a': 5, 'b': 7, 'c': 2}

    def test(self) -> bool:
        return bool(re.match(r'^c *?= *?b *?\- *?a', self.source))


class ShowCValue2(ShowCValue):
    instructions = 'Muestra el valor de "c" escribiendo "c" y pulsando Enter:'
    env = {'a': 5, 'b': 7, 'c': 2}


class MakeMultiplication(OnelinerExercise):
    instructions = ('El siguiente operador es el de multiplicación, el cual '
                    'tiene el símbolo de *, prueba multiplicar los números 10 '
                    'y 6:')
    hints = ['Recuerda utilizar el símbolo * para multiplicar.']

    def test(self) -> bool:
        return bool(re.match(r'^10 *?\* *?6', self.source))


class MakeDivision(OnelinerExercise):
    instructions = ('La división se realiza con el operador /, prueba dividir '
                    '20 entre 3:')
    hints = ['Realiza la división con el símbolo /']

    def test(self) -> bool:
        return bool(re.match('^20 *?\/ *?3', self.source))


class MakeDivision2(OnelinerExercise):
    instructions = 'Ahora intenta dividir 20 entre 2.'

    def test(self) -> bool:
        return bool(re.match('^20 *?\/ *?2', self.source))


class MakeFloorDivision(OnelinerExercise):
    instructions = 'Intenta dividir 20 entre 2 de nuevo, pero utilizando //:'
    hints = [
        'Recuerda utilizar en esta ocasión el operador //.',
    ]

    def test(self) -> bool:
        return bool(re.match(r'^20 *?\/\/ *?2', self.source))


class MakeModulo(OnelinerExercise):
    instructions = ('Para obtener el sobrante de una división se utiliza el '
                    'operador de módulo, que emplea el símbolo %. Prueba '
                    'escribir 20 % 3 para ver el resultado.')

    def test(self) -> bool:
        return bool(re.match(r'^20 *?\% *?3', self.source))


class MakePower(OnelinerExercise):
    instructions = ('Para calcular potencias se emplea el operador ** (dos '
                    'astericos) en la forma a ** b. Intenta elevar 3 al '
                    'cuadrado:')
    hints = [
        'Recuerda que para elevar a una potencia se usa a ** b.',
    ]

    def test(self) -> bool:
        return bool(re.match(r'^3 *?\*\* *?2', self.source))


class UseCompoundExpression(OnelinerExercise):
    instructions = 'Prueba a escribir la operación 3 + 4 * 5:'

    def test(self) -> bool:
        return bool(re.match(r'^3 *?\+ *?4 *?\* *?5', self.source))


class UseParentheses(OnelinerExercise):
    instructions = 'Utiliza paréntesis para encerrar la suma en 3 + 4 * 5:'
    hints = [
        'Verifica que se encuentran los paréntesis de apertura y de cierre.',
        'Revisa que solamente "3 * 4" esté entre paréntesis.',
    ]

    def test(self) -> bool:
        return bool(re.match(r'^\(3 *?\+ *?4\) *?\* *?5', self.source))


lesson_04_arithmetic_ops = Lesson(
    'operadores-aritmeticos',
    'Operadores aritméticos',
    [
        'Cuando se crea una programa en Python, es bastante común requerir '
        'hacer operaciones con las variables declaradas. Las operaciones '
        'aritméticas son posibles en Python gracias a los operadores '
        'aritméticos.',

        'El operador de suma, como su nombre lo indica, permite obtener la '
        'suma de dos números, tanto enteros como de punto flotante.',

        SumTwoNumbers(),

        'También es posible hacer sumas utilizando nombres de variables, a '
        'continuación se han declarado las variables "a" y "b", observa lo '
        'que sucede al sumar ambas variables escribiendo a + b:\n\n'
        '[default]>>> a = 5\n'
        '>>> b = 7\n'
        '>>> a + b\n'
        '12[/]',

        'Hasta ahora el resultado se ha mostrado en pantalla, pero no se ha '
        'conservado en memoria. En Python, es posible asignar el resultado de '
        'la suma (y de cualquier operación) dentro de otra variable.',

        StoreSumInVariable(),

        ShowCValue(),

        'Como se observa, el valor de 12 ha quedado guardado en la variable c '
        'y ahora puede ser utilizada para más operaciones.\n\n'
        'El operador de resta permite obtener la diferencia de dos números '
        'mediante la sintaxis b - a.',

        MakeSubstraction(),

        StoreSubstraction(),

        ShowCValue2(),

        'Ahora el valor de c es de 2, por lo que se puede confirmar que se ha '
        'asignado el resultado de la resta. Además, habrás notado que se ha '
        'reemplazado el valor que tenía c anteriormente (12), esto es porque '
        'las variables pueden cambiar de valor. En el caso de Python, cuando '
        'se realiza una asignación a una variable por primera vez la variable '
        'se crea, y si ya existe solamente se actualiza su valor, sin importar '
        'si es el mismo tipo de dato o es distinto.',

        MakeMultiplication(),

        MakeDivision(),

        MakeDivision2(),

        'Como puedes notar, a pesar de ser una división sin residuo, el '
        'resultado sigue teniendo una parte decimal, esto sucede porque el '
        'operador de división devuelve siempre una variable de punto flotante. '
        'Para obtener el resultado como un número entero se deve utilizar el '
        'operador //.',

        MakeFloorDivision(),

        'Ahora se ha devuelto el resultado como un entero, sin embargo, en el '
        'caso de realizar esta operación en una división con residuo, el '
        'resultado conservará solo la parte entera y el residuo de la división '
        'se perderá.',

        MakeModulo(),

        MakePower(),

        'Por último, cabe recalcar que el operador de suma tiene otra '
        'funcionalidad. Se puede emplear con cadenas de texto para unir los '
        'valores de dos variables de texto, a esto se le llama concatenación. '
        'En el siguiente ejemplo se muestra cómo se utiliza:\n\n'
        '[default]>>> \'un nuevo \' + \'ejemplo\'[/]',

        'También es importante notar que el primer valor termina con un '
        'espacio. Esto es porque ambos textos son puestos uno justo después '
        'del otro. Si se quiere separar los textos con un espacio se debe '
        'considerar en los valores.',

        'No es posible realizar una concatenación con variables de distintos '
        'tipos de dato, sin embargo, se puede convertir las variables a texto '
        'con la instrucción str, como en el siguiente ejemplo:\n\n'
        '[default]>>> \'Valor: \' + str(5)[/]',

        'Por último, es necesario mencionar que, al igual que en otros '
        'lenguajes, se pueden combinar los operadores en una sola expresión.',

        UseCompoundExpression(),

        'Habrás notado que el resultado es 23 y no 35, esto se debe a que las '
        'expresiones siguen la jerarquía de operadores, para cambiar este '
        'comportamiento prueba a encerrar la suma entre paréntesis.',

        UseParentheses(),

        'Se pueden utilizar tantos paréntesis como sean necesarios en una sola '
        'expresión, pero siempre deben corresponderle un paréntesis de cierre '
        'a uno de apertura.',
    ],
    lesson_03_booleans
)
