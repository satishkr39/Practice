from PIL import Image
import os

#to get all the image of directory
input_path = "C:\\Users\\ssing255\\Downloads\\DownloadedImages"
output_path = "C:\\Users\\ssing255\\Downloads\\ModifiedImages\\"
all_tems = os.listdir(input_path)
print(len(all_tems))

for items in os.listdir(input_path):
    image_path = input_path+"\\"+items
    print(image_path)
    im = Image.open(image_path).convert("RGB")
    new_image = im.resize((640,480))
    new_image = new_image.rotate(90)
    file_name = (items.split("."))[0]
    print(file_name)
    new_image.save(output_path+file_name+".jpeg","jpeg")