
# Instructions

## Get started
```
cd darknet
PATH=/usr/local/cuda/bin/:$PATH make
wget https://pjreddie.com/media/files/yolov3.weights
./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
```

## Training

```shell
cd /home/zli/data/weapons
~/workspace/github/darknet/darknet detector train cfg/weapon_train.data cfg/weapon_yolov3.cfg results/weapon_yolov3_best.weights -map -gpus 0,1
```

The flag ```-clear``` will reset the iterations saved in the weights.

```-gpus``` is optional

9.Test and demo

## Test a list of files

```shell
cd /home/zli/data/weapons
/home/zli/workspace/github/darknet/darknet detector test cfg/knife_train.data cfg/knife_yolov3_test.cfg results/knife-yolov3_best.weights < knife_test_images.txt
```

**Pseudo-labelling: use existing model to pre-label a list of images**

```
~/workspace/github/darknet/darknet detector test cfg/coco.data cfg/yolov3.cfg results/yolov3.weights -thresh 0.25 -dont_show -save_labels < images.txt
```

## Test a video and save results

```
cd /home/zli/data/weapons
/home/zli/workspace/github/darknet/darknet detector demo cfg/weapon_train.data cfg/weapon_yolov3.cfg results/weapon_yolov3_best.weights test.mp4 -out_filename result.mp4
```

## Demo with a webcam

```shell
cd /home/zli/data/weapons
/home/zli/workspace/github/darknet/darknet detector demo cfg/knife_train.data cfg/knife_yolov3_test.cfg results/knife-yolov3_best.weights -c 0
```

## Calculate mAP

```shell
cd /home/zli/data/weapons
/home/zli/workspace/github/darknet/darknet detector map cfg/weapon_train.data cfg/weapon_yolov3_test.cfg results/weapon_yolov3_best.weights
```

## Transfer learning

```stopbackward=1``` will disable all layers below. For example, one can put that line before the first `Yolo` layer for fine-tuning a small dataset, and run 

```
~/workspace/github/darknet/darknet detector train cfg/small_weapon_train.data cfg/small_weapon_yolov3.cfg results/weapon_yolov3_last.weights -map
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