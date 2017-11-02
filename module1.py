import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
from datetime import datetime

def createTable():
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='okazakibruce2019',
        KeySchema=[
            {
                'AttributeName': 'god_id', 
                'KeyType': 'HASH'
            },
        ], 
        AttributeDefinitions=[
            {
                'AttributeName': 'god_id', 
                'AttributeType': 'S'
            }, 
        ], 
        ProvisionedThroughput={
            'ReadCapacityUnits': 1, 
            'WriteCapacityUnits': 1
        }
    )

    table.meta.client.get_waiter('table_exists').wait(TableName='okazakibruce2019')
    print(table.item_count)
# Create God account
def createGod(god_id,god_name,god_pic):
    # Create a DynamoDB resource
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
 
    data = {}
    data['god_id']= str(god_id)
    data['god'] = {}
    data['god']['god_name'] = god_name
    data['god']['god_pic'] = god_pic
    data['god']['log'] = []
    data['guardian'] = {}
    data['children'] = {}
    
    table.put_item(Item= data)
    return 0

# Remove God Account
# If multiple GODS, first delete account
# if only GOD run this function
def delGod(god_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')

    table.delete_item(
        Key={
            'god_id': str(god_id)
        }
    )
    return 0

# Get God 
def getGod(god_id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')

    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    return response['Item']

# Add Log Entry
def addLog(god_id,message):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    new = {}
    new['time'] = str(datetime.now())
    new['message'] = str(message)
    data = {}
    data['god_id'] = str(god_id)
    data['god'] ={}
    data['god']['log'] = []
    data['god']['log'].append(new)

    table.put_item(Item= data)
    return 0
# Remove a log entry
# For testing purposes, I remove by message, but removing by time is just the same
def remLog(god_id,message):
    s3 = boto3.client('s3')
    bucket_name = 'okazakibruce2019'
    filename = str(god_id) + ".json"

    try:
         s3.download_file(bucket_name,filename,filename)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    with open(filename, 'r') as f:
        data = json.load(f)
    i = 0
    for x in data['god']['log']:
        if x['message'] == str(message):
            break
        ++i
    del data['god']['log'][i]

    with open(filename, 'w') as f:
        f.write(json.dumps(data))

    s3.upload_file(filename, bucket_name, filename)
    return 0

# Delete the whole Log
def delLog(god_id,permission):
    s3 = boto3.client('s3')
    bucket_name = 'okazakibruce2019'
    filename = str(god_id) + ".json"

    try:
         s3.download_file(bucket_name,filename,filename)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    with open(filename, 'r') as f:
        data = json.load(f)
    try:
        del data['god']['log']
        data['god']['log'] = []
    except:
        return -1

    with open(filename, 'w') as f:
        f.write(json.dumps(data))

    s3.upload_file(filename, bucket_name, filename)
    return 0
# Change God Name
def godName(god_id,god_name):
    s3 = boto3.client('s3')
    bucket_name = 'okazakibruce2019'
    filename = str(god_id) + ".json"

    try:
        s3.download_file(bucket_name,filename,filename)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    with open(filename, 'r') as f:
        data = json.load(f)
    data['god']['god_name'] = god_name
    
    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0
# Change God Image
def godPic(god_id,god_pic):
    s3 = boto3.client('s3')
    bucket_name = 'okazakibruce2019'
    filename = str(god_id) + ".json"

    try:
        s3.download_file(bucket_name,filename,filename)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    with open(filename, 'r') as f:
        data = json.load(f)
    data['god']['god_pic'] = god_pic
    
    with open(filename, 'w') as f:
        f.write(json.dumps(data))

    s3.upload_file(filename, bucket_name, filename)
    return 0
# Get God Name
def get_godName(god_id):
    s3 = boto3.client('s3')
    bucket_name = 'okazakibruce2019'
    filename = str(god_id) + ".json"

    try:
        s3.download_file(bucket_name,filename,filename)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    with open(filename, 'r') as f:
        data = json.load(f)
    return data['god']['god_name']

# Get God Image
def get_godPic(god_id):
    s3 = boto3.client('s3')
    bucket_name = 'okazakibruce2019'
    filename = str(god_id) + ".json"

    try:
        s3.download_file(bucket_name,filename,filename)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    with open(filename, 'r') as f:
        data = json.load(f)
    return data['god']['god_pic']

# Get Log
def getLog(god_id):
    s3 = boto3.client('s3')
    bucket_name = 'okazakibruce2019'
    filename = str(god_id) + ".json"

    try:
         s3.download_file(bucket_name,filename,filename)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    with open(filename, 'r') as f:
        data = json.load(f)

    return data['god']['log']

#createTable()
createGod(101010,"Paul Rogel","happy.jpg")
addLog(101010,"Account created")
addLog(101010,"Second Account")