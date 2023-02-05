from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 𝗔𝗗𝗗 𝗠𝗘 𝗘𝗟𝗦𝗘 𝗬𝗢𝗨 𝗚𝗔𝗬 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝗛𝗲𝗹𝗽 😇",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀 😎", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="😇 𝗔𝗗𝗗 𝗠𝗘 𝗘𝗟𝗦𝗘 𝗬𝗢𝗨 𝗚𝗔𝗬 😇",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝗛𝗲𝗹𝗽 😌", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗿𝗼𝘂𝗽 😇", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝗢𝘄𝗻𝗲𝗿 ❤", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="𝗦𝗼𝘂𝗿𝗰𝗲 ⚠️", url=config.UPSTREAM_REPO
            )
        ],
     ]
    return buttons
