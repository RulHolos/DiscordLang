import discord, asyncio, json, configparser
from discord.ext import commands, tasks

from .models import FileAlreadyExists, FieldDoesNotExists, LangAlreadyExists

class lang(object):
    """The Discord database client.
    Parameters
    ----------
    bot : discord.ext.commands.Bot
        An instance of discord.py Client or Bot representing your discord application
    lang_file : File path
        A file in which the lang data will be dumped into.
    mode : str
        The mode of storage for the data.
    """
    def __init__(self, bot, lang_file:str, mode:str):
        self.__bot = bot
        self.__lang_file = lang_file
        self.__mode = mode.lower()
        self.modes = ["configparser", "json"]

    def check_server_lang(self, message):
        if self.__mode == "json":
            with open(self.__lang_file, 'r') as f:
                data = json.load(f)
            if str(message.guild.id) in data["servers"]:
                pass
            else:
                data["servers"][str(message.guild.id)] = "en"
            with open(self.__lang_file, 'w') as f:
                json.dump(data, f, indent=2)
        elif self.__mode == "configparser":
            config = configparser.ConfigParser()
            config.read(self.__lang_file)
            if str(message.guild.id) in config["servers"]:
                pass
            else:
                config["servers"][str(message.guild.id)] = "en"
                with open(self.__lang_file, 'w') as f:
                    config.write(f)

    def create_file(self, langs):
        """Create the lang file.
        Parameters
        -----------
        langs : list
            A list of base languages (only used for init)"""
        try:
            with open(self.__lang_file, 'x') as f:
                pass
            self._set_mode(langs)
        except:
            raise FileAlreadyExists(f"This file already exists : {self.__lang_file}")

    def _set_mode(self, langs):
        """Initialize the file's mode.
        THIS WILL OVERWRITE ANYTHING ALREADY IN THE FILE.
        Parameters
        -----------
        langs : list
            A list of base languages (only used for init)"""
        if self.__mode == "configparser":
            config = configparser.ConfigParser()
            config.read(self.__lang_file)
            config["servers"] = {}
            for lang in langs:
                config[lang] = {}
            with open(self.__lang_file, 'w') as configfile:
                config.write(configfile)
        elif self.__mode == "json":
            with open(self.__lang_file, 'w') as f:
                f.write("{}")
            with open(self.__lang_file, 'r') as f:
                data = json.load(f)
                data["servers"] = {}
                for lang in langs:
                    data[lang] = {}
            with open(self.__lang_file, 'w') as f:
                json.dump(data, f, indent=2)

    def change_lang(self, _id:int, _lang:str):
        _id = str(_id)
        if self.__mode == "configparser":
            config = configparser.ConfigParser()
            config.read(self.__lang_file)
            if not _lang in config:
                raise LangDoesntExist("This language doesn't exist.")
            config["servers"][_id] = _lang
            with open(self.__lang_file, 'w') as f:
                config.write(f)
        elif self.__mode == "json":
            with open(self.__lang_file, "r") as f:
                data = json.load(f)
            if not _lang in data:
                raise LangDoesntExist("This language doesn't exist.")
            data["servers"][_id] = _lang
            with open(self.__lang_file, 'w') as f:
                json.dump(data, f, indent=2)
    
    def get_lang(self, _id:int, field:str):
        try:
            _id = str(_id)
            if self.__mode == "configparser":
                config = configparser.ConfigParser()
                config.read(self.__lang_file)
                return config[config["servers"][_id]][field]
            elif self.__mode == "json":
                with open(self.__lang_file, "r") as f:
                    data = json.load(f)
                return data[data["servers"][_id]][field]
        except:
            raise FieldDoesNotExists(f'The field "{field}" does not exists.')

    def add_lang(self, lang:str):
        if self.__mode == "configparser":
            config = configparser.ConfigParser()
            config.read(self.__lang_file)
            if lang in config:
                raise LangAlreadyExists(f"This language already exists : {lang}")
            else:
                config[lang] = {}
                for key, value in config["en"].items():
                    config[lang][key] = ""
                with open(self.__lang_file, 'w') as f:
                    config.write(f)
        elif self.__mode == "json":
            with open(self.__lang_file, 'r') as f:
                data = json.load(f)
            if lang in data:
                raise LangAlreadyExists(f"This language already exists : {lang}")
            data[lang] = {}
            for key, value in data["en"].items():
                data[lang][key] = ""
            with open(self.__lang_file, 'w') as f:
                json.dump(data, f, indent=2)