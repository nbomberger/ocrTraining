# -*- encoding: utf-8 -*-
'''Main Processing Logic'''
# from imageprocessing.helpers import accepts, returns
from imageprocessing import ImageGenerator
# Generate our fonts and image sets
# pylint: disable=C0326

ImageGenerator.for_characters(
    characters=['A','B'],
)

# ImageGenerator.generate_image_of_character(
#     'B',
#     enhancement_props=rotate_45
# )
# ImageGenerator.generate_image_of_character(
#     'C',
#     enhancement_props=rotate_contrast_0015
# )
# ImageGenerator.generate_image_of_character(
#     'D',
#     enhancement=rotate_45_contrast_0015
# )
# ImageGenerator.generate_images_by_enhancement(
#     READABLE_CHARACTERS,
# )

# ImageGenerator.generate_images_by_font(
#     font,
#     READABLE_CHARACTERS,
#     rotate_45
# )
# ImageGenerator.generate_images_by_character(
#     READABLE_CHARACTERS[0],
#     fonts=ALL_FONTS
# )
# ImageGenerator.process_characters(TEST_CHARACTERS, ALL_FONTS, IMAGEPROP1)
print '`generate_data_set - FINISHED'
