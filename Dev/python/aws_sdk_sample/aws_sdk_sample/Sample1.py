# Import the SDK
import boto
import uuid

s3 = boto.connect_s3()

bucket_name = "python-sdk-sample-%s" % uuid.uuid4()
print "Creating new bucket with name: " + bucket_name
bucket = s3.create_bucket(bucket_name)

from boto.s3.key import Key
k = Key(bucket)
#k.key = 'python_sample_key'
#print "Uploading some data to " + bucket_name + " with key: " + k.key
#k.set_contents_from_string('Hello World!')

k.key = 'sample_img'
k.set_contents_from_filename('sss.jpg');

expires_in_seconds = 1800

print "Generating a public URL for the object we just uploaded. This URL will be active for %d seconds" % expires_in_seconds
print
print k.generate_url(expires_in_seconds)
print
raw_input("Press enter to delete both the object and the bucket...")

print "Deleting the object."
k.delete()

print "Deleting the bucket."
s3.delete_bucket(bucket_name)
