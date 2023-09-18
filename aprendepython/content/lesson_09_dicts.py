import re

from ..models.exercise import InteractiveExercise, OnelinerExercise
from ..models.lesson import Lesson
from .lesson_08_tuples import lesson_08_tuples


class PrintDict(OnelinerExercise):
    instructions = ('Imprime el valor de contactos para visualizar su '
                    'estructura:')
    hints = [
        'Puedes usar el nombre de la variable directamente o usar la '
        'instrucción "print".',
    ]
    env = {'contactos': {'Juan': 9591234567, 'Alejandro': 9591745235}}

    def test(self) -> bool:
        return bool(
            re.match(r'^contactos|print *?\( *?contactos *?\)', self.source))


class AddContact(InteractiveExercise):
    instructions = ('Como ejercicio, agrega un contacto llamado Ana con el '
                    'número 9597654321 en el diccionario anterior, este ya ha '
                    'sido inicializado en el entorno de trabajo. Al final '
                    'escribe comprobar() para continuar:')
    hints = [
        'Verifica que el nombre Ana esté escrito correctamente.',
        'Revisa que el número sea el indicado.',
        'Observa que el número esté guardado como entero y no como texto.',
    ]
    env = {'contactos': {'Juan': 9591234567, 'Alejandro': 9591745235}}

    def test(self) -> bool:
        contacts = self.env.get('contactos')
        if not isinstance(contacts, dict):
            return False
        return contacts.get('Ana') == 9597654321


class GetValueFromDict(OnelinerExercise):
    instructions = ('Como ejercicio, imprime el valor del contacto Ana '
                    'registrado previamente:')
    hints = [
        'Utiliza la instrucción "print" para mostrar el resultado.',
        'Recuerda usar comillas para acceder al elemento "Ana".',
    ]
    env = {'contactos': {'Juan': 9591234567,
                         'Alejandro': 9591745235, 'Ana': 9597654321}}

    def test(self) -> bool:
        return bool(re.match(
            r'^print *?\( *?contactos *?\[ *?[\'\"]Ana[\'\"] *?\] *?\)',
            self.source))


lesson_09_dicts = Lesson(
    'diccionarios',
    'Diccionarios',
    [
        'Los diccionarios son un tipo de datos similar a las listas, excepto '
        'que trabaja con claves y valores en lugar de referencias elementos '
        'por índices. Cada valor en un diccionario se puede acceder por medio '
        'de una clave, la cual puede ser una cadena de texto, un número, una '
        'tupla, etc., en lugar de utilizar índices numéricos.',

        'Para declarar un diccionario se utiliza la sintaxis de llaves:\n\n'
        '[default]>>> contactos = {}[/]',

        'Para asignar un valor a una clave se realiza de manera similar a los '
        'arreglos:\n\n'
        '[default]>>> contactos\\[\'Juan\'] = 9591234567\n'
        '>>> contactos\\[\'Alejandro\'] = 9591745235',

        PrintDict(),

        'Para inicializar un diccionario con valores ya incluidos se utiliza '
        'una notación como la que se mostró en el resultado anterior:\n\n'
        '[default]>>> contactos = {\n'
        '...     \'Juan\': 9591234567,\n'
        '...     \'Alejandro\': 9591745235\n'
        '... }[/]',

        AddContact(),

        'Al igual que con las listas y las tuplas, se puede comprobar si un '
        'elemento existe dentro del diccionario por medio de su clave:\n\n'
        '[default]>>> \'Juan\' in contactos\n'
        'True[/]',

        'Para obtener el valor de un elemento se utilizan corchetes incluyendo '
        'la clave de la cual se desea obtener su valor:\n\n'
        '[default]>>> contactos\\[\'Alejandro\']\n'
        '9591745235[/]',

        GetValueFromDict(),
    ],
    lesson_08_tuples
)
