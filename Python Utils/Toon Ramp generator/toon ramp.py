from PIL import Image, ImageDraw

#TODO
#make it a sys.argv
w = 512
h = 512
steps = 11


gradientSize = w/(steps+1) #+1 because of the white end
colors = []
colorStep = 255.0/steps

#generate ramp
for j in xrange(steps+1):
    colors.append((int(j*colorStep),int(j*colorStep),int(j*colorStep)))

#generate Image
size = (w,h)
a = Image.new("RGB",size,(0,0,0))
d = ImageDraw.Draw(a)
for i in xrange(steps+1):
    f = i * gradientSize
    d.rectangle((f,0,w+f,h),colors[i])
       

a.save("ramp.png")
