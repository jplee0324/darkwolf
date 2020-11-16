import pandas as pd
import sqlite3
import json

try:
    with open('rows.json') as f:  
        print("READING IN rows.json")
        rawdata = json.loads(f.read())
        cols = [col["fieldName"].strip(":") for col in rawdata["meta"]["view"]["columns"]]
        print("CREATING DATAFRAME")
        df = pd.DataFrame(rawdata["data"], columns = cols)
        df = df[['sid','saleamount','propertytype','listyear']]
except Exception as e:
    print("Error reading in json file : {}".format(e))
    exit()


try:
    print("CONNECTING TO DATABASE")
    conn = sqlite3.connect('sales.db')
    df.to_sql("salesdata", conn, if_exists="replace")
    print("DATA INSERTED INTO sales.salesdata")
    print("CLOSING CONNECTION")
    conn.close()
except Exception as e:
    print("Error with database : {}".format(e))
    exit()
