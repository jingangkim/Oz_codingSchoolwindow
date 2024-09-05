import pymysql
import random

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password':'@Ab1480718',
    'database': 'mydb',    
}

batch_size = 100000
total_records = 320000000

connection = pymysql.connect(**db_config) #별표 두개로 db_config을 풀어헤친다 라고 생각하면 됨
cursor = connection.cursor()

insert_with_index = "INSERT INTO books_with_index (call_number) VALUES (%s)"
insert_without_index = "INSERT INTO books_with_index (call_number) VALUES (%s)"

for i in range(0, total_records, batch_size):
    batch = [(random.randint(0, 999),) for _ in range(batch_size)]
    
    cursor.executemany(insert_with_index, batch)
    cursor.executemany(insert_without_index, batch)
    print(f"{i//batch_size + 1}'번째 배치 삽입'")
    
    
print('배치 완료')
