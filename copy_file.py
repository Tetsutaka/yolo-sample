import os
from shutil import copy
import glob

def run(label_list, image, dest):
    os.makedirs(dest, exist_ok=True)
    for file in label_list:
        basename = os.path.splitext(os.path.basename(file))[0]
        # dirname = os.path.dirname(file)
        try:
            copy(os.path.join(image, f"{basename}.jpg"), dest)
            # print(f"copied {basename}.jpg to {dest}")
        except BaseException as e:
            print(e)


def main():
    LABEL_SOURCE = "Label"
    IMAGE_SOURCE = "JPGFiles"
    DESTINATION = "Images"
    files = glob.glob(os.path.join(LABEL_SOURCE, "*.txt"))
    print(len(files))
    run(label_list=files, image=IMAGE_SOURCE, dest=DESTINATION)

if __name__ == "__main__":
    main()
