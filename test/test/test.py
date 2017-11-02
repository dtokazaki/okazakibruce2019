import boto3,json,io,botocore,collections
from datetime import datetime
    
# Create God account
def createGod(god_id,god_name,god_pic):
    # Create an S3 client
    s3 = boto3.client('s3')
    bucket_name = 'okazakibruce2019'
    filename = str(god_id) + ".json"
    
    data = {}
    data['god'] = {}
    data['god']['god_name'] = god_name
    data['god']['god_pic'] = god_pic
    data['god']['log'] = []
    data['guardian'] = {}
    data['children'] = {}
    
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Remove God Account
# If multiple GODS, first delete account
# if only GOD run this function
def delGod(god_id):
    s3 = boto3.client('s3')
    bucket_name = 'okazakibruce2019'
    filename =str(god_id) + ".json"

    try:
       s3.delete_object(Bucket= bucket_name,Key= filename)
    except botocore.exceptions.ClientError as e:
       if e.response['Error']['Code'] == "404":
           print("The object does not exist.")
       else:
           raise
    return 0

# Get God 
def getGod(god_id):
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
    return data['god']

# Add Log Entry
def addLog(god_id,message):
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
    new = {}
    new['time'] = str(datetime.now())
    new['message'] = str(message)
    data['god']['log'].append(new)

    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
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

# Create Guardian
def createGuardian(god_id,guardian_id,guardian_name,guardian_pic):
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

    data['guardian'][str(guardian_id)] = {}
    data['guardian'][str(guardian_id)]['guardian_name'] = guardian_name
    data['guardian'][str(guardian_id)]['guardian_pic'] = guardian_pic
    data['guardian'][str(guardian_id)]['permissions'] = {}

    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Delete Guardian
def delGuardian(god_id,guardian_id):
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
        del data['guardian'][str(guardian_id)]
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Get Guardian
def getGuardian(god_id,guardian_id):
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
    return data['guardian'][str(guardian_id)]

# Change Guardian name
def guardianName(god_id,guardian_id,guardian_name):
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
    data['guardian'][str(guardian_id)]['guardian_name'] = guardian_name
    
    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Guardian Image
def guardianPic(god_id,guardian_id,guardian_pic):
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
    data['guardian'][str(guardian_id)]['guardian_pic'] = guardian_pic
    
    with open(filename, 'w') as f:
        f.write(json.dumps(data))

    s3.upload_file(filename, bucket_name, filename)
    return 0

# Initial add Permission
def addPermission(god_id,guardian_id,child_id):
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
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)] = {}
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['name'] = 0 
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['pic'] = 0
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['chore'] = 0
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['wish'] = 0     
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['achieve'] = 0
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['points'] = 0 # "1" = can add and remove points from child 
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['childPerm'] = 0 # "1" = can change child permissions
  
    except:
        return -1

    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Guardian Name Permissions
def guardian_namePerm(god_id,guardian_id,child_id,name_lvl):
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
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['name'] = name_lvl
       
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Guardian Pic Permissions
def guardian_picPerm(god_id,guardian_id,child_id,pic_lvl):
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
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['pic'] = pic_lvl
      
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Guardian Chore Permissions
def guardian_chorePerm(god_id,guardian_id,child_id,chore_lvl):
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
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['chore'] = chore_lvl
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Guardian Wish Permissions
def guardian_wishPerm(god_id,guardian_id,child_id,wish_lvl):
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
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['wish'] = wish_lvl
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Guardian Achieve Permissions
def guardian_achievePerm(god_id,guardian_id,child_id,achieve_lvl):
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
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['achieve'] = achieve_lvl
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Guardian Points Permissions
def guardian_pointsPerm(god_id,guardian_id,child_id,points_lvl):
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
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['points'] = points_lvl
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Guardian -> childPerm Permissions
def guardian_childPerm(god_id,guardian_id,child_id,childPerm_lvl):
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
        data['guardian'][str(guardian_id)]['permissions'][str(child_id)]['childPerm'] = childPerm_lvl
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Remove Permissions for a given child
def remPermission(god_id,guardian_id,child_id):
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
        del data['guardian'][str(guardian_id)]['permissions'][str(child_id)]
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Delete all permissions
def delPermission(god_id,guardian_id):
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
        del data['guardian'][str(guardian_id)]['permissions']
        data['guardian'][str(guardian_id)]['permissions'] = {}
    except:
        return -1

    with open(filename, 'w') as f:
        f.write(json.dumps(data))

    s3.upload_file(filename, bucket_name, filename)
    return 0

# Get Guardian Permission lvl for a specific child
def get_guardianPerm(god_id,guardian_id,child_id):
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
    return data['guardian'][str(guardian_id)]['permissions'][str(child_id)]

# Get Guardian Name
def get_guardianName(god_id,guardian_id):
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
    return data['guardian'][str(guardian_id)]['guardian_name']

# Get Guardian Image
def get_guardianPic(god_id,guardian_id):
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
    return data['guardian'][str(guardian_id)]['guardian_pic']

# Create Child
def createChild(god_id,child_id,child_name,child_pic):
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

    
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Delete Child
def delChild(god_id,child_id,permission):
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
        if permission == 2:
            del data['children'][str(child_id)]
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Get Child
def getChild(god_id,child_id):
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
    return data['children'][str(child_id)]

# Change Child name
def childName(god_id,child_id,child_name,permission):
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
    if permission >= 1:
        data['children'][str(child_id)]['child_name'] = child_name
    else: 
        return -1

    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0


# Change Child Image
def childPic(god_id,child_id,child_pic,permission):
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
    if permission >= 1:
        data['children'][str(child_id)]['child_pic'] = child_pic
    else:
        return -1
   
    with open(filename, 'w') as f:
        f.write(json.dumps(data))

    s3.upload_file(filename, bucket_name, filename)
    return 0

# Add Log Entry
def add_childLog(god_id,child_id,message):
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
    new = {}
    new['time'] = str(datetime.now())
    new['message'] = str(message)
    data['children'][str(child_id)]['log'].append(new)

    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Get Child Log
def getChildLog(god_id,child_id):
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

    return data['children'][str(child_id)]['log']
# Remove a Child log entry
# For testing purposes, I remove by message, but removing by time is just the same
def rem_childLog(god_id,child_id,message):
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
    flag = 0
    for x in data['children'][str(child_id)]['log']:
        if x['message'] == str(message):
            flag = 1
            break
        ++i
    if flag == 1:
        del data['children'][str(child_id)]['log'][i]

    with open(filename, 'w') as f:
        f.write(json.dumps(data))

    s3.upload_file(filename, bucket_name, filename)
    return 0

# Delete the whole Child Log
def del_childLog(god_id,child_id,permission):
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
        if permission == 2:
            del data['children'][str(child_id)]['log']
            data['children'][str(child_id)]['log'] = []
    except:
        return -1

    with open(filename, 'w') as f:
        f.write(json.dumps(data))

    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Child Name Permissions
def child_namePerm(god_id,child_id,permission,name_lvl):
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
        if permission >= 1:
            data['children'][str(child_id)]['permissions']['name'] = name_lvl
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0


# Change Child Pic Permissions
def child_picPerm(god_id,child_id,permission,pic_lvl):
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
        if permission >= 1:
            data['children'][str(child_id)]['permissions']['pic'] = pic_lvl
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Get Child Permission lvl
def get_childPerm(god_id,child_id):
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
    return data['children'][str(child_id)]['permissions']

# Add Points to Child
def addPoints(god_id,child_id,permission,message,amount):
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
        if permission >= 1:
            prev = data['children'][str(child_id)]['points']
            data['children'][str(child_id)]['points'] = (amount + int(prev))
            if message != None:
                add_childLog(god_id,child_id,message)

    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Remove Points from Child
def remPoints(god_id,child_id,permission,message,amount):
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
        if permission >= 1:
            if message != None:
                add_childLog(god_id,child_id,message)
            prev = data['children'][str(child_id)]['points']
            data['children'][str(child_id)]['points'] = (int(prev) - amount)
            if data['children'][str(child_id)]['points'] < 0:
                data['children'][str(child_id)]['points'] = 0
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Get Child Points
def getPoints(god_id,child_id):
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
    return int(data['children'][str(child_id)]['points'])

# Add Chore Entry
def addChore(god_id,child_id,name,points,interval,day_reset,time_reset,image):
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
        new = {}
        new['name'] = name
        new['confirm'] = 0
        new['points'] = points
        new['interval'] = interval
        new['day_reset'] = time_reset
        new['image'] = image

        data['children'][str(child_id)]['chore'].append(new)
    except:
        return -1

    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Remove a Child log entry
# For testing purposes, I remove by message, but removing by time is just the same
def remChore(god_id,child_id,name):
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
    flag = 0
    for x in data['children'][str(child_id)]['chore']:
        if x['name'] == str(name):
            flag = 1
            break
        ++i
    if flag == 1:
        del data['children'][str(child_id)]['chore'][i]

    with open(filename, 'w') as f:
        f.write(json.dumps(data))

    s3.upload_file(filename, bucket_name, filename)
    return 0

# Delete the whole Chore List
def del_choreList(god_id,child_id):
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
        del data['children'][str(child_id)]['chore']
        data['children'][str(child_id)]['chore'] = []
    except:
        return -1

    with open(filename, 'w') as f:
        f.write(json.dumps(data))

    s3.upload_file(filename, bucket_name, filename)
    return 0

# Get Chore List
def get_choreList(god_id,child_id):
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

    return data['children'][str(child_id)]['chore']

# Get a Child Chore
# For testing purposes, I remove by message, but removing by time is just the same
def getChore(god_id,child_id,name):
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
        i = 0
        flag = 0
        for x in data['children'][str(child_id)]['chore']:
            if x['name'] == str(name):
                flag = 1
                break
            ++i
        if flag == 1:
            data['children'][str(child_id)]['chore'][i]['name'] = name
    except:
        return -1

    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Chore Points
def chorePoints(god_id,child_id,name,points):
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

    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Chore Day Reset
def choreDay(god_id,child_id,name,day):
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

    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Chore Interval Reset
def choreInterval(god_id,child_id,name,interval):
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

    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Chore Time Reset
def choreTime(god_id,child_id,name,time):
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

    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Chore Confirm
def choreConfirm(god_id,child_id,name,confirm):
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

    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Chore Image
def choreImage(god_id,child_id,name,image):
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

    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0



createGod(101010,"Paul","thing.jpg")
godName(101010,"John")
print(get_godName(101010) )
print(get_godPic(101010) )
addLog(101010,"This account was created")
addLog(101010,"First Achievement Completed")
print(getLog(101010))
remLog(101010,"This account was created")
delLog(101010,3)
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
print(getChore(101010,56789,"Wash the Dishes"))



     