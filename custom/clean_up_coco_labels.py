import os
import os.path as osp


def get_file_list(full_path):
    files = []
    for root, _, filenames in os.walk(full_path):
        for filename in filenames:
            files.append(osp.join(root, filename))

        break

    return files


def keep_only_labels(label_path, label):
    files = get_file_list(label_path)

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

if __name__ == '__main__':
    keep_only_labels(osp.join(osp.expanduser(
        '~'), 'Data/Coco/labels/train2017'), '0')
