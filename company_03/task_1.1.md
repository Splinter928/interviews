### Есть лог web-сервиса (nginx) размером более нескольких миллионов строк (10-20 млн.).Проанализируйте и запишите в БД SQL максимально быстро\эффективно.  
Существует несколько способов оптимизировать запись больших объемов данных в БД, вот некоторые из них:  
•	Использовать пакетную вставку (bulk insert) для загрузки пакета данных за одно подключение к БД.  
•	Удалить индексы из таблицы, а после окончания записи вернуть, чтобы избежать пересчета индексов в процессе записи данных.  
•	Удалить внешние ключи, а после окончания записи вернуть, чтобы избежать проверок ссылочной целостности по ним в процессе записи.  
•	и т.д.  