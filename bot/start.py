from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, Chat, CallbackQuery

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
      await m.reply(f"āØ **Hello, I am a telegram video streaming bot.**\n\nš­ **I was created to stream videos in group video chats easily.**\n\nā **To find out how to use me, please press the help button below** šš»",
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
   else:
      await m.reply("**āØ bot is online now āØ**")
