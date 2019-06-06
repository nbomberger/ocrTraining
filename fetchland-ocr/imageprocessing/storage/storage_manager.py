# -*- encoding: utf-8 -*-
'''
Provides universal storage mechanism to allow switching between
aws and local disk.
'''
from imageprocessing.storage.abstract_storage import StorageType
from imageprocessing.storage.aws_s3_storage import AwsS3 
from imageprocessing.storage.local_storage import Local

class StorageManager(object):
    '''Provide model to handle storage of image dataset'''
    # pylint: disable=R0913
    # pylint: disable=R0902
    def __init__(self, storage_type=None):
        self._storage_type = storage_type

    @property 
    def storage_type(self):
        '''
        Provide storage type
        '''
        return self._storage_type

    @storage_type.setter
    def storage_type(self, value):
        '''
        Change the default storage location
        '''
        self._storage_type = value

        

    def setup(self):
        '''
        Check directory if it exists
        '''
        if self._storage_type is StorageType.aws_s3:
            return AwsS3()

        if self._storage_type is StorageType.aws_s3:
            return AwsS3()