import numpy as np

a = np.arange(12).reshape(3, 4)

b = np.arange(16).reshape(4, 4)

#  Файл сохранится в той же папке что и исполняемый скрипт
np.save('example_1', a)
#  Файл будет сохранен в папке example


c = np.load('example_1.npy')
print(c)