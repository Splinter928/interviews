### Реализуйте web-интерфейс с возможностью сортировки по всем колонкам и классам.

Для реализации web-интерфейса с возможностью сортировки по всем колонкам и классам используем фреймворк Django.  
 - Для передачи параметров "class" и "sort" в GET запросе в Django можно использовать объект __request.GET__, который представляет словарь всех переданных параметров. 
 Код функции представления:
```python
# views.py
from django.shortcuts import render

def my_view(request):
    my_class = request.GET.get('class')
    my_sort = request.GET.get('sort')
    
    # Здесь можно добавить логику для сортировки и фильтрации данных.
    # В данном примере параметры просто передаем дальше в шаблон.
    
    return render(request, 'my_template.html', {'class': my_class, 'sort': my_sort})
```
- В шаблоне __my_template.html__ можно использовать значения параметров для установки соответствующих классов CSS и для отображения отсортированных данных.
Например, для установки класса CSS в таблице можно использовать следующий код:
```html
<table class="table table-striped">
  <thead>
    <tr>
      <th><a href="?class=column1&sort={{ sort }}">Column 1</a></th>
      <th><a href="?class=column2&sort={{ sort }}">Column 2</a></th>
      <th><a href="?class=column3&sort={{ sort }}">Column 3</a></th>
    </tr>
  </thead>
```
- Для сортировки данных в шаблоне можно использовать фильтры Django, например, __order_by__:
 ```html
 {% for row in data.order_by(sort) %}
<tr>
  <td>{{ row.column1 }}</td>
  <td>{{ row.column2 }}</td>
  <td>{{ row.column3 }}</td>
</tr>
{% endfor %}
```
