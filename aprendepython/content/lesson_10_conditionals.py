from ..models.exercise import InteractiveExercise
from ..models.lesson import Lesson
from .lesson_09_dicts import lesson_09_dicts


class ReadInputAndPrintTest(InteractiveExercise):
    instructions = ('Para poner a prueba los condicionales, utiliza la función '
                    '"input" para leer un texto del usuario y si la palabra '
                    'es "test" imprime "logrado".\n\n'
                    'Pista: la función input() se puede utilizar de la '
                    'siguiente manera:\n\n'
                    '>>> valor = input("Escribe algo: ")')
    hints = [
        'Puedes usar la función input como "valor = input()".',
        'Compara el valor de entrada con el operador "==".',
        'Recuerda indentar la instrucción print().',
    ]

    def test(self) -> bool:
        return 'test' in self.stdin and 'logrado' in self.stdout


class CompareGradeIfElse(InteractiveExercise):
    instructions = ('A continuación se ha declarado la variable '
                    '"calificacion = 6". Como ejercicio, utilizando la '
                    'sintaxis if y else, imprime "aprobado" si la variable '
                    'calificacion es mayor o igual a 7, de lo contrario, '
                    'imprime "reprobado":')
    hints = [
        'Recuerda indentar las líneas que están después de if y después de '
        'else.',
    ]
    env = {'calificacion': 6}

    def test(self) -> bool:
        return 'reprobado' in self.stdout


lesson_10_conditionals = Lesson(
    'condicionales',
    'Condicionales',
    [
        'Los bloques condicionales sirven para determinar si se va a ejecutar '
        'una serie de instrucciones con base en una condición previa. Esto es '
        'útil porque frecuentemente los programas requieren que el usuario '
        'tome una decisión o que se cumplan ciertas restricciones para poder '
        'llevar a cabo una acción.',

        'La sintaxis de un bloque condicional es:\n\n'
        '[default]>>> if <condición>:\n'
        '...     instruccion()\n'
        '...     instruccion()[/]',

        'Nota que las instrucciones a ejecutarse van acompañadas de una '
        'indentación o 4 espacios al inicio de la línea. Esto es importante '
        'porque así es como se espara el código que se ejecutará por la '
        'condición del resto del programa.',

        ReadInputAndPrintTest(),

        'Así como se puede decidir si ejecutar un bloque de código según una '
        'condición, también se puede especificar otro bloque de código para '
        'que se ejecute si la condición no se ha cumplido:\n\n'
        '[default]>>> if <condición>:\n'
        '...     <código se condición se cumple>\n'
        '... else:\n'
        '...     <código si condición no se cumple>[/]',

        CompareGradeIfElse(),

        'Como puedes notar, se ha ejecutado solamente el bloque else, pues la '
        'condición no se ha cumplido.',

        'Es posible anidar bloques de código, de modo que pueda quedar una '
        'estructura similar a la siguiente:\n\n'
        '[default]>>> if <condición-1>:\n'
        '...     if <condición-2>:\n'
        '...         <instrucciones>\n'
        '... else:\n'
        '...     <instrucciones>[/default]\n\n'
        'Nota que el bloque else pertenece a la primera condición y no a la '
        'segunda, según el nivel de la indentación.',

        'Sin embargo, para simplificar el flujo del código y su legibilidad, '
        'es posible utilizar la sintaxis "elif". Su función es evaluar una '
        'nueva condición en caso de que las anteriores no se hayan '
        'cumplido:\n\n'
        '[default]>>> if <condicion-1>:\n'
        '...     <instrucciones>\n'
        '... elif <condicion-2>:\n'
        '...     <instrucciones>\n'
        '... else:\n'
        '...     <instrucciones>[/]',

        'Si la condición 1 se cumple se ejecutará su bloque de código, si no, '
        'se evaluará la condición 2; en caso de tampoco cumplirse, se evaluará '
        'la siguiente condición sucesivamente. Si ninguna condición se cumple, '
        'se ejecutará el bloque else, en caso de haberlo.',
    ],
    lesson_09_dicts
)
