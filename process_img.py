from maix import image,display,app

#创建图像很简单,传参就好，宽度，高度，格式

img=image.Image(320,240,image.Format.FMT_RGB888)
print(img)
#可以用image.save保存

#image.draw_rect是画框,参数自己查api文档
#同理draw_string写字符串,draw_line画线,draw_circle画圆

#支持中文和自定义字体,建议不用，麻烦

#resize缩放,返回新图像原图像不变
img_new=img.resize(640,520)
#crop剪裁
#rotate旋转
#copy拷贝

#affine仿射变换(这是什么
#draw_keypoints(画关键点)
#画十字，箭头，图,转换格式,还可以数据变为bytes(原来是什么,好像是字符串？)

while not app.need_exit():
    display.send_to_maixvision(img_new)
