"""Несколько простых функций"""
def multiplication(number1, number2):
    """Функция умножение двух чисел"""
    answer = number1 * number2
    return answer

def devision(multiplication, number3):
    """Деление функции multiplication"""
    dev = multiplication/number3
    return dev

print(devision(multiplication(5,8), 2))