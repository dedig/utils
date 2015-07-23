from PIL import Image
import random

grayscale = True

smoothness = 2

w = 1024
h = 1024
size = (w,h)

a = Image.new("RGB",size,(0,0,0))

for i in xrange(0,w,smoothness):
    for j in xrange(0,h,smoothness):
        if(random.randint(0,100) < 5):
            r = random.randint(0,100)
            if(grayscale):
                g = b = r
            else:
                g = random.randint(0,100)
                b = random.randint(0,100)
            a.putpixel((i,j),(r,g,b))


a.save("output.png")
