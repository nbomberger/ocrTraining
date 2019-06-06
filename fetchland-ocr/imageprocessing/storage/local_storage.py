# -*- encoding: utf-8 -*-
'''
Provide local storage configuration options and actions
for use with image processing module. It inherits from Storage.
'''
from imageprocessing.storage.abstract_storage import AbstractStorage, StorageType
from imageprocessing.lib.myutil import next_file_id, next_id, klass_id
from imageprocessing.lib.myio import make_sure_path_exists

class Local(AbstractStorage):
    '''Provide model to handle storage of image dataset'''
    # pylint: disable=R0913
    # pylint: disable=R0902
    def __init__(self,
                 image=None,
                 filename='local-unamed.png',
                 output_dir='data'):
        super(Local, self).__init__(image, filename, StorageType.local)
        self._output_dir = output_dir
        self.initialize()
        self._filename = "{0}/{1}-{2}.png".format(output_dir, klass_id(), filename)
        self.imagewriter = None

    def initialize(self):
        '''
        Check directory if it exists
        '''
        make_sure_path_exists(self._output_dir)
        
    @property
    def filename(self):
        '''
        formatted file name and path stored locall
        '''
        return "{0}/{1}-{2}.png".format(
            self._output_dir,
            klass_id(),
            next_file_id())

    @property
    def storage_type(self):
        return StorageType.local

    def save(self, data):
        '''Save the file to the chosen storage mechansim'''
        ## filename and type
        # super(Local, self).save(data)
        if not data:
            raise RuntimeError('Storage object requires PIL.Image in constructor')
        self._image = data
        self._image.save(self.filename)
        next_id()

    def load(self, filename='local-unamed.png'):
        '''
        Load file from local disk
        '''
        self.imagewriter.finish()
        print 'load file {0}'.format(filename)

    @property
    def image(self):
        '''
        Return Pillow Image (PIL.Image.Image)
        '''
        self._image = super(Local, self).image
        return self._image

    @image.setter
    def image(self, value):
        '''
        Return Pillow Image (PIL.Image.Image)
        '''
        self._image = super(Local, self).image(value)
        return self._image
