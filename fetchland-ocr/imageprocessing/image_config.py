# -*- encoding: utf-8 -*-
'''
Provides a central place where you can configure
the type of images that you want to generate. 
'''
from imageprocessing.enhancement_props import EnhancementProps
from imageprocessing.font_props import FontProps
from imageprocessing.image_props import ImageProps

IMAGE_ORIGINAL_EN = EnhancementProps(rotation=45)
font                = FontProps()


print "\n{0} fonts to be processed.\n".format(len(ALL_FONTS))

# FONT_PROPS_LIST = list()
# for fnt in ALL_FONTS:
    # FONT_PROPS_LIST.append(FontProps(path=fnt))


# Character set that will be readable
# pylint: disable=C0301
# font = ALL_FONTS[0]
# print font.capability
# print font.decorative
# print font.count_chars()
# print "\n"
# print font.family
# print font.file
# print font.fontformat
# print font.foundry
# print font.fullname
# print "\n"
# print font.has_char(u'A')
# print font.has_char(u'朝')
# print font.index    
# print "\n"
# print font.outline  
# print font.print_pattern
# print font.scalable
# print font.slant
# print font.spacing
# print font.style
# print font.weight
# print font.width
UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
CHARACTERS = ["'", ","]

READABLE_CHARACTERS = UPPERCASE + LOWERCASE + NUMBERS + CHARACTERS

TEST_CHARACTERS = ['J']

# IMAGE_ORIGINAL      = ImageProps(name='original',
#                                  enhancement=rotate_45,
#                                  font=font,
#                                  background_color=(255, 255, 255, 255))
# IMAGE_ROTATE_45     = ImageProps('rotate_45', rotate_45, font)
# IMAGE_ROTATE_90     = ImageProps(name='rotate_90', rotation=90)
# IMAGE_ROTATE_135    = ImageProps(name='rotate_135', rotation=135)
# IMAGE_ROTATE_180    = ImageProps(name='rotate_180', rotation=180)
# IMAGE_ROTATE_225    = ImageProps(name='rotate_225', rotation=225)
# IMAGE_ROTATE_270    = ImageProps(name='rotate_270', rotation=270)
# IMAGE_ROTATE_315    = ImageProps(name='rotate_315', rotation=315)
#
# IMAGE_CONTRAST_015  = ImageProps(name='contrast_0_15', contrast=0.15)
# IMAGE_CONTRAST_025  = ImageProps(name='contrast_0_25', contrast=0.25)
# IMAGE_CONTRAST_035  = ImageProps(name='contrast_0_35', contrast=0.35)
# IMAGE_CONTRAST_045  = ImageProps(name='contrast_0_45', contrast=0.45)
# IMAGE_CONTRAST_055  = ImageProps(name='contrast_0_55', contrast=0.55)
# IMAGE_CONTRAST_065  = ImageProps(name='contrast_0_65', contrast=0.65)

# IMAGE_COLOR_080     = ImageProps(name='color_80', background_color=(80, 80, 80, 155))
# IMAGE_COLOR_096     = ImageProps(name='color_96', background_color=(96, 96, 96, 155))
# IMAGE_COLOR_120     = ImageProps(name='color_120', background_color=(120, 120, 120, 255))
# IMAGE_COLOR_128     = ImageProps(name='color_128', background_color=(128, 128, 128, 255))
# IMAGE_COLOR_LG      = ImageProps(name='color_128', background_color=(0, 204, 128, 255))

# IMAGE_ROTATED = [
#     IMAGE_ROTATE_45,
#     IMAGE_ROTATE_90,
#     IMAGE_ROTATE_135,
#     IMAGE_ROTATE_180,
#     IMAGE_ROTATE_225,
#     IMAGE_ROTATE_270,
#     IMAGE_ROTATE_315

# ]
# IMAGE_CONTRAST = [
#     IMAGE_CONTRAST_015,
#     IMAGE_CONTRAST_025,
#     IMAGE_CONTRAST_035,
#     IMAGE_CONTRAST_045,
#     IMAGE_CONTRAST_055,
#     IMAGE_CONTRAST_065
# ]
# IMAGE_COLOR = [
#     IMAGE_COLOR_080,
#     IMAGE_COLOR_096,
#     IMAGE_COLOR_120,
#     IMAGE_COLOR_128,
#     IMAGE_COLOR_LG
# ]

# IMAGE_PROPS_LIST = [IMAGE_ORIGINAL] + IMAGE_ROTATED + IMAGE_CONTRAST + IMAGE_COLOR