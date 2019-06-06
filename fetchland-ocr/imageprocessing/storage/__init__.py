'''
Provides persistence support to Amazon S3 and local storage
'''
# disable line too long linter message
#pylint: disable=C0301
# from lib.mystringtools import camel_to_snake
# from lib.myerrors import ArgumentValidationError, InvalidArgumentNumberError, InvalidReturnType
from imageprocessing.lib.myio import FileWriter, make_sure_path_exists
from imageprocessing.storage.abstract_storage import AbstractStorage, StorageType
from imageprocessing.storage.aws_s3_storage import AwsS3
from imageprocessing.storage.mock_storage import MockStorage
from imageprocessing.storage.local_storage import Local
from imageprocessing.storage.storage_manager import StorageManager
