def simpson_integration(f, a, b, n):
    """
    Принимает функцию f, нижний и верхний пределы a и b, и количество интервалов n.
    Возвращает приближенное значение определенного интеграла функции f на интервале [a, b] методом Симпсона.
    """
    # Вычисляем шаг интервала
    h = (b - a) / n

    # Считаем сумму значений функции в точках x_i = a + i*h для i = 0, 1, ..., n
    sum_1 = sum(f(a + i*h) for i in range(1, n, 2))  # Сумма значений в нечётных точках
    sum_2 = sum(f(a + i*h) for i in range(2, n, 2))  # Сумма значений в чётных точках

    # Вычисляем приближенное значение интеграла методом Симпсона
    integral = (1/3) * h * (f(a) + 4*sum_1 + 2*sum_2 + f(b))

    return integral

def f(x):
    return x  # Функция, которую мы будем интегрировать

a = 0.5  # Нижний предел интегрирования
b = 1  # Верхний предел интегрирования
n = 5  # Количество интервалов

integral = simpson_integration(f, a, b, n)

print("Приближенное значение интеграла:", integral)