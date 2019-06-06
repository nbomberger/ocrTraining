# -*- encoding: utf-8 -*-
'''
The `FilterFactory` module takes in property type files
(end with Props) and applys the filter(s).
'''
import pdb
from enum import Enum
import copy
import numpy
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

class FilterType(Enum):
    '''
    These are the supported enhancements that can be
    generated.
    '''
    rotation = 0
    color_adjust = 1
    contrast = 2
    sharpness = 3
    brightness = 4
    noise = 5
    unsharpen = 6
    blur = 7
    transpose = 8
    solarize = 9

class FilterFactory(object):
    '''
    Takes in props and generates applies the appropriate
    action to the image.  This can be chainged together.
    '''
    # pylint: disable=R0913
    # pylint: disable=R0902

    def __init__(self,
                 image=None,
                 enhancemnt_props=None):

        self._image = image
        self._enhancement_props = enhancemnt_props

    @property
    def image(self):
        '''
        Return an image
        '''
        return self._image

    @image.setter
    def image(self, image):
        '''
        Set the image
        '''
        self._image = image

    def apply(self):
        '''
        Applies the enhancement to the image.
        This calls a dispatcher that then applies the
        filter
        '''
        # do something
        print '* Applying filter...'
        if self._enhancement_props:
            self.rotate()
            self.transpose()
            self.contrast()
            self.sharpness()
            self.brightness()
            self.color_adjust()

        self.solarize()
        return self.image

    def process(self):
        '''
        Swith logic here
        '''
        print 'process not implemented'


    def noise(self,
              multiple=3,
              contrast=355,
              alpha=0.25):
        '''
        Add randomized pixels to image
        '''
        if multiple < 2 or multiple is None or multiple > 4:
            raise ValueError('Contrast thingy can only be 2, 3 , or 4')

        # pylint: disable=E1101
        imarray = numpy.random.rand(28, 28, multiple) * contrast
        img = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
        img = copy.deepcopy(img)
        self._image = Image.blend(self._image, img, alpha=alpha)
        return self

    def rotate(self, background_color=(150, 150, 150, 120)):
        '''
        Rotate image
        '''
        if self._enhancement_props:
            if  self._enhancement_props.rotation != 0:
                print '---> rotation: {0}'.format(self._enhancement_props.rotation)
                self._image = self.image.rotate(self._enhancement_props.rotation)
                canvas = Image.new('RGBA', (28, 28), background_color)
                canvas.paste(self.image)
                self._image = canvas
        return self

    def transpose(self):
        '''
        Transpose image (flip or rotate in 90 degree steps)
        '''
        if self._enhancement_props.transpose:
            print '---> tranpose: {0}'.format(self._enhancement_props.transpose)
            self._image  = self.image.transpose(self._enhancement_props.transpose)
        return self

    def contrast(self):
        '''
        Contrast image
        '''
        if self._enhancement_props.contrast and \
            self._enhancement_props.contrast != 1.0:
            print '---> contrast: {0}'.format(self._enhancement_props.contrast)
            enh = ImageEnhance.Contrast(self.image)
            self._image = enh.enhance(self._enhancement_props.contrast)
        return self

    def sharpness(self):
        '''
        Adjust sharpness of an image.  ranage (0.0..2.0)
        '''
        if self._enhancement_props.sharpness and \
            self._enhancement_props.sharpness != 1.0:
            enh = ImageEnhance.Sharpness(self.image)
            print '---> sharpness: {0}'.format(self._enhancement_props.sharpness)
            self._image = enh.enhance(self._enhancement_props.sharpness)
        return self

    def brightness(self):
        '''
        Adjust brightness of an image.  ranage (0.0..1.0)
        '''
        if self._enhancement_props.brightness and \
            self._enhancement_props.brightness != 1.0:
            enh = ImageEnhance.Brightness(self.image)
            print '---> brightness: {0}'.format(self._enhancement_props.brightness)
            self._image = enh.enhance(self._enhancement_props.brightness)
        return self

    def color_adjust(self):
        '''
        Color adjust of an image.  ranage (0.0..1.0)
        '''
        if self._enhancement_props.color_adjust and \
            self._enhancement_props.brightness != 1.0:
            print '---> color_adjust: {0}'.format(self._enhancement_props.color_adjust)
            enh = ImageEnhance.Color(self.image)
            self._image = enh.enhance(self._enhancement_props.color_adjust)
        return self

    # No enhancment props needed
    def grayscale(self):
        '''Covert image to grayscale (bitonal)'''
        print '===> grayscale'
        self._image = ImageOps.grayscale(self.image)
        return self

    def invert(self):
        '''Invert image to grayscale (bitonal)'''
        print '===> invert'
        self._image = ImageOps.grayscale(self.image)
        return self

    def equalize(self):
        '''
        Equalize the image histogram. This function applies a non-linear
        mapping to the input image, in order to create a uniform distribution
        of grayscale values in the output image.
        '''
        print '===> equalize'
        self._image = ImageOps.equalize(self.image, mask=None)
        return self

    def colorize(self):
        '''Covert image to grayscale (bitonal)'''
        print '===> colorize'
        self._image = ImageOps.colorize(
            self.image,
            black=(0, 0, 0, 255),
            white=(255, 255, 255, 255))
        return self

    def flip(self):
        '''Flip the image vertically (top to bottom).'''
        print '===> flip'
        self._image = ImageOps.flip(self.image)
        return self

    def mirror(self):
        '''Flip horizontally (left to right)'''
        self._image = ImageOps.mirror(self.image)
        return self

    def posterize(self):
        '''Reduce the number of bits for each color channel.'''
        print '===> posterize'
        self._image = ImageOps.posterize(self.image, bits=6)
        return self

    def solarize(self):
        '''Invert all pixel values above a threshold.'''
        print '===> solarize'
        if self._enhancement_props and self._enhancement_props.solarize:
            tmp = self._image.convert('RGB')
            result = ImageOps.solarize(tmp, threshold=128)
            self._image = result.convert('RGBA')
        return self

    def auto_contrast(self):
        '''Covert image to grayscale (bitonal)'''
        print '===> auto_contrast'
        self._image = ImageOps.grayscale(self.image)
        return self

    # filters
    #
    def blur(self, threshold=2):
        self._image = self._image.filter(ImageFilter.GaussianBlur(threshold))
        return self

    def blur2(self):
        self._image = self._image.filter(ImageFilter.BLUR)
        return self

    def contour(self):
        self._image = self._image.filter(ImageFilter.CONTOUR)
        return self

    def unsharpen(self, radius=2, percent=150, threshold=3):
        self._image = self._image.filter(ImageFilter.UnsharpMask(
            radius,
            percent,
            threshold))
        return self

    def emboss(self):
        self._image = self._image.filter(ImageFilter.EMBOSS)
        return self

    def __str__(self):
        attrs = vars(self)
        desc = '\n'.join("%s: %s" % item for item in attrs.items())
        return desc
