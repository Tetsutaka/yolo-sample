'''
This program creates a dataset with a directory structure suitable for training in YOLOv8 from a downloaded dataset.
Original dataset can be downloaded from the link below.
https://www.kaggle.com/datasets/aditya276/face-mask-dataset-yolo-format
'''
import os
import shutil

src_dirs = [f"dataset/images/{dirname}" for dirname in ["test", "train", "valid"]]
dst_dirs_texts = ["datasets/label/test", "datasets/label/train", "datasets/label/valid"]
dst_dirs_images = ["datasets/images/test", "datasets/images/train", "datasets/images/valid"]
image_type = (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG")

for dst in dst_dirs_texts + dst_dirs_images:
    if not os.path.exists(dst):
        os.makedirs(dst)

for src, dst_text, dst_image in zip(src_dirs, dst_dirs_texts, dst_dirs_images):
    for filename in os.listdir(src):
        src_path = os.path.join(src, filename)
        if filename.endswith(".txt"):
            shutil.copy(src_path, dst_text)
            print(f"Copied {src_path} -> {dst_text}")
        elif filename.endswith(image_type):
            shutil.copy(src_path, dst_image)
            print(f"Copied {src_path} -> {dst_image}")
