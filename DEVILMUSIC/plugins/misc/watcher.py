from pyrogram import filters
from pyrogram.types import Message

from DEVILMUSIC import app
from DEVILMUSIC.core.call import DEVIL

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await DEVIL.stop_stream_force(message.chat.id)
