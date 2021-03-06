from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	π·π΄π»π»πΎ {message.from_user.first_name }
        πΈ π°πΌ π²π· π΅πΈπ»π΄ ππ΄π½π°π½π΄π π±πΎπ πΏπ»π ππ΄π½π³ π°π½π ππ΄π»π΄πΆππ°πΌ
        π³πΎπ²ππΌπ΄π½π πΎπ ππΈπ³π΄πΎ π°π½π³ π΄π½ππ΄π π΅πΈπ»π΄ π½π°πΌπ΄ ππΎ ππ΄π½π°πΌπ΄ πΈπ
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("π²π·π°π½π½π΄π»" ,url="https://t.me/publicchannalin"), 
	  InlineKeyboardButton("πΆππΎππΏ", url="https://t.me/cine_makotta")
          ],[
          InlineKeyboardButton("πΎππ½π΄π", url="https://t.me/cine_makotta")
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
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("π Rename ",callback_data = "rename")
       ,InlineKeyboardButton("CancelβοΈ",callback_data = "cancel")  ]]))
