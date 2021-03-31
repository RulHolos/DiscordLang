# DiscordLang

A discord extension that makes working with languages a little bit easier.

### Features
* Adding languages to the database
* Supports json and configparser (ini) formats.
* Work with a lot of different languages
* No need to tweak anything with your other config files. 

### Installation

To install current latest release you can use following command:
```sh
python3 -m pip install DiscordLang
```


### Basic Example
```python
from discord.ext import commands, DiscordLang

class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix="!")
        self.lang = DiscordLang.lang(
            client=self,
            lang_file="The name of file you want",
            mode="json/configparser, the way you want to interract with your lang file"
        )
    
    async def on_message(self, message):
        self.lang.check_server_lang(message)
        """
        This is needed for your bot to work correctly with DiscordLang.
        What it does is checking if the message's guild is in the lang file.
        It will then be able to read the language of the guild from its entry.
        
        The base lang when setting up the guild in the lang file is english."""

    @commands.command()
    async def print_some_text(self, ctx):
        await ctx.send(self.lang.get_lang(ctx.guild.id, "test_text"))
        """
        Given the lang file (json) :
        {
            "en": {
                "test_text": "some value to print"
            },
            "fr": {
                "test_text": "une valeur"
            },
            "servers": {
                some_guild_id: "en"
            }
        },
        the bot will print the value of the field, by the guild's lang.
        """

bot = MyBot()
bot.run("TOKEN")
```

### Requirements
* discord.py

### Documentation
Head over to [documentation] for full API reference.

[documentation]: https://discordlang.readthedocs.io/en/latest/