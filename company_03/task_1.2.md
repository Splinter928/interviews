### Сделайте с помощью SQL статистические выборки.  
Запросы сделаны для таблицы logs, следующего вида:
| id  | ip  | browser_name | browser_ver | status | response_time |
|-----|-----|--------------|-------------|--------|---------------|
- по частоте запросов пользователей\IP,
```sql
SELECT 
  ip, 
  COUNT(*) as requests_count 
FROM logs 
GROUP BY ip
ORDER BY requests_count DESC;
```
- по браузеру с градацией версии и т.д.,
```sql
SELECT 
  browser_name, 
  browser_version, 
  COUNT(*) as requests_count 
FROM logs
GROUP BY browser_name, browser_version 
ORDER BY requests_count DESC;
```
- по кодам ответов,
```sql
SELECT 
  status, 
  COUNT(*) as requests_count 
FROM logs
GROUP BY status 
ORDER BY requests_count DESC;
```
- по времени отклика.
```sql
SELECT 
  response_time, 
  COUNT(*) as requests_count 
FROM logs
GROUP BY response_time
ORDER BY response_time;
```
