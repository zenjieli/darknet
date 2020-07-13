Training YOLOv3 Object Detector - Snowman

1. Install awscli

`pip3 install awscli` 

2. Get the relevant OpenImages files needed to locate images of our interest

`wget https://storage.googleapis.com/openimages/2018_04/class-descriptions-boxable.csv`

`wget https://storage.googleapis.com/openimages/2018_04/train/train-annotations-bbox.csv`

3. Download the images from OpenImagesV4

`python3 getDataFromOpenImages_snowman.py`

4. Create the train-test split

`python3 splitTrainAndTest.py /data-ssd/sunita/snowman/JPEGImages`

Give the correct path to the data JPEGImages folder. The 'labels' folder should be in the same directory as the JPEGImages folder.

5. Install Darknet and compile it.
```
cd ~
git clone https://github.com/pjreddie/darknet
cd darknet
make
```
6.Get the pretrained model

`wget https://pjreddie.com/media/files/darknet53.conv.74 -O ~/darknet/darknet53.conv.74`

7.Fill in correct paths in the darknet.data file

8.Start the training as below, by giving the correct paths to all the files being used as arguments

```shell
cd /home/zli/data/weapons
~/workspace/github/darknetv4/darknet detector train cfg/weapon_train.data cfg/weapon_yolov3.cfg results/weapon_yolov3_best.weights -map -gpus 0,1
```

```-gpus``` is optional

9.Test with an image

```shell
cd /home/zli/data/weapons
/home/zli/workspace/github/darknetv4/darknet detector test cfg/knife_train.data cfg/knife_yolov3_test.cfg results/knife-yolov3_best.weights < knife_test_images.txt
```

Demo with a webcam:

```shell
cd /home/zli/data/weapons
/home/zli/workspace/github/darknetv4/darknet detector demo cfg/knife_train.data cfg/knife_yolov3_test.cfg results/knife-yolov3_best.weights -c 0
```

Calculate mAP

```shell
cd /home/zli/data/weapons
/home/zli/workspace/github/darknetv4/darknet detector map cfg/weapon_train.data cfg/weapon_yolov3_test.cfg results/weapon_yolov3_best.weights
```

## Extra information

### Image data sets

<https://github.com/spmallick/learnopencv/tree/master/YOLOv3-Training-Snowman-Detector>

ImageNet for "crash helmet"
Mask: Balaclava

Get image URLs at <http://www.image-net.org/api/text/imagenet.synset.geturls.getmapping?wnid=n03127747>

#### How to train tiny-yolo

<https://github.com/AlexeyAB/darknet#how-to-train-tiny-yolo-to-detect-your-custom-objects>

### Annotation

<https://github.com/AlexeyAB/Yolo_mark>

```shell
cd ~/data/weapons

/home/zli/workspace/github/Yolo_mark/yolo_mark weapon_train_images weapon_train_images.txt cfg/obj.names
```

<http://www.robots.ox.ac.uk/~vgg/software/via/via_demo.html>
<https://www.programmersought.com/article/1815101352/>
<https://github.com/AlexeyAB/darknet#how-to-improve-object-detection>
