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
from .lesson_08_tuples import lesson_08_tuples
from .lesson_09_dicts import lesson_09_dicts
from .lesson_10_conditionals import lesson_10_conditionals
from .lesson_11_loops import lesson_11_loops
from .lesson_12_functions import lesson_12_functions
from .lesson_13_classes import lesson_13_classes


lessons: List[Lesson] = [
    lesson_00_intro,
    lesson_01_numerics,
    lesson_02_strings,
    lesson_03_booleans,
    lesson_04_arithmetic_ops,
    lesson_05_relational_ops,
    lesson_06_logical_ops,
    lesson_07_lists,
    lesson_08_tuples,
    lesson_09_dicts,
    lesson_10_conditionals,
    lesson_11_loops,
    lesson_12_functions,
    lesson_13_classes,
]
