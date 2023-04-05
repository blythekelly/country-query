# Country Query using Flask and SQL

In this project, I created a Flask app that functioned as a world information query webpage. The world information originates from a SQL database stored in my AWS RDS instance. 
![image](https://user-images.githubusercontent.com/86129067/230121588-bc9d48e1-5d35-40c5-828a-7fe247384c43.png)

The first three buttons on the webpage are methods to filter and search the database. On the backend, this uses SQL to query the database according to the user input on the HTML form. I utilized a JOIN to combine the country and country_language tables under the condition that the language was the official language. This population query used an HTML form and a template variable to display either population or life expectancy depending on which button the user pushed. 

![image](https://user-images.githubusercontent.com/86129067/230121656-2a4db254-60d6-4548-b6d9-ac2b57c4470f.png)

When performing the search above for countries with populations over 80000000, the results are the following:
![image](https://user-images.githubusercontent.com/86129067/230121689-b57886d7-88c6-431c-81cf-0e2876c46c41.png)


The life expectancy query uses the same form as the population query, but the template variable switches the wording to “life expectancy” because the form uses a conditional statement within it. 
![image](https://user-images.githubusercontent.com/86129067/230121729-bc0ca436-fd5c-48ec-9b3a-571266c685ff.png)


These are the results from the life expectancy query above:
![image](https://user-images.githubusercontent.com/86129067/230121776-03c4c0cd-fadb-4534-963d-4a631ece66a7.png)

The name query uses another HTML form that sends information to a SQL search statement:
![image](https://user-images.githubusercontent.com/86129067/230121806-95a0fda3-f000-4377-aa65-1852b3219af3.png)


Result from the name query:
![image](https://user-images.githubusercontent.com/86129067/230121839-b91bf5ff-f3ef-4f05-9f5d-e01bb87f3d8f.png)


The last button on the home screen brings the user to a login screen. For CRUD compatibility, I included the ability to create a new admin account. Once an account is created, the user can log into the admin page. This page has options for deleting an account, updating an existing account’s password, or reading all account information in the non-relational DynamoDB database. There is also the option to view all of the country data without any search filters.

The login screen checks if the password corresponds to the one stored in the DynamoDB database. If it is not the same or if there is any other discrepancy, such as a wrong username or no input provided, the login button will just direct the user to the same login screen again. 
![image](https://user-images.githubusercontent.com/86129067/230122065-c35f8266-7a75-41fb-b9ad-e999fe58bd43.png)


The login screen also has a create account button, which sends and stores the data in the database. 
![image](https://user-images.githubusercontent.com/86129067/230122156-74c88e3a-11c2-48dc-b6f9-2ce5f3c8abd8.png)


Once logged in, the admin screen has buttons to view all of the country information in the database, update an account’s password, delete an account, view all account information, or log out. 
![image](https://user-images.githubusercontent.com/86129067/230122183-058cfe76-c29e-4d49-9d4f-befa574a9278.png)


View all country information button:
![image](https://user-images.githubusercontent.com/86129067/230122218-223011e2-357e-447e-88a6-df9b2be21644.png)


Update account screen:
![image](https://user-images.githubusercontent.com/86129067/230122240-7e8d3bef-99d2-45a8-abb0-1690c2039840.png)


Delete account screen:
![image](https://user-images.githubusercontent.com/86129067/230122289-387e0837-3ced-44b6-9c13-6c050b369eca.png)


Screen to read all of the account information:
![image](https://user-images.githubusercontent.com/86129067/230122327-64487135-5647-482d-82ce-796c3a41c319.png)



Popup screen when an action was completed successfully:
![image](https://user-images.githubusercontent.com/86129067/230122372-74f8245b-bae8-4527-b0bf-ac72ad0107e4.png)


Lastly, I displayed an image that was stored in my S3 bucket. In summary, this project included a user interface to search through a SQL database, CRUD compatibility with a DynamoDB database, and AWS compatibility.

