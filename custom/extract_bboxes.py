from yolo_result_parsing import try_parse_bb

image_path_token = 'Enter Image Path:'
person_token = 'person:'


def try_add_patch(lines, img_patches):
    if len(lines) <= 1:
        return
    else:
        line = lines[0]
        if not line.startswith(image_path_token):
            raise Exception(f'Expected: {image_path_token}; Actual: {line}')

        token_len = len(image_path_token)
        img_path = line[token_len: line.find(':', token_len)].strip()

        for i in range(1, len(lines)):
            bb = try_parse_bb(lines[i], 50)
            if bb != None:
                bb['img'] = img_path
                img_patches.append(bb)


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
    threshold_percent - [0, 100]
    """
    batch_lines = []
    img_patches = []
    for line in results:
        if line.startswith(image_path_token):
            if len(batch_lines) > 0:
                try_add_patch(batch_lines, img_patches)
                batch_lines.clear()

            batch_lines.append(line)
        elif line.startswith(person_token):
            batch_lines.append(line)

    return img_patches    


if __name__ == '__main__':
    result_file = open(
        '/home/zli/data/hospital/ChieriCorridor/1/result.txt', 'r')
    img_patches = extract_bboxes(result_file.readlines())
    
    from image_cropping import crop_and_save_images
    crop_and_save_images(img_patches)
