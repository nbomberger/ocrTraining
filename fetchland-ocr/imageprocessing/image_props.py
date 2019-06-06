# -*- encoding: utf-8 -*-
'''A convenience class that provides properties to use in transforming images objects'''
import pdb
from imageprocessing.enhancement_props import EnhancementProps
class ImageProps(object):
    '''A convenience class that provides properties to use in transforming images objects'''

    # pylint: disable=R0913
    # pylint: disable=R0902
    def __init__(self,
                 name='original',
                 enhancement_props=EnhancementProps(),
                 background_color=(255, 255, 255, 255)):

        self._name = name
        self._enhancement_props = enhancement_props
        self._background_color = background_color

    def __eq__(self, other):
        '''Overrides the default implementation'''
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        '''Overrides the default implementation (unnecessary in Python 3)'''
        return not self.__eq__(other)

    @property
    def name(self):
        '''Name of the image property state'''
        pdb.set_trace()
        if self._enhancement_props.name:
            return self._enhancement_props.name
        return self._name

    @property
    def background_color(self):
        '''Background color on the image'''
        return self._background_color

    def rotation(self):
        '''degrees of rotation, counter clockwise'''
        return self._enhancement_props.rotation

    def contrast(self):
        '''Change contrast of image from 0.0...1.0'''
        return self._enhancement_props.contrast

    def sharpness(self):
        '''Change sharepness of image from 0.0...1.0....2.0'''
        return self._enhancement_props.sharpness

    def brightness(self):
        '''Change brigthness of image from 0.0...1.0'''
        return self._enhancement_props.brightness

    def color_adjust(self):
        '''Change brigthness of image from 0.0...1.0'''
        return self._enhancement_props.color_adjust

    def size(self):
        '''Tuple (width, height) Size of image '''
        return self._enhancement_props.size

    def __str__(self):
        attrs = vars(self)
        return '\n'.join("%s: %s" % item for item in attrs.items())
    