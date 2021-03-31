class DiscordLangException(Exception):
    """Base error class for DiscordLang errors"""
    pass

class FileAlreadyExists(DiscordLangException):
    """Raised when the lang_file already exists"""
    pass

class FieldDoesNotExists(DiscordLangException):
    """Raised when a requested field doesn't exists in the lang file"""
    pass

class LangAlreadyExists(DiscordLangException):
    """Raised when a language already exists within the lang file"""
    pass

class LangDoesntExist(DiscordLangException):
    """Raised when a language doesn't exists within the config file"""
    pass