from .config import config
from .content import lessons
from .utils import console, safe_exit, selection


class Menu:
    def __init__(self):
        self.lessons = lessons

    def show(self):
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
                lesson.run()
            else:
                console.print(
                    '[red]No puedes tomar esta lección aún. Primero necesitas '
                    f'completar "{lesson.prev.name}".\n[/]'
                )
