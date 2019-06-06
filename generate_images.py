'''
Command line interface to image generation.
'''
import copy
import os
import atexit
from enum import Enum
import fontconfig
import numpy
from imageprocessing.image_props import ImageProps
from imageprocessing.content_props import ContentProps
from imageprocessing.enhancement_props import EnhancementProps
from imageprocessing.font_props import FontProps
from imageprocessing.storage.local_storage import Local
from imageprocessing.storage.mock_storage import MockStorage
from PIL import Image, ImageFont, ImageDraw
from cleo import Command

class GenerateImages(Command):
    '''
    Generate images of characters.  Useful for training
    OCR engines.

    demo:greet
        {name? : Who do you want to greet?}
        {--y|yell : If set, the task will yell in uppercase letters}
    '''

    def handle(self):
        name = self.argument('name')

        if name:
            text = 'Hello %s' % name
        else:
            text = 'Hello'

        if self.option('yell'):
            text = text.upper()

        self.line(text)