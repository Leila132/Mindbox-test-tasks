# Mindbox-test-tasks

## Task 1
### Описание:

Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. Дополнительно к работоспособности оценим:

- Юнит-тесты
- Легкость добавления других фигур
- Вычисление площади фигуры без знания типа фигуры в compile-time
- Проверку на то, является ли треугольник прямоугольным

### Решение:

Основной файл с решением находится по пути: task_1/src/test_figures_package/main.py


Для решения использовался фабричный паттерн. Класс FigureFactory создает фигуру в зависимости от того, какой тип укажет пользователь:

```
data = {"a": 3, "b": 4, "c": 5}
figure = FigureFactory.create_figure("triangle", data)

data = {"r": 3}
figure = FigureFactory.create_figure("circle", data)
```
Для того, чтобы создать новую фигуру, нужно создать класс с новой фигурой, отнаследовавшись от класса Figure, а затем зарегистрировать его в FigureFactory:

```
class Rectangle(Figure):
        def __init__(self, data: dict):
            if "a" not in data.keys() or "b" not in data.keys():
                raise ValueError("Do not finded correct shapes")
            if not (data["a"] > 0 and data["b"] > 0):
                raise ValueError("Shapes must be greated than zero")
            self.a = data["a"]
            self.b = data["b"]

        def square(self):
            return self.a * self.b

FigureFactory.register_figure("rectangle", Rectangle)
```

Библиотека загружена на PyPI: https://pypi.org/project/test-figures-package/0.0.1/

Установить ее можно с помощью команды:

```
pip install test-figures-package
```

Или для поставки внешним клиентам можно предать файл task_1/src/dist/test_figures_package-0.0.1.tar.gz и станвить с помощью команды:
```
pip install test_figures_package-0.0.1.tar.gz
```


## Task 2
### Описание:

В PySpark приложении датафреймами(pyspark.sql.DataFrame) заданы продукты, категории и их связи. Каждому продукту может соответствовать несколько категорий или ни одной. А каждой категории может соответствовать несколько продуктов или ни одного. Напишите метод на PySpark, который в одном датафрейме вернет все пары «Имя продукта – Имя категории» и имена всех продуктов, у которых нет категорий.

### Решение:

Реализовано две функции. Первая возвращается всю таблицу с продуктами, где у продуктов без категории стоит NULL. Вторая возвращает таблицу только с продуктами, у которых найдена категория, и отдельно список названий продуктов, у которых нет категорий.
