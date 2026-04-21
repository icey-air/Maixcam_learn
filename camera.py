from maix import camera,image,app,display

'''

#cam = camera.Camera(640,480,image.Format.FMT_GRAYSCALE)
#第三个参数是设置灰度
#第一个和第二个是width,heigth，是设置分辨率的
#可以通过fps来设置帧率
cam=camera.Camera(640,480,image.Format.FMT_YVU420SP,fps=30)
#NV21图像 亮度(Y),色度(UV)

#摄像头初始化的时间可能采集的图片怪，可以用skip_frames跳过
cam.skip_frames(30)

#可以设置曝光，增益，白平衡(不懂)(特殊情况下检测颜色白平衡可能有用)

#可以用buff_num设置更低抓图延时(不清楚)


#可以设置亮度(luma)，对比度(constrast)，饱和度(saturation)


while not app.need_exit():

    display.send_to_maixvision(cam.read())

'''

#不重新开一个py了

#可以读取原始raw图(有用,自己实现算法时)
cam = camera.Camera(raw=True)
#不清楚为什么调用print,有空查一下api
#打印到终端了
while 1:
    print(cam.read_raw())