import psycopg2
from datetime import datetime

now = datetime.now().date()

DB_URL = 'postgresql://postgres:qwerty@localhost:5767/postgres'
conn = psycopg2.connect(DB_URL)

departments = [('bookkeeping',), ('sale_department',), ('complaint_department',)]
employees = [('Иванов Иван Иванович', 'главный бухгалтер', 'bookkeeping'),
             ('Селиверстова Анжелика Михайловна', 'бухгалтер', 'bookkeeping'),
             ('Михайлов Михаил Михайлович', 'Старший менеджер', 'sale_department'),
             ('Никитюк Никита Сергеевич', ' менеджер', 'sale_department'),
             ('Липенко Юлия Антоновна', 'менеджер', 'sale_department'),
             ('Огонь Надежда Павловна', 'управляющий отделом жалоб', 'complaint_department'),
             ('Розанова Жанна Аркадьевна', 'стажер', 'complaint_department')]
orders = [(now, 'sale', 'покупка анализатора', 847654, 'Михайлов Михаил Михайлович'),
          (now, 'service case', 'ТО через 1 год после покупки', 46322, 'Огонь Надежда Павловна'),
          (now, 'repair', 'аппарат не включается', 322145, 'Огонь Надежда Павловна'),
          (now, 'replacement detail', 'замена детали после поломки', 987600, 'Селиверстова Анжелика Михайловна'),
          (now, 'call', 'плановый звонок клиенту', 908543, 'Никитюк Никита Сергеевич')]


INSERT_QUERY_DEPARTMENTS = """INSERT INTO departments (department_name) VALUES ('%s')"""
INSERT_QUERY_EMPLOYEES = """INSERT INTO employees (fio, position, department_id) VALUES ('%s', '%s', (SELECT 
department_id FROM departments WHERE department_name = '%s')) """
INSERT_QUERY_ORDERS = f"""INSERT INTO orders (created_dt, order_type, description, serial_no, creator_id) VALUES (
'%s','%s', '%s', '%d', (SELECT employee_id FROM employees WHERE fio = '%s'))"""

SELECT_QUERY_ORDERS = """SELECT * FROM orders WHERE creator_id = '%d' AND created_dt = '%s' AND status = '%s'"""
SELECT_QUERY_EMPLOYEES = """SELECT e.fio, d.department_name FROM employees e, departments d WHERE e.department_id = 
d.department_id """
SELECT_QUERY_STATUS = """SELECT created_dt, COUNT(*) FROM orders WHERE status = '%s' GROUP BY created_dt"""
SELECT_QUERY_CREATOR_ORDERS = """SELECT o.order_id, e.fio FROM orders o, employees e WHERE o.creator_id = 
e.employee_id """


with conn.cursor() as cursor:
    cursor.execute("""CREATE TABLE IF NOT EXISTS departments (
    department_id SERIAL primary key,
    department_name TEXT NOT NULL
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
    employee_id SERIAL primary key,
    fio TEXT NOT NULL,
    position TEXT NOT NULL,
    department_id INTEGER REFERENCES departments (department_id)
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL primary key,
    created_dt DATE NOT NULL,
    updated_dt DATE,
    order_type TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT default ('ожидает рассмотрения'),
    serial_no INTEGER NOT NULL,
    creator_id INTEGER REFERENCES employees (employee_id)
    )""")
    for i in range(len(departments)):
        cursor.execute(INSERT_QUERY_DEPARTMENTS % (departments[i]))
    for i in range(len(employees)):
        cursor.execute(INSERT_QUERY_EMPLOYEES % (employees[i]))
    for i in range(len(orders)):
        name = orders[i][4]
        cursor.execute(INSERT_QUERY_ORDERS % (orders[i]))
    conn.commit()

with conn.cursor() as cursor:
    cursor.execute(SELECT_QUERY_ORDERS % (6, now, 'ожидает рассмотрения'))
    cursor.execute(SELECT_QUERY_EMPLOYEES)
    cursor.execute(SELECT_QUERY_STATUS % 'ожидает рассмотрения')
    cursor.execute(SELECT_QUERY_CREATOR_ORDERS)

    data = cursor.fetchall()
    conn.commit()
    print(data)
