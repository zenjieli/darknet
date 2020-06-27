import csv
import subprocess
import os

bb_file = 'train-annotations-bbox.csv'
classes = ['Helmet']

# Create a dictionary for class_name -> class_id
data_dir = os.path.join(os.path.expanduser('~'), 'data/yolov3/openimages/')
with open(os.path.join(data_dir, data_dir + 'class-descriptions-boxable.csv'), mode='r') as infile:
    reader = csv.reader(infile)
    dict_list = {rows[1]: rows[0] for rows in reader}

for class_idx in range(0, len(classes)):

    # Get the class name
    className = classes[class_idx]
    print("Class " + str(class_idx) + " : " + className)

    # Extract annotations for this class
    commandStr = "grep " + dict_list[className] + " " + data_dir + bb_file
    print(commandStr)
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
        if not os.path.exists(data_dir + 'images1/' + image_id + ".jpg"):        
            print("annotation count : " + str(count))

            subprocess.run(['aws', 's3', '--no-sign-request', '--only-show-errors', 'cp',
                            's3://open-images-dataset/' +
                            'train/' + image_id + ".jpg",
                            data_dir + 'images1/' + image_id + ".jpg"])
