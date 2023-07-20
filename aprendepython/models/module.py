from typing import Optional, Collection
from .lesson import Lesson


class Module:
    def __init__(self, name: str, lessons: Optional[Collection[Lesson]] = None):
        self.name = name
        if lessons is not None:
            self.lessons = lessons
        else:
            self.lessons = []

    def __str__(self) -> str:
        return self.name
