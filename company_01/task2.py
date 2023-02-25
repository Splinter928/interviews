import numpy as np
import pandas as pd

# Сгенерируем данные для задачи
data = pd.DataFrame(
    np.random.randint(low=0, high=5, size=(5000000, 2)),
    columns=['prev_segment', 'new_segment']
)

# Строим таблицу сопряженности
cross_tab = pd.crosstab(data['prev_segment'], data['new_segment'],
                        rownames=[""],
                        colnames=['segment'],
                        normalize='index')

# Добавляем недостающие столбцы и строки, заполняя их нулями
cross_tab = cross_tab.reindex(columns=[0, 1, 2, 3, 4], index=[0, 1, 2, 3, 4],
                              fill_value=0)

# Форматирование для соответствия вывода образцу
cross_tab = cross_tab.applymap(lambda x: f'{x:.2f}'.rstrip('0').rstrip('.'))
print(cross_tab)
