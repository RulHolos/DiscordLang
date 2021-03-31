.. _intro:


Introduction
============

A discord extension that makes working with languages a little bit easier.
It makes adding languages and getting information from them really easy and fast.


Requirements
------------

**discord.py**
    It requires ``discord.py`` as a main wrapper.


Installing
----------

You can install DiscordLang directly from PyPI using PIP and following command
in shell or command prompt: ::

    python3 -m pip install DiscordLang


Basic Usage
-----------

.. code-block:: python3

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