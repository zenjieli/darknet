import os

labels_path = '/home/zli/data/yolov3/openimages/labels'
images_path = '/home/zli/data/yolov3/openimages/images'

labels = set()
for f in os.listdir(labels_path):
    if os.path.isfile(os.path.join(labels_path, f)):
        labels.add(os.path.splitext(f)[0])

for f in os.listdir(images_path):
    if not (os.path.splitext(f)[0] in labels):
        os.remove(os.path.join(images_path, f))        
