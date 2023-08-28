"""
Module representing lessons in the course and user progress tracking.

This module provides the 'Lesson' class, which represents a lesson in the
course. Each lesson contains an ID, a name, content (a sequence of information
and exercises to be displayed to the user), and an optional previous lesson that
must be completed before taking the current lesson.
"""

from typing import Optional, Sequence

from .exercise import Exercise
from ..config import config
from ..utils import QuitLesson, confirm_quit_lesson, console


class Lesson:
    """Represents a lesson in the course."""

    def __init__(self, id_: str, name: str, content: Sequence[str | Exercise],
                 prev: Optional['Lesson'] = None):
        """
        Initialise the Lesson instance.

        Args:
            id_ (int):
                A unique identifier.
            name (str):
                The name to be shown to the user.
            content (Sequence[str | Exercise]):
                A sequence of information and exercises to be displayed to the
                user.
            prev (Optional[Lesson]):
                An optional previous lesson to be completed before the user can
                take the current lesson.
        """

        self.id_ = id_
        self.name = name
        self.content = content
        self.prev = prev
        self.completed = False

    def __str__(self) -> str:
        if self.completed:
            return f'[green]{self.name}[/]'
        return f'[yellow]{self.name}[/]'

    def run(self):
        """
        Displays the information or runs the exercises present within the
        content attribute.

        Note:
            The lesson id is appended to the completed_lessons array in the
            config object, but does not save changes.
        """

        for block in self.content:
            while True:
                try:
                    if isinstance(block, Exercise):
                        block.run()
                    else:
                        console.print(block)

                    console.input('\n...\n\n')
                    break
                except (KeyboardInterrupt, EOFError, QuitLesson):
                    if confirm_quit_lesson():
                        raise QuitLesson

        console.print(
            f'¡Felicidades! Has completado la lección "{self.name}". Ahora '
            'puedes continuar con el resto del curso.\n'
        )

        if self.id_ not in config['completed_lessons']:
            self.completed = True
            config['completed_lessons'].append(self.id_)
