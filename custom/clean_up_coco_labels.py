import os
import os.path as osp
from random import randrange
from shutil import copyfile

import coco_fileutils
from coco_fileutils import get_file_list
from coco_fileutils import user_path

# Keep only a label when the Id is equal to the input one
def keep_only_labels(label_dir, label_id):
    files = get_file_list(label_dir, True, '.txt')

    for filepath in files:
        lines = []
        with open(filepath, 'r') as f:
            lines = f.readlines()

        newlines = []
        for line in lines:
            words = line.split()
            if len(words) > 0 and words[0].strip() == label_id:
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


# size_low_threshold, size_high_threshold: [0, 1], the range for a bounding box
def get_files_with_boxes_in_range(image_dir, size_low_threshold, size_high_threshold):
    good_files = []
    files = get_file_list(image_dir, True, '.jpg')

    for filename in files:
        label_filename = coco_fileutils.filename_change_ext(filename, '.txt')

        if osp.isfile(label_filename):
            area = coco_fileutils.min_box_area(coco_fileutils.read_bounding_boxes(label_filename))
            if area >= size_low_threshold and area <= size_high_threshold:
                good_files.append(filename)

    return good_files


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


def randomly_select_images(src_image_dir, select_count):
    filenames = get_file_list(src_image_dir, True, '.jpg')
    file_count = len(filenames)
    indices = set()

    if select_count >= file_count:
        return filenames
    else:
        selected_filenames = []
        for i in range(select_count):
            idx = randrange(file_count)
            while idx in indices:
                idx = randrange(file_count)

            indices.add(idx)
            selected_filenames.append(filenames[idx])

        return selected_filenames


def randomly_select_labelless_images(src_image_dir, select_count):
    filenames = files_without_labels(src_image_dir)
    file_count = len(filenames)

    selected_filenames = []
    indices = set()
    for i in range(select_count):
        idx = randrange(file_count)
        while idx in indices:
            idx = randrange(file_count)

        indices.add(idx)
        selected_filenames.append(filenames[idx])

    return selected_filenames

# Copy corresponding labels from label_dir to image_dir


def copy_labels(image_dir, label_dir):
    filenames = get_file_list(image_dir, True, '.jpg')

    for filename in filenames:
        label_filename = coco_fileutils.get_label_filename(filename, label_dir)
        if not osp.isfile(label_filename):
            raise Exception(f'File does not exist: {label_filename}')

        copyfile(label_filename, osp.join(image_dir, osp.basename(label_filename)))


if __name__ == "__main__":
    keep_only_labels('/home/zli/Data/Person/cctv1', '0')
    # filenames = randomly_select_images(user_path('Data/Coco/images/train'), 10000)
    # coco_fileutils.copy_files(filenames, '/home/zli/Data/Coco/images/3/')
    # filenames = randomly_select_labelless_images(
    #     user_path('Data/Coco/images/val2017'), 500)
    # coco_fileutils.copy_files(filenames, '/home/zli/Data/Coco/images/2/')
    # write_labelled_images_filenames(
    #     user_path('Data/Coco/images/train2017'), user_path('/home/zli/Data/Coco/images/train_images.txt'))

# keep_only_labels(osp.join(osp.expanduser('~'), 'Data/Coco/labels/train2017'), '0')
# coco_fileutils.copy_files_dir(user_path(
#     'Data/Coco/labels/val2017'), user_path('Data/Coco/images/val2017'))
