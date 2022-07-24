from datetime import datetime

from application.db import people

from application import salary

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print(datetime.now())
