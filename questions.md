*Список дополняется...*
## Python:

1.	Принципы DRY, KISS, SOLID.
2.	О-большое. Сложности основных алгоритмов сортировок. 
3.	Что такое компиляция и интерпретация, в чем отличие?
4.	Что означают _ и __ в имени поля класса?
5.	Что такое модуль?
6.	За что отвечает файл \_\_init__.py? 
7.	Что такое контекстный менеджер? Зачем он нужен?
8.	Что такое декоратор? Какие декораторы знаете?
9.	Асинхронность. Что такое event loop, корутина? В какой момент создается корутина? Когда начинается ожидание? Сколько потоков?
10.	В каких случаях асинхронный код может работать медленнее синхронного?
11.	В чем разница между асинхронностью и многопоточностью?
12.	Чем отличается процесс от потока? В каком случае используются потоки, а в каком процессы?
13.	Что такое состояние гонки? 
14.	Чем отличается статический метод от абстрактного? Можно ли переопределить статический метод?
15.	Чем отличается статический метод от метода класса? Зачем нужны методы класса?
16.	Что такое slots в классе, зачем он нужен?
17.	Чем отличается композиция от агрегации классов?
18.	Какие виды API существуют? (REST, gRPC)

## Django:

1.	Посчитать сумму определенного числового столбца через ORM: 
 ```python
result = MyModel.objects.aggregate(total=Sum('my_field')) 
```
2.	Как быстро вставить много элементов? 
 ```python
data = [MyModel(name='John', age=25), MyModel(name='Jane', age=30)]
MyModel.objects.bulk_create(data)
 ```
## SQL, БД:
1.	Отличие WHERE от HAVING.
2.	Отличие UNION от UNION ALL.
3.	Отличие LEFT JOIN от INNER JOIN. Что будет при отсутствии значений при использовании LEFT JOIN? Есть 2 таблицы с 1 млрд строк в каждой, сколько строк будет если сделать их INNER JOIN по произвольному полю?
4.	Что такое primary key, foreign key? Зачем нужны? Какие ограничения накладывает FK? Нужен ли FK для JOIN?
5.	Что такое атомарность? Где она встречается в БД?
6.	Что такое транзакция? Уровни изолированности, какие использовали? Виды ошибок по уровням изолированности.
7.	Открыли 2 транзакции на уровне изолированности serializable и запустили одновременно, что будет? (одна пройдет, одна упадет с ошибкой)
8.	С какими базами работали?
9.	Нормализация БД. Какие формы нормализации существуют? Для чего нужна нормализация и денормализация БД?
10.	Зачем нужны индексы? Как они работают? Какая сложность поиска с индексом и без?


## Web:
1.	Что такое HTTP, web socket?
2.	Структура HTTP запроса.
3.	Чем отличаются методы PUT и PATCH в HTTP?
4.	В чем разница между GET и POST запросами? 
5.	Какие запросы кэшируемы? (GET)
6.	Отличие TCP и UDP? Когда что лучше использовать?

## Linux:
1.	Основные команды - дерево процессов (ps aux), место на диске (df –h). 



