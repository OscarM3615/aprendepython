from ..models.lesson import Lesson
from .lesson_07_lists import lesson_07_lists


lesson_08_tuples = Lesson(
    'tuplas',
    'Tuplas',
    [
        'Las tuplas son colecciones similares a las listas, con la diferencia '
        'de que una tupla es inmutable, es decir, no se pueden modificar los '
        'elementos que la conforman, tampoco es posible agregar o eliminar '
        'elementos. Una tupla se declara de la siguiente manera:\n\n'
        '[default]>>> tupla = (1, 2, 3, 4, 5)[/]\n\n'
        'Nota que se utilizan paréntesis en lugar de corchetes.',

        'La forma de acceder a los elementos de una tupla es exactamente igual '
        'a la de una lista:\n\n'
        '[default]>>> x = tupla\\[2][/]',

        'También es posible verificar si un elemento exoste dentro de una '
        'tupla de la misma manera:\n\n'
        '[default]>>> 4 in tupla\n'
        'True[/]',

        'Las principales ventajas de las tuplas sobre las listas es su '
        'rendimiento, pues al ser inmutables y contar con una cantidad menor '
        'de métodos los accesos a sus elementos son mucho más rápidos y la '
        'colección ocupa menos espacio en memoria.',
    ],
    lesson_07_lists
)
