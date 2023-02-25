import numpy as np
from scipy.stats import ttest_ind

# Сгенерируем данные для задачи
control = np.random.lognormal(mean=5, sigma=2, size=(100000,))
test = np.random.lognormal(mean=5.02, sigma=2, size=(100000,))

# Двухвыборочный t-тест
# Предполагаем, что распределение средних чеков в каждой группе нормальное.
# Вычисляем t-статистику и p-value (уровень значимости).
t_stat, p_value = ttest_ind(test, control, equal_var=False)

# Задаем уровень значимости
alpha = 0.05

# Выводим результаты теста
if p_value < alpha:
    print("Наблюдаем значимые различия между средними чеками контрольной и тестовой групп.")
else:
    print("Не наблюдаем значимых различий между средними чеками контрольной и тестовой групп.")