import os

# Path for the directory containing both images and labels
image_label_path = '/home/zli/data/yolov3/weapons/knife_test'

for root, dirs, filenames in os.walk(image_label_path):
    for f in filenames:    
        name_without_ext, ext = os.path.splitext(f)
        if ext.lower() == '.txt' and not os.path.exists(os.path.join(root, name_without_ext + '.jpg')):
            os.remove(os.path.join(root, f))
    
    break

