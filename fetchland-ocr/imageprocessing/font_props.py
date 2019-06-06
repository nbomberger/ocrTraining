# -*- encoding: utf-8 -*- #
'''Convenience class to store properties about fonts that will be used
to generate image data sets'''
import sys
import os
import pdb
import fontconfig
from PIL import ImageFont
from imageprocessing.lib.mystringtools import camel_to_snake
# pylint: disable=E1101

def clean_fonts(fonts):
    '''Clean up bad fonts that have non ascii characters - no need to use them'''
    if not isinstance(fonts, list):
        raise AttributeError(
            'Clean font requires a list inorder to remove fonts that break the workflow')
    try:
        fonts.remove(u"/System/Library/Fonts/ヒラギノ角ゴシック W0.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ明朝 ProN.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ明朝 ProN.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ角ゴシック W1.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ角ゴシック W2.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ角ゴシック W7.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ角ゴシック W8.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ角ゴシック W8.ttc")
        fonts.remove(u"/System/Library/Fonts/ヒラギノ角ゴシック W9.ttc")
        return fonts
    except ValueError:
        pass # or scream: thing not in some_list!
    except AttributeError:
        print "Unexpected error:", sys.exc_info()[0]


class FontProps(object):
    '''A convenience class that provides properties to use modifying fonts for images objects'''
    @staticmethod
    def all_fonts():
        '''
        Factory method to create a FontProp instance. Must be of type fontconfig.FcFconfig.
        '''
        fontconfig_objects = clean_fonts(fontconfig.query(lang='en'))

        all_fonts = []
        for idx, _ in enumerate(fontconfig_objects):
            all_fonts.append(FontProps.create(font=fontconfig_objects[idx]))
            
        return all_fonts
    @staticmethod
    def create(font=None, color=(0, 0, 0, 255), size=29):
        '''
        Factory method to create a FontProp instance. Must be of type fontconfig.FcFconfig.
        '''
        if not font:
            font = fontconfig.query(lang='en')[12]
        return FontProps(font, color, size)

    def __init__(self,
                 font=None,
                 color=(0, 0, 0, 255),
                 size=29):

        self._font = font
        if not self._font:
            self._font = fontconfig.query(lang='en')[0]

        try:
            (_, fontname) = self._font.fullname[0]
        except IndexError:
            self._font = fontconfig.query(lang='en')[0]
            (_, fontname) = self._font.fullname[0]
        except UnicodeEncodeError:
            self._font = fontconfig.query(lang='en')[0]
            (_, fontname) = self._font.fullname[0]

        self._color = color
        self._size = size

    def __eq__(self, other):
        '''Overrides the default implementation'''
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        '''Overrides the default implementation (unnecessary in Python 3)'''
        return not self.__eq__(other)

    @property
    def color(self):
        '''Font color'''
        return self._color

    @property
    def size(self):
        '''Size of the font'''
        return self._size

    @property
    def image_font(self):
        '''Generates a PIL ImageFont object'''
        image_font = None
        try:
            image_font = ImageFont.truetype(self.filename(), self._size)
        except:
            raise TypeError('Unable to create ImageFont.')
        return image_font 

    @property
    def font(self):
        '''Property that represents current fontconfig.FcFont object'''
        return self._font

    def fontname(self):
        '''Function that retuns unicode file path location'''
        return str(os.path.basename(str(self._font.file)))

    def name(self):
        '''Function that returns the basename of the font with the extension'''
        (_name, _ext) = os.path.splitext(self.filename())
        return _name
    
    def filename(self):
        '''
        returns the full filename including path
        '''
        return self._font.file
    
    def foldername(self):
        '''Function that returns the name of the font.  It lowercases the string,
        strips out any spaces and replaces with "-" '''
        (_name, _ext) = os.path.splitext(self.filename())
        return camel_to_snake(_name).lower()

    def __str__(self):
        attrs = vars(self)
        return '\n'.join("%s: %s" % item for item in attrs.items())
  