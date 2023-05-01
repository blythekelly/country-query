import pymysql
import creds 
import boto3
from boto3.dynamodb.conditions import Key


TABLE_NAME="account_info"
dynamodb=boto3.resource('dynamodb', region_name='us-east-1')
table=dynamodb.Table(TABLE_NAME)

username="blythe"
password="password"
def crudtest():
    try:
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
    except:
        print("Fail")
    

# Driver Code
if __name__ == "__main__" :
    crudtest()