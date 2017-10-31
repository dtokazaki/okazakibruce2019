import boto3,json,io,datetime,botocore,collections,copy

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
def remGod(god_id):
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

    data['god']['log'].append({'time': datetime.date.now(tz=None),'message': message})

    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0
# Remove Log Entry
def remLog(god_id,time,message):
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
        data['god']['log'].remove({'time': time,'message': message}) 
    except:
        print("The object does not exist.")

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
def getGod_name(god_id):
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
def getGod_pic(god_id):
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

    int(guardian_id)
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
    new['guardian'][guardian_id] = {}
    new['guardian'][guardian_id]['guardian_name'] = guardian_name
    new['guardian'][guardian_id]['guardian_pic'] = guardian_pic
    #new['guardian'][guardian_id]['permissions'] = {}

    merge(data,new)
    #data = dict(data)
    #data.union(new)
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Delete Guardian
def remGuardian(god_id,guardian_id):
    s3 = boto3.client('s3')
    bucket_name = 'okazakibruce2019'
    filename = str(god_id) + ".json"
    int(guardian_id)

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
        del data['guardian'][guardian_id]
    except:
        return -1
    with open(filename,'w') as f:
        f.writelines(json.dumps(data))
    s3.upload_file(filename, bucket_name, filename)
    return 0

# Add Permission
def addPermission(god_id,guardian_id,child_id,chore_lvl,wish_lvl):
    s3 = boto3.client('s3')
    bucket_name = 'okazakibruce2019'
    filename = str(god_id) + ".json"
    int(guardian_id)
    int(child_id)

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
        #new = {}
        #new['guardian'] = {}
        #new['guardian'][guardian_id] = {}
        #new['guardian'][guardian_id]['permissions'] = {}
        #new['guardian'][guardian_id]['permissions'][child_id] = {}
        #new['guardian'][guardian_id]['permissions'][child_id]['chore'] = chore_lvl
        #new['guardian'][guardian_id]['permissions'][child_id]['wish'] = wish_lvl      
        #merge(data,new)

        new = copy.deepcopy(data)
        new['guardian'][guardian_id]['permissions'] = {}
        new['guardian'][guardian_id]['permissions'][child_id] = {}
        new['guardian'][guardian_id]['permissions'][child_id]['chore'] = chore_lvl
        new['guardian'][guardian_id]['permissions'][child_id]['wish'] = wish_lvl      

        #data.update({'guardian':{guardian_id: {'permissions': {child_id: {'chore': chore_lvl,'wish':wish_lvl}}}}})

        #data['guardian'][guardian_id]['permissions'][child_id] = {}

        #data['guardian'][guardian_id].append({'permissions'})

        #d = collections.defaultdict(list)
        #for k, v in data:
        #    d[k].append(v)
        #for k, v in new:
        #    d[k].append(v)
    except:
        return -1
    with open(filename,'w') as f:
        #f.writelines(json.dumps(data))
        f.writelines(json.dumps(new))
    s3.upload_file(filename, bucket_name, filename)
    return 0
# Get Guardian Name
def getGuardian_name(god_id,guardian_id):
    s3 = boto3.client('s3')
    bucket_name = 'okazakibruce2019'
    filename = str(god) + ".json"

    try:
        s3.download_file(bucket_name,filename,filename)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    with open(filename, 'r') as f:
        data = json.load(f)
    return data['guardian']['guardian_name']

# Get Guardian Image
def getGuardian_pic(god_id,guardian_id):
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
    return data['guardian']['guardian_pic']
createGod(101010,"Paul","thing.jpg")
#godName(101010,"John")
print(getGod_name(101010) )
print(getGod_pic(101010) )
#print(getGod_log(101010) )
#remGod(101010)
createGuardian(101010,12345,"Daniel Okazaki","sad_face.jpg")
createGuardian(101010,11111,"test","happy_face.jpg")
#remGuardian(101010,12345)
addPermission(101010,12345,98765,"r","r")
addPermission(101010,12345,56789,"r","r")

     