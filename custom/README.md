
# Instructions

## Get started
```
cd darknetv4
PATH=/usr/local/cuda/bin/:$PATH make
wget https://pjreddie.com/media/files/yolov3.weights
./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
```

## Training

```shell
cd /home/zli/data/weapons
~/workspace/github/darknetv4/darknet detector train cfg/weapon_train.data cfg/weapon_yolov3.cfg results/weapon_yolov3_best.weights -map -gpus 0,1
```

```-gpus``` is optional

9.Test and demo

## Test a list of files

```shell
cd /home/zli/data/weapons
/home/zli/workspace/github/darknetv4/darknet detector test cfg/knife_train.data cfg/knife_yolov3_test.cfg results/knife-yolov3_best.weights < knife_test_images.txt
```

## Test a video and save results

```
cd /home/zli/data/weapons
/home/zli/workspace/github/darknetv4/darknet detector demo cfg/weapon_train.data cfg/weapon_yolov3.cfg results/weapon_yolov3_best.weights test.mp4 -out_filename result.mp4
```

## Demo with a webcam

```shell
cd /home/zli/data/weapons
/home/zli/workspace/github/darknetv4/darknet detector demo cfg/knife_train.data cfg/knife_yolov3_test.cfg results/knife-yolov3_best.weights -c 0
```

## Calculate mAP

```shell
cd /home/zli/data/weapons
/home/zli/workspace/github/darknetv4/darknet detector map cfg/weapon_train.data cfg/weapon_yolov3_test.cfg results/weapon_yolov3_best.weights
```

## Transfer learning

```stopbackward=1``` will disable all layers below. For example, one can put that line before the first `Yolo` layer for fine-tuning a small dataset, and run 

```
~/workspace/github/darknetv4/darknet detector train cfg/small_weapon_train.data cfg/small_weapon_yolov3.cfg results/weapon_yolov3_last.weights -map
```



## Annotation

<https://github.com/AlexeyAB/Yolo_mark>

```shell
cd ~/data/weapons

/home/zli/workspace/github/Yolo_mark/yolo_mark weapon_train_images weapon_train_images.txt cfg/obj.names
```

# Old information

### Image data sets

<https://github.com/spmallick/learnopencv/tree/master/YOLOv3-Training-Snowman-Detector>

ImageNet for "crash helmet"
Mask: Balaclava

Get image URLs at <http://www.image-net.org/api/text/imagenet.synset.geturls.getmapping?wnid=n03127747>

#### How to train tiny-yolo

<https://github.com/AlexeyAB/darknet#how-to-train-tiny-yolo-to-detect-your-custom-objects>

<http://www.robots.ox.ac.uk/~vgg/software/via/via_demo.html>
<https://www.programmersought.com/article/1815101352/>
<https://github.com/AlexeyAB/darknet#how-to-improve-object-detection>