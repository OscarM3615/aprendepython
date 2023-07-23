from typing import Optional, Sequence

from .exercise import Exercise
from ..config import config
from ..utils import console


class Lesson:
    def __init__(self, id_: str, name: str, content: Sequence[str | Exercise],
                 prev: Optional['Lesson'] = None):
        self.id_ = id_
        self.name = name
        self.content = content
        self.prev = prev

    def __str__(self) -> str:
        return self.name

    def run(self):
        for block in self.content:
            # TODO: Check if block is text or an exercise.
            console.print(block)
            console.input('\n...\n\n')

        console.print(
            f'¡Felicidades! Has completado la lección "{self.name}". Ahora '
            'puedes continuar con el resto del curso.\n'
        )

        if self.id_ not in config['completed_lessons']:
            config['completed_lessons'].append(self.id_)
