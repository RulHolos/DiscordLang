.. role:: raw-html(raw)
    :format: html

API Reference
=============

Reference to all of available classes, methods, attributes, etc.


DiscordLang Client
------------------

.. py:class:: DiscordLang.lang(client, lang_file, mode)

    :param discord.Bot client: The client instance of your bot.
    :type client: :class:`discord.Bot`
    :param str lang_file: The name of your file.
    :type lang_file: :class:`str`
    :param str mode: json/configparser
    :type mode: :class:`str`

    :raw-html:`<br />`

    .. py:method:: check_server_lang(message)

        Checks if the message's guild exists in the config file
        If not, write its id to the config file.
        Base lang is "en".

        :param discord.Message message: Given by the on_message event.
        :type message: :class:`discord.Message`

        :raw-html:`<br />`

    .. py:method:: create_file(langs)

        Create the configuration file.

        :param list langs: A `list` of langs which will populate the configuration file.
        :type langs: :class:`list`
        
        :raw-html:`<br />`

    .. py:method:: change_lang(id, lang)

        Change the guild's lang.

        :param int id: The id of the targeted guild.
        :type id: :class:`int`
        :param str lang: The lang prefix.
        :type lang: :class:`str`

        :raw-html:`<br />`

    .. py:method:: get_lang(id, field)

        Get a translated string depending of the guild's lang.

        :param int id: The id of the targeted guild.
        :type id: :class:`int`
        :param str field: The field name from which the data will be taken.
        :type field: :class:`str`
        :return: A translated string
        :rtype: :class:`str`

        :raw-html:`<br />`

    .. py:method:: add_lang(lang)

        Adds a lang into the config file.

        :param str lang: The lang name to add to the configuration file.
        :type lang: :class:`str`

Exceptions
----------

.. py:class:: DiscordLang.models.DiscordLangException

    Base Exception for the DiscordLang module. All exceptions inherits from this one.

    :raw-html:`<br />`

.. py:class:: DiscordLang.models.FileAlreadyExists

    Raised when the lang_file already exists

    :raw-html:`<br />`

.. py:class:: DiscordLang.models.FieldDoesNotExists

    Raised when a requested field doesn't exists in the lang file

    :raw-html:`<br />`

.. py:class:: DiscordLang.models.LangAlreadyExists

    Raised when a language already exists within the lang file

    :raw-html:`<br />`

.. py:class:: DiscordLang.models.LangDoesntExist

    Raised when a language doesn't exists within the config file

    :raw-html:`<br />`