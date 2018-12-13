
import boto3

#aws_access_key_id = AKIAIF4RYNPRSNUTI6FA
#aws_secret_access_key = uFiFHKn3ADI1zQLAVbPD5vbBnUzvtvGzsRZ2M83
#region=us-west-1


# Create an S3 client
s3 = boto3.client('s3')

# Call S3 to list current buckets
response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)

print("This is a test")