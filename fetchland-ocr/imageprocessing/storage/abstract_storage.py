# -*- encoding: utf-8 -*-
'''Provide model to handle storage of image dataset.

This module should be responsible for interfacing with
any storage - S3, local disk.  It should also handle
saving, and retrieving data.

This module stores the image in a ByteIO proxy to allow swapping
of the storage device at runtime.
'''
import pdb
from abc import ABCMeta, abstractmethod, abstractproperty
from enum import Enum
from io import BytesIO
from PIL import Image

class StorageType(Enum):
    '''
    Enumerated storage types.
    '''
    local = 0 # to disk
    aws_s3 = 1 # to s3
    mock = 2 # doesn't save but prints message

'''
TODO: Create way to serialize them to bytes
from io import BytesIO
from PIL import Image, ImageDraw

image = Image.new("RGB", (28, 28))
draw = ImageDraw.Draw(image)
draw.text((0, 0), "This text is drawn on image")

byte_io = BytesIO()

image.save(byte_io, 'PNG')
'''
class AbstractStorage:
    '''Provide abstraction model to handle storage of image dataset.
    Storage mechanisms should implement this class'''
    __metaclass__ = ABCMeta

    def __init__(self, image, filename, storage_type):
        self._filename = filename
        self._storage_type = storage_type
        self._image = image
        self._bytes = BytesIO()
        if self._image:
            self._image.save(self._bytes, 'PNG')

    @property
    def bytes(self):
        '''
        returns bytes
        '''
        return self._bytes

    @bytes.setter
    def bytes(self, value):
        '''
        returns bytes
        '''
        pdb.set_trace()
        self._bytes = value

    @property
    def filename(self):
        '''
        The image to be saved
        '''
        return self._filename

    @filename.setter
    def filename(self, val):
        '''
        The image to be saved
        '''
        self._filename = val

    @property
    def image(self):
        '''
        The image to be saved. We use bytes as a proxy
        so that we can provide the client with more saving options
        '''
        self.bytes.seek(0)
        tmp = self.bytes.read()
        byt = BytesIO(tmp)
        return Image.open(byt)

    @image.setter
    def image(self, image):
        '''
        The image to be saved
        '''
        image.save(self._bytes, 'PNG')

    @abstractproperty
    def storage_type(self):
        '''This function returns the string name for the
            return 'S3'
        '''
        return self._storage_type

    @abstractmethod
    def save(self, data):
        '''
        Saves the the specificed storage device (S3, Local)
        '''
        pass

    @abstractmethod
    def load(self, filename='unamed'):
        '''
        Loads the filename
        '''
        pass


    def __str__(self):
        attrs = vars(self)
        return '\n'.join("%s: %s" % item for item in attrs.items())
