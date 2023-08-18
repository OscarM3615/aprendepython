from typing import List
from ..models.lesson import Lesson

from .lesson_00_intro import lesson_00_intro
from .lesson_01_numerics import lesson_01_numerics
from .lesson_02_strings import lesson_02_strings
from .lesson_03_booleans import lesson_03_booleans


lessons: List[Lesson] = [
    lesson_00_intro,
    lesson_01_numerics,
    lesson_02_strings,
    lesson_03_booleans,
]
