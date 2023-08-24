from typing import List
from ..models.lesson import Lesson

from .lesson_00_intro import lesson_00_intro
from .lesson_01_numerics import lesson_01_numerics
from .lesson_02_strings import lesson_02_strings
from .lesson_03_booleans import lesson_03_booleans
from .lesson_04_arithmetic_ops import lesson_04_arithmetic_ops
from .lesson_05_relational_ops import lesson_05_relational_ops
from .lesson_06_logical_ops import lesson_06_logical_ops
from .lesson_07_lists import lesson_07_lists


lessons: List[Lesson] = [
    lesson_00_intro,
    lesson_01_numerics,
    lesson_02_strings,
    lesson_03_booleans,
    lesson_04_arithmetic_ops,
    lesson_05_relational_ops,
    lesson_06_logical_ops,
    lesson_07_lists,
]
