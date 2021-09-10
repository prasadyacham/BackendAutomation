import sqlite3
import pandas as pd

conn =  sqlite3.connect('week1.db')
c = conn.cursor()
read_emp = pd.read_csv(r'emp.csv')
read_emp.to_sql('emp', conn, if_exists='append', index = False) # Insert the values from the csv file into the table 'emp'

read_dept = pd.read_csv(r'dept.csv')
read_dept.to_sql('dept', conn, if_exists='append', index = False) # Insert the values from the csv file into the table 'dept'

#Example 1
for row in c.execute('''
select * from emp
'''):
    print(row)

colnames = c.description
for row in colnames:
    print(row[0])

# Example 2
c.execute('''
select * from emp
''')

df = pd.DataFrame(c.fetchall(), columns=['EMPNO',
'ENAME',
'JOB',
'MGR',
'HIREDATE',
'SAL',
'COMM',
'DEPTNO'])
print(df)
