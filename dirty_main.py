from application.salary import *
from application.db.people import *
import datetime

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.datetime.today().strftime('%d/%m/%Y'))