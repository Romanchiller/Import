from application import salary as s
from application.db import people as p
import videoxt
import datetime
if __name__ == '__main__':
    s.calculate_salary()
    p.get_employees()
    today = datetime.date.today()

    print(today)






