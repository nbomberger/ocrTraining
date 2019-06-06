
# -*- encoding: utf-8 -*-
'''A convenience class that provides properties that can change in the image'''
import json
class EnhancementProps:
    '''A convenience class that provides properties that can change in the image'''
    # pylint: disable=R0913
    # pylint: disable=R0902
    def __init__(self,
                 name='original',
                 rotation=0,
                 contrast=1.0,
                 brightness=1.0,
                 color_adjust=1.0,
                 sharpness=1.0,
                 size=(28, 28),
                 noise=None,
                 transpose=None,
                 blur=None,
                 unsharpen=None,
                 solarize=None):
        self._name = name
        self._rotation = rotation
        self._contrast = contrast
        self._color_adjust = color_adjust
        self._sharpness = sharpness
        self._brightness = brightness
        self._size = size
        self._noise = noise 
        self._transpose = transpose
        self._blur = blur 
        self._unsharpen = unsharpen 
        self._solarize = solarize


    def __eq__(self, other):
        '''Overrides the default implementation'''
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        '''Overrides the default implementation (unnecessary in Python 3)'''
        return not self.__eq__(other)

    @property
    def transpose(self):
        '''
        
        '''
        return self._transpose

    @transpose.setter
    def transpose(self, transpose):
        self._transpose = transpose

    @property
    def noise(self):
        '''Sets a variance of background noise'''
        return self._noise

    @noise.setter
    def noise(self, value):
        '''Sets a variance of background noise'''
        self._noise = value

    @noise.setter
    def noise(self, amp, freq):
        '''Sets a variance of background noise'''
        self._noise = (amp, freq)

    @property
    def name(self):
        '''Name of the image property state'''
        return self._name

    @property
    def rotation(self):
        '''degrees of rotation, counter clockwise'''
        return self._rotation

    @property
    def contrast(self):
        '''Change contrast of image from 0.0...1.0'''
        return self._contrast

    @property
    def sharpness(self):
        '''Change sharepness of image from 0.0...1.0....2.0'''
        return self._sharpness

    @property
    def brightness(self):
        '''Change brigthness of image from 0.0...1.0'''
        return self._brightness

    @property
    def color_adjust(self):
        '''Change brigthness of image from 0.0...1.0'''
        return self._color_adjust

    @property
    def size(self):
        '''Tuple (width, height) Size of image '''
        return self._size

    @property
    def solarize(self):
        ''' Solarize the image'''
        return self._solarize

    @property
    def blur(self):
        ''' Blur the image'''
        return self._blur

    def to_json(self):
        '''
        Convert to json output
        '''
        return json.dumps(self, default=lambda o: o.__str__, 
            sort_keys=True, indent=4)

    def __str__(self):
        attrs = vars(self)
        return ','.join("%s: %s" % item for item in attrs.items())
    