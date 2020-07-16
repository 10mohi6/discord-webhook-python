# discordwebhook

[![PyPI](https://img.shields.io/pypi/v/discordwebhook)](https://pypi.org/project/discordwebhook/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/10mohi6/discord-webhook-python/branch/master/graph/badge.svg)](https://codecov.io/gh/10mohi6/discord-webhook-python)
[![Build Status](https://travis-ci.com/10mohi6/discord-webhook-python.svg?branch=master)](https://travis-ci.com/10mohi6/discord-webhook-python)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/discordwebhook)](https://pypi.org/project/discordwebhook/)
[![Downloads](https://pepy.tech/badge/discordwebhook)](https://pepy.tech/project/discordwebhook)

discordwebhook is a python library for discord webhook with discord rest api on Python 3.6 and above.


## Installation

    $ pip install discordwebhook

## Usage

### basic
```python
from discordwebhook import Discord

discord = Discord(url="<your webhook url>")
discord.post(content="Hello, world.")
```
![basic.png](https://raw.githubusercontent.com/10mohi6/discord-webhook-python/master/tests/basic.png)

### basic, username and avatar_url
```python
from discordwebhook import Discord

discord = Discord(url="<your webhook url>")
discord.post(
    content="Hello, world.",
    username="10mohi6",
    avatar_url="https://avatars2.githubusercontent.com/u/38859131?s=460&amp;v=4"
)
```
![basic-username.png](https://raw.githubusercontent.com/10mohi6/discord-webhook-python/master/tests/basic-username.png)

### basic embed
```python
from discordwebhook import Discord

discord = Discord(url="<your webhook url>")
discord.post(
    embeds=[{"title": "Embed Title", "description": "Embed description"}],
)
```
![basic-embed.png](https://raw.githubusercontent.com/10mohi6/discord-webhook-python/master/tests/basic-embed.png)

### advanced embed
```python
from discordwebhook import Discord

discord = Discord(url="<your webhook url>")
discord.post(
    embeds=[
        {
            "author": {
                "name": "Embed Name",
                "url": "https://github.com/10mohi6/discord-webhook-python",
                "icon_url": "https://picsum.photos/24/24",
            },
            "title": "Embed Title",
            "description": "Embed description",
            "fields": [
                {"name": "Field Name 1", "value": "Value 1", "inline": True},
                {"name": "Field Name 2", "value": "Value 2", "inline": True},
                {"name": "Field Name 3", "value": "Field Value 3"},
            ],
            "thumbnail": {"url": "https://picsum.photos/80/60"},
            "image": {"url": "https://picsum.photos/400/300"},
            "footer": {
                "text": "Embed Footer",
                "icon_url": "https://picsum.photos/20/20",
            },
        }
    ],
)
```
![advanced-embed.png](https://raw.githubusercontent.com/10mohi6/discord-webhook-python/master/tests/advanced-embed.png)

### send file
```python
from discordwebhook import Discord

discord = Discord(url="<your webhook url>")
discord.post(
    file={
        "file1": open("tests/file1.jpg", "rb"),
        "file2": open("tests/file2.jpg", "rb"),
    },
)
```
![send-file.png](https://raw.githubusercontent.com/10mohi6/discord-webhook-python/master/tests/send-file.png)


## Getting started

For help getting started with discord webhook, view our online [documentation](https://discordapp.com/developers/docs/resources/webhook).


## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request