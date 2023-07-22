from typing import Sequence
from .exercise import Exercise


class Lesson:
    def __init__(self, id_: str, name: str, completed: bool,
                 dependencies: Sequence[str],
                 content: Sequence[str | Exercise]):
        self.id_ = id_
        self.name = name
        self.completed = completed
        self.dependencies = dependencies
        self.content = content

    def __str__(self) -> str:
        return self.name

    def run(self):
        ...
