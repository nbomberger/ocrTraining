# -*- coding: utf-8 -*-
'''Image Generator

This module's main objective is to generate images bsaed on passing
in ImageProps.  `ImageProps` can be initialized with `FontProps` and and
`ImageEnhancement`.

Example:
    In order to generate images, static methods that create ImageGenerator
    objects publicly available and should be the only interface needed to
    generate a character dataset.

        ImageGenerator.generate_images_by_enhancement(
            ['a', 'B'],
        )

`ImageEnhancemnt` holds all the image variations that are possible.  The

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

    Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html
'''
import copy
from enum import Enum
import fontconfig
import pdb
from imageprocessing.image_props import ImageProps
from imageprocessing.content_props import ContentProps
from imageprocessing.enhancement_props import EnhancementProps
from imageprocessing.font_props import FontProps
from imageprocessing.storage.local_storage import Local
from imageprocessing.filter_factory import FilterFactory
from imageprocessing.lib.myutil import next_file_id, next_klass_id, klass_id
from PIL import Image, ImageDraw

class LifeCycle(Enum):
    '''
    Tells what state the generate is in.  Helpful to make sure
    we hit our pipeline properly.
    '''
    init = 0
    initialize = 1
    background_color_added = 2
    background_noise_added = 3
    text_added = 4
    enhancements_applied = 5
    saved = 6

class ImageGenerator(object):
    '''
    This class provides a fluid interface to image manipulation.  The purpose
    is to generate images of fonts.  Those images are then fed into an OCR to
    create a model.

    This class has way too much responsiblity, but for now it works.

    TODO: Move filters to Filter factory
    TODO: Add a WorkFlow protocol to allow FilterFactory and Generator to work
          together
    '''
    def __init__(self,
                 content_props=None,
                 image_props=None,
                 font_props=None,
                 storage=None):
        self._content_props = content_props
        self._image_props = image_props
        self._font_props = font_props
        self._storage = storage
        self._image = content_props.image
        self._state = {}
        self._state[LifeCycle.init] = 'COMPLETED'

    @staticmethod
    def for_font(characters, font):
        '''
        Generate image set for tons
        '''
        for character in characters:
            ImageGenerator.for_character(
                character=character
            ) 
    @staticmethod
    def with_characters_and_fonts(characters, font_props=None):
        '''
        Generate image set based on list of characters
        '''
        if not font_props:
            raise AttributeError('`font_props` must be a list of font_props')
        print len(font_props)
        for character in characters:
            for props in font_props:
                ImageGenerator.for_character(
                    character=character,
                    font_props=props
                )
            next_klass_id()

    @staticmethod
    def for_characters(characters, font_props=None):
        '''
        Generate image set based on list of characters
        '''
        if not font_props:
            font_props = FontProps()
        for character in characters:
            ImageGenerator.for_character(
                character=character,
                font_props=font_props
            )
    @staticmethod
    def for_character(character, font_props=None):
        '''Statically called method that takes a list of characters, generates the data set
        This is equivalent to a main processing function and is the entry point for outside
        integration'''

        if not isinstance(character, str) and not isinstance(character, int):
            raise TypeError('Must be of type str or integer ')

        print "\n===> Generating images for character {0} <===\n".format(character)
        rotation_enhancements = [
            EnhancementProps(name='original'),
            EnhancementProps(name='rotate_45',
                             rotation=45),
            EnhancementProps(name='rotate_90',
                             rotation=90),
            EnhancementProps(name='rotate_135',
                             rotation=135),
            EnhancementProps(name='rotate_180',
                             rotation=180),
            EnhancementProps(name='rotate_225',
                             rotation=225),
            EnhancementProps(name='rotate_270',
                             rotation=270),
            EnhancementProps(name='rotate_315',
                             rotation=315)
        ]
        contrast_enhancements = [
            EnhancementProps(name='original'),
            EnhancementProps(name='contrast_045',
                             contrast=0.81),
            EnhancementProps(name='contrast_055',
                             brightness=1.0,
                             contrast=0.85),
            EnhancementProps(name='contrast_065',
                             contrast=0.75),
            EnhancementProps(name='contrast_075',
                             contrast=0.86),
            EnhancementProps(name='contrast_085',
                             contrast=0.90)
        ]
        sharpness_enhancements = [
            EnhancementProps(name='sharpness',
                             brightness=1.0,
                             sharpness=0.8),
            EnhancementProps(name='sharpness',
                             sharpness=0.8),
            EnhancementProps(name='sharpness',
                             sharpness=0.6),
            EnhancementProps(name='sharpness',
                             brightness=1.0,
                             sharpness=0.8),
            EnhancementProps(name='sharpness',
                             sharpness=0.9),
            EnhancementProps(name='sharpness',
                             sharpness=1.2),
            EnhancementProps(name='sharpness',
                             sharpness=1.4),
            EnhancementProps(name='sharpness',
                             sharpness=1.5),
            EnhancementProps(name='sharpness',
                             sharpness=1.6),
        ]
        solarize_enhancement = [
            EnhancementProps(name='solarize',
                             solarize=True)
        ]

        brightness_enhancements = [
            EnhancementProps(brightness=0.85),
            EnhancementProps(brightness=0.94),
            EnhancementProps(brightness=0.93),
            EnhancementProps(brightness=0.92),
            EnhancementProps(brightness=0.91),
        ]

        content_props = ContentProps(text=character)

        enhancement_prop = EnhancementProps(name=None)

        storage = Local(content_props.image)
        image_props = ImageProps()

        generator = ImageGenerator(
            content_props=content_props,
            image_props=image_props,
            font_props=font_props,
            storage=storage)

        # GENERATE BACKGROUND COLORS
        (generator.initialize()
          .add_background_color(
            background_color=(90, 50, 20, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=0)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(0, 70, 140, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-1)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(140, 70, 0, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-2)
         .save())
        
        (generator.initialize()
          .add_background_color(
            background_color=(140, 175, 255, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save())

          
        (generator.initialize()
          .add_background_color(
            background_color=(60, 170, 40, 255))
         .draw_text(
             horizontal_offset=1,
             vertical_offset=-3)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(100, 255, 90, 255))
         .draw_text(
             horizontal_offset=2,
             vertical_offset=-3)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(180, 25, 25, 255))
         .draw_text(
             horizontal_offset=-1,
             vertical_offset=-3)
         .save())

        # GENERATE NOISE
        (generator.initialize()
          .add_background_color(
            background_color=(120, 120, 120, 255))
         .draw_text(
             horizontal_offset=-2,
             vertical_offset=-3)
         .add_background_noise(3, 255, 0.4)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(90, 50, 20, 255))
         .draw_text(
             horizontal_offset=-1,
             vertical_offset=-2)
         .add_background_noise(3, 255, 0.4)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(0, 70, 140, 255))
         .draw_text(
             horizontal_offset=2,
             vertical_offset=1)
         .add_background_noise(3, 255, 0.4)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(140, 70, 0, 255))
         .draw_text(
             horizontal_offset=1,
             vertical_offset=-1)
         .add_background_noise(3, 255, 0.4)
         .save())
        
        (generator.initialize()
          .add_background_color(
            background_color=(140, 175, 255, 255))
         .draw_text(
             horizontal_offset=2,
             vertical_offset=-2)
         .add_background_noise(3, 255, 0.4)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(60, 170, 40, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .add_background_noise(3, 255, 0.4)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(100, 255, 90, 255))
         .draw_text(
             horizontal_offset=1,
             vertical_offset=-2)
         .add_background_noise(3, 255, 0.4)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(180, 25, 25, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-0)
         .add_background_noise(3, 255, 0.3)
         .save())

        # Noise and rotation
        (generator.initialize()
          .add_background_color(
            background_color=(120, 120, 120, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=0)
         .add_background_noise(3, 255, 0.4)
         .save()
         .apply_enhancements(rotation_enhancements))

        (generator.initialize()
          .add_background_color(
            background_color=(90, 50, 20, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .add_background_noise(3, 255, 0.5)
         .save()
         .apply_enhancements(rotation_enhancements))

        (generator.initialize()
          .add_background_color(
            background_color=(0, 70, 140, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .add_background_noise(3, 255, 0.5)
         .save()
         .apply_enhancements(rotation_enhancements)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(140, 70, 0, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .add_background_noise(3, 255, 0.5)
         .save()
         .apply_enhancements(rotation_enhancements))
        
        (generator.initialize()
          .add_background_color(
            background_color=(140, 175, 255, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .add_background_noise(3, 255, 0.5)
         .save()
         .apply_enhancements(rotation_enhancements))

        (generator.initialize()
          .add_background_color(
            background_color=(60, 170, 40, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .add_background_noise(3, 255, 0.5)
         .save()
         .apply_enhancements(rotation_enhancements))

        (generator.initialize()
          .add_background_color(
            background_color=(100, 255, 90, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .add_background_noise(3, 255, 0.5)
         .save()
         .apply_enhancements(rotation_enhancements)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(180, 25, 25, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .add_background_noise(3, 255, 0.5)
         .save()
         .apply_enhancements(rotation_enhancements)
         .save())

        (generator.initialize()
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .apply_enhancements(rotation_enhancements))
        

        (generator.initialize()
          .add_background_color(
            background_color=(100, 100, 100, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .apply_enhancements(rotation_enhancements))

        (generator.initialize()
          .add_background_color(
            background_color=(120, 120, 120, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .apply_enhancements(sharpness_enhancements))

        (generator.initialize()
          .add_background_color(
            background_color=(140, 140, 140, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .apply_enhancements(sharpness_enhancements))

        (generator.initialize()
          .add_background_color(
            background_color=(90, 90, 90, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .apply_enhancements(contrast_enhancements))

        (generator.initialize()
          .add_background_color(
            background_color=(50, 50, 50, 156))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()            
         .apply_enhancements([enhancement_prop])
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(70, 60, 30, 175))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()            
         .apply_enhancements([enhancement_prop]))

       
        (generator.initialize()
         .add_background_color(
            background_color=(0, 128, 255, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .to_blur(1)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(98, 170, 200, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .apply_enhancements([enhancement_prop])
         .to_blur(1)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(40, 50, 175, 125))
         .add_background_noise(3, 333, 0.33)
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .to_blur(1)
         .save())

        (generator.initialize()
          .add_background_color(
            background_color=(40, 50, 175, 125))
         .add_background_noise(3, 333, 0.20)
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .apply_enhancement(enhancement_prop)
         .save())
         
        (generator.initialize()
         .add_background_color(
            background_color=(10, 100, 200, 200))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .apply_enhancements(brightness_enhancements))

        (generator.initialize()
          .add_background_color(
            background_color=(102, 51, 0, 255))
         .add_background_noise(3, 333, 0.33)
          .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .to_blur(1)
         .apply_enhancements(sharpness_enhancements))

        (generator.initialize()
          .add_background_color(
            background_color=(255, 51, 102, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .initialize()
         .add_background_noise(3, 104, 0.10)
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .to_blur(1)
         .apply_enhancements(sharpness_enhancements))

        (generator.initialize()
          .add_background_color(
            background_color=(5, 51, 102, 128))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .add_background_noise(3, 444, 0.44)
         .save()
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .apply_enhancements(sharpness_enhancements))

        (generator.initialize()
          .add_background_color(
            background_color=(128, 0, 255, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .initialize()
         .add_background_noise(3, 235, 0.30)
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .to_blur(1)
         .apply_enhancements(sharpness_enhancements)
         .to_grayscale()
         .save())
         
        (generator.initialize()
          .add_background_color(
            background_color=(128, 50, 25, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .add_background_noise(3, 235, 0.65)
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .apply_enhancements(sharpness_enhancements))

        (generator.initialize()
         .add_background_color(
            background_color=(128, 255, 0, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .add_background_noise(3, 605, 0.30)
         .save()
         .to_bitonal_image()
         .save()
         .apply_enhancement(brightness_enhancements[0])
         .to_grayscale()
         .save()
         .apply_enhancements(sharpness_enhancements)
         .save()
         .apply_enhancement(brightness_enhancements[2])
         .save())
        
        (generator.initialize()
         .add_background_color(
            background_color=(128, 255, 0, 255))
         .add_background_noise(3, 605, 0.50)
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .to_blur(1)
         .apply_enhancement(brightness_enhancements[3])
         .save()
         .apply_enhancement(brightness_enhancements[4])
         .save()
         .apply_enhancement(brightness_enhancements[2])
         .save())

        (generator.initialize()
         .add_background_color(
            background_color=(128, 255, 0, 255))
         .add_background_noise(3, 605, 0.50)
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-1)
         .to_blur(1)
         .apply_enhancement(brightness_enhancements[2])
         .save()
         .apply_enhancement(brightness_enhancements[3])
         .save()
         .apply_enhancement(brightness_enhancements[4])
         .save()) 


        (generator.initialize()
         .add_background_color(
            background_color=(200, 30, 128, 255))
         .add_background_noise(3, 100, 0.25)
         .draw_text(
             horizontal_offset=-2,
             vertical_offset=0)
         .apply_enhancements(rotation_enhancements)
         .apply_enhancement(brightness_enhancements[2])
         .save()) 

        (generator.initialize()
         .add_background_color(
            background_color=(30, 40, 50, 255))
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .initialize()
         .add_background_noise(3, 555, 0.25)
         .draw_text(
             horizontal_offset=0,
             vertical_offset=-3)
         .save()
         .to_grayscale()
         .save()
         .to_blur(1)
         .apply_enhancements(rotation_enhancements)
         .apply_enhancement(contrast_enhancements[3]))

        # (generator.initialize()
        #  .add_background_color(
        #     background_color=(30, 40, 50, 255))
        #  .draw_text(
        #      horizontal_offset=0,
        #      vertical_offset=-3)
        #  .save()
        #  .add_background_noise(3, 555, 0.25)
        #  .save())

        # (generator.initialize()
        #  .add_background_color(
        #     background_color=(70, 70, 70, 255))
        #  .draw_text(
        #      horizontal_offset=0,
        #      vertical_offset=-3)
        #  .save()
        #  .add_background_noise(3, 355, 0.35)
        #  .save()
        #  .initialize()
        #  .draw_text(
        #      horizontal_offset=-0,
        #      vertical_offset=-3)
        #  .save()
        #  .initialize()
        #  .add_background_color((3, 255, 89, 255))
        #  .draw_text(
        #      horizontal_offset=-0,
        #      vertical_offset=-3)
        #  .save()
        #  .apply_enhancements(rotation_enhancements))

          
        # (generator.initialize()
        #  .add_background_color(
        #     background_color=(50, 90, 30, 185))
        #  .draw_text(
        #      horizontal_offset=-2,
        #      vertical_offset=-2)
        #  .save()
        #  .apply_enhancements(brightness_enhancements)
        #  .initialize()
        #  .draw_text(
        #      horizontal_offset=2,
        #      vertical_offset=-3)
        #  .save()
        #  .apply_enhancements(contrast_enhancements)
        #  .initialize()
        #  .draw_text(
        #      horizontal_offset=1,
        #      vertical_offset=-1)
        #  .apply_enhancements(sharpness_enhancements))

        # (generator.initialize()
        #  .draw_text(
        #      horizontal_offset=-2,
        #      vertical_offset=-1)
        #  .save()
        #  .to_grayscale()
        #  .apply_enhancements(contrast_enhancements)
        #  .initialize()
        #  .draw_text(
        #      horizontal_offset=0,
        #      vertical_offset=-3)
        #  .apply_enhancements(rotation_enhancements))

        # (generator.initialize()
        #  .draw_text(
        #      horizontal_offset=-2,
        #      vertical_offset=-2)
        #  .save()
        #  .apply_enhancements(rotation_enhancements)
        #  .apply_enhancements(contrast_enhancements)
        #  .apply_enhancements(rotation_enhancements))


        # (generator.initialize()
        #  .draw_text(
        #      horizontal_offset=1,
        #      vertical_offset=1)
        #  .add_background_noise(3, 100, 0.25)
        #  .save()
        #  .to_solarize()
        #  .apply_enhancements(rotation_enhancements)
        #  .apply_enhancements(sharpness_enhancements)
        #  .apply_enhancements(rotation_enhancements))

        # (generator.initialize()
        #  .add_background_color(
        #      background_color=(255, 128, 25, 255)
        #  )
        #  .draw_text(
        #      horizontal_offset=-2,
        #      vertical_offset=-5)
        #  .apply_enhancements(rotation_enhancements))

        # (generator.initialize()
        #  .add_background_color(
        #      background_color=(70, 70, 70, 165)
        #  )
        #  .draw_text(
        #      horizontal_offset=3,
        #      vertical_offset=3)
        #  .save()
        #  .to_blur(1)
        #  .apply_enhancements(contrast_enhancements))

        # (generator.initialize()
        #  .add_background_noise(3, 555, 0.25)
        #  .draw_text(
        #      horizontal_offset=2,
        #      vertical_offset=2)
        
        #  .apply_enhancements(rotation_enhancements)
        #  .save()
        #  .to_blur(1)
        #  .save())


        # (generator.initialize()
        #   .add_background_noise(3, 100, 0.6)
        #   .draw_text(
        #      horizontal_offset=2,
        #      vertical_offset=0)
        #  .save()
        #  .apply_enhancements(rotation_enhancements)
        #  .to_blur(1)
        #  .apply_enhancements(sharpness_enhancements))

        # (generator.initialize()
        #  .add_background_noise(3, 555, 0.25)
        #  .draw_text(
        #      horizontal_offset=0,
        #      vertical_offset=-3)
        #  .to_blur(1)
        #  .save()
        #  .apply_enhancements(rotation_enhancements)
        #  .apply_enhancements(sharpness_enhancements))

        # (generator.initialize()
        #  .add_background_color(
        #      background_color=(2, 22, 221, 155))
        #  .draw_text(
        #      horizontal_offset=0,
        #      vertical_offset=0)
        #  .to_solarize()
        #  .save()
        #  .apply_enhancements([enhancement_prop]))

    def __eq__(self, other):
        '''Overrides the default implementation'''
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        '''Overrides the default implementation (unnecessary in Python 3)'''
        return not self.__eq__(other)

    def props_description(self):
        '''
        Print out all prop types needed.  Useful for debugging
        '''
        print '--> Image Props...'
        print self._image_props
        print '\n--> Font Props...'
        print self._font_props
        print '\n--> Content Props...'
        print self._content_props
        print '\n--> Storage object...'
        print self._storage

    def print_lifecycle(self):
        '''
        Show the lifecylce state and where it is at
        '''
        for name, member in LifeCycle.__members__.items():
            print name, member

    def reset_lifecycle(self):
        '''
        Resets the lifecycle
        '''
        self._state[LifeCycle.initialize] = None
        self._state[LifeCycle.background_color_added] = None
        self._state[LifeCycle.background_noise_added] = None
        self._state[LifeCycle.text_added] = None
        self._state[LifeCycle.enhancements_applied] = None
        self._state[LifeCycle.saved] = None

    def initialize(self):
        '''
        Mostly validaiton but also create an empty image. Takes properties of
        `ImageProps`  and returns an image.

        This method does not save the image, but simply generates it for pipeline
        management. We also do major validation to make sure that we are injecting
        properly constructed classes.
        '''
        print '* Reinitializing pipeline...'
        # self.print_lifecycle()
        self.reset_lifecycle()

        if not self._storage:
            raise AttributeError('Generator requires a concrete `Storage` mechanism')

        if not isinstance(self._content_props, ContentProps):
            raise TypeError('`content_props` must be of type ContentProps, NOT NoneType')

        if not isinstance(self._content_props, ContentProps):
            raise TypeError('`content_props` must be of type ContentProps, NOT NoneType')

        # pylint: disable=E1101
        if not isinstance(self._font_props, FontProps):
            raise TypeError('`font_props` must be of type `fontconfig.FcFont`')

        if not self._image_props:
            raise ValueError('`image_props` must be of type ImageProps, NOT NoneType')

        if not self._content_props.text:
            raise ValueError('`content_props.text` must be of type str, NOT empty or None')

        if not self._font_props:
            raise ValueError('`font_props` must be of type FontProps, NOT NoneType')

        if not self._font_props.image_font:
            raise ValueError('`_font_props.image_font` must be of type PIL.ImageFont, NOT NoneType')

        if not self._font_props.color:
            raise ValueError('`_font_props.color` must be of type PIL.ImageFont, NOT NoneType')

        if not self._font_props.font:
            raise AttributeError('Font not found')


        if not self._font_props:
            raise ValueError('`font_props` must be of type FontProps, NOT NoneType')

        if not self._font_props.image_font:
            raise ValueError('`_font_props.image_font` must be of type PIL.ImageFont, NOT NoneType')

        if not self._font_props.color:
            raise ValueError('`_font_props.color` must be of type PIL.ImageFont, NOT NoneType')

        if not self._font_props.font:
            raise AttributeError('Font not found')

        # pylint: disable=E1101
        if not isinstance(self._font_props.font, fontconfig.FcFont):
            raise TypeError('`font_prps.font` must be of type `fontconfig.FcFont`')

        self._image = self._content_props.image.copy()

        self._state[LifeCycle.initialize] = 'COMPLETED'
        return self

    def add_background_color(self, background_color=(128, 128, 128, 255)):
        '''
        Add background noise to the image. Goes through each
        pixel and randomizes a color and modifies it and then
        outputs a new image
        '''
        if not isinstance(background_color, tuple):
            raise AttributeError('`background_color` must be a tuple.')

        (r, g, b, alpha) = background_color
        if not isinstance(alpha, int) and abs(alpha/255) <= 1.0:
            print '`alpha` not set in `add_background`'

        print '* Adding background color...'

        img = Image.new('RGBA', self._content_props.image_size, background_color)
        self._image = Image.blend(self.image, img, alpha=alpha/255.0)
        self._state[LifeCycle.background_color_added] = 'COMPLETED'
        self._state[LifeCycle.saved] = None
        return self

    def add_background_noise(self,
                             multiple=3,
                             contrast=555,
                             alpha=0.25):
        '''
        Add background noise to the image. Goes through each
        pixel and randomizes a color and modifies it and then
        outputs a new image
        '''
        # pylint: disable=E1101

        image_factory = FilterFactory(self.image)
        image_factory.noise(multiple, contrast, alpha)
        self._image = image_factory.apply()

        self._state[LifeCycle.background_noise_added] = 'COMPLETED'
        self._state[LifeCycle.saved] = None
        return self

    def remove_transparency(self, background_color=(128, 128, 128)):
        '''
        Remove transparent pixels.  Useful after a rotation
        '''
        # Only process if image has transparency (http://stackoverflow.com/a/1963146)
        if self.image.mode in ('RGBA', 'LA') \
            or (self.image.mode == 'P' \
            and 'transparency' in self.image.info):
            # Need to convert to RGBA if LA format due to a bug in PIL
            # (http://stackoverflow.com/a/1963146)

            alpha = self.image.convert('RGBA').split()[-1]
            # Create a new background image of our matt color.
            # Must be RGBA because paste requires both images have the same format
            # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
            bgi = Image.new("RGBA", self.image.size, background_color + (255,))
            bgi.paste(self.image, mask=alpha)
            self._image = bgi

        return self

    def draw_text(self, horizontal_offset=0, vertical_offset=0):
        '''
        Adds text the the generators image.  It relies on
        making sure that we have a font, we have ackgroun image,
        and we have text. The offsets allow you to position text
        '''
        print '* Drawing text...'
        # setup font
        # self.props_description()

        if not self.image:
            raise AttributeError('Font not found')

        font_props = self._font_props
        # canvas = self.image.copy()
        # create drawing context
        draw = ImageDraw.Draw(self._image)
        if not draw:
            raise RuntimeError('Unable to create draw context')

        # Attempt to center the font inside the background canvas
        text_x, text_y = font_props.image_font.getsize(self._content_props.text)
        width, height = self._content_props.image_size
        x_r = (width - text_x)/2 + horizontal_offset
        y_r = (height - text_y)/2 + vertical_offset
        # Write the text ont h
        draw.text(
            (x_r, y_r),
            self._content_props.text,
            font=self._font_props.image_font,
            fill=self._font_props.color
        )
        self._state[LifeCycle.text_added] = 'COMPLETED'
        self._state[LifeCycle.saved] = None
        return self


    def apply_enhancement(self, enhancement_prop=None):
        '''
        Apply the injected enhancement to the image and create a new copy
        of the image with the transformations.
        '''
        if not enhancement_prop:
            return self

        self._state[LifeCycle.saved] = None
        # TODO: FILTER FACTORY GOES HERE
        if not enhancement_prop:
            enhancement_prop = self._image_props._enhancement_props

        filter_factory = FilterFactory(self._image, enhancement_prop)
        self._image = filter_factory.apply()
        self._state[LifeCycle.enhancements_applied] = 'COMPLETED'
        return self

    def apply_filter(self, image_filter):
        '''
        directly apply a filter
        '''
        self._image = image_filter.apply()
        return self

    def apply_enhancements(self, enhancement_props=None, save_each=True):
        '''
        Apply the injected enhancement to the image and create a new copy
        of the image with the transformations.
        '''
        if not enhancement_props:
            return self

        if not save_each:
            for enh in enhancement_props:
                self.apply_enhancement(enh)
            return self

        for enh in enhancement_props:
            self.apply_enhancement(enh).save()

        self._state[LifeCycle.saved] = None

        return self

    def apply_backfill(self, backfill_color):
        '''
        Apply the injected enhancement to the image and create a new copy
        of the image with the transformations.
        '''
        if not backfill_color:
            return self

        self._state[LifeCycle.saved] = None
        # TODO: Add backfill - when image rotates, it loses some background

        filter_factory = FilterFactory(self.image, backfill_color)
        # print '\n{0}\n'.format(self._image_props._enhancement_props)
        # TODO: Add factory generator
        self._image = filter_factory.apply()

        self._state[LifeCycle.enhancements_applied] = 'COMPLETED'
        return self

    def to_bitonal_image(self):
        '''
        Creates a black and white version of the image.
        '''
        self._image = self.image.convert('1')
        return self

    def to_grayscale(self):
        '''
        Creates a black and white version of the image.
        '''
        img_filter = FilterFactory(self.image)
        self._image = img_filter.grayscale().image
        return self

    def to_blur(self, threshold=1):
        '''
        Guassian blur with threshold
        '''
        img_filter = FilterFactory(self.image)
        self._image = img_filter.blur(threshold).image
        return self

    def to_blur2(self):
        '''
        Pillow default blur
        '''
        img_filter = FilterFactory(self.image)
        self._image = img_filter.blur2().image
        return self

    def to_solarize(self):
        '''
        Pillow default blur
        '''
        img_filter = FilterFactory(self.image)
        self._image = img_filter.solarize().image
        return self

    def to_emboss(self):
        '''
        Show raised edges in image 
        '''
        img_filter = FilterFactory(self.image)
        self._image = img_filter.emboss().image
        return self

    def to_contour(self):
        '''
        Creates a black and white version of the image.
        '''
        img_filter = FilterFactory(self.image)
        self._image = img_filter.contour().image
        return self

    def show(self):
        '''
        Display the image.  Useful during debugging, however, you
        shouldn't run this on a large generation.
        '''
        if not isinstance(self.image, Image.Image):
            raise TypeError("Must be of type PIL.Image")

        print '---> Attempting to show the image <---'
        self._image = self.image
        self.image.show()
        return self

    def save(self):
        '''Saves the image to designated storeage location specified
        in order to grab the class, image id, and image_propss object.  Since
        this calls `filename`, an instance of the default image_propss object
        is created if there isn't one'''
        print '* Saving file: {0}'.format(self._storage.filename)
        if self.image and self._state[LifeCycle.saved] is None:
            self._storage.save(self.image)
            self._state[LifeCycle.saved] = None
        else:
            self._state[LifeCycle.saved] = 'FAILED'
            raise IOError(
                "Unable to save image file")
        

        return self

    @property 
    def storage(self):
        '''
        Returns the storage type being used
        '''
        return self._storage
    @storage.setter
    def storage(self, value):
        '''
        Switches the storage type being used
        '''
        self._storage = value

    @property
    def state(self):
        '''
        Holds the state of the image generation process
        '''
        return self._state

    @property
    def text(self):
        '''The text to be rendered on the image. Probably should be a letter'''
        return self._content_props.text

    @property
    def output_dir(self):
        '''The output directory where the generated images
        will be stored. Used in the saving and naming of the file.
        '''
        return self._storage.output_dir

    @property
    def image_props(self):
        '''Image id - should be incremented for each image generated. Used
        in the naming of the file.'''
        return self._image_props

    @image_props.setter
    def image_props(self, value):
        '''ImageProp object.  This object must be of type ImageProps'''
        if not isinstance(value, list):
            raise TypeError("image_props must be a list of type ImageProps")

        if value == self._image_props:
            raise ValueError('''Incoming image_props is identical to
                             current! Are you sure you want that to happen?''')

        if self._state == LifeCycle.saved:
            raise RuntimeError('Already saved this file')

        self._image_props = value


    @property
    def image(self):
        '''Returns the test object image.  `image` is
        of type Pil.Image'''
        return self._image


    @image.setter
    def image(self, value):
        '''Sets the image to be used.  This should normally be set
        during initialization, but this is here for convenience. The
        value must be an instance of PIL.Image.'''
        if not isinstance(value, Image):
            raise TypeError("Image must be of type PIL.Image")
        self._image = value

    @property
    def saved(self):
        '''Convenience value to prevent images being saved twice.'''
        self._state[LifeCycle.saved] = '* Save property called'
        return self._state[LifeCycle.saved]

    def __str__(self):
        attrs = vars(self)
        desc = '\n'.join("%s: %s" % item for item in attrs.items())
        return desc
