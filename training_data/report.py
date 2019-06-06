# -*- coding: utf-8 -*-
import os
f = open('report.html','w')

images = []
for file in os.listdir("./"):
    if file.endswith(".png"):
        images.append(file)

num_images = len(images)
content = "<p>{0} geneated images <p>".format(num_images)
message = '''<html>
    <head></head>
    <body>
    {0}
    </body>
    </html>'''.format(content)


f.write(message)
f.close()
