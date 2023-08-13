import os
import glob
import shutil
import random
import copy_file


label = glob.glob("./Dataset/Label/*.txt")
print(label[:5])
random.shuffle(label)
print(label[:5])

valid_num = int(len(label) * 0.15)
test_num = int(len(label) * 0.15)

valid_data = label[:valid_num]
test_data = label[valid_num:valid_num+test_num]
train_data = label[valid_num+test_num:]

for file_type in ["labels", "images"]:
    for name in ["valid", "test", "train"]:
        os.makedirs(f"./datasets/{file_type}/{name}", exist_ok=True)

print(len(valid_data), len(test_data), len(train_data))
for file in valid_data:
    shutil.copy(file, "./datasets/labels/valid")
copy_file.run(label_list=valid_data, image="./Dataset/Images", dest="./datasets/images/valid")

for file in test_data:
    shutil.copy(file, "./datasets/labels/test")
copy_file.run(label_list=test_data, image="./Dataset/Images", dest="./datasets/images/test")

for file in train_data:
    shutil.copy(file, "./datasets/labels/train")
copy_file.run(label_list=train_data, image="./Dataset/Images", dest="./datasets/images/train")
