from PIL import Image, ImageDraw
from CreateConfig import ConfigClass
from DrawFunction import DrawFunction
import os

# create and get config
configfile_name = "config.ini"
Config = ConfigClass(configfile_name)

if not os.path.isfile(configfile_name):
    Config.create_config()
Config.get_whole_config()

if not os.path.isdir('images'):
    os.mkdir('images')
if not os.path.isdir('texts'):
    os.mkdir('texts')
    test_text = open('texts/text1.txt', "w")
    test_text.write("Test line\n")
    test_text.write("%\n")
    test_text.write("*Second test* line\n")
    test_text.close()

    test_text2 = open('texts/test2.txt', "w")
    test_text2.write("Second text here\n")


def create_image():
    img = Image.new('RGB', (Config.width, Config.height), color=Config.background_color)
    draw = ImageDraw.Draw(img)

    draw_function = DrawFunction(draw, Config, lines)
    draw_function.start_drawing()

    img.save(folder_name+'/img'+str(x)+'.jpg')


for file in os.listdir("texts"):
    if file.endswith(".txt"):
        text_name = os.path.join("texts", file)
        folder_name = os.path.join('images/', file[:-4])

        if os.path.isdir(folder_name):
            for i in os.listdir(folder_name):
                os.remove(os.path.join(folder_name, i))
        else:
            os.mkdir(folder_name)

        all_lines = open(text_name, mode='r', encoding='utf-8-sig')
        lines = []
        x = 1

        for line in all_lines:
            if line.strip('\n') == "%":
                create_image()
                x += 1
                lines = []
            else:
                lines.append(line)
        create_image()
        all_lines.close()

