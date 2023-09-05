import sqlite3
from sqlite3 import Error


def execute_script(connect, script):
    cursor = connect.cursor()
    try:
        cursor.execute(script)
        connect.commit()
        print('Execute successful')
    except Error as err:
        print(f'The error "{err}" occurred')

def select_script(connect, script):
    cursor = connect.cursor()
    cursor.execute(script)
    print(cursor.fetchall()) 

# with sqlite3.connect(r'Python_Basic_diploma\database\database.db') as connect:
#     for script in create_tables.playlist():
#         execute_script(connect, script)

script = '''
select `id`, `name` from 'students' where LENGTH(`name`) > 4
'''
 
with sqlite3.connect(r'Python_Basic_diploma\database\database.db') as connect:
    # execute_script(connect, script)
    select_script(connect, script)

