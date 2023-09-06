"""
Module representing the menu for choosing and running lessons.
"""

from typing import Sequence

from .config import config
from .models.lesson import Lesson
from .utils import QuitLesson, console, safe_exit, selection


class Menu:
    """
    Represents the menu for choosing and running lessons.

    Attributes:
        lessons (Sequence[Lesson]):
            A list of Lesson objects representing available lessons.

    Methods:
        show(self):
            Displays the menu and allows the user to select and run a lesson.
    """

    def __init__(self, lessons: Sequence[Lesson]):
        self.lessons = lessons

        for lesson in lessons:
            if lesson.id_ in config['completed_lessons']:
                lesson.completed = True

    def show(self):
        """
        Display the available lessons and allow the user to select and run a
        lesson.

        Note: This function will create a loop until the user wants to exit.
        """

        while True:
            selected = selection(
                self.lessons,
                title='Por favor elige una lección o escribe 0 para salir de '
                '[bold green]aprendepython[/].'
            )

            if selected == 0:
                safe_exit()

            # Run the lesson if user completed its dependency.
            lesson = self.lessons[selected - 1]
            if not lesson.prev or lesson.prev.id_ in config['completed_lessons']:
                try:
                    lesson.run()
                except QuitLesson:
                    ...  # back to main menu
            else:
                console.print(
                    '[red]No puedes tomar esta lección aún. Primero necesitas '
                    f'completar "{lesson.prev.name}".\n[/]'
                )
