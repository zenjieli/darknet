from shutil import copyfile
import os.path as osp
import os


def user_path(path1):
    return osp.join(osp.expanduser('~'), path1)


def get_file_list(root_dir, need_fullpath):
    files = []
    for root, _, filenames in os.walk(root_dir):
        for filename in filenames:
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
