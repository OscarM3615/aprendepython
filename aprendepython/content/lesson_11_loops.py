from ..models.exercise import InteractiveExercise
from ..models.lesson import Lesson
from .lesson_10_conditionals import lesson_10_conditionals


class PrintVowels(InteractiveExercise):
    instructions = ('Intenta realizar un ciclo for, pero en este caso '
                    'declarando una tupla llamada "vocales" donde se incluyan '
                    'las 5 vocales. El resultado debe ser solamente una vocal '
                    'por línea:')
    hints = [
        'Recuerda que la variable "vocales" debe ser una tupla.',
        'El resultado debe ser una vocal en cada línea sin ningún mensaje '
        'adicional.',
        'Para imprimir la vocal solamente escribe print(vocal).',
    ]

    def test(self) -> bool:
        vowels = self.env.get('vocales')
        return isinstance(vowels, tuple) and 'a\ne\ni\no\nu\n' in self.stdout


class Print10Numbers(InteractiveExercise):
    instructions = ('Como ejercicio, realiza un ciclo for que recorra los '
                    'números del 1 al 10 (incluyendo a este último):')
    hints = [
        'Recuerda que un rango se detiene antes del número de fin.',
        'Recuerda que el rango debe recibir los valores de inicio y de fin.',
    ]

    def test(self) -> bool:
        return '1\n2\n3\n4\n5\n6\n7\n8\n9\n10' in self.stdout


class WhileInputExit(InteractiveExercise):
    instructions = ('Crea una variable llamada "entrada" igual a una cadena de '
                    'texto vacía, después haz un ciclo while que se repita '
                    'mientras la cadena no sea "salir", dentro del ciclo lee '
                    'la entrada del usuario y guarda en la variable "entrada":')
    hints = [
        'Recuerda declarar "entrada" como una cadena vacía.',
        'Recuerda leer la entrada del usuario con input().',
    ]

    def test(self) -> bool:
        return (self.stdin.endswith('salir\n')
                and self.env.get('entrada') == 'salir')


class PrintEvenNumbers(InteractiveExercise):
    instructions = ('A continuación, crea un ciclo for que por medio del uso '
                    '"break" o "continue" (determina el más adecuado), imprima '
                    'los números pares del 1 al 20.')
    hints = [
        'Recuerda que break termina todo el ciclo y continue la iteración '
        'actual.',
        'Recuerda que para incluir el número 20 se debe indicar el rango hasta '
        '21.',
        'Recuerda imprimir el valor del número actual.',
        'Prueba dividir entre 2 y revisar el residuo para saber si es par.',
    ]

    def test(self) -> bool:
        return '2\n4\n6\n8\n10\n12\n14\n16\n18\n20\n' in self.stdout


lesson_11_loops = Lesson(
    'ciclos',
    'Ciclos',
    [
        'Los ciclos sirven para repetir una serie de acciones múltiples veces. '
        'En Python existen dos tipos de ciclos: for y while.',

        'Un ciclo for permite recorrer una colección para acceder a sus '
        'elementos. Por ejemplo:\n\n'
        '[default]>>> nums = \\[1, 2, 3, 4, 5]\n'
        '>>> for x in nums:\n'
        '...     print(\'El número es \' + str(x))\n'
        '...\n'
        'El número es 1\n'
        'El número es 2\n'
        'El número es 3\n'
        'El número es 4\n'
        'El número es 5[/default]',

        PrintVowels(),

        'Es posible también realizar un ciclo for sin declarar primero la '
        'colección, como en el siguiente ejemplo que utiliza una tupla:\n\n'
        '[default]>>> for i in (1, 2, 3, 4, 5):\n'
        '...     print(i)\n'
        '...\n'
        '1\n'
        '2\n'
        '3\n'
        '4\n'
        '5[/default]',

        'El ciclo anterior tiene exactamente el mismo funcionamiento que el '
        'primer ejemplo de la lección. Sin embargo, para crear series de '
        'números como en los ejemplos anteriores es preferible utilizar la '
        'colección "range", la cual tiene 3 forma de utilizarse.',

        'Este ejemplo imprimirá los números 0, 1, 2, 3, 4, ya que se indica '
        'cuándo detenerse:\n\n'
        '[default]>>> for i in range(5):\n'
        '...     print(i)\n'
        '...\n'
        '0\n'
        '1\n'
        '2\n'
        '3\n'
        '4[/default]',

        'Al siguiente rango se le indica un inicio y un fin:\n\n'
        '[default]>>> for i in range(3, 6):\n'
        '...     print(i)\n'
        '...\n'
        '3\n'
        '4\n'
        '5[/default]',

        'Por último, al siguiente rango también se le indica el salto, en este '
        'caso, el rango avanza de 2 en 2:\n\n'
        '[default]>>> for i in range(3, 8, 2):\n'
        '...     print(i)\n'
        '...\n'
        '3\n'
        '5\n'
        '7[/default]',

        'El tercer valor de range puede ser negativo, en este caso, el valor '
        'de inicio deberá ser más grande que el de fin o de lo contrario no se '
        'incluirá ningún número.',

        Print10Numbers(),

        'El ciclo while, a diferencia del ciclo for, se repetirá mientras se '
        'siga cumpliendo una condición lógica en lugar de recorrer una '
        'colección. Por ejemplo:\n\n'
        '[default]>>> numero = 0\n'
        '>>> while numero < 5:\n'
        '...     print(numero)\n'
        '...     numero = numero + 1\n'
        '...\n'
        '0\n'
        '1\n'
        '2\n'
        '3\n'
        '4[/default]',

        WhileInputExit(),

        'Hay dos maneras de cambiar el flujo normal de un ciclo, ya sea para '
        'terminar el ciclo antes de lo esperado o para omitir una iteración. '
        'Ambos casos se pueden realizar con "break" y "continue".',

        'La palabra "break" permite salir completamente de un ciclo y seguir '
        'ejecutando el resto del código.',

        'Por otro lado, continue permite omitir solamente el resto de la '
        'iteración actual y continuar con las restantes.',

        'El siguiente ejemplo permite ilustrar lo que sucede en el caso de '
        '"break":\n\n'
        '[default]>>> for x in range(5):\n'
        '...     if x == 3:\n'
        '...         break\n'
        '...     print(x)\n'
        '...\n'
        '0\n'
        '1\n'
        '2[/default]\n\n'
        'Se puede observar cómo al llegar al número 3 se ejecuta el '
        'condicional con la palabra "break", haciendo que se interrumpa el '
        'completamente sin llegar a la instrucción print() de nuevo.',

        'Por otro lado, el siguiente ejemplo muestra el uso de "continue":\n\n'
        '[default]>>> for x in range(5):\n'
        '...     if x == 3:\n'
        '...         continue\n'
        '...     print(x)\n'
        '...\n'
        '0\n'
        '1\n'
        '2\n'
        '4[/default]\n\n'
        'En esta caso, se puede observar que solamente se omitió la iteración '
        'en donde x era igual a 3, omitiendo las instrucciones que restaban '
        '(print) y continuó con el resto de iteraciones.',

        PrintEvenNumbers(),
    ],
    lesson_10_conditionals
)
