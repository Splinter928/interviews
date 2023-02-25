import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score

# Загрузка данных из файла
data = pd.read_csv('drug_consumption.data', header=None, index_col=0)

# Назначение имен столбцов
data.columns = ['Age', 'Gender', 'Education', 'Country', 'Ethnicity', 'Neuroticism', 'Extraversion', 'Openness',
              'Agreeableness', 'Conscientiousness', 'Impulsive', 'SS', 'Alcohol', 'Amphet', 'Amyl', 'Benzos', 'Caff',
              'Cannabis', 'Choc', 'Coke', 'Crack', 'Ecstasy', 'Heroin', 'Ketamine', 'Legalh', 'LSD', 'Meth',
              'Mushrooms', 'Nicotine', 'Semer', 'VSA']

# Сводим классификацию потребителей наркотиков к бинарной числовой.
# Определим тех кто не пробовал и пробовал больше 10 лет назад как не потребителей (0), а остальных как потребителей (1)
data = data.replace({
    'CL0': 0, 'CL1': 0,
    'CL2': 1, 'CL3': 1, 'CL4': 1, 'CL5': 1, 'CL6': 1, 'CL7': 1,
})

# Признаки "Gender", "Education", "Country" можно считать категориальными, потому что они имеют небольшое конечное число
# уникальных значений на весь датасет (2, 8 и 29 соотвественно). Преобразуем их в числовые с помощью LabelEncoder().
categorical_columns = ["Gender", "Education", "Country"]
for column in categorical_columns:
    encoder = LabelEncoder()
    data[column] = encoder.fit_transform(data[column])

# Отбор признаков.
# Возраст, пол, образование, личностные характеристики и показатели импульсивности вполне представительны.
features = ['Age', 'Gender', 'Education', 'Neuroticism', 'Extraversion', 'Openness', 'Agreeableness',
            'Conscientiousness', 'Impulsive', 'SS']

# Выбираем количество наркотиков для оценки (max=19)
drugs = 19
# словарь для оценки точности моделей
accuracy = {}
# Разделение данных на обучающую и тестовую выборки
X = data[features]
for drug in data.columns[31 - drugs:]:
    y = data[drug]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Создание моделей
    rf = RandomForestClassifier(random_state=42)
    lr = LogisticRegression(random_state=42)
    knn = KNeighborsClassifier(n_neighbors=5)
    gb = GradientBoostingClassifier(random_state=42)

    # Схема валидации: пятикратная кросс-валидация
    scores_rf = cross_val_score(rf, X_train, y_train, cv=5)
    scores_lr = cross_val_score(lr, X_train, y_train, cv=5)
    scores_knn = cross_val_score(knn, X_train, y_train, cv=5)
    scores_gb = cross_val_score(gb, X_train, y_train, cv=5)

    # Оценка точности на тренирочной выборке
    accuracy['acc_rf_train'] = accuracy.get('acc_rf_train', 0) + scores_rf.mean()
    accuracy['acc_lr_train'] = accuracy.get('acc_lr_train', 0) + scores_lr.mean()
    accuracy['acc_knn_train'] = accuracy.get('acc_knn_train', 0) + scores_knn.mean()
    accuracy['acc_gb_train'] = accuracy.get('acc_gb_train', 0) + scores_gb.mean()

    # Обучение моделей
    rf.fit(X_train, y_train)
    lr.fit(X_train, y_train)
    knn.fit(X_train, y_train)
    gb.fit(X_train, y_train)

    # Предсказания на тестовой выборке
    y_pred_rf = rf.predict(X_test)
    y_pred_lr = lr.predict(X_test)
    y_pred_knn = knn.predict(X_test)
    y_pred_gb = gb.predict(X_test)

    # Оценка точности на тестовой выборке
    accuracy['acc_rf_test'] = accuracy.get('acc_rf_test', 0) + accuracy_score(y_test, y_pred_rf)
    accuracy['acc_lr_test'] = accuracy.get('acc_lr_test', 0) + accuracy_score(y_test, y_pred_lr)
    accuracy['acc_knn_test'] = accuracy.get('acc_knn_test', 0) + accuracy_score(y_test, y_pred_knn)
    accuracy['acc_gb_test'] = accuracy.get('acc_gb_test', 0) + accuracy_score(y_test, y_pred_gb)


print(f"Accuracy (Random Forest): train={accuracy['acc_rf_train']/drugs:.3f}, test={accuracy['acc_rf_test']/drugs:.3f}.")
print(f"Accuracy (Logistic Regression): train={accuracy['acc_lr_train']/drugs:.3f}, test={accuracy['acc_lr_test']/drugs:.3f}.")
print(f"Accuracy (KNN): train={accuracy['acc_knn_train']/drugs:.3f}, test={accuracy['acc_knn_test']/drugs:.3f}.")
print(f"Accuracy (Gradient Boosting): train={accuracy['acc_gb_train']/drugs:.3f}, test={accuracy['acc_gb_test']/drugs:.3f}.")

# Наилучший результат получен при использовании Логистической регрессии.