from ub import bot as javes
from telethon import events

import asyncio

from ub.utils import admin_cmd

@javes.on(admin_cmd("evil"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(
        10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    )

    await event.edit("EVIL IS WAKE UP...HA...HA...HA ... !!!")
    animation_chars = [
            "😈",
            "👿",
            ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 2])
