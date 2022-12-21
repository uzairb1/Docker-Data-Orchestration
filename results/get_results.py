import mysql.connector
import json
import sqlalchemy
import os

print(os.path.isdir('./data'))

try:
    engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")
    connection = engine.connect()

    metadata = sqlalchemy.schema.MetaData(engine)
    print(metadata)
    query = "select b.COUNTRY as Country, count(a.GIVEN_NAME) as Count_People_In_Country from people a, places b where a.PLACE_OF_BIRTH = b.CITY group by b.COUNTRY"

    try:
        with open('./data/summary_output.json', 'w') as json_file:
            rows = connection.execute(query).fetchall()
            print(rows)
            rows = [{'id': row[0], 'name': row[1]} for row in rows]
            json.dump(rows, json_file, separators=(',', ':'))
    except Exception as e:
        print("cannot write: ",e)
except Exception as e:
    print("failed to connect",e)

try:
    with open("./data/summary_output.json",'r') as fd:
        line = fd.readlines()
        print(line)
except:
    print("file not found")