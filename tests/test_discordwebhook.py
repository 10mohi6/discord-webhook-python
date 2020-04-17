import os
import pytest
import time
import requests
from discordwebhook import Discord


@pytest.fixture(scope="module", autouse=True)
def scope_module():
    url = os.environ["DISCORD_WEBHOOK_URL"]
    yield Discord(url=url)


@pytest.fixture(scope="function", autouse=True)
def discord(scope_module):
    time.sleep(1)
    yield scope_module


# @pytest.mark.skip
def test_discord_post_basic(discord):
    expected = requests.codes.no_content
    actual = discord.post(content="Hello, world.").status_code
    assert expected == actual


# @pytest.mark.skip
def test_discord_post_basic_username(discord):
    expected = requests.codes.no_content
    actual = discord.post(
        content="Hello, world.",
        username="10mohi6",
        avatar_url="https://avatars2.githubusercontent.com/u/38859131?s=460&amp;v=4",
    ).status_code
    assert expected == actual


# @pytest.mark.skip
def test_discord_post_basic_embed(discord):
    expected = requests.codes.no_content
    actual = discord.post(
        embeds=[{"title": "Embed Title", "description": "Embed description"}],
    ).status_code
    assert expected == actual


# @pytest.mark.skip
def test_discord_post_advanced_embed(discord):
    expected = requests.codes.no_content
    actual = discord.post(
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
    ).status_code
    assert expected == actual


# @pytest.mark.skip
def test_discord_post_send_file(discord):
    expected = requests.codes.ok
    actual = discord.post(
        file={
            "file1": open("tests/file1.jpg", "rb"),
            "file2": open("tests/file2.jpg", "rb"),
        },
    ).status_code
    assert expected == actual
