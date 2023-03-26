import os
from .config import MAX_DIGITS


def imageBuilder(number: int) -> list[str]:
    numbers_str = str(number).zfill(MAX_DIGITS)
    file_path = "./static/images"
    numbers_path = []
    for n in numbers_str:
        numbers_path.append(os.path.join(file_path, n + ".svg"))
    return numbers_path


if __name__ == '__main__':
    print(imageBuilder(123))
