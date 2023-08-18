from typing import List
from ..models.lesson import Lesson

from .lesson_00 import lesson_00
from .lesson_01 import lesson_01
from .lesson_02 import lesson_02
from .lesson_03 import lesson_03


lessons: List[Lesson] = [
    lesson_00,
    lesson_01,
    lesson_02,
    lesson_03,
]
