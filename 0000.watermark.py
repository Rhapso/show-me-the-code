from PIL import Image, ImageDraw, ImageFont

image_path = r'.\data\qq_avatar.png'
font_path = r'.\data\PeppaPigW07-Regular.ttf'
image_save_path = r'.\data\qq_avatar_numadded.png'
avatar = Image.open(image_path)
dr = ImageDraw.Draw(avatar)
# dr.line((0,0) + avatar.size, fill = 128, width=40)
# dr.line((0, avatar.size[1], avatar.size[0], 0), fill=128)
font = ImageFont.truetype(font_path, size=100)
dr.text((avatar.size[0]*0.8, avatar.size[1]*0.1), '4', font=font, fill=(230, 0, 0))
avatar.save(image_save_path)
