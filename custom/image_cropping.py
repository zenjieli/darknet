from PIL import Image
from os import path as osp
import os


def crop_and_save_images(img_patches):
    """
    img_patches: A list of dictionaries. Each dictionary defines the image path and a bounding box
    """

    for patch in img_patches:
        path = patch['img']
        img = Image.open(path)
        left = patch['left']
        top = patch['top']
        right = left + patch['width']
        bottom = top + patch['height']

        out_dir = osp.dirname(path) + '_cropped'

        if not osp.exists(out_dir):
            os.mkdir(out_dir)

        out_path = f'{out_dir}/{osp.splitext(osp.basename(path))[0]}_{left}_{top}.jpg'
        img.crop((left, top, right, bottom)).save(out_path)
