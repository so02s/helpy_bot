import sys

def function1(arg1_name, arg2_name):
    print(f"Function1 called with arg1: {arg1_name}, arg2: {arg2_name}")

def function2(arg1_name, arg3_name):
    print(f"Function2 called with arg1: {arg1_name}, arg3: {arg3_name}")


# Получаем текущий модуль
current_module = sys.modules[__name__]

# Получаем все атрибуты текущего модуля
all_attributes = dir(current_module)

# Выводим все атрибуты
print(all_attributes)