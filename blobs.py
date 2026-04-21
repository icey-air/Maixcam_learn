#太简单了maixcam，把底层封装好了,得自己学点东西
from maix import image,camera,display,app

cam = camera.Camera(320,240)
disp = display.Display()

#thresholds阈值链表,L_MIN,L_MAX，A_MIN,A_MAX,B_MIN,B_MAX
#LAB颜色空间,L:亮度,A:红绿通道,B:蓝绿通道

thresholds=[[0,80,40,80,10,80]]#L:0~80,A:40~80,B:10~80      red

while not app.need_exit():
    img=cam.read()
    blobs=img.find_blobs(thresholds,pixels_threshold=300)#第一个参数是阈值列表(好像还是[[]]?),第二个是像素点阈值
    #最重要的就是！！find_blobs的实现(内部实现，算法,返回了什么？)
    for blob in blobs:
        img.draw_rect(blob[0],blob[1],blob[2],blob[3],image.COLOR_GREEN)#找到了画个框

    disp.show(img)