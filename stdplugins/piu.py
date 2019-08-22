"""Emoji

Available Commands:

.piu"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.01
    animation_ttl = range(0, 288)
    input_str = event.pattern_match.group(1)
    if input_str == "think":
        await event.edit(input_str)
        animation_chars = [
            "ⓟⓘⓤ",
            "ᴘɪᴜ",
            "pooh",
            "Priya",
            "love you",
            "Dala",
            "ριυ",
            "p҉i҉u҉",
            "𝓅𝒾𝓊",
            "ᎮᎥᏬ",
            "קเย",
            "ᕿᓿᑗ",
            "ꉣꀤꀎ",
            "𝘱𝘪𝘶",
            "𝚙𝚒𝚞",
            "【p】【i】【u】",
            "p͓̽i͓̽u͓̽",
            "p͎i͎u͎❤️❤️❤️",
            "p͆i͆u͆❤️❤️❤️💕",
            "ⓟⓘⓤ❤️❤️",
            "Darling",
            "Baby",
            "p♥i♥u♥❤️❤️😊🌹😍💞",
            "Love you",
            "ᎵᎥu❤️❤️😊🌹😍💞",
            "ρσσн❤️",
            "𝕡𝕠𝕠𝕙❤️",
            "𝕡𝕣𝕚𝕪𝕒❤️",
            "ρяιүα💖😍❤️",
            "卩尺丨ㄚ卂💖😍❤️",
            "My love",
            "𝓅𝓇𝒾𝓎𝒶💖😍❤️",
            "קȑȋÿå💖😍❤️",
            "Bunny",
            "love you",
            "ᏞᎾᏉᎬ ᎽᎾu sᎾ muᏟh💖💞❤️💕😍"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 72])
