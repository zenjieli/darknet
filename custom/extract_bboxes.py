image_path_token = 'Enter Image Path:'
person_token = 'person:'

# lines - a list of strings
def try_add_one_detecton(lines):
    patches = []
    if len(lines) <= 1:
        return patches
    else:
        line = lines[0]
        if not line.startswith(image_path_token):
            raise Exception(f'Expected: {image_path_token}; Actual: {line}')

        token_len = len(image_path_token)
        img_path = line[len(token_len): line.find(':', token_len) - token_len]

        for i in range(1, len(lines)):
            line = lines[i]
            if not line.startswith(person_token):
                raise Exception(f'Expected: {person_token}; Actual: {line}')


def extract_bboxes(results, object_name='person', threshold_percent='50'):
    """
    Extract bounding boxes from the darknet export text file

    Args:
    results - lines of output from darknet inference, e.g.
        CUDNN_HALF=1
        seen 64, trained: 32013 K-images (500 Kilo-batches_64)
        Enter Image Path: /home/zli/data/hospital/ChieriCorridor/1/1.jpg: Predicted in 26.807000 milli-seconds.
        Enter Image Path: /home/zli/data/hospital/ChieriCorridor/1/13.jpg: Predicted in 32.587000 milli-seconds.
        person: 97%	(left_x: 1234   top_y:   70   width:   91   height:  236)
    threshold_percent - [0, 100]"""
    batch = []
    for line in results:
        if line.startswith(image_path_token):
            if len(batch) > 0:
                try_add_one_detecton(batch)
                batch.clear()

            batch.append(line)
        elif line.startswith(person_token):
            batch.append(line)

if __name__ == '__main__':
    result_file = open('/home/zli/data/hospital/ChieriCorridor/1/result.txt', 'r')
    extract_bboxes(result_file.readlines())
