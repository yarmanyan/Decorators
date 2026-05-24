


from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
from decorators import logger  # импортируем декоратор

if __name__ == '__main__':
    # Применяем декоратор с разными путями для разных модулей
    logged_calculate_salary = logger('logs/salary.log')(calculate_salary)
    logged_get_employees = logger('logs/people.log')(get_employees)

    print(logged_calculate_salary())
    print(logged_get_employees())

    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d")
    print(f'Текущая дата: {formatted_datetime}')


