import mysql.connector
from opencart_automation.utils.json_reader import read_json
from opencart_automation.utils.csv_reader import read_csv

creds = read_json('db_creds.json')
db = mysql.connector.connect(
    host=creds['host'],
    user=creds['user'],
    password=creds['password'],
    database=creds['database']
)

cursor = db.cursor()
def insert_data_sql(query,data:list):
    try:
        cursor.executemany(query,data)
        print('Query executed successfully!!')
    except Exception as e:
        print(e.with_traceback())
    cursor.close()

def select_data_sql(query):
    try:
        cursor.execute(query)
        print('Query executed successfully!!')
    except Exception as e:
        print(e.with_traceback())
    cursor.close()


# for unit testing
categories = ['All Categories', 'Desktops', 'PC', 'Mac', 'Laptops & Notebooks', 'Macs', 'Windows', 'Components',
              'Mice and Trackballs', 'Monitors', 'test 1', 'test 2', 'Printers', 'Scanners', 'Web Cameras',
              'Tablets', 'Software', 'Phones & PDAs', 'Cameras', 'MP3 Players', 'test 11', 'test 12',
              'test 15', 'test 16', 'test 17', 'test 18', 'test 19', 'test 20', 'test 25', 'test 21',
              'test 22', 'test 23', 'test 24', 'test 4', 'test 5', 'test 6', 'test 7', 'test 8', 'test 9']
query = '''
insert into product_categories(category) values(%s);
'''
insert_data_sql(query,data=categories)


