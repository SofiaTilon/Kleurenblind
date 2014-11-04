# Print names to a map
# Needed: list with locations/names/colors. Should line-up
#
#
#

from PIL import Image, ImageDraw, ImageFont

# Lists voor x,y en naam
locations = [(68,87), (68, 150), (180,93), (150,210), (280,70), (290,165), (290,265), (235, 540), (814, 708), (755,445), (370,760), (600, 300)]
names = ["LEON", "ZAMORA", "JAEN", "BURGOS", "GUIPUZCOA", "MURCIA", "TOLEDO", "BARCELONA", "ALAVA", "LA CORUNA", "LAS PALMAS", "BADAJOZ"]
color = [(0,0,0,255), (0,0,255,255), (0,255,0,255), (255,0,0,255)]

# load basemap image
basemap = Image.open('spain_.jpg').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', basemap.size, (0,0,0,0))
# get a font
font = ImageFont.truetype('calibri.ttf', 20)
# get a drawing context
draw = ImageDraw.Draw(txt)

for i in range(len(names)):
	# draw text, full opacity
	draw.text(locations[i], names[i], font=font, fill=color[i%4])

out = Image.alpha_composite(basemap, txt)

out.show()

