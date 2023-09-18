"""
Module providing exercise classes for interactive learning.

This module defines abstract exercise classes and concrete implementations for
interactively checking and testing user-submitted solutions.
"""

import random
from abc import ABCMeta, abstractmethod
from code import InteractiveConsole
from typing import Any, Dict, Optional, Sequence

from ..utils import (
    CheckExercise, confirm_quit_lesson, console, exercise_check, exercise_exit
)


class Exercise(metaclass=ABCMeta):
    """
    Abstract base class for interactive exercises.

    This class defines the basic needed attributes for an exercise to run.
    It also defines the methods that must be implemented in exercise subclasses.
    """

    instructions: str = 'Please override the instructions attribute in your class.'
    env: Dict[str, Any] = {}
    hints: Sequence[str] = ['Inténtalo de nuevo por favor.']

    def __init__(self):
        """Initializes the exercise environment."""

        self.env = {
            **self.env,
            'exit': exercise_exit,
            'quit': exercise_exit,
            'comprobar': exercise_check,
        }

    @abstractmethod
    def run(self): ...

    @abstractmethod
    def test(self) -> bool: ...


class OnelinerExercise(Exercise):
    """
    Interactive exercise class for single-line code solutions.

    Note:
        User-defined exercises must implement the test() method to define the
        validation logic.
    """

    def __init__(self):
        super().__init__()
        self.source = ''

    def run(self):
        """Runs the interactive exercise for single-line code solutions."""

        console.print(self.instructions + '\n')

        while True:
            shell = InteractiveConsole(self.env)
            self.source = shell.raw_input('>>> ')
            shell.runsource(self.source)

            try:
                solution_valid = self.test()
            except Exception as ex:
                console.print(f'[red]{ex}[/]')
                solution_valid = False

            if solution_valid:
                console.print('\n[green]¡Bien hecho![/]')
                break
            else:
                console.print(f'\n[red]{random.choice(self.hints)}[/]\n')


class InteractiveExercise(Exercise):
    """
    Interactive exercise class for multi-line code solutions.

    Note:
        User-defined exercises must implement the test() method to define the
        validation logic.
    """

    def __init__(self):
        super().__init__()
        self.stdin = ''
        self.stdout = ''
        self.env = {**self.env, 'print': self._print, 'input': self._input}

    def _print(self, *values: object, sep: str = ' ', end: str = '\n'):
        """
        Modified version of the print function that appends all the printed text
        to the stdout attribute.
        """

        self.stdout += sep.join(map(str, values)) + end
        print(*values, sep=sep, end=end)

    def _input(self, prompt: str = '') -> str:
        """
        Modified version of the input function that appends all the received
        text to the stdin attribute.
        """

        value = input(prompt)
        self.stdin += value + '\n'
        return value

    def run(self):
        """Runs the interactive exercise for multi-line code solutions."""

        console.print(self.instructions + '\n')

        while True:
            try:
                shell = InteractiveConsole(self.env).interact('', '')
            except CheckExercise:
                try:
                    solution_valid = self.test()
                except Exception as ex:
                    console.print(f'[red]{ex}[/]')
                    solution_valid = False

                if solution_valid:
                    console.print('\n[green]¡Bien hecho![/]')
                    break
                else:
                    console.print(f'\n[red]{random.choice(self.hints)}[/]\n')
