from maix import display,camera,app

cam=camera.Camera(640,480)
disp = display.Display()
#maixvision会爆红,打算用vscode写
disp.set_backlight(50)#背光强度
while not app.need_exit():
    img=cam.read()
    disp.show(img)#占内存,还需先初始化display类
    #可以用display.send_to_maixvision(img)