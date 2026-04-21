from maix import image,display

disp = display.Display()
img = image.load("/root/head.png")
while 1:
    disp.show(img)