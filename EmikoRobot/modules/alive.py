import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/282542026d3570aedf7c1.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hallo [{event.sender.first_name}](tg://user?id={event.sender.id}), Aku Toji Robot.** \n\n"
    TEXT += "⚪ **Saya Bekerja Dengan Benar** \n\n"
    TEXT += f"⚪ **Owner Ku : [IKI](https://t.me/skytrixsz)** \n\n"
    TEXT += f"⚪ **Library Version :** `{telever}` \n\n"
    TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += "**Terima Kasih Telah Menambahkan Saya Di Sini ❤️**"
    BUTTON = [
        [
            Button.url("Help", "https://t.me/skytrixszbot?start=help"),
            Button.url("Support", "https://t.me/wibuhouse"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
