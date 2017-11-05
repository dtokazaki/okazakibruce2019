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
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    data['god']['log'].append(new)

    table.put_item(Item= data)
    return 0
# Remove a log entry
# For testing purposes, I remove by message, but removing by time is just the same
def remLog(god_id,message):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    i = 0
    for x in data['god']['log']:
        if x['message'] == str(message):
            break
        ++i
    del data['god']['log'][i]

    table.put_item(Item= data)
    return 0

# Delete the whole Log
def delLog(god_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']

    del data['god']['log']
    data['god']['log'] = []

    table.put_item(Item= data)
    return 0
# Change God Name
def godName(god_id,god_name):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']

    data['god']['god_name'] = god_name
    
    table.put_item(Item= data)
    return 0
# Change God Image
def godPic(god_id,god_pic):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    data['god']['god_pic'] = god_pic
    
    table.put_item(Item= data)
    return 0
# Get God Name
def get_godName(god_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    return data['god']['god_name']

# Get God Image
def get_godPic(god_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    return data['god']['god_pic']

# Get Log
def getLog(god_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']

    return data['god']['log']

# Create Guardian
def createGuardian(god_id,guardian_id,guardian_name,guardian_pic):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']

    data['guardian'][str(guardian_id)] = {}
    data['guardian'][str(guardian_id)]['guardian_name'] = guardian_name
    data['guardian'][str(guardian_id)]['guardian_pic'] = guardian_pic
    data['guardian'][str(guardian_id)]['permissions'] = {}

    table.put_item(Item= data)
    return 0

# Delete Guardian
def delGuardian(god_id,guardian_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        del data['guardian'][str(guardian_id)]
    except:
        return -1
    table.put_item(Item= data)
    return 0

# Get Guardian
def getGuardian(god_id,guardian_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    return data['guardian'][str(guardian_id)]

# Change Guardian name
def guardianName(god_id,guardian_id,guardian_name):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    data['guardian'][str(guardian_id)]['guardian_name'] = guardian_name
    
    table.put_item(Item= data)
    return 0

# Change Guardian Image
def guardianPic(god_id,guardian_id,guardian_pic):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    data['guardian'][str(guardian_id)]['guardian_pic'] = guardian_pic
    
    table.put_item(Item= data)
    return 0

# Initial add Permission
def addPermission(god_id,guardian_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
   
    data['guardian'][str(guardian_id)]['permissions'][str(child_id)] = {}
    data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['name'] = 0 
    data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['pic'] = 0
    data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['chore'] = 0
    data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['wish'] = 0     
    data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['achieve'] = 0
    data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['points'] = 0 # "1" = can add and remove points from child 
    data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['childPerm'] = 0 # "1" = can change child permissions

    table.put_item(Item= data)
    return 0

# Change Guardian Name Permissions
def guardian_namePerm(god_id,guardian_id,child_id,name_lvl):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    
    try:
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['name'] = name_lvl
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Guardian Pic Permissions
def guardian_picPerm(god_id,guardian_id,child_id,pic_lvl):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    
    try:
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['pic'] = pic_lvl
      
    except:
        return -1
    table.put_item(Item= data)
    return 0

# Change Guardian Chore Permissions
def guardian_chorePerm(god_id,guardian_id,child_id,chore_lvl):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    
    try:
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['chore'] = chore_lvl
    except:
        return -1
    table.put_item(Item= data)
    return 0

# Change Guardian Wish Permissions
def guardian_wishPerm(god_id,guardian_id,child_id,wish_lvl):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    
    try:
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['wish'] = wish_lvl
    except:
        return -1
    table.put_item(Item= data)
    return 0

# Change Guardian Achieve Permissions
def guardian_achievePerm(god_id,guardian_id,child_id,achieve_lvl):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    
    try:
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['achieve'] = achieve_lvl
    except:
        return -1
    table.put_item(Item= data)
    return 0

# Change Guardian Points Permissions
def guardian_pointsPerm(god_id,guardian_id,child_id,points_lvl):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    
    try:
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['points'] = points_lvl
    except:
        return -1
    table.put_item(Item= data)

# Change Guardian -> childPerm Permissions
def guardian_childPerm(god_id,guardian_id,child_id,childPerm_lvl):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    
    
    try:
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['childPerm'] = childPerm_lvl
    except:
        return -1
    table.put_item(Item= data)
    return 0

# Remove Permissions for a given child
def remPermission(god_id,guardian_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    
    try:
        del data['guardian'][str(guardian_id)]['permissions'][str(child_id)]
    except:
        return -1
    table.put_item(Item= data)
    return 0

# Delete all permissions
def delPermission(god_id,guardian_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        del data['guardian'][str(guardian_id)]['permissions']
        data['guardian'][str(guardian_id)]['permissions'] = {}
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Get Guardian Permission lvl for a specific child
def get_guardianPerm(god_id,guardian_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']

    return data['guardian'][str(guardian_id)]['permissions'][str(child_id)]

# Get Guardian Name
def get_guardianName(god_id,guardian_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    return data['guardian'][str(guardian_id)]['guardian_name']

# Get Guardian Image
def get_guardianPic(god_id,guardian_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    return data['guardian'][str(guardian_id)]['guardian_pic']
# Create Child
def createChild(god_id,child_id,child_name,child_pic):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
  
    data['children'][str(child_id)] = {}
    data['children'][str(child_id)]['child_name'] = child_name
    data['children'][str(child_id)]['child_pic'] = child_pic
    data['children'][str(child_id)]['points'] = 0
    data['children'][str(child_id)]['chore'] = []
    data['children'][str(child_id)]['wish'] = []
    data['children'][str(child_id)]['achievements'] = []
    data['children'][str(child_id)]['permissions'] = {}
    data['children'][str(child_id)]['permissions']['name'] = 1
    data['children'][str(child_id)]['permissions']['pic'] = 1
    data['children'][str(child_id)]['log'] = []

    table.put_item(Item= data)
    return 0

# Delete Child
def delChild(god_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
       del data['children'][str(child_id)]
    except:
        return -1
    table.put_item(Item= data)
    return 0

# Get Child
def getChild(god_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    return data['children'][str(child_id)]

# Change Child name
def childName(god_id,child_id,child_name,permission):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    if permission >= 1:
        data['children'][str(child_id)]['child_name'] = child_name
    else: 
        return -1

    table.put_item(Item= data)
    return 0


# Change Child Image
def childPic(god_id,child_id,child_pic,permission):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    if permission >= 1:
        data['children'][str(child_id)]['child_pic'] = child_pic
    else:
        return -1
   
    table.put_item(Item= data)
    return 0

# Get Child Name
def get_childName(god_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    return data['children'][str(child_id)]['child_name']

# Get Child Image
def get_childPic(god_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    return data['children'][str(child_id)]['child_pic']

# Add Log Entry
def add_childLog(god_id,child_id,message):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']

    new = {}
    new['time'] = str(datetime.now())
    new['message'] = str(message)
    data['children'][str(child_id)]['log'].append(new)

    table.put_item(Item= data)
    return 0

# Get Child Log
def get_childLog(god_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']

    return data['children'][str(child_id)]['log']
# Remove a Child log entry
# For testing purposes, I remove by message, but removing by time is just the same
def rem_childLog(god_id,child_id,message):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    i = 0
    flag = 0
    for x in data['children'][str(child_id)]['log']:
        if x['message'] == str(message):
            flag = 1
            break
        ++i
    if flag == 1:
        del data['children'][str(child_id)]['log'][i]

    table.put_item(Item= data)
    return 0

# Delete the whole Child Log
def del_childLog(god_id,child_id,permission):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        if permission == 2:
            del data['children'][str(child_id)]['log']
            data['children'][str(child_id)]['log'] = []
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Child Name Permissions
def child_namePerm(god_id,child_id,permission,name_lvl):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    
    try:
        if permission >= 1:
            data['children'][str(child_id)]['permissions']['name'] = name_lvl
    except:
        return -1
    table.put_item(Item= data)
    return 0


# Change Child Pic Permissions
def child_picPerm(god_id,child_id,permission,pic_lvl):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    
    try:
        if permission >= 1:
            data['children'][str(child_id)]['permissions']['pic'] = pic_lvl
    except:
        return -1
    table.put_item(Item= data)
    return 0

# Get Child Permission lvl
def get_childPerm(god_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    
    return data['children'][str(child_id)]['permissions']

# Add Points to Child
def addPoints(god_id,child_id,permission,message,amount):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    
    try:
        if int(permission) >= 1:
            data['children'][str(child_id)]['points'] += int(amount)
            if message != None:
                add_childLog(god_id,child_id,message)

    except:
        return -1
    table.put_item(Item= data)
    return 0

# Remove Points from Child
def remPoints(god_id,child_id,permission,message,amount):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    
    try:
        if permission >= 1:
            if message != None:
                add_childLog(god_id,child_id,message)
            prev = data['children'][str(child_id)]['points']
            data['children'][str(child_id)]['points'] = (int(prev) - amount)
            if data['children'][str(child_id)]['points'] < 0:
                data['children'][str(child_id)]['points'] = 0
    except:
        return -1
    table.put_item(Item= data)
    return 0

# Get Child Points
def getPoints(god_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    return int(data['children'][str(child_id)]['points'])

# Add Chore Entry
def addChore(god_id,child_id,name,points,interval,day_reset,time_reset,image):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        new = {}
        new['name'] = name
        new['confirm'] = 0
        new['points'] = points
        new['interval'] = interval
        new['day_reset'] = day_reset
        new['time_reset'] = time_reset
        new['image'] = image

        data['children'][str(child_id)]['chore'].append(new)
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Remove a Child Chore
# For testing purposes, I remove by message, but removing by time is just the same
def remChore(god_id,child_id,name):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    i = 0
    flag = 0
    for x in data['children'][str(child_id)]['chore']:
        if x['name'] == str(name):
            flag = 1
            break
        ++i
    if flag == 1:
        del data['children'][str(child_id)]['chore'][i]

    table.put_item(Item= data)
    return 0

# Delete the whole Chore List
def del_choreList(god_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        del data['children'][str(child_id)]['chore']
        data['children'][str(child_id)]['chore'] = []
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Get Chore List
def get_choreList(god_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']

    return data['children'][str(child_id)]['chore']

# Get a Child Chore
# For testing purposes, I remove by message, but removing by time is just the same
def getChore(god_id,child_id,name):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    i = 0
    flag = 0
    for x in data['children'][str(child_id)]['chore']:
        if x['name'] == str(name):
            flag = 1
            break
        ++i
    if flag == 1:
        return data['children'][str(child_id)]['chore'][i]
    else:
        return -1

# Change Chore Name
def choreName(god_id,child_id,name,newName):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['chore']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['chore'][i]['name'] = newName
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Chore Points
def chorePoints(god_id,child_id,name,points):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['chore']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['chore'][i]['points'] = points
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Chore Day Reset
def choreDay(god_id,child_id,name,day):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['chore']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['chore'][i]['day'] = day
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Chore Interval Reset
def choreInterval(god_id,child_id,name,interval):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['chore']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['chore'][i]['interval'] = interval
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Chore Time Reset
def choreTime(god_id,child_id,name,time):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['chore']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['chore'][i]['time'] = time
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Chore Confirm
def choreConfirm(god_id,child_id,name,confirm):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['chore']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['chore'][i]['confirm'] = confirm
    except:
        return -1

    table.put_item(Item= data)

# Change Chore Image
def choreImage(god_id,child_id,name,image):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['chore']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['chore'][i]['image'] = image
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Add Wish Entry
def addWish(god_id,child_id,name,image):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        new = {}
        new['name'] = name
        new['confirm'] = 0
        new['cost'] = 0
        new['image'] = image

        data['children'][str(child_id)]['wish'].append(new)
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Remove a Child Wish entry
# For testing purposes, I remove by message, but removing by time is just the same
def remWish(god_id,child_id,name):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    i = 0
    flag = 0
    for x in data['children'][str(child_id)]['wish']:
        if x['name'] == str(name):
            flag = 1
            break
        ++i
    if flag == 1:
        del data['children'][str(child_id)]['wish'][i]

    table.put_item(Item= data)
    return 0

# Delete the whole Wish List
def del_wishList(god_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        del data['children'][str(child_id)]['wish']
        data['children'][str(child_id)]['wish'] = []
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Get Wish List
def get_wishList(god_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']

    return data['children'][str(child_id)]['wish']

# Get a Child Wish
# For testing purposes, I remove by message, but removing by time is just the same
def getWish(god_id,child_id,name):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    i = 0
    flag = 0
    for x in data['children'][str(child_id)]['wish']:
        if x['name'] == str(name):
            flag = 1
            break
        ++i
    if flag == 1:
        return data['children'][str(child_id)]['wish'][i]
    else:
        return -1

# Change Wish Name
def wishName(god_id,child_id,name,newName):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['wish']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['wish'][i]['name'] = newName
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Wish Cost
def wishCost(god_id,child_id,name,cost):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['wish']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['wish'][i]['cost'] = cost
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Wish Confirm
def wishConfirm(god_id,child_id,name,confirm):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['wish']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['wish'][i]['confirm'] = confirm
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Wish Image
def wishImage(god_id,child_id,name,image):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['wish']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['wish'][i]['image'] = image
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Add Achievement Entry
def addAchieve(god_id,child_id,name,reward,recurring,day_reset,time_reset,progress,image):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        new = {}
        new['name'] = name
        new['complete'] = 0
        new['recurring'] = 0
        new['reward'] = reward
        new['day_reset'] = day_reset
        new['time_reset'] = time_reset
        new['progress'] = 0
        new['image'] = image

        data['children'][str(child_id)]['achievements'].append(new)
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Remove a Child Achievement
# For testing purposes, I remove by message, but removing by time is just the same
def remAchieve(god_id,child_id,name):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    i = 0
    flag = 0
    for x in data['children'][str(child_id)]['achievements']:
        if x['name'] == str(name):
            flag = 1
            break
        ++i
    if flag == 1:
        del data['children'][str(child_id)]['achievements'][i]

    table.put_item(Item= data)
    return 0

# Delete the whole Achievement List
def del_achieveList(god_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        del data['children'][str(child_id)]['achievements']
        data['children'][str(child_id)]['achievements'] = []
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Get Achievement List
def get_achieveList(god_id,child_id):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']

    return data['children'][str(child_id)]['achievements']

# Get a Child Achievement
# For testing purposes, I remove by message, but removing by time is just the same
def getAchieve(god_id,child_id,name):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    i = 0
    flag = 0
    for x in data['children'][str(child_id)]['achievements']:
        if x['name'] == str(name):
            flag = 1
            break
        ++i
    if flag == 1:
        return data['children'][str(child_id)]['achievements'][i]
    else:
        return -1

# Change Achievements Name
def achieveName(god_id,child_id,name,newName):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['achievements']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['achievements'][i]['name'] = newName
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Achievement Reward
def achieveReward(god_id,child_id,name,reward):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['achievements']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['achievements'][i]['reward'] = reward
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Achievement recurring bool
def achieveBool(god_id,child_id,name,bool):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['achievements']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['achievements'][i]['recurring'] = bool
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Achievement Day Reset
def achieveDay(god_id,child_id,name,day):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['achievements']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['achievements'][i]['day'] = day
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Achievement Interval Reset
def achieveInterval(god_id,child_id,name,interval):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['achievements']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['achievements'][i]['interval'] = interval
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Achievement Time Reset
def achieveTime(god_id,child_id,name,time):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['achievements']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['achievements'][i]['time'] = time
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Achievement Complete
def achieveComplete(god_id,child_id,name,complete):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['achievements']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['achievements'][i]['complete'] = complete
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Achievement Progress
def achieveProgress(god_id,child_id,name,progress):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['achievements']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['achievements'][i]['progress'] = progress
    except:
        return -1

    table.put_item(Item= data)
    return 0

# Change Achievement Image
def achieveImage(god_id,child_id,name,image):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('okazakibruce2019')
    
    response = table.get_item(
        Key={
            'god_id': str(god_id)
        }
    )
    data = response['Item']
    try:
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['achievements']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['achievements'][i]['image'] = image
    except:
        return -1

    table.put_item(Item= data)
    return 0

#createTable()
createGod(101010,"Paul Rogel","happy.jpg")
addLog(101010,"Account created")
addLog(101010,"Second Account")
godName(101010,"John")
godPic(101010,"smile.jpg")
print(get_godName(101010) )
print(get_godPic(101010) )
print(getLog(101010))
remLog(101010,"Account created")
#delLog(101010,3)
#delGod(101010)
createGuardian(101010,12345,"Daniel Okazaki","sad_face.jpg")
createGuardian(101010,11111,"test","happy_face.jpg")
guardianName(101010,12345,"Gabe") 
guardianPic(101010,12345,"progress.jpg")
print(get_guardianName(101010,12345) )
print(get_guardianPic(101010,12345) )
addPermission(101010,12345,98765)
addPermission(101010,12345,56789)
guardian_namePerm(101010,12345,98765,1)
guardian_picPerm(101010,12345,98765,2)
guardian_chorePerm(101010,12345,98765,3)
guardian_wishPerm(101010,12345,98765,4)
guardian_achievePerm(101010,12345,98765,5)
guardian_pointsPerm(101010,12345,98765,6)
guardian_childPerm(101010,12345,98765,7)
print(get_guardianPerm(101010,12345,56789))
#delPermission(101010,12345)
delGuardian(101010,11111)
#remPermission(101010,12345,56789)
createChild(101010,98765,"Mason Bruce","winning.jpg")
createChild(101010,56789,"Mickey H","programming.jpg")
delChild(101010,56789,3)
#god_childPic(101010,98765,"Harry")
#god_childName(101010,98765,"losing.jpg")
childName(101010,98765,"Chris",1)
childPic(101010,98765,"test.jpg",2)
add_childLog(101010,98765,"First Achievement Completed")
#rem_childLog(101010,98765,"First Achievement Completed")
del_childLog(101010,98765,3)
child_picPerm(101010,98765,1,0)
child_namePerm(101010,98765,1,0)
addPoints(101010,98765,1,None,10)
remPoints(101010,98765,1,None,20)
print(get_childPerm(101010,56789))
print(getPoints(101010,98765))
addChore(101010,56789,"Wash the Dishes",10,1,1,1,"dishes.jpg")
#remChore(101010,56789,"Wash the Dishes")
#del_choreList(101010,56789)
print(get_choreList(101010,56789))
chorePoints(101010,56789,"Wash the Dishes",110)
choreInterval(101010,56789,"Wash the Dishes",1)
choreDay(101010,56789,"Wash the Dishes",123)
choreTime(101010,56789,"Wash the Dishes",1555)
choreConfirm(101010,56789,"Wash the Dishes",1)
choreImage(101010,56789,"Wash the Dishes","Dishes2.jpg")
choreName(101010,56789,"Wash the Dishes","Wash")
print(getChore(101010,56789,"Wash"))
addWish(101010,56789,"Bike","bike.jpg")
#remWish(101010,56789,"Bike")
#del_wishList(101010,56789)
print(get_wishList(101010,56789))
wishCost(101010,56789,"Bike",110)
wishConfirm(101010,56789,"Bike",1)
wishImage(101010,56789,"Bike","Bike2.jpg")
wishName(101010,56789,"Bike","Scooter")
print(getWish(101010,56789,"Scooter"))
addAchieve(101010,56789,"First Achievement",10,0,1,1,1,"one.jpg")
#remAchieve(101010,56789,"First Achievement")
#del_AchieveList(101010,56789)
print(get_achieveList(101010,56789))
achieveReward(101010,56789,"First Achievement",110)
achieveDay(101010,56789,"First Achievement",123)
achieveTime(101010,56789,"First Achievement",1555)
achieveComplete(101010,56789,"First Achievement",1)
choreImage(101010,56789,"First Achievement","happy.jpg")
achieveProgress(101010,56789,"First Achievement",100)
achieveName(101010,56789,"First Achievement","New")
print(getAchieve(101010,56789,"New"))

