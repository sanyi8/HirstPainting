import colorgram as cg

color_list = cg.extract("image.jpg", 30)

color_palette = []
# from stackoverflow
for i in range(len(color_list)):
    r = color_list[i].rgb.r
    g = color_list[i].rgb.g
    b = color_list[i].rgb.b
    new_color = (r, g, b)

    # ignore colors with possible bg grays where each color codes around 255
    colorcheck = r+g+b
    # set sensitivity 600-700
    if colorcheck < 700:
        color_palette.append(new_color)


print(color_palette)
