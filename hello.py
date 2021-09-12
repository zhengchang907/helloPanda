from PIL import Image
import glob
from pathlib import Path

## load face
face_images = []        
for f in glob.glob('./face/*.png'):
    face_images.append(Image.open(f))

## load accessories
accessories_images = []        
for f in glob.glob('./accessories/*.png'):
    accessories_images.append(Image.open(f))

## load ear
ear_images = []        
for f in glob.glob('./ear/*.png'):
    ear_images.append(Image.open(f))

## load eye
eye_images = []        
for f in glob.glob('./eye/*.png'):
    eye_images.append(Image.open(f))

## load head
head_images = []        
for f in glob.glob('./head/*.png'):
    head_images.append(Image.open(f))

## load mouth
mouth_images = []        
for f in glob.glob('./mouth/*.png'):
    mouth_images.append(Image.open(f))

print("Hello Panda")

for face in face_images: 
    for head in head_images: 
        for mouth in mouth_images: 
            for accessory in accessories_images: 
                background = Image.new('RGBA', (24, 24), (255, 0, 0, 0))
                background.paste(face, (0, 0), face)
                background.paste(head, (0, 0), head)
                background.paste(mouth, (0, 0), mouth)
                background.paste(accessory, (0, 0), accessory)
                background.save('./target/test.png')
                facefilename = Path(str(face.filename)).stem
                headfilename = Path(str(head.filename)).stem
                if headfilename == 'empty':
                    headfilename = ''
                else:
                    headfilename = ' with ' + headfilename
                mouthfilename = Path(str(mouth.filename)).stem
                if mouthfilename == 'empty':
                    mouthfilename = ''
                elif headfilename == '':
                    mouthfilename = ' with ' + mouthfilename
                else:
                    mouthfilename = ' and ' + mouthfilename
                accessoryfilename = Path(str(accessory.filename)).stem
                if accessoryfilename == 'empty':
                    accessoryfilename = ''
                elif ((headfilename == '') and (mouthfilename == '')):
                    accessoryfilename = ' with ' + accessoryfilename
                else:
                    accessoryfilename = ' and ' + accessoryfilename
                filename =  facefilename + headfilename + mouthfilename + accessoryfilename
                background.save('./target/' + filename + '.png')