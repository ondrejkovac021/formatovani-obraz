from PIL import Image, ImageFilter, ImageEnhance

image = Image.open("images/input_image.jpg")

blurred_image = image.filter(ImageFilter.BLUR)
contrasted_image = ImageEnhance.Contrast(image).enhance(2)

cropped_image = image.crop((100, 100, 400, 400))  # Oříznutí na čtverec

resized_image = image.resize((500, 500), Image.ANTIALIAS)  # Změna velikosti na 500x500 pixelů

blurred_image.save("images/blurred_image.jpg")
contrasted_image.save("images/contrasted_image.jpg")
cropped_image.save("images/cropped_image.jpg")
resized_image.save("images/resized_image.jpg")

blurred_image.show()
contrasted_image.show()
cropped_image.show()
resized_image.show()
