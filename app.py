from flask import Flask
from flask import render_template
from datetime import time
import sqlite3
import json

# Connect to sqlite db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/bar_chart")
def chart():
    try:
        conn = sqlite3.connect('sales.db')
        cur = conn.cursor()
    except Exception as e:
        print("Error connecting to database, shutting down program: \n{}".format(e))
        exit()
    # Make list of labels for line chart
    cur.execute("SELECT MIN(listyear) FROM numsales")
    minYear = int(cur.fetchone()[0])
    cur.execute("SELECT MAX(listyear) FROM numsales")
    maxYear = int(cur.fetchone()[0])
    labels = [year for year in range(minYear, maxYear+1)]

    # Create dict of keys (property) and the corresponding data for that property group
    cur.execute("SELECT * FROM numsales")
    rows = cur.fetchall()
    dic = {}
    for row in rows:
        if not row[1]:
            row = (row[0], "None", row[2])
        if row[1] not in dic.keys():
            dic[row[1]] = [[row[2], round(row[0],2)]]
        else:
            dic[row[1]].append([row[2], row[0]])

    return render_template('bar_chart.html', mapped=dic, labels=labels, legend="Average sale price per Year")


@app.route("/line_chart")
def line_chart():
    try:
        conn = sqlite3.connect('sales.db')
        cur = conn.cursor()
    except Exception as e:
        print("Error connecting to database, shutting down program: \n{}".format(e))
        exit()
    # Make list of labels for line chart
    cur.execute("SELECT MIN(listyear) FROM avgsales")
    minYear = int(cur.fetchone()[0])
    cur.execute("SELECT MAX(listyear) FROM avgsales")
    maxYear = int(cur.fetchone()[0])
    labels = [year for year in range(minYear, maxYear+1)]

    # Create dict of keys (property) and the corresponding data for that property group
    cur.execute("SELECT * FROM avgsales")
    rows = cur.fetchall()
    dic = {}
    for row in rows:
        if not row[1]:
            row = (row[0], "None", row[2])
        if row[1] not in dic.keys():
            dic[row[1]] = [[row[2], round(row[0],2)]]
        else:
            dic[row[1]].append([row[2], round(row[0],2)])
    
    return render_template('line_chart.html', mapped=dic, labels=labels, legend="Average sale price per Year")


@app.route("/pie_chart")
def pie_chart():
    try:
        conn = sqlite3.connect('sales.db')
        cur = conn.cursor()
    except Exception as e:
        print("Error connecting to database, shutting down program: \n{}".format(e))

    # # Make list of labels for line chart
    cur.execute("SELECT MIN(listyear) FROM avgsales")
    minYear = int(cur.fetchone()[0])
    cur.execute("SELECT MAX(listyear) FROM avgsales")
    maxYear = int(cur.fetchone()[0])
    years = [year for year in range(minYear, maxYear+1)]

    # # Create dict of keys (property) and the corresponding data for that property group
    cur.execute("SELECT * FROM numsales")
    rows = cur.fetchall()
    dic = {}
    for row in rows:
        if not row[1]:
            row = (row[0], "None", row[2])
        if row[2] not in dic.keys():
            dic[row[2]] = [
                [row[1]], [row[0]]
                ]
        else:
            dic[row[2]][0].append(row[1])
            dic[row[2]][1].append(row[0])
    return render_template('pie_chart.html', mapped=dic, years=years, minYear=minYear, legend="Property Type Sale Distribution")


if __name__ == "__main__":
    app.run(debug=True)
