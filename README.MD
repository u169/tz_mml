### Тестовое задание

##### Запуск
```bash
python3 app.py
```

##### Подход к решению задачи
Процесс получения данных и оценки важности критериев не был указан в ТЗ.  
Поэтому создал более гибкую систему в ущерб простоты.  

###### Сырые части (TODO)
_src.params.data_: написать процесс получения данных по вариантам заправок  
_coefficients.json_: подобрать коэффициенты критериев по заправкам

###### Процесс
1. Получаем данные по заправкам
2. По каждой заправке считаем профит
    - перемножаем пары коэф - критерий заправки
    - берем среднеарифметическое произведений
3. Выбираем из полученных среднеарифметических профитов- максимальный


##### Почему не написал более конкретный алгоритм
Т.к. я не совсем понимаю, что важнее:  
- быстрее заправиться
- заплатить меньше
- потратить меньше бензина
- и т.д.  

то решил использовать подход с коэффициентами критериев  

Плюсы коэффициентов:
- могут быть отрицательными
- нормализация критериев


### TODO
Написать тесты (использую __pytest__)

### P.S.
Очень буду признателен фидбеку по реализации данной задачи  
Спасибо