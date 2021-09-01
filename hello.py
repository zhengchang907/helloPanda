from PIL import Image

msg = "Hello World"

face = Image.open('./face/tpanda.png')
hat = Image.open('./hat/colorful.png')
mouth = Image.open('./mouth/bamboo.png')
background = Image. new('RGB', (100, 30), color = (73, 109, 137))

background.paste(face, (38, 3), face)
background.paste(hat, (38, 3), hat)
background.paste(mouth, (38, 3), mouth)

background.save('./target/test.png')
print(msg)