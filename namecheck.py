import os
imgpath = "C:/Users/jinsung/Anaconda3/envs/yolov5/yolov5/datasets/images/train"
lblpath = "C:/Users/jinsung/Anaconda3/envs/yolov5/yolov5/datasets/labels/train"

imglist = []
lbllist = []

for i in os.listdir(imgpath):
    imglist.append(str(i).rsplit('.')[0])

for j in os.listdir(lblpath):
    lbllist.append(str(j).rsplit('.')[0])



namelist = sorted(list(set(imglist) - set(lbllist)))


for k in namelist:
    # os.remove("C:/Users/jinsung/Anaconda3/envs/yolov5/yolov5/datasets/images/train/" + k + ".png")
    print(k)

