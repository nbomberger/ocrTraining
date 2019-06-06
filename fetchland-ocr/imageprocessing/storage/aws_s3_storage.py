# -*- encoding: utf-8 -*-
'''Provide model to handle storage of image dataset.

This module should be responsible for interfacing with
any storage - S3, local disk.  It should also handle
saving, and retrieving data from a specific bucket on S3.

Internally this uses `boto3`, a python wrapper aroudn a few
AWS functions.

**`Note:`** Make sure to set up AWS credentials or this will
not work.
'''
import pdb
import boto3
from imageprocessing.storage.abstract_storage import AbstractStorage, StorageType

class AwsS3(AbstractStorage):
    '''Provide model to handle storage of image dataset'''
    aws_s3 = boto3.resource('s3')
    def __init__(self,
                 image=None,
                 bucket=None,
                 filename=None,
                 root_folder='training_data'):

        super(AwsS3, self).__init__(image, filename, StorageType.aws_s3)
        self._bucket = bucket
        self._root_folder = root_folder

    @property
    def image(self):
        return self.image

    def save(self, data=None):
        '''Save the file to the chosen storage mechanism'''
        if not self.image:
            raise RuntimeError('Storage object requires PIL.Image in constructor')
        pdb.set_trace()  
        # tmp = self.bytes.read()
        # byt = BytesIO(tmp)
        # buk = self.bucket_name
        # self._bucket.put_object(
        #     Bucket=self.bucket_name,
        #     Key=
        #     Body=Image.open(byt))
        # in_memory_file = BytesIO()
        # img.imwrite(in_memory_file)
        # obj = bucket.Object(filepath+'/'+second+'.jpg')
        # obj.upload_fileobj(in_memory_file)
                
        # data = open(self., 'rb')
        #     s3.Bucket(self._bucket).put_object(Key='test.jpg', Body=data)

    def load(self, filename=None):
        '''
        Load data from S3
        '''
        if not self.image:
            raise RuntimeError('Storage object requires PIL.Image in constructor')

    def storage_type(self):
        '''
        Returns type of storage (StorageType.aws_s3)
        '''
        return StorageType.aws_s3

    def bucket(self):
        '''
        List available buckets on aws.  Useful for debugging and setup.
        '''
        return self.aws_s3.bucket(self._bucket)

    def buckets(self):
        '''
        List available buckets on aws.  Useful for debugging and setup.
        '''
        return self.aws_s3.buckets.all()
