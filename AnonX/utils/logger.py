from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AnonX import app
from AnonX.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
**{MUSIC_BOT_NAME} ᴩʟᴀʏ ʟᴏɢɢᴇʀ**

**𝗜𝘀𝗸𝗶 𝗖𝗵𝘂𝘁💦:** {message.chat.title} [`{message.chat.id}`]
**𝗦𝗲𝗮𝗿𝗰𝗵𝗲𝗿 𝗠𝗮𝗱𝗮𝗿𝗰𝗵𝗼𝗱😎:** {message.from_user.mention}
**𝗕𝗵𝗲𝗡𝗰𝗵𝗼𝗱 𝗞𝗮 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲⚠️:** @{message.from_user.username}
**𝗠𝗮𝗱𝗮𝗿𝗰𝗵𝗼𝗱 𝗞𝗶 𝗜𝗱 😌:** `{message.from_user.id}`
**𝗖𝗵𝘂𝘁 𝗸𝗮𝗮 𝗟𝗶𝗻𝗸 😂:** {chatusername}

**𝗬𝗲 𝗱𝗵𝘂𝗻𝗱 𝗿𝗵𝗮 𝗵 𝗯𝗸𝗹 😎:** {message.text}

**𝗞𝗮𝗶𝘀𝗲 𝗕𝗷𝗮𝗶 😂:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
