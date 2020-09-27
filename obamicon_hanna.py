from PIL import Image
im = Image.open("rsz_olddanny.jpg")
colors = list(im.getdata())

# dark_blue = (0, 51, 76)
# light_blue = (112, 150, 158)
# red = (217, 26, 33)
# yellow = (252, 227 , 166)
new_colors = list()
for pixel in colors: 
		intensity = pixel[0] + pixel[1] + pixel[2]
		# intense = tuple(intensity)
		if intensity < 182: 
			pixel = (0, 51, 76)
		elif intensity < 364: 
			pixel = (217, 26, 33)
		elif intensity < 546:
			pixel = (112, 150, 158)
		else:
			pixel = (252, 227, 166)
		new_colors.append(pixel)

new_im = Image.new("RGB", im.size)
new_im.putdata(new_colors)
new_im.save("newdanny.jpg")