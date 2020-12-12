def parse_bb_internal(str):
    """
    str: For example, (left_x: 1234   top_y:   70   width:   91   height:  236)
    """

    # Tokens
    left_tk = 'left_x:'
    top_tk = 'top_y:'
    width_tk = 'width:'
    height_tk = 'height:'

    str = str.strip()
    left_idx = str.find(left_tk)
    top_idx = str.find(top_tk)
    width_idx = str.find(width_tk)
    height_idx = str.find(height_tk)

    if left_idx <= 0 or top_idx < 0 or width_idx < 0 or height_idx < 0:
        raise Exception(f'Failed to find bounding boxes in {str}.')

    bb = {}
    bb['left'] = int(str[left_idx + len(left_tk): top_idx])
    bb['top'] = int(str[top_idx + len(top_tk): width_idx])
    bb['width'] = int(str[width_idx + len(width_tk): height_idx])
    bb['height'] = int(str[height_idx + len(height_tk): len(str) - 1])

    return bb


def try_parse_bb(str, conf_threshold):
    """
    person: 97%	(left_x: 1234   top_y:   70   width:   91   height:  236)
    conf_threshold: Confidence threshold [0, 100]
    """

    person_tk = 'person:'

    str = str.strip()

    if not str.startswith(person_tk):
        raise Exception(f'{person_tk} missing in {str}')

    percent = int(str[len(person_tk): str.find('%', len(person_tk))].strip())
    if (percent < conf_threshold):
        return None

    return parse_bb_internal(str)
