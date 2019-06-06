#!/usr/bin/env python

# conda execute
# env:
#  - python >=3
#  - numpy
import subprocess
import fontconfig
from subprocess import call

uppercase=[ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
lowercase=[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
numbers=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
characters=[ '\'', '\,' ]
idx=0
file = open("ocr.csv","a") 
file.write("Class")
file.close()
fonts = fontconfig.query()
for font in fonts:

# for index in $(convert -list font | grep Font | awk '{print $2}'); 
# do
#     cls=0
#     for i in "${uppercase[@]}"
#     do
#     `convert -font $index -background white -fill black -size 28x28 -gravity center -pointsize 28 label:$i $cls-$idx.png;`
#     `echo "$cls" >> ocr.csv`;
#     `convert $cls-$idx.png -rotate 90 $cls-$idx-rotate_90.png;`
#     `echo "$cls" >> ocr.csv`;
#     `convert $cls-$idx.png -rotate 180 $cls-$idx-rotate_180.png;`
#     `echo "$cls" >> ocr.csv`;
#     `convert $cls-$idx.png -rotate 270 $cls-$idx-rotate_270.png;`
#     `echo "$cls" >> ocr.csv`;
#     ((idx++))
#     ((cls++))
#     done
#     for i in "${lowercase[@]}"
#     do 
#     `convert -font $index -background white -fill black -size 28x28 -gravity center -pointsize 28 label:$i $cls-$idx.png;`
#     `echo "$cls" >> ocr.csv`;
#     `convert $cls-$idx.png -rotate 90 $cls-$idx-rotate_90.png;`
#     `echo "$cls" >> ocr.csv`
#     `convert $cls-$idx.png -rotate 180 $cls-$idx-rotate_180.png;`
#     `echo "$cls" >> ocr.csv`
#     `convert $cls-$idx.png -rotate 270 $cls-$idx-rotate_270.png;`
#     `echo "$cls" >> ocr.csv`
#     ((idx++))
#     ((cls++))
#     done
#     for i in "${numbers[@]}"
#     do 
#     `convert -font $index -background white -fill black -size 28x28 -gravity center -pointsize 28 label:$i $cls-$idx.png;`
#     `echo "$cls" >> ocr.csv`;
#     `convert $cls-$idx.png -rotate 90 $cls-$idx-rotate_90.png;`
#     `echo "$cls" >> ocr.csv`;
#     `convert $cls-$idx.png -rotate 180 $cls-$idx-rotate_180.png;`
#     `echo "$cls" >> ocr.csv`;
#     `convert $cls-$idx.png -rotate 270 $cls-$idx-rotate_270.png;`
#     `echo "$cls" >> ocr.csv`;
#     ((idx++))
#     ((cls++))
#     done
#     for i in "${characters[@]}"
#     do 
#     `convert -font $index -background white -fill black -size 28x28 -gravity center -pointsize 28 label:$i $cls-$idx.png;`
#     `echo "$cls" >> ocr.csv`;
#     `convert $cls-$idx.png -rotate 90 $cls-$idx-rotate_90.png;`
#     `echo "$cls" >> ocr.csv`;
#     `convert $cls-$idx.png -rotate 180 $cls-$idx-rotate_180.png;`
#     `echo "$cls" >> ocr.csv`;
#     `convert $cls-$idx.png -rotate 270 $cls-$idx-rotate_270.png;`
#     `echo "$cls" >> ocr.csv`;
#     ((idx++))
#     ((cls++))
#     done
# done

