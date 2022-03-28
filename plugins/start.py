from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	𝙷𝙴𝙻𝙻𝙾 {message.from_user.first_name }
        𝙸 𝙰𝙼 𝙲𝙷 𝙵𝙸𝙻𝙴 𝚁𝙴𝙽𝙰𝙽𝙴𝚁 𝙱𝙾𝚃 𝙿𝙻𝚉 𝚂𝙴𝙽𝙳 𝙰𝙽𝚈 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
        𝙳𝙾𝙲𝚄𝙼𝙴𝙽𝚃 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾 𝙰𝙽𝙳 𝙴𝙽𝚃𝙴𝚁 𝙵𝙸𝙻𝙴 𝙽𝙰𝙼𝙴 𝚃𝙾 𝚁𝙴𝙽𝙰𝙼𝙴 𝙸𝚃
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("𝙲𝙷𝙰𝙽𝙽𝙴𝙻" ,url="https://t.me/publicchannalin"), 
	  InlineKeyboardButton("𝙶𝚁𝙾𝚄𝙿", url="https://t.me/cine_makotta")
          ],[
          InlineKeyboardButton("𝙾𝚆𝙽𝙴𝚁", url="https://t.me/cine_makotta")
          ]]
          )
        )



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename ",callback_data = "rename")
       ,InlineKeyboardButton("Cancel✖️",callback_data = "cancel")  ]]))
