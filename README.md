# Country Query using Flask and SQL

In this project, I created a Flask app that functioned as a world information query webpage. The world information originates from a SQL database stored in my AWS RDS instance. 

The first three buttons on the webpage are methods to filter and search the database. On the backend, this uses SQL to query the database according to the user input on the HTML form. I utilized a JOIN to combine the country and country_language tables under the condition that the language was the official language. This population query used an HTML form and a template variable to display either population or life expectancy depending on which button the user pushed. 

When performing the search above for countries with populations over 80000000, the results are the following:

The life expectancy query uses the same form as the population query, but the template variable switches the wording to “life expectancy” because the form uses a conditional statement within it. 

These are the results from the life expectancy query above:
The name query uses another HTML form that sends information to a SQL search statement:

Result from the name query:

The last button on the home screen brings the user to a login screen. For CRUD compatibility, I included the ability to create a new admin account. Once an account is created, the user can log into the admin page. This page has options for deleting an account, updating an existing account’s password, or reading all account information in the non-relational DynamoDB database. There is also the option to view all of the country data without any search filters.




The login screen checks if the password corresponds to the one stored in the DynamoDB database. If it is not the same or if there is any other discrepancy, such as a wrong username or no input provided, the login button will just direct the user to the same login screen again. 

The login screen also has a create account button, which sends and stores the data in the database. 

Once logged in, the admin screen has buttons to view all of the country information in the database, update an account’s password, delete an account, view all account information, or log out. 


View all country information button:



Update account screen:

Delete account screen:

Screen to read all of the account information:




Popup screen when an action was completed successfully:

Lastly, I displayed an image that was stored in my S3 bucket. In summary, this project included a user interface to search through a SQL database, CRUD compatibility with a DynamoDB database, and AWS compatibility.

