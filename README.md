# Dark Wolf Solutions Coding Assignment

My code implementation uses the following python libraries which will need to be installed before running the code:

<ol>
<li> pandas (for data processing script)</li>
<li> flask (for web app)</li>
</ol>

install with command: 
    <code>pip install [library name]</code>

To run the application, type "python app.py" and go to http://127.0.0.1:5000/ to view it

This project uses Flask as the backend in order to route the data from the sqlite3 database to the html templates, and Chart.js for the actual data visualizations.

The SQLite3 database has the schema <code>(id, saleamount, propertytype, listyear)</code> and stores all of the filtered property sales available in rows.json. Two views were built on top of this database to preprocess the data so it could be more easily visualized. These views were called avgsales and numsales and can be seen in /Data Processing/create.sql







 
