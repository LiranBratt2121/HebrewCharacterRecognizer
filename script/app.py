from rembg import remove
from ultralytics import YOLO
from PIL import Image

"""
    The initial script that should work exactly the same as the OOP based one but this one is wayyy more basic.
    It loads the model, removes the background from the input image, and then saves the output image.
    The output image is then used as input for the YOLO model to predict the class of the object in the image.
    The predicted class is then printed to the console.
"""

model = YOLO("weights/best.pt")

input_image = Image.open('example_images/test4.jpeg')
output_image = remove(input_image)

output_image = output_image.convert("RGBA")

data = output_image.getdata()
updated_image_data = [(0, 0, 0, 255) if item[3] > 0 else item for item in data]
output_image.putdata(updated_image_data)

output_image = output_image.resize((800, 600))

white_background = Image.new("RGBA", list(map(lambda s: s * 2, output_image.size)), (255, 255, 255, 255))
white_background.paste(output_image, list(map(lambda s: s // 2, output_image.size)), output_image)

white_background.save("output.png")
white_background.show()

result = model.predict(source="output.png", conf=0.2, verbose=False)[0]
print(result.names.get(result.boxes.cls[0].item(), 'Unknown'))