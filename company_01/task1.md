# Название таблицы примем за balance

Заполнение таблицы, если между двумя заполненными значениями для одного пользователя не встречаются незаполненные
1) Вариант с обновлением исходной таблицы:
 ```sql
UPDATE balance t
SET value = (
    SELECT subq.value
    FROM (
        SELECT value, date
        FROM balance
        WHERE client_id = t.client_id AND value IS NOT NULL
        ORDER BY date DESC
        LIMIT 1
    ) subq
    WHERE t.date > subq.date
)
WHERE value IS NULL;
 ```
2) Вариант SELECT запроса с заполнением:
 ```sql
WITH cte1 as (
    SELECT subq.* FROM (
        SELECT bal.*,
        ROW_NUMBER() OVER(PARTITION BY client_id ORDER_BY date DESC) as rn
        FROM balance bal
        WHERE value IS NOT NULL
    ) subq
    WHERE subq.rn = 1
)
SELECT
  bal.client_id,
  bal.date,
  COALESCE(bal.value, cte1.value) as value
FROM balance bal
LEFT JOIN cte1 on bal.client_id = cte1.client_id
 ```
3) Заполнение таблицы, если между двумя заполненными значениями для одного пользователя встречаются незаполненные
 ```sql
UPDATE balance t1
SET value = COALESCE(t1.value, (
    SELECT t2.value
    FROM balance t2
    WHERE t2.client_id = t1.client_id
        AND t2.date < t1.date
        AND t2.value IS NOT NULL
    ORDER BY t2.date DESC
    LIMIT 1
));
 ```