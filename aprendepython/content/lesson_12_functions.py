from types import FunctionType

from ..models.exercise import InteractiveExercise
from ..models.lesson import Lesson
from .lesson_11_loops import lesson_11_loops


class UseDefinedFunction(InteractiveExercise):
    instructions = ('Para entender cómo funciona, llama la función escribiendo '
                    'su nombre seguido de paréntesis de apertura y de cierre:')
    hints = [
        'Verifica que el nombre "mostrar_mensaje" esté escrito correctemante.',
        'Recuerda colocar el par de paréntesis después del nombre.',
    ]

    def __init__(self):
        self.env = {'mostrar_mensaje': self._mostrar_mensaje,
                    '_called_function': False}
        super().__init__()

    def _mostrar_mensaje(self):
        self.env['_called_function'] = True
        self._print('Hola mundo')

    def test(self) -> bool:
        return (self.env.get('_called_function') == True
                and 'Hola mundo' in self.stdout)


class CreateOwnFunction(InteractiveExercise):
    instructions = ('Crea una función llamada "mi_funcion" que al invocarla '
                    'muestre el mensaje "Estoy programando en Python", después '
                    'llama a la función que definiste:')
    hints = [
        'Revisa que la función tenga el nombre correcto.',
        'Verifica que tu función imprime el mensaje correcto con mayúsculas y '
        'minúsculas.',
    ]

    def test(self) -> bool:
        user_function = self.env.get('mi_funcion')
        return (isinstance(user_function, FunctionType)
                and 'Estoy programando en Python' in self.stdout)


class UseSumFunction(InteractiveExercise):
    instructions = ('Utiliza la función sumar para obtener el resultado de la '
                    'suma de 5 y 7:')
    hints = [
        'Escribe los valores 5 y 7 entre los paréntesis de la función.',
        'Separa los argumentos 5 y 7 con una coma.',
    ]

    def __init__(self):
        self.env = {'sumar': self._sumar,
                    '_called_function': False, '_args_used': None}
        super().__init__()

    def _sumar(self, num1: int, num2: int) -> int:
        self.env['_called_function'] = True
        self.env['_args_used'] = (num1, num2)
        return num1 + num2

    def test(self) -> bool:
        return (self.env.get('_called_function') == True
                and self.env.get('_args_used') == (5, 7))


class CreateEqualsFunction(InteractiveExercise):
    instructions = ('Para practicar la declaración de funciones con '
                    'argumentos, declara una función "son_iguales" que reciba '
                    'dos argumentos y devuelva True si ambos valores son '
                    'iguales y que de lo contrario se devuelva False:')
    hints = [
        'Verifica que el nombre de la función esté correcto.',
        'Puedes utilizar el operador == para saber si los argumentos son '
        'iguales.',
        'Recuerda incluir la palabra "return" para devolver el resultado.',
    ]

    def test(self) -> bool:
        equals = self.env.get('son_iguales')
        return (isinstance(equals, FunctionType)
                and equals('a', 'a') and not equals(2, 0))


lesson_12_functions = Lesson(
    'funciones',
    'Funciones',
    [
        'Las funciones son una manera práctica de separar bloques de código '
        'permitiéndonos ordenar nuestro código y hacerlo reutilizable. Las '
        'funciones se declaran utilizando la palabra clave "def", seguida del '
        'nombre que tendrá la función.',

        'Por ejemplo, este código declara una función "mostrar_mensaje":\n\n'
        '[default]>>> def mostrar_mensaje():\n'
        '...     print(\'Hola mundo\')\n'
        '...[/default]',

        UseDefinedFunction(),

        'Como puedes ver, se ha ejecutado la instrucción definida en el bloque '
        'de código de la función.',

        CreateOwnFunction(),

        'Las funciones también pueden recibir argumentos, es decir, valores '
        'son recibidos desde donde fueron llamadas. Por ejemplo:\n\n'
        '[default]>>> def saludar(nombre):\n'
        '...     print(\'Hola \' + nombre)\n'
        '...saludar(\'Juan\')\n'
        'Hola Juan[/default]',

        'Las funciones pueden devolver valores para guardar el resultado '
        'utilizando la palabra clave "return", por ejemplo:\n\n'
        '[default]>>> def sumar(num1, num2):\n'
        '...     return num1 + num2\n'
        '...[/default]',

        UseSumFunction(),

        CreateEqualsFunction(),
    ],
    lesson_11_loops
)
