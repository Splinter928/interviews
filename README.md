### В этом проекте можно собрано все, что относится к собеседованиям на позицию Python разработчика:
1. [Вопросы с собеседований.](questions.md)
2. [Задачи с собеседований.](tasks.md)
3. Тестовые задания для самостоятельного выполнения:

<details><summary> Задания первой компании (каталог company_01)</summary>

### Задание №1
> SQL
>
Предположим, что у вас в базе есть табличка с балансом по всем счетам клиента на конец дня. Из-за особенностей построения таблицы, часть значений незаполнена и физически это означает отсутствие информации об изменении баланса. Для простоты будем считать, пропущенные значения для одного пользователя не могут встретиться между двумя заполненными. Напишите SQL запрос для заполнения неизвестных значений по каждому клиенту последним известным.

| client_id	  |date	|      value      |
|:-----------:|:---------:|:---------------:|
|     1	      |14.04.2020	|      10000      |
|     1	      |15.04.2020	|      5000       |
|     1	      |16.04.2020	|       NaN       |
|     1	      |17.04.2020	|       NaN       |
|     1	      |18.04.2020	|       NaN       |
|     2	      |14.04.2020	|     250000      |
|     2	      |15.04.2020	|     250000      |
|     2	      |16.04.2020	|     230000      |
|     2	      |17.04.2020	|     230000      |
|     2	      |18.04.2020	|     225000      |
|     3	      |14.04.2020	|      50000      |
|     3	      |15.04.2020	|       NaN       |
|     3	      |16.04.2020	|       NaN       |
|     3	      |17.04.2020	|       NaN       |
|     3	      |18.04.2020	|       NaN       |

> Решение: [task1.md](company_01/task1.md)
### Задание №2 
> numpy, pandas

Пусть клиенты обладают рядом статусов, закодированных цифрами: 0 - "улица", 1 - "зарплатник", 2 - "премиум", 3 - "пенсионер", 4 - "студент". У нас есть матрица с логами смен статусов за некоторый период, разверните ее в матрицу статус - статус с частотами перехода между ними.
Пример, как было:

| client_id  |	prev_segment|  new_segment   |
|:----------:|:-----------:|:--------------:|
|     1      |     0      |       1        |
|     2      |     0	   |       2        |
|     3      |     4	   |       3        |
Пример, как нужно:

|segment| 0 |  1 |2	|   3| 4   |
|:-----:|:---:|:---:|:---:|:------:|:---:|
|  0	   | 0	  | 0.5 |0.5|   0	   |  0  |
|  1	   | 0	  | 0	  |0	|   0	   |  0  |
|  2	   | 0	  | 0	  |0	|   0	   |  0  |
|  3	   | 0	  | 0	  |0	|   0	   |  0  |
|  4	   | 0	  | 0	  |0	|   1	   |  0  |

<br>В процессе выполнения задания разрешается пользоваться библиотеками numpy и pandas.
> Решение: [task2.py](company_01/task2.py)
### Задание №3. 
> pandas, sklearn

Постройте прогнозую модель для датасета с UCI Machine Learning: предобработайте категориальные фичи, отберите их, соберите схему валидации и отберите модели с помощью нее. 
Данная задача multilabel multiclass classification, поэтому предлагаю начать с одного из подходов:
Свести задачу к multilabel binary classification, как это указано в описании к датасету;
Свести задачку к binary classification тем или иным способом;
Обучить множество multiclass/binary classification моделей;
Что-то еще, что придет в голову.

<br>Датасет: https://archive.ics.uci.edu/ml/machine-learning-databases/00373/drug_consumption.data
<br>Описание датасета : https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29
> Решение: [task3.py](company_01/task3.py)
### Задание №4.
> scipy, numpy

Предположим, что мы построили рекомендательную систему, и ожидаем, что средний чек клиента вследствие этого должен вырасти. 
Мы провели AB-тест и собрали данные по контрольной и тестовой группе. 
Предложите и проведите статистический тест, который можно применить к этим данным.
> Решение: [task4.py](company_01/task4.py)
</details>

<details><summary> Задания второй компании (каталог company_02)</summary>
  
  ### Задание №1. Сетевой фонарь.
> asyncio, aiohttp, unittest
  
Требуется написать управляемый по сети фонарь. Команды управления фонарь
принимает от сервера фонаря. Предполагается, что реализация сервера уже
существует (однако недоступен вам в процессе разработки клиента фонаря). Фонарь
и сервер общаются по Протоколу Управления Фонарем (ПУФ), работающему поверх
соединения TCP.
ПУФ устроен следующим образом. Для изменения состояния фонаря сервер
передает ему команду управления. Все команды передаются в формате json вида:
  
{
"command" = text,
"metadata" = double
}
  
ПУФ версии 1 описывает три команды:  
- ON (включить фонарь),  
- OFF (выключить фонарь)  
- COLOR (сменить цвет)    
Цвет (при необходимости) кладется в поле метадата.

Реализация фонаря должна удовлетворять следующим требованиям:
1. При запуске фонарь должен запрашивать хост:порт (по умолчанию
127.0.0.1:9999), подсоединяться по TCP и после этого начать
отрабатывать протокол управления.
2. При получении данных от сервера фонарь проверяет команду,
и, если она известна, обрабатывает команду, иначе молча ее игнорирует.
3. При получении команды ON фонарь включается (отрисовку
фонаря оставляем на ваше усмотрение).
4. При получении команды OFF фонарь выключается.
5. При получении команды COLOR фонарь меняет цвет.
6. При завершении работы фонарь корректно закрывает соединение
с сервером.
7. Реализация фонаря позволяет легко добавлять любые новые команды.
Проработанность обработки исключительных ситуаций (ошибки
установления соединения, обрывы соединения) — на ваше усмотрение.  

  Технологические требования:  
1. Задание принимается в виде готового к выполнению Python-пакета.
Обязательно наличие инструкции по запуску.
2. Версия Python — 3.7+.
3. Реализация сетевого протокола может быть на aiohttp, tornado или fastAPI.
4. Репозиторий с исходниками должен быть доступен на GitHub или GitLab.
> Решение: [flashlight.py](company_02/flashlight.py)   
> Unit-tests: [tests.py](company_02/tests.py)

  ### Задание №2. Проектирование БД.
> SQL  

Спроектировать схему БД. Модель данных реляционная.

Сущности: 

1. Номенклатура (наименование, кол-во, цена)

2. Каталог номенклатуры/Дерево категорий.
Необходимо хранить данные о категориях товара, при этом сами категории могут иметь неограниченный уровень вложенности. Схема данных категорий номенклатуры должна безболезненно позволять добавлять категории любого уровня вложенности. На этапе проектирования максимальный уровень вложенности неизвестен.

3. Клиенты (наименование, адрес)

4. Заказы покупателей. Необходимо предусмотреть возможность делать заказ из разного набора товаров.

Написать следующие SQL запросы:

2.1. Получение информации о сумме товаров заказанных под каждого клиента (Наименование клиента, сумма)

2.2. Найти количество дочерних элементов первого уровня вложенности для категорий номенклатуры.
> [Решение](company_02/README.md)   
  </details>

<details><summary> Задания третьей компании (каталог company_03)</summary>

1. Есть лог web-сервиса (nginx) размером более нескольких миллионов строк (10-20 млн.).  
1.1.	Проанализируйте и запишите в БД SQL максимально быстро\эффективно.

1.2.	Сделайте с помощью SQL статистические выборки
- по частоте запросов пользователей\IP,
- по браузеру с градацией версии и т.д.,
- по кодам ответов,
- по времени отклика.

1.3. Реализуйте классификатор с возможностью самообучения и наиболее точного определения классов новых входных данных. Добейтесь максимальной точности определения > 97%.    
1.4. Реализуйте web-интерфейс с возможностью сортировки по всем колонкам и классам.      

2. Есть сеть, несколько десятков\сотен подсетей /24 и /16, с большим количеством хостов – более 10000.
Необходимо найти дубликаты открытых SSH ключей, учитывая, что порты могут отличаться от 22.
Реализовать оповещения об изменении открытых ключей для хостов.
Проверки желательно выполнять несколько раз в сутки (2-8 раз).

</details>
