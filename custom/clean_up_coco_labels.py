import os
import os.path as osp

import coco_fileutils
from coco_fileutils import get_file_list
from coco_fileutils import user_path


def keep_only_labels(label_dir, label):
    files = get_file_list(label_dir, True)

    for filepath in files:
        lines = []
        with open(filepath, 'r') as f:
            lines = f.readlines()

        newlines = []
        for line in lines:
            words = line.split()
            if len(words) > 0 and words[0].strip() == label:
                newlines.append(line)

        if len(newlines) < len(lines):
            with open(filepath, 'w') as f:
                f.writelines(newlines)


def write_labelled_images_filenames(image_dir, out_filename):
    files = get_file_list(image_dir, False)
    with open(out_filename, 'w') as f:
        for filename in files:
            if filename.endswith('.jpg') and osp.isfile(osp.join(image_dir, coco_fileutils.filename_change_ext(filename, '.txt'))):
                f.write(osp.join(image_dir, filename) + '\n')


if __name__ == "__main__":
    write_labelled_images_filenames(
        user_path('Data/Coco/images/train2017'), user_path('/home/zli/Data/Coco/images/train_images.txt'))

# keep_only_labels(osp.join(osp.expanduser('~'), 'Data/Coco/labels/train2017'), '0')
# coco_fileutils.copy_files(user_path(
#     'Data/Coco/labels/val2017'), user_path('Data/Coco/images/val2017'))
