# Задача 2. Содержимое

import os

user_path = os.path.join('c:', os.path.sep, 'windows')

print('Содержимое каталога C:', user_path)

for element in os.listdir(user_path):
    print(os.path.join(user_path, element))
