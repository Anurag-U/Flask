from tokenize import Name
from urllib.request import Request
from flask import Flask, flash,render_template, request, url_for, session
from flask_mysqldb import MySQL
import mysql.connector
import json

from sqlalchemy import JSON

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Anurag@06'
app.config['MYSQL_DB'] = 'dbb5'
 
mysql = MySQL(app)
 
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/personData', methods = ['GET'])
def personData():
    print(request)
    cursor=mysql.connection.cursor()
    cursor.execute("SELECT * FROM PERSONS")
    data = cursor.fetchall()
    dataResponse = []
    for i in data:
        jsonData = {
            'name' : i[0],
            'age' : i[1]
        }
        dataResponse.append(jsonData)
    cursor.close()
    return json.dumps(dataResponse)

@app.route('/insertPersonData', methods = ['POST'])
def insertPersonData():
    if request.method == 'POST':
        reqData = request.get_json()
        print(reqData)
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO PERSONS VALUES(%s,%s)''',(reqData['name'],reqData['age']))
        mysql.connection.commit()
        cursor.close()
        return "Person Data inserted Successfully !!"


@app.route('/updatePersonData', methods = ['PUT'])
def updatePersonData():
    if request.method == 'PUT':
        reqData = request.get_json()
        cursor = mysql.connection.cursor()
        cursor.execute('''UPDATE PERSONS SET name = %s WHERE age = %s ''',(reqData['name'],reqData['age']))       
        mysql.connection.commit()
        cursor.close()
        return "Person Data Updated Successfully !!"

@app.route('/deletePersonData', methods = ['DELETE'])
def deletePersonData():
    if request.method == 'DELETE':
        reqData = request.get_json()
        cursor = mysql.connection.cursor()
        age=reqData['age']
        sql = ('''Delete from PERSONS where age = %s''')
        cursor.execute(sql,(age,))
        mysql.connection.commit()
        cursor.close()
        return "Person Data Deleted Successfully !!"


@app.route("/searchdata", methods=["GET", "POST"])
def index():
  # (C1) SEARCH FOR USERS
  if request.method == "GET":
    name= ('Anurag',)
    # console.log(name)
    sql_select_Query = ("""select * from PERSONS
    where name = %s """)
    cursor = mysql.connection.cursor()
    cursor.execute(sql_select_Query,name)
    # get all records
    records = cursor.fetchall()
 
  # (C2) RENDER HTML PAGE
  return render_template("index.html", data=records)


app.run(host='localhost',debug=True)
