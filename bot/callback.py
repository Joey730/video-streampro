from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""ā HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @tg_video_stream to your group.
4.) turn on the voice chat first before start to stream video.
5.) type /stream (reply to video) to start streaming.
6.) type /stop to end the video streaming.

ā” __Maintained by Veez Project Team__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "š” Go Back", callback_data="cbstart")
      ]]
    ))

@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.edit_message_text(f"āØ **Hello, I am a telegram video streaming bot.**\n\nš­ **I was created to stream videos in group video chats easily.**\n\nā **To find out how to use me, please press the help button below** šš»",
                                reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "ā HOW TO USE THIS BOT", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "š©š»āš» Developer", url="https://t.me/dlwrml")
                       ],[
                          InlineKeyboardButton(
                             "š­ Group", url="https://t.me/VeezSupportGroup"),
                          InlineKeyboardButton(
                             "āØ Channel", url="https://t.me/levinachannel")
                       ]]
                    ))
