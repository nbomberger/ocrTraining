# -*- encoding: utf-8 -*-
'''Main Processing Logic'''
# from imageprocessing.helpers import accepts, returns
import pdb
import os
from imageprocessing.enhancement_props import EnhancementProps
from imageprocessing.image_generator import ImageGenerator
from imageprocessing.image_props import ImageProps
from imageprocessing.content_props import ContentProps
from imageprocessing.font_props import FontProps
from imageprocessing.storage.storage_manager import StorageManager
# Generate our fonts and image sets
# pylint: disable=C0326

numbers=[ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
uppercase=[ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
lowercase=[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
# characters=[ "'", "," ]
test_characters = uppercase + lowercase
# test_characters = ['A', 'B']


ALL_PROPS = FontProps.all_fonts()
new_props = [prop for prop in ALL_PROPS if os.path.dirname(prop.filename()) == '/Users/nbomberger/Library/Fonts']
ImageGenerator.with_characters_and_fonts(
    characters=test_characters,
    font_props=new_props
)
