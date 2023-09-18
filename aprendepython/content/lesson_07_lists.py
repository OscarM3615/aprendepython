import re

from ..models.exercise import InteractiveExercise, OnelinerExercise
from ..models.lesson import Lesson
from .lesson_06_logical_ops import lesson_06_logical_ops


class PrintList(OnelinerExercise):
    instructions = 'Muestra el valor de lista para observar su contenido:'
    hints = [
        'Puedes escribir el nombre de la lista o usar la instrucción print.',
    ]
    env = {'lista': [1, 2, 3]}

    def test(self) -> bool:
        return bool(re.match(r'^lista|print *?\( *?lista *?\)', self.source))


class GetThirdElement(OnelinerExercise):
    instructions = 'Como ejercicio, intenta obtener el número 3 de la lista:'
    hints = [
        'Recuerda que los índices inician en 0.',
        'Debes utilizar la sintaxis de corchetes lista\\[i].',
    ]
    env = {'lista': [1, 2, 3]}

    def test(self) -> bool:
        return bool(re.match(r'^lista\[2\]', self.source))


class UseNegativeIndex(OnelinerExercise):
    instructions = ('Obtén el primer elemento de la lista usando índices '
                    'negativos:')
    hints = [
        'Recuerda que los índices negativos recorren la lista en reversa.',
    ]
    env = {'lista': [1, 2, 3]}

    def test(self) -> bool:
        return bool(re.match(r'^lista\[\-3\]', self.source))


class PrintAnotherList(OnelinerExercise):
    instructions = 'Prueba a mostrar el contenido de la nueva lista:'
    hints = [
        'Puedes escribir el nombre de la lista o usar la instrucción print.',
    ]
    env = {'otra_lista': [3, 2, 1]}

    def test(self) -> bool:
        return bool(
            re.match(r'^otra_lista|print *?\( *?otra_lista *?\)', self.source))


class DeclareList(InteractiveExercise):
    instructions = ('Como ejercicio declara una lista que contenga los valores '
                    '"hola" y "mundo" con el nombre "mi_lista". Después '
                    'escribe comprobar() para validar la solución y continuar:')
    hints = [
        'La lista debe llamarse "mi_lista".',
        'La lista debe tener 2 elementos.',
        'Verifica que la lista contenga ambas cadenas de texto.',
    ]

    def test(self) -> bool:
        mi_lista = self.env.get('mi_lista')
        return mi_lista == ['hola', 'mundo']


class CheckValueInList(OnelinerExercise):
    instructions = ('A continuación se han declarado las siguientes '
                    'variables:\n\n'
                    '[default]>>> aprobatorias = \\[7, 8, 9, 10]\n'
                    'calificacion = 8[/]\n\n'
                    'Mediante el uso del operador "in", determina si la '
                    'variable calificacion es aprobatoria:')
    hints = [
        'Verifica si "calificacion" se encuentra en la lista "aprobatorias".',
    ]
    env = {'aprobatorias': [7, 8, 9, 10], 'calificacion': 8}

    def test(self) -> bool:
        return bool(re.match(r'^calificacion *?in *?aprobatorias', self.source))


lesson_07_lists = Lesson(
    'listas',
    'Listas',
    [
        'Las listas son un tipo de dato especial que pertenece a las '
        'colecciones, es decir, puede contener varios elementos. Una lista '
        'puede contener tantos valores como se desee y sin importar el tipo de '
        'dato que sean. El siguiente es un ejemplo de cómo declarar una '
        'lista:\n\n'
        '[default]>>> lista = \\[]\n'
        '>>> lista.append(1)\n'
        '>>> lista.append(2)\n'
        '>>> lista.append(3)[/]',

        PrintList(),

        'El método "append" ha agregado los números a la lista, de modo que al '
        'mostrarla se enlistan sus elementos. Se puede acceder a un elemento '
        'único por medio de índices utilizando la notación "lista[i]", donde '
        '"i" es un número que indica la posición del elemento, por ejemplo:\n\n'
        '[default]>>> lista\\[0]\n'
        '1[/]',

        'Como puedes observar, la numeración de los índices inicia desde el 0, '
        'siendo el primer elemento de la lista, por lo que una lista con tres '
        'elementos tendría los índices desde el 0 hasta el 2, siendo el 2 el '
        'tercer y último elemento.',

        GetThirdElement(),

        'También es posible usar índices con un orden inverso, esto es útil '
        'cuando no se conoce el tamaño exacto de una lista, por ejemplo, para '
        'obtener el último elemento:\n\n'
        '[default]>>> lista\\[-1]\n'
        '3[/]',

        'Esta sería otra manera de obtener el númera tres. El índice -1 '
        'corresponde al último elemento, al penúltimo le corresponde el -2 y '
        'así sucesivamente.',

        UseNegativeIndex(),

        'Una funcionalidad importante para las listas es conocer la cantidad '
        'de elementos que contienen. Para esto se utiliza la función "len", de '
        'este modo:\n\n'
        '[default]>>> len(lista)\n'
        '3[/]\n\n'
        'Como podrás notar, ha devuelto la cantidad de elementos que contiene '
        'la lista.',

        'Otra forma de declarar listas es indicando sus elementos desde un '
        'inicio:\n\n'
        '[default]>>> otra_lista = \\[3, 2, 1][/]\n'
        'De este modo, la lista tendrá inicialmente los números 3, 2 y 1 en '
        'ese mismo orden.',

        PrintAnotherList(),

        DeclareList(),

        'Ahora que ya conoces las listas es momento de presentar un nuevo '
        'operador, el cual lleva como sintaxis la palabra clave "in". Sirve '
        'para comprobar si un elemento está dentro de una colección, en este '
        'caso, una lista. Ejemplo:\n\n'
        '[default]>>> lista = \\[1, 2, 3, 4, 5]\n'
        '>>> 4 in lista\n'
        'True[/]',

        'El código anterior devuelve True, pues el número 4 está presente en '
        'la lista indicada.',

        CheckValueInList(),
    ],
    lesson_06_logical_ops
)
