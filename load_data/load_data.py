import mysql.connector
import csv
import sqlalchemy
import json
# connect to the database

# function to insert people data
def load_people(conn):
    print("loading people data")
    with open('./people.csv', encoding="utf8") as csv_file:
        try:
            csv_reader = csv.reader(csv_file, delimiter=',')
            conn.execute("truncate table codetest.people") #truncating table so that any previously inserted data is removed and we get correct results, can be removed if data already exists
            next(csv_reader)
            i = 1
            for row in csv_reader:
                #print("inserting row",i, flush=True)
                try:
                    conn.execute('INSERT INTO codetest.people(GIVEN_NAME, \
                            FAMILY_NAME, DATE_OF_BIRTH, PLACE_OF_BIRTH )' \
                            'VALUES("%s", "%s", %s, "%s")', 
                            row)
                except Exception as e:
                    print("unable to insert row:", e)
                i = i+1
        except:
            print("file not found")

# function to insert places data
def load_places(conn):
    print("loading places data")
    try:
        with open('./places.csv', encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            conn.execute("truncate table codetest.places") #truncating table so that any previously inserted data is removed and we get correct results, can be removed if data already exists
            next(csv_reader)
            print(csv_reader)
            i = 1
            for row in csv_reader:
                #print("inserting row",i, flush=True)
                try:
                    conn.execute('INSERT INTO codetest.places(CITY, \
                            COUNTY, COUNTRY)' \
                            'VALUES("%s", "%s", "%s")', 
                            row)
                except Exception as e:
                    print("unable to insert row:", e)
                i = i+1
    except:
        print("file not found")


try:
    engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")
    connection = engine.connect()

    metadata = sqlalchemy.schema.MetaData(engine)
    print(metadata)
    load_places(connection)
    load_people(connection)
    #write_output(connection)
    print("data has been loaded, please wait for the query results to be displayed")
except Exception as e:
    print("failed to connect",e)

