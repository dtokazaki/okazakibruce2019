import boto3,json,io,botocore,collections
from datetime import datetime

def merge(a, b, path=None):
    "merges b into a"
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass # same leaf value
            else:
                raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a
    
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
def delLog(god_id):
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

    new = {}
    new['guardian'] = {}
    new['guardian'][str(guardian_id)] = {}
    new['guardian'][str(guardian_id)]['guardian_name'] = guardian_name
    new['guardian'][str(guardian_id)]['guardian_pic'] = guardian_pic
    new['guardian'][str(guardian_id)]['permissions'] = {}

    merge(data,new)

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
def addPermission(god_id,guardian_id,child_id,name_lvl,pic_lvl,chore_lvl,wish_lvl,achieve_lvl):
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
        new['guardian'] = {}
        new['guardian'][str(guardian_id)] = {}
        new['guardian'][str(guardian_id)]['permissions'] = {}
        new['guardian'][str(guardian_id)]['permissions'][str(child_id)] = {}
        new['guardian'][str(guardian_id)]['permissions'][str(child_id)]['name'] = name_lvl
        new['guardian'][str(guardian_id)]['permissions'][str(child_id)]['pic'] = pic_lvl
        new['guardian'][str(guardian_id)]['permissions'][str(child_id)]['chore'] = chore_lvl
        new['guardian'][str(guardian_id)]['permissions'][str(child_id)]['wish'] = wish_lvl     
        new['guardian'][str(guardian_id)]['permissions'][str(child_id)]['achieve'] = achieve_lvl  
        merge(data,new)
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
# Remove Permission
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

# Get Guardian Permission lvl
def getPermission(god_id,guardian_id,child_id):
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

    new = {}
    new['children'] = {}
    new['children'][str(child_id)] = {}
    new['children'][str(child_id)]['child_name'] = child_name
    new['children'][str(child_id)]['child_pic'] = child_pic
    new['children'][str(child_id)]['points'] = 0
    new['children'][str(child_id)]['chore'] = {}
    new['children'][str(child_id)]['wish'] = {}
    new['children'][str(child_id)]['achievements'] = {}
    new['children'][str(child_id)]['permissions'] = {}
    new['children'][str(child_id)]['permissions']['name'] = "w"
    new['children'][str(child_id)]['permissions']['pic'] = "w"

    merge(data,new)
    
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0
# Delete Child
def delChild(god_id,guardian_id):
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
        del data['children'][str(guardian_id)]
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Child name GOD ACCOUNT ONLY
def childName(god_id,child_id,child_name):
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
    data['children'][str(child_id)]['child_name'] = child_name
    
    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Change Child Image GOD ACCOUNT ONLY
def childPic(god_id,child_id,child_pic):
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
    data['children'][str(child_id)]['child_pic'] = child_pic
    
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
delLog(101010)
#delGod(101010)

createGuardian(101010,12345,"Daniel Okazaki","sad_face.jpg")
createGuardian(101010,11111,"test","happy_face.jpg")
guardianName(101010,12345,"Gabe") 
guardianPic(101010,12345,"progress.jpg")
print(get_guardianName(101010,12345) )
print(get_guardianPic(101010,12345) )
addPermission(101010,12345,98765,"r","r","r","r","r")
addPermission(101010,12345,56789,"r","r","r","r","r")
guardian_namePerm(101010,12345,98765,"w")
guardian_picPerm(101010,12345,98765,"w")
guardian_chorePerm(101010,12345,98765,"w")
guardian_wishPerm(101010,12345,98765,"w")
guardian_achievePerm(101010,12345,98765,"w")
print(getPermission(101010,12345,56789))
#delPermission(101010,12345)
delGuardian(101010,11111)
#remPermission(101010,12345,56789)
createChild(101010,98765,"Mason Bruce","winning.jpg")
createChild(101010,56789,"Mickey H","programming.jpg")
delChild(101010,56789)
childPic(101010,98765,"Harry")
childName(101010,98765,"losing.jpg")



     