from typing import List

# Task: https://edabit.com/challenge/FmowTJecDKQMRqsHS

def get_direction_table() -> List[List[int]]:
    return [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1)
    ]

def crop_hydrated(fields: List[List[str]]) -> bool:
    row_len = len(fields[0])
    col_len = len(fields)

    if any(len(row) != row_len for row in fields):
        raise ValueError()

    crop = 'c'
    water = 'w'
    if all(crop in single_field for row in fields for single_field in row):
        return False    # there is no water field
    
    crop_positions = [(i,j) for i, row in enumerate(fields) for j, single_field in enumerate(row) if crop == single_field]
    
    direction_table = get_direction_table()

    crop_areas = []

    for crop in crop_positions:
        search_positions = [tuple(map(sum, zip(crop, direction))) for direction in direction_table]
        crop_areas.append([pos for pos in search_positions if 0 <= pos[0] < col_len and 0 <= pos[1] < row_len])
        if len(search_positions) == 0:
            continue
    
    for crop, area in zip(crop_positions, crop_areas):
        print(crop)
        print(area)

    for crop_area in crop_areas:
        if not any(water == fields[point[0]][point[1]] for point in crop_area):
            #print(crop_area)
            return False

    return True

example = [
        [ "c", "w", "c", "c", "w", "w" ],
        [ "c", "c", "w", "c", "c", "c" ],
        [ "w", "c", "c", "c", "c", "w" ],
        [ "c", "w", "c", "c", "c", "c" ],
        [ "c", "c", "c", "c", "w", "w" ]
]

if __name__ == "__main__":
    result = crop_hydrated(example)
    print(result)