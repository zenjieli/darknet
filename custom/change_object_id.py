import os


def replace_line_id(line):
    words = line.split()
    if words[0] == old_id:
        words[0] = new_id
        return True, ' '.join(words)

    return False, line


label_path = '/home/zli/data/weapons/gun_train_images'
old_id = '0'
new_id = '1'

# Get all text files
text_files = []
for root, dirs, filenames in os.walk(label_path):
    for filename in filenames:
        if filename.lower().endswith('.txt'):
            text_files.append(os.path.join(root, filename))

    break

# Update all text files
for filepath in text_files:
    file = open(filepath, 'r')
    lines = file.readlines()
    new_lines = []
    file_updated = False
    for line in lines:
        updated, new_line = replace_line_id(line)
        file_updated = file_updated or updated
        new_lines.append(new_line)

    if file_updated:
        open(filepath, 'w').writelines(new_lines)
