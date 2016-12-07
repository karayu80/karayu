# connection
from boto.s3.connection import S3Connection
conn = S3Connection('AKIAJPW6EVHX5H25YHRA', '1Aver7vyi7/UhnO97pEaIt1C4Dil+Dtm7BF8zjuG')
conn = S3Connection()

import boto
conn = boto.connect_s3()

# create bucket
bucket = conn.create_bucket('kara_mybucket')

from boto.s3.connection import Location
print '\n'.join(i for i in dir(Location) if i[0].isupper())
conn.create_bucket('kara_mybucket_test', location=Location.DEFAULT)

# set data
from boto.s3.key import Key
k = Key(bucket)
k.key = 'foobar'
k.set_contents_from_string('This is a test of S3')

import boto
c = boto.connect_s3()
b = c.get_bucket('kara_mybucket')
from boto.s3.key import Key
k = Key(b)
k.key = 'foobar'
k.get_contents_as_string()
#'This is a test of S3'

k = Key(b)
k.key = 'myfile'
k.set_contents_from_filename('sss.jpg')
k.get_contents_to_filename('ggg.jpg')

# get key
import boto
c = boto.connect_s3()
b = c.get_bucket('kara_mybucket')

possible_key = b.get_key('myfile')
key_we_know_is_there = b.get_key('myfile', validate=False)


conn.get_all_buckets()
mybucket = conn.get_bucket('una-test3333333')
mybucket.get_all_keys()

# delete bucket
conn.delete_bucket('kara_mybucket')

full_bucket = conn.get_bucket('kara_mybucket')
for key in full_bucket.list():
    key.delete()

conn.delete_bucket('kara_mybucket')