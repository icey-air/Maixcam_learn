from maix import image, display

disp = display.Display()
img = image.Image(320, 240)
img.draw_rect(0, 0, disp.width(), disp.height(), color=image.Color.from_rgb(255, 0, 0), thickness=-1)
img.draw_rect(10, 10, 100, 100, color=image.Color.from_rgb(255, 0, 0))
img.draw_string(10, 10, "Hello MaixPy!", color=image.Color.from_rgb(255, 255, 255))
while 1:
    disp.show(img)
