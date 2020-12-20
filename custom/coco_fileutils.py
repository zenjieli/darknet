from shutil import copyfile
import os.path as osp
import os


def user_path(path1):
    return osp.join(osp.expanduser('~'), path1)


def get_file_list(root_dir, need_fullpath, ext=''):
    files = []
    ext = ext.lower()
    for root, _, filenames in os.walk(root_dir):
        for filename in filenames:
            # Wrong extension, skip it
            if ext != '' and not filename.lower().endswith(ext):
                continue

            if need_fullpath:
                files.append(osp.join(root, filename))
            else:
                files.append(filename)

        break

    return files


def count_images_with_persons(label_path):
    count = 0
    files = get_file_list(label_path, True)

    for filepath in files:
        lines = []
        with open(filepath, 'r') as f:
            lines = f.readlines()

        if len(lines) > 0:
            count += 1

    return count


def filename_change_ext(filename, new_ext):
    pre, _ = osp.splitext(filename)
    return pre + new_ext


def copy_files_dir(src_dir, dest_dir):
    files = get_file_list(src_dir, False)

    for filename in files:
        copyfile(osp.join(src_dir, filename), osp.join(dest_dir, filename))


def copy_files(src_files, dest_dir):
    for filename in src_files:
        copyfile(filename, osp.join(dest_dir, osp.basename(filename)))

        if not osp.isfile(osp.join(dest_dir, osp.basename(filename))):
            print('Error')


def read_bounding_boxes(label_path):
    boxes = []
    lines = []
    with open(label_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        words = line.split()

        if len(words) != 0 and len(words) != 5:
            raise Exception(f"Wrong label " + line)

        boxes.append({'x_center': float(words[1]), 'y_center': float(words[2]),
                      'width': float(words[3]), 'height': float(words[4])})

    return boxes


def get_label_filename(image_filename, label_dir):
    basename = osp.basename(image_filename)

    return osp.join(label_dir, filename_change_ext(basename, '.txt'))


def min_box_area(boxes):
    areas = list(map(lambda box: box['width'] * box['height'], boxes))

    return min(areas) if len(areas) > 0 else 0
