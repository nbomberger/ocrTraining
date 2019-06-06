# -*- encoding: utf-8 -*-
'''
Provide mock storage configuration options and actions
for use with image processing module. Useful for debugging
and testing.
'''
from imageprocessing.storage.abstract_storage import AbstractStorage, StorageType

class MockStorage(AbstractStorage):
    '''Provide model to handle storage of image dataset'''
    # pylint: disable=R0913
    # pylint: disable=R0902
    def __init__(self,
                 image=None):

        super(MockStorage, self).__init__(image, "MOCKED", StorageType.mock)
        self._image = image

    @property
    def image(self):
        '''
        Returns the image to be saved.
        '''
        return self._image

    @image.setter
    def image(self, val):
        '''
        Returns the image to be saved.
        '''
        self._image = val

    def save(self, filename='MOCKED-FILENAME'):
        '''Save the file to the chosen storage mechansim'''
        if not self.image:
            raise RuntimeError('Storage object requires PIL.Image in constructor')

        print 'MOCK STORAGE SAVED: {0}'.format(filename)

    def load(self, filename='MOCKED-FILENAME'):
        '''Fake loading of a file'''
        if not self.image:
            raise RuntimeError('Storage object requires PIL.Image in constructor')
        print 'MOCK STORAGE LOADED: {0}'.format(filename)

    def storage_type(self):
        return StorageType.mock