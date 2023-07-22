from typing import Optional, Sequence
from .lesson import Lesson


class Module:
    def __init__(self, name: str, lessons: Optional[Sequence[Lesson]] = None):
        self.name = name
        if lessons is not None:
            self.lessons = lessons
        else:
            self.lessons = []

    def __str__(self) -> str:
        return self.name
