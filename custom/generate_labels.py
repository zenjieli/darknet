import csv
import subprocess
import os

runMode = "test"
classes = ['Shotgun', 'Handgun']
class_numbers = ['1', '1']
image_dir_name = 'gun_train_images/'

# Create a dictionary for class_name -> class_id

data_dir = os.path.join(os.path.expanduser('~'), 'data/weapons/archive/')
with open(os.path.join(data_dir, data_dir + 'class-descriptions-boxable.csv'), mode='r') as infile:
    reader = csv.reader(infile)
    dict_list = {rows[1]: rows[0] for rows in reader}

for class_idx in range(0, len(classes)):

    # Get the class name
    className = classes[class_idx]
    print("Class " + str(class_idx) + " : " + className)

    # Extract annotations for this class
    commandStr = "grep " + dict_list[className] + " " + data_dir + runMode + "-annotations-bbox.csv"
    print(commandStr)
    class_annotations = subprocess.run(commandStr.split(), stdout=subprocess.PIPE).stdout.decode('utf-8')
    class_annotations = class_annotations.splitlines()

    totalNumOfAnnotations = len(class_annotations)
    count = 0
    for line in class_annotations[0:totalNumOfAnnotations]:  # For each annotation
        count = count + 1

        if count % 10 == 0:
            print("annotation count : " + str(count))

        lineParts = line.split(',')

        image_id = lineParts[0]
        if os.path.exists(data_dir + image_dir_name + image_id + ".jpg"):
            # Create or append this annotation
            xmin = lineParts[4]
            xmax = lineParts[5]
            ymin = lineParts[6]
            ymax = lineParts[7]
            with open(data_dir + image_dir_name + '/%s.txt' % (lineParts[0]), 'a') as f:
                f.write(' '.join([class_numbers[class_idx], str((float(xmax) + float(xmin))/2),
                                    str((float(ymax) + float(ymin))/2),
                                    str(float(xmax)-float(xmin)),
                                    str(float(ymax)-float(ymin))])+'\n')