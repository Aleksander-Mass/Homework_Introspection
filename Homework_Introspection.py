def introspection_info(obj):
    # Получаем информацию о типе объекта
    obj_type = type(obj)
    obj_type_name = obj_type.__name__

    # Модуль, к которому объект принадлежит
    obj_module = obj_type.__module__

    # Получаем список всех атрибутов и методов
    all_attributes = dir(obj)

    # Фильтруем методы и атрибуты
    attributes = [attr for attr in all_attributes if not callable(getattr(obj, attr))]
    methods = [method for method in all_attributes if callable(getattr(obj, method))]

    # Формируем итоговый словарь с информацией
    introspection_result = {
        'type': obj_type_name,
        'module': obj_module,
        'attributes': attributes,
        'methods': methods,
    }

    return introspection_result

# Тестирование функции
# Для лучшего понимания создадим свой класс, объект которого передадим в функцию для анализа.

# Пример пользовательского класса
class MyClass:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

    def display(self):
        print(self.value)

# Создаем объект класса MyClass
my_object = MyClass(42)

# Вызываем функцию introspection_info и печатаем результат
object_info = introspection_info(my_object)
print(object_info)

# Вывод на консоль:
"""
{'type': 'MyClass', 'module': '__main__', 'attributes': ['__dict__', '__doc__', '__module__', '__weakref__', 'value'], 
 'methods': ['__class__', '__delattr__', '__dir__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', 
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'display', 'increment']}

"""