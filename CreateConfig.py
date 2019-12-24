import configparser
from PIL import ImageColor


class ConfigClass(object):

    def __init__(self, configfile_name):
        self.Config = configparser.ConfigParser()
        self.configfile_name = configfile_name
        self.section = "options"
        self.width = ''
        self.height = ''
        self.font_color = ''
        self.second_font_color = ''
        self.background_color = ''
        self.min_font_size = ''
        self.max_font_size = ''

    def get_whole_config(self):
        # config variables
        self.width = self.get_config("width")
        self.height = self.get_config("height")
        self.font_color = self.get_config("font_color", False)
        self.second_font_color = self.get_config("second_font_color", False)
        self.background_color = ImageColor.getrgb(self.get_config("background_color", False))
        self.min_font_size = self.get_config("min_font_size")
        self.max_font_size = self.get_config("max_font_size")

    def create_config(self):
        width = input("width of .jpg file in px: ")
        height = input("height of .jpg file in px: ")
        font_color = input("First font color: ")
        second_font_color = input("Second font color: ")
        background_color = input("Background color: ")
        min_font_size = input("Min font size: ")
        max_font_size = input("Max font size: ")

        cfg_file = open(self.configfile_name, 'w')
        self.Config.add_section(self.section)
        self.Config.set(self.section, 'width', width)
        self.Config.set(self.section, 'height', height)
        self.Config.set(self.section, 'min_font_size', min_font_size)
        self.Config.set(self.section, 'max_font_size', max_font_size)
        self.Config.set(self.section, 'font_color', font_color)
        self.Config.set(self.section, 'second_font_color', second_font_color)
        self.Config.set(self.section, 'background_color', background_color)
        self.Config.write(cfg_file)
        cfg_file.close()

    def get_config(self, option, is_int=True):
        self.Config.read(self.configfile_name)
        config_option = self.Config.get(self.section, option)
        if is_int:
            config_option = int(config_option)
        return config_option
