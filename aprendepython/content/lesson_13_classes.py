import re

from ..models.exercise import InteractiveExercise, OnelinerExercise
from ..models.lesson import Lesson
from .lesson_12_functions import lesson_12_functions


class MiClase:
    atributo = 'Este es un atributo'

    def metodo(self):
        print('Este mensaje se imprime desde la clase.')


class ClaseTest:
    def __init__(self):
        self.called_method = False

    def __repr__(self):
        return f'<__main__.ClaseTest object at {hex(id(self))}>'

    def mensaje(self):
        self.called_method = True
        print(self)


class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.called_method = False

    def mostrar_titulo(self):
        self.called_method = True
        print(self.titulo)


class PrintObjectAttribute(OnelinerExercise):
    instructions = ('Muestra el atributo anterior en pantalla utilizando la '
                    'función print():')
    hints = [
        'Se accede a un atributo de la forma "<objeto>.<atributo>".',
        'Recuerda utilizar la función print().',
    ]
    env = {'objeto': MiClase()}

    def test(self) -> bool:
        return bool(
            re.match(r'^print *?\( *?objeto\.atributo *?\)', self.source))


class PrintSelf(InteractiveExercise):
    instructions = ('Crea un objeto llamado "mi_objeto" a partir de '
                    '"ClaseTest" y manda a llamar a su método mensaje para '
                    'observar qué sucede:')
    hints = [
        'Recuerda llamar al objeto como "mi_objeto".',
        'Verifica que estás utilizando la clase "Clase Test".',
        'Se accede a un atributo de la forma "<objeto>.<atributo>".',
    ]
    env = {'ClaseTest': ClaseTest}

    def test(self) -> bool:
        obj = self.env.get('mi_objeto')
        return isinstance(obj, ClaseTest) and obj.called_method == True


class PrintBookTitle(OnelinerExercise):
    instructions = ('Utiliza el objeto anterior llamado "mi_libro" (ya está '
                    'declarado) para llamar al nuevo método "mostrar_titulo" y '
                    'observa lo que sucede:')
    hints = [
        'Recuerda incluir paréntesis vacíos al llamar al método.',
    ]
    env = {'mi_libro': Libro('Hamlet')}

    def test(self) -> bool:
        obj = self.env.get('mi_libro')
        return bool(obj and obj.called_method == True)


class CreatePersonClass(InteractiveExercise):
    instructions = ('Como último ejercicio, crea una clase Persona que reciba '
                    'un argumento nombre y lo guarde como atributo. Además, la '
                    'clase debe contener un método presentar(), el cual debe '
                    'imprimir \'Hola, mi nombre es \' y el nombre de la '
                    'persona. Después crea un objeto pasando tu nombre como '
                    'argumento y llama al método presentar():')
    hints = [
        'Recuerda indentar correctamente los contenido de la clase.',
        'Recuerda hacer uso del parámetro self en el método.',
        'Puedes concatenar textos con el atributo nombre.',
        'Recuerda recibir el nombre en el método __init__.',
    ]

    def test(self) -> bool:
        person_class = self.env.get('Persona')
        if not isinstance(person_class, type):
            return False
        test_obj = person_class('Test')
        return 'Hola, mi nombre es' in self.stdout and test_obj.nombre == 'Test'


lesson_13_classes = Lesson(
    'clases-y-objetos',
    'Clases y objetos',
    [
        'Los objetos son una forma de encapsular múltiples variables y '
        'funciones en una sola entidad a partir de plantillas que se conocen '
        'como clases. En Python una clase se declara de la siguiente '
        'manera:\n\n'
        '[default]>>> class MiClase:\n'
        '...     atributo = \'Este es un atributo\'\n'
        '...\n'
        '...     def metodo(self):\n'
        '...         print(\'Este mensaje se imprime desde la clase.\')\n'
        '...[/default]',

        'Nota que las variables y las funciones se incluyen en la clase por '
        'medio de la indentación. Además, las variables de una clase son '
        'llamadas atributos y sus funciones se conocen como métodos.',

        'Para crear un objeto de la clase esta se debe "mandar llamar", por '
        'ejemplo:\n\n'
        '[default]>>> objeto = MiClase()[/default]',

        'Al haber creado un objeto, este obtiene los atributos y métodos de la '
        'clase a partir de la cual se creó, por lo que podemos acceder a un '
        'atributo del siguiente modo:\n\n'
        '[default]>>> objeto.atributo\n'
        '\'Este es un atributo\'[/default]',

        PrintObjectAttribute(),

        'Del mismo modo, se puede asignar nuevos valores al atributo con el '
        'operador "=":\n\n'
        '[default]>>> objeto.atributo = \'Nuevo valor\'[/default]',

        'También se puede llamar al método con la sintaxis de punto:\n\n'
        '[default]>>> objeto.metodo()\n'
        'Este mensaje se imprime desde la clase.[/default]',

        'Observa que aunque en la clase se recibe un parámetro self, al '
        'haberlo llamado no se proporcionó ningún argumento y el código se '
        'ejecutó sin ningún error. Esto es porque al declarar métodos para una '
        'clase se debe incluir como primer argumento una referencia al objeto '
        'desde el cual se está mandando llamar.',

        'Al invocar el método, no es necesario proporcionar el valor del '
        'parámetro self, pues Python se encarga automáticamente de asignar ese '
        'valor al objeto actual, observa la siguiente declaración:\n\n'
        '[default]>>> class ClaseTest:\n'
        '...     def mensaje(self):\n'
        '...         print(self)\n'
        '...[/default]',

        PrintSelf(),

        'Como se puede observar, self tiene asignado como valor un objeto de '
        'tipo ClaseTest, esto significa que self es lo mismo que mi_objeto, '
        'pero self permite que se pueda hacer referencia al objeto sin conocer '
        'el nombre con el que fue declarado.',

        'Las clases puede tener métodos especiales que ya tienen un rol '
        'predefinido por Python, uno de los métodos más importantes es el '
        'método __init__, su importancia está en que es llamado cuando se crea '
        'un objeto.',

        'El método __init__ funciona como en otros lenguajes de programación '
        'actúa un método constructor. Por ejemplo:\n\n'
        '[default]>>> class Libro:\n'
        '...     def __init__(self, titulo):\n'
        '...         self.titulo = titulo\n'
        '...[/default]\n\n'
        'El método __init__ es utilizado principalmente para inicializar '
        'atributos que se recibirán desde el resto del código.',

        'Al haber definido parámteros adicionales para el método __init__, la '
        'manera de crear objetos para dicha clase cambia ligeramente:\n\n'
        '[default]>>> mi_libro = Libro(\'Hamlet\')[/default]\n\n'
        'Observa que ahora es necesario indicar los argumentos que recibirá '
        '__init__, en este caso el título (recuerda que self se asigna '
        'automáticamente).',

        'Los métodos de una clase puede utilizar el argumento self para hacer '
        'refrencia al objeto actual y acceder a sus atributos o al resto de '
        'métodos. Se han hecho algunos cambios a la clase anterior para '
        'incluir un nuevo método:\n\n'
        '[default]>>> class Libro:\n'
        '...     def __init__(self, titulo):\n'
        '...         self.titulo = titulo\n'
        '...\n'
        '...     def mostrar_titulo(self):\n'
        '...         print(self.titulo)\n'
        '...[/default]\n\n',

        PrintBookTitle(),

        'Como se puede notar, el método hizo referencia al objeto desde el '
        'cual se llamó (mi_libro) y accedió al atributo "titulo".',

        CreatePersonClass(),
    ],
    lesson_12_functions
)
