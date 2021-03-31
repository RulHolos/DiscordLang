import re
import setuptools


with open("discord/ext/DiscordLang/__init__.py") as stream:
    version = re.search(
        r"^__version__\s*=\s*[\'\"]([^\'\"]*)[\'\"]", stream.read(), re.MULTILINE
    ).group(1)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Topic :: Internet",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

extras_require = {
    "docs": ["sphinx", "sphinxcontrib_trio", "sphinx-rtd-theme"],
}

project_urls = {
    "Issue Tracker": "https://github.com/AtaeKurri/discord-ext-DiscordLang/issues",
    "Source": "https://github.com/AtaeKurri/discord-ext-DiscordLang",
}

setuptools.setup(
    author="AtaeKurri",
    classifiers=classifiers,
    description="A discord.py extension to make languages a bit easier to work with",
    extras_require=extras_require,
    install_requires=["discord.py"],
    license="Apache Software License",
    name="DiscordLang",
    packages=["discord.ext.DiscordLang"],
    project_urls=project_urls,
    python_requires=">=3.5.3",
    url="https://github.com/AtaeKurri/discord-ext-DiscordLang",
    version=version,
    long_description=long_description,
    long_description_content_type="text/markdown",
)