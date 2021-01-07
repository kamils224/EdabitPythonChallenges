from typing import List

# Task: https://edabit.com/challenge/3A3mHS5B3NNZddQL2


class QuestionsDifficulty:
    VERY_EASY = 5
    EASY = 10
    MEDIUM = 15
    HARD = 20


questions = [
    QuestionsDifficulty.VERY_EASY,
    QuestionsDifficulty.VERY_EASY,
    QuestionsDifficulty.EASY,
    QuestionsDifficulty.EASY,
    QuestionsDifficulty.MEDIUM,
    QuestionsDifficulty.MEDIUM,
    QuestionsDifficulty.HARD,
    QuestionsDifficulty.HARD,
]


def interview(lst: List[int], tot: int) -> str:
    time_limit = 120
    fail = "disqualified"
    success = "qualified"
    if tot > time_limit or len(lst) != len(questions):
        return fail
    correct = [a for q, a in zip(questions, lst) if a <= q]
    if len(correct) != len(questions):
        return fail
    return success
