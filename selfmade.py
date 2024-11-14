import colorgram

from main import color_list

# from main import new_color

colors = colorgram.extract('image.jpg', 30)

# list for colors
rgb_colors = []
# to get in RGB format use loop
for color in colors:
    # rgb_colors.append(color.rgb)  # e.g. (255, 151, 210)
    # RGB are named tuples, so values can be accessed as properties.
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    # create the tuple
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)

# remove colours with numbers close to 255 they are bg whites
color_list = [(132, 168, 203), (193, 164, 142), (62, 89, 139), (120, 78, 99), (184, 152, 172), (158, 75, 47), (54, 119, 94), (220, 230, 85), (137, 191, 151), (45, 52, 106), (113, 116, 184), (36, 44, 62), (226, 134, 14), (175, 187, 214), (176, 95, 115), (90, 47, 62), (213, 181, 194), (35, 29, 28), (41, 49, 45), (56, 41, 51), (109, 168, 71), (111, 39, 36), (224, 79, 40), (233, 174, 157), (165, 208, 176), (23, 98, 79)]
