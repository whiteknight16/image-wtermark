from PIL import Image,ImageFont,ImageDraw
import matplotlib.pyplot as plt
import time

file=input("Enter file path: ")
file=file.strip('""')
image=Image.open(file)

watermark_image=image.copy()
draw=ImageDraw.Draw(watermark_image)

w,h=image.size
x,y=int(w/4),int(h/4)
font_size=max(x,y)

font=ImageFont.truetype("arial.ttf",int(font_size/3))

draw.text((x,y),input("Enter the watermark text: "),fill=input("Enter the color: "),font=font,anchor="ms")
plt.subplot(1, 2, 1)
print("Adding watermark ......")
time.sleep(2)
plt.title("Watermarked_image")
watermark_image.save(input("Enter the name to save image with:")+".png")
print("Image Saved.....")