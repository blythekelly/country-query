from flask import Flask
from flask import render_template
import pymysql
import creds 
from flask import request
import boto3
from boto3.dynamodb.conditions import Key

app=Flask(__name__)

#First page of the website
@app.route('/')
def first():
    return render_template('layout.html')
    

def get_conn():
    conn = pymysql.connect(
        host= creds.host,
        user= creds.user, 
        password = creds.password,
        db=creds.db,
        )
    return conn

#Defining function to execute SQL queries
def execute_query(query, args=()):
    cur = get_conn().cursor()
    cur.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows


#display the query in a html table
def display_html(rows):
    html = ""
    html += """<table><tr><th>Name</th><th>Population</th><th>Life Expectancy</th><th>Capital</th><th>GNP</th><th>Language</th></tr>"""

    for r in rows:
        html += "<tr><td>" + str(r[0]) + "</td><td>" + str(r[1]) + "</td><td>" + str(r[2]) + "</td><td>" + str(r[3]) + "</td><td>" + str(r[4]) + "</td><td>"+ str(r[5]) + "</td></tr>"
    html += "</table></body>"
    return html

  
#Population query (uses JOIN)
@app.route("/populationquery/population")
def popquery(population):
    rows = execute_query("""SELECT name, population, lifeexpectancy, capital, gnp, language
        FROM country JOIN countrylanguage
        WHERE countrycode=code AND isofficial = True AND population >= %s
        ORDER BY population DESC
        Limit 500""", (str(population)))
    
    return display_html(rows)
 
#Textbox to get information from the user for the search
@app.route("/popquerytextbox", methods = ['GET'])
def pop_form():
    return render_template('textbox.html', fieldname = "population")

@app.route("/popquerytextbox", methods = ['POST'])
def time_form_post():
  text = request.form['text']
  return popquery(text)

#Life expectancy query (uses JOIN)
@app.route("/lifeexpquery/lifeexp")
def lifequery(lifeexpectancy):
    rows = execute_query("""SELECT name, population, lifeexpectancy, capital, gnp, language
        FROM country JOIN countrylanguage
        WHERE countrycode=code AND isofficial = True AND lifeexpectancy >= %s 
        ORDER BY lifeexpectancy DESC
        Limit 500""", (str(lifeexpectancy)))
    
    return display_html(rows)
 
#Textbox to get life expectancy search information
@app.route("/lifequerytextbox", methods = ['GET'])
def life_form():
    return render_template('textbox.html', fieldname = "lifeexpectancy")

@app.route("/lifequerytextbox", methods = ['POST'])
def life_form_post():
  text = request.form['text']
  return lifequery(text)
  
#Name  Query (uses JOIN)
@app.route("/namequery/name")
def namequery(name):
    rows = execute_query("""SELECT name, population, lifeexpectancy, capital, gnp, language
        FROM country JOIN countrylanguage
        WHERE countrycode=code AND isofficial = True AND name = %s 
        ORDER BY lifeexpectancy DESC
        Limit 500""", (str(name)))
    
    return display_html(rows)
 
#Textbox to get the name of the country to search for
@app.route("/namequerytextbox", methods = ['GET'])
def name_form():
    return render_template('nametextbox.html', fieldname = "name")

@app.route("/namequerytextbox", methods = ['POST'])
def name_form_post():
    try:
        text = request.form['text']
        return namequery(text)
    except:
        print("Country not found. Please try again.")
        
#Log in screen
TABLE_NAME="account_info"
dynamodb=boto3.resource('dynamodb', region_name='us-east-1')
table=dynamodb.Table(TABLE_NAME)

@app.route("/login")
def login(username, password):
    try:
        #retrieving the data on that username
        response = table.get_item(
            Key={
                'Username': username
            }
        )
        account=response.get("Item")
        correct_password=account["Password"]
        
        #checking if password is correct
        if password==correct_password:
            return render_template('loggedin.html')
        
        #if password isn't correct, the user returns to the log in screen
        else:
            return render_template('login.html')
    except:
        return render_template('login.html')
    
#The log in textbox
@app.route("/logintextbox", methods = ['GET'])
def login_form():
    return render_template('login.html', fieldname = "login")

@app.route("/logintextbox", methods = ['POST'])
def login_form_post():
  username = request.form['username']
  password = request.form['password']
  return login(username, password)
 
 
#Create account screen
@app.route("/createaccount") 
def create_account(username, password):
    try:
        #putting the new username and password into the database
        table.put_item(
            Item={
               "Username":username,
               "Password":password
            }
            )
        return render_template('loggedin.html')
    except:
        #if the username already exists, the user is returned to the log in screen
        return render_template('login.html')

@app.route("/create_account_textbox", methods=['GET'])
def create_account_form():
    return render_template('create_account.html')
    
@app.route("/create_account_textbox", methods = ['POST'])
def create_account_form_post():
  username = request.form['username']
  password = request.form['password']
  return create_account(username, password)
  

 
"""Admin Screens
CRUD is implemented here
"""

#Function to update account password
@app.route("/updateaccount")
def updateaccount(username, newpass):
    try:
        #updating password for the given username
        table.update_item(
        Key={'Username':str(username)
            },
        UpdateExpression="SET Password=:p",
        ExpressionAttributeValues={
        ':p':str(newpass),
        }
        )
        return render_template("success.html")
    except:
        return render_template("login.html")
    
#Textbox for updating account
@app.route("/updateaccounttextbox", methods = ['GET'])
def update_account_form():
    return render_template('crud.html', fieldname = "updateaccount")
    
@app.route("/updateaccounttextbox", methods = ['POST'])
def update_account_form_post():
    try:
        username=request.form['username']
        newpass=request.form['newpass']
        
        return updateaccount(username, newpass)
    except:
        return render_template("login.html")
    

@app.route("/deleteaccount")
def delete_account(username, password):
    try:
        #searching for the record of the account based off the given username
        response = table.get_item(
            Key={
                'Username': str(username)
            }
        )
        account=response.get("Item")
        correct_password=account["Password"]
        
        #checking if password is correct
        if password==str(correct_password):
            table.delete_item(
                Key={
                    'Username': str(username)
                }
            )
            return render_template("success.html")
        else:
            return render_template("login.html")
    except:
        return render_template("login.html")
        
@app.route("/deleteaccounttextbox", methods = ['GET'])
def delete_account_form():
    return render_template('crud.html', fieldname = "deleteaccount")
    
@app.route("/deleteaccounttextbox", methods = ['POST'])
def delete_account_form_post():
    try:
        username=request.form['username']
        password=request.form['password']
        
        return delete_account(username, password)
    except:
        return render_template("layout.html")
        
        
#printing all of the account information
@app.route("/readaccounts")
def readaccounts():
    done=False
    start_key=None
    while not done:
        response=table.scan()
            
            
        html = ""
        html += """<table><tr><th>Username</th><th>Password</th></tr>"""
        for account in response["Items"]:
            html += "<tr><td>" + str(account["Username"]) + "</td><td>" + str(account["Password"]) + "</td></tr>"
        html += "</table></body>"
                
        start_key=response.get("LastEvaluateKey", None)
        done=start_key is None
        return html

#printing all of the country information
@app.route("/readcountries")
def readcountries():
    rows = execute_query("""SELECT name, population, lifeexpectancy, capital, gnp, language
        FROM country JOIN countrylanguage
        WHERE countrycode=code AND isofficial = True
        """)
    
    return display_html(rows)

 

#runnning flask app 
if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)