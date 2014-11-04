# Print names to a map
# Needed: list with locations/names. Should line-up. -> EDIT to handle classes later?
#
#
#

from PIL import Image, ImageDraw, ImageFont

# Lists voor x,y en naam
locations = [(68,87), (68, 150), (180,93), (150,210), (280,70), (290,165), (290,265), (235, 540), (814, 708), (755,445), (370,760), (600, 300)]
names = ["LEON", "ZAMORA", "JAEN", "BURGOS", "GUIPUZCOA", "MURCIA", "TOLEDO", "BARCELONA", "ALAVA", "LA CORUNA", "LAS PALMAS", "BADAJOZ"]
colors = [(0,0,0,255), (0,0,255,255), (0,255,0,255), (255,0,0,255)]

def plot_to_map(coordinates, names, colors):
	'''
	Takes as input three lists, which should all line-up:
		- names (list in which all province/state names are stored)
		- coordinates (list with coordinates formatted as (x,y))
		- colors ()

	'''
	# load basemap image and make blank image for text
	basemap = Image.open('spain_.jpg').convert('RGBA')
	txt = Image.new('RGBA', basemap.size)

	# get font
	font = ImageFont.truetype('calibri.ttf', 20)

	# get a drawing context
	draw = ImageDraw.Draw(txt)

	for i in range(len(names)):
		# draw text on map, rotate colors
		draw.text(locations[i], names[i], font=font, fill=colors[i%len(colors)])

	# draw text layer on top of image layer
	out = Image.alpha_composite(basemap, txt)

	# showtime .. 
	out.show()

# try it!
plot_to_map(locations, names, colors);

