# This is coded in Visual studio

import mysql.connector
import pymysql
import numpy as np

db = mysql.connector.connect(user='root', password='Your_Mysql_Password', host='127.0.0.1',port=3306, database='mydb')

# Below code is to get the names of the columns
mycursor = db.cursor()
mycursor.execute('SHOW columns FROM employees;')
columnNames = mycursor.fetchall()


# Below code is to get the rows of the data
mycursor2 = db.cursor()
mycursor2.execute('select * from employees')
allObjs = mycursor2.fetchall()


data = []
allColumnNames = []



for i in columnNames:
    allColumnNames.append(i[0])

for i in allObjs:
    obj = {
        allColumnNames[0]: i[0],
        allColumnNames[1]: i[1],
        allColumnNames[2]: i[2],
        allColumnNames[3]: i[3],
        allColumnNames[4]: i[4],
        allColumnNames[5]: i[5],
        allColumnNames[6]: i[6],
        allColumnNames[7]: i[7],
        allColumnNames[8]: i[8],
        allColumnNames[9]: i[9],
    }
    data.append(obj)

arr = np.array(data)

# Reason to slice the array, as in promt, we are not able to send the huge data, as we are using the FREE version of chat garq
newData = arr[1:3]
mycursor.close()
db.close()


from langchain_groq import ChatGroq

llm = ChatGroq(
    model="mixtral-8x7b-32768",
    groq_api_key='Your_Char_garq_Api_key',
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("""
Below is the employees data
{newData}

Whats the salary of the jennifer, please just say in 5 words
""")


chain_extract = prompt | llm
res = chain_extract.invoke(input={'newData':newData})
print('Result', res.content)
























