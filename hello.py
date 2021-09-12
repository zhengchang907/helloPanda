from PIL import Image
import cv2
import numpy
import glob

folders = glob.glob('/home/zhengchang/workspace/helloPanda/accessories')
imagenames_list = []
for folder in folders:
    for f in glob.glob(folder+'/*.jpg'):
        imagenames_list.append(f)

read_images = []        
for image in imagenames_list:
    read_images.append(cv2.imread(image, cv2.IMREAD_GRAYSCALE))

print(read_images)

# msg = "Hello World"

# face = Image.open('./face/tpanda.png')
# hat = Image.open('./hat/colorful.png')
# mouth = Image.open('./mouth/bamboo.png')
# background = Image. new('RGB', (100, 30), color = (73, 109, 137))

# background.paste(face, (38, 3), face)
# background.paste(hat, (38, 3), hat)
# background.paste(mouth, (38, 3), mouth)

# background.save('./target/test.png')
# print(msg)