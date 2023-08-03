import random
from abc import ABCMeta, abstractmethod
from typing import Any, Mapping, Sequence
from code import InteractiveConsole

from ..utils import console


def exercise_exit(): raise SystemExit


class Exercise(metaclass=ABCMeta):
    instructions: str = 'Please override the instructions attribute in your class.'
    env: Mapping[str, Any] = {}
    hints: Sequence[str] = ['Inténtalo de nuevo por favor.']

    def __init__(self):
        self.locals = {
            **self.env,
            '__doc__': None,
            'exit': exercise_exit
        }

    @abstractmethod
    def run(self): ...

    @abstractmethod
    def test(self) -> bool: ...


class OnelinerExercise(Exercise):
    def __init__(self):
        super().__init__()
        self.source = ''

    def run(self):
        console.print(self.instructions + '\n')

        while True:
            shell = InteractiveConsole(self.locals)
            self.source = shell.raw_input('>>> ')
            shell.runsource(self.source)

            if self.test():
                console.print('\n[green]¡Bien hecho![/]')
                break
            else:
                console.print(f'\n[red]{random.choice(self.hints)}[/]\n')
