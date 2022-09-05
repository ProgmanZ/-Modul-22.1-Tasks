# Задача 3. Корень диска

import os


def disk(path):
    result = os.path.abspath(path)
    result = result.strip(os.sep)[:2]
    return result


user_path = os.path.join(os.sep)
print(disk(user_path))

