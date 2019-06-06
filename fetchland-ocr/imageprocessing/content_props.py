# -*- encoding: utf-8 -*-
'''Convenience class to store properties about content - image and text - used
to generate image data sets'''
from PIL import Image

class ContentProps(object):
    '''
    Stores and generates text and image content. `ContentProps`
    defauls to `text='A'` and an image with size (28, 28) pixel
    (color is black but with `alpha=0`it makes it invisible).
    '''
    def __init__(self,
                 text='A',
                 image=Image.new('RGBA', (28, 28), (255, 255, 255, 255)),
                 text_size=28,
                 image_size=(28, 28)):

        self._text = text
        self._image = image
        self._text_size = text_size
        self._image_size = image_size

    def __eq__(self, other):
        '''Overrides the default implementation of equal'''
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        '''Overrides the default implementation (unnecessary in Python 3)'''
        return not self.__eq__(other)

    @property
    def image(self):
        '''Image to be rendered'''
        return self._image

    @property
    def text(self):
        '''Character to be rendered'''
        return self._text

    @property
    def image_size(self):
        '''Size of the image '''
        return self._image_size

    @property
    def text_size(self):
        '''Size of the text'''
        return self._text_size

    @property
    def background_color(self):
        '''Size of the text'''
        return self._text_size

    # def __str__(self):
    #     attrs = vars(self)
    #     return '\n'.join("%s: %s" % item for item in attrs.items())
    