
from telethon import events
from ub import bot as javes
import asyncio

from ub.utils import admin_cmd

@javes.on(admin_cmd("evil"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(
        10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    )

    await event.edit("â ï¸EVIL IS WAKE UP...HA...HA...HA ...ð½â¼ï¸ð¾")
    animation_chars = [
            "ð",
            "ð¿",
            "ð",
            "ð",
            "ð»",
            ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5])
