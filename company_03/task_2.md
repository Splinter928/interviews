•	Собрать список всех открытых SSH ключей на всех хостах в сети. Для этого можно воспользоваться утилитами типа ssh-keyscan или nmap.  
•	Удалить дубликаты из списка ключей, оставив только уникальные. Для этого можно использовать утилиты linux типа sort и uniq или сравнение хеш сумм 
(алгоритм хеширования например sha256)  
•	Сохранить список ключей в БД/файл и периодически проверять изменения в открытых ключах на хостах. В случае изменений  добавить 
оповещение на почту пользователя (например используя smtplib)  

```python
import ssh_keyscan
import hashlib
import time

# Функция для получения открытых ключей хостов
def get_ssh_keys(hosts):
    keys = []
    for host in hosts:
        ssh_keyscan.scan(host) # Использование утилиты ssh-keyscan для получения ключей
        keys += ssh_keyscan.get_keys()
    return keys

# Функция для удаления дубликатов ключей
def remove_duplicates(keys):
    unique_keys = []
    hash_keys = set()
    for key in keys:
        key_hash = hashlib.sha256(key.encode()).hexdigest() # Получение хеш-суммы ключа
        if key_hash not in hash_keys:
            unique_keys.append(key)
            hash_keys.add(key_hash)
    return unique_keys

# Функция для отправки уведомления об изменениях (можно реализовать, используя smtplib)
def send_notification(changes):
  pass

# Основной цикл проверки ключей
previous_keys = []
while True:
    current_keys = remove_duplicates(get_ssh_keys(hosts))
    if current_keys != previous_keys:
        changes = set(current_keys) - set(previous_keys)
        send_notification(changes)
        previous_keys = current_keys
    time.sleep(3600*3) # Проверка каждые 3 часа
```
