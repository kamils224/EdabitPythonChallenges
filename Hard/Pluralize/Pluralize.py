from collections import Counter
from typing import List, Set


# task: https://edabit.com/challenge/LR98GCwLGYPSv8Afb

def pluralize(items: List[str]) -> Set[str]:
    counter = Counter(items)
    result = set()
    for item, value in counter.items():
        result.add(f'{item}s') if value > 1 else result.add(item)
    return result


if __name__ == '__main__':
    pass
