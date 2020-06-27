import csv
import subprocess
import os

bb_file = 'train-annotations-bbox.csv'
classes = ['Shotgun', 'Handgun', 'Knife']
image_dir_name = 'gun_images/'

# Create a dictionary for class_name -> class_id
data_dir = os.path.join(os.path.expanduser(
    '~'), 'workspace/github/security_images/')
with open(os.path.join(data_dir, data_dir + 'class-descriptions-boxable.csv'), mode='r') as infile:
    reader = csv.reader(infile)
    dict_list = {rows[1]: rows[0] for rows in reader}

for class_idx in range(0, len(classes)):
    labelled_images = set()
    class_count = 0

    # Get the class name
    className = classes[class_idx]
    print("Class " + str(class_idx) + " : " + className)

    # Extract annotations for this class
    commandStr = "grep " + dict_list[className] + " " + data_dir + bb_file    
    class_annotations = subprocess.run(
        commandStr.split(), stdout=subprocess.PIPE).stdout.decode('utf-8')
    class_annotations = class_annotations.splitlines()

    totalNumOfAnnotations = len(class_annotations)
    count = 0
    for line in class_annotations[0:totalNumOfAnnotations]:  # For each annotation
        lineParts = line.split(',')

        # Download the corresponding image
        image_id = lineParts[0]

        count = count + 1

        if os.path.exists(data_dir + image_dir_name + image_id + ".jpg"):
            class_count += 1
            labelled_images.add(image_id)
        elif not os.path.exists(data_dir + image_dir_name + image_id + ".txt"):
            open(data_dir + image_dir_name + image_id + '.txt', 'a').close()

    print('Number of annotations for class %d %s: %d. Images: %d' %
          (class_idx, classes[class_idx], class_count, len(labelled_images)))
