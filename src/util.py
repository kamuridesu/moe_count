import os
from config import MAX_DIGITS


def imageBuilder(number: int) -> list[str]:
    numbers_str = str(number)
    file_path = "./media"
    if len(numbers_str) > MAX_DIGITS:
        numbers_str = "9" * MAX_DIGITS
    while len(numbers_str) < MAX_DIGITS:
        numbers_str = "0" + numbers_str
    numbers_path = []
    for number in numbers_str:
        for file in os.listdir(file_path):
            if file.startswith(number):
                numbers_path.append(os.path.join(file_path, file))
    return numbers_path


if __name__ == '__main__':
    print(imageBuilder(123))
