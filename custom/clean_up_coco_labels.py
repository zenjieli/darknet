import os
import os.path as osp
from random import randrange

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


def files_with_large_enough_boxes(image_dir, count_to_extract):
    good_files = []
    files = get_file_list(image_dir, True, '.jpg')

    for filename in files:
        label_filename = coco_fileutils.filename_change_ext(filename, '.txt')

        if osp.isfile(label_filename):
            area = coco_fileutils.min_box_area(
                coco_fileutils.read_bounding_boxes(label_filename))
            if area > 0:
                good_files.append({'filepath': filename, 'area': area})

    good_files.sort(key=lambda f: f['area'])
    good_files = good_files[len(good_files) -
                            count_to_extract: len(good_files)]
    return list(map(lambda f: f['filepath'], good_files))


def files_without_labels(image_dir):
    target_files = []
    filenames = get_file_list(image_dir, True, '.jpg')

    for filename in filenames:
        label_filename = coco_fileutils.filename_change_ext(filename, '.txt')
        if osp.isfile(label_filename) and len(coco_fileutils.read_bounding_boxes(label_filename)) == 0:
            target_files.append(filename)

    return target_files


def copy_files_with_with_large_enough_boxes(src_image_dir, dest_image_dir, count_to_extract):
    filenames = files_with_large_enough_boxes(src_image_dir, count_to_extract)
    coco_fileutils.copy_files(filenames, dest_image_dir)


def randomly_select_labelless_images(src_image_dir, select_count):
    filenames = files_without_labels(src_image_dir)
    file_count = len(filenames)

    selected_filenames = []
    for i in range(select_count):
        selected_filenames.append(filenames[randrange(file_count)])

    return selected_filenames


if __name__ == "__main__":    
    # filenames = randomly_select_labelless_images(user_path('Data/Coco/images/train2017'), 2500)
    # coco_fileutils.copy_files(filenames, '/home/zli/Data/Coco/images/train/')
    # write_labelled_images_filenames(
    #     user_path('Data/Coco/images/train2017'), user_path('/home/zli/Data/Coco/images/train_images.txt'))

# keep_only_labels(osp.join(osp.expanduser('~'), 'Data/Coco/labels/train2017'), '0')
# coco_fileutils.copy_files_dir(user_path(
#     'Data/Coco/labels/val2017'), user_path('Data/Coco/images/val2017'))
