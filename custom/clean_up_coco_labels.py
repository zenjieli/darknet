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


def copy_files_with_with_large_enough_boxes(src_image_dir, dest_image_dir):
    filenames = files_with_large_enough_boxes(src_image_dir, 30000)
    coco_fileutils.copy_files(filenames, dest_image_dir)


if __name__ == "__main__":
    copy_files_with_with_large_enough_boxes(user_path('Data/Coco/images/train2017'),
                                            user_path('Data/Coco/images/train'))
    # write_labelled_images_filenames(
    #     user_path('Data/Coco/images/train2017'), user_path('/home/zli/Data/Coco/images/train_images.txt'))

# keep_only_labels(osp.join(osp.expanduser('~'), 'Data/Coco/labels/train2017'), '0')
# coco_fileutils.copy_files_dir(user_path(
#     'Data/Coco/labels/val2017'), user_path('Data/Coco/images/val2017'))
