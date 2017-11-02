from boto3 import resource
from boto3.dynamodb.conditions import Key

# Create God account
def createGod(god_id,god_name,god_pic):
    # Create a DynamoDB resource
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
 
    data = {}
    data['god'] = {}
    data['god']['god_name'] = god_name
    data['god']['god_pic'] = god_pic
    data['god']['log'] = []
    data['guardian'] = {}
    data['children'] = {}
    
    table.put_item(Item=data)
    return 0

createGod(101010,"Paul Rogel","happy.jpg")