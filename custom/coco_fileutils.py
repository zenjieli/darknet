from shutil import copyfile
import os.path as osp
import os


def user_path(path1):
    return osp.join(osp.expanduser('~'), path1)


def get_file_list(root_dir, need_fullpath, ext = ''):
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


def copy_files(src, dest):
    files = get_file_list(src, False)

    for filename in files:
        copyfile(osp.join(src, filename), osp.join(dest, filename))

def read_bounding_boxes(label_path):
    boxes = []
    lines = []
    with open(label_path, 'r') as f:
        lines = f.readline()
    
    for line in lines:
        words = line.split()

        if len(words) != 0 and len(words) != 5:
            raise Exception(f"Wrong label " + line)                

        boxes.append({'left': words[1], 'top', words[2], 'w', words[3], 'h', words[4]})
    
    return boxes

def are_boxes_large_enough(boxes, min_w, min_h):
    for box in boxes:
        if box['w'] < min_w and box['w'] < min_h:
            return False
    
    # Boxes are large enough unless the list is emptry
    return len(boxes) > 0
