'''Generate a file name from Image props.  Mostly used to allow for
more complex descriptive naming schemes such as 1-1-rotate_90-contrast_0.2.png
'''
from imageprocessing.image_props import ImageProps
class NameGenerator(object):
    '''Generate a file name from Image props.  Mostly used to
    allow for more complex descriptive naming schemes such as
    1-1-rotate_90-contrast_0.2.png
    '''
    # pylint: disable=R0913
    # pylint: disable=R0902

    def __init__(self,
                 name='UNAMED.png',
                 klass=0,
                 image_props=ImageProps()):

        self._klass = klass
        self._image_props = image_props
        self._name = name

    def __eq__(self, other):
        '''Overrides the default implementation'''
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        '''Overrides the default implementation (unnecessary in Python 3)'''
        return not self.__eq__(other)

    @property
    def image_props(self):
        '''The image properties used to generate the name. If none
        this will initialize a new ImageProps object to use
        its default properties,  and provide a default file name
        `original` suffix.
        '''
        if not self._image_props:
            self._image_props = ImageProps()
        return self._image_props

    @property
    def name(self):
        '''The generated name from based on the font and image properties.
       '''
        self._name = "%s-%s-%s" % (self.image_props.klass,
                                   self._klass, self.image_props.name)
        return self._name
