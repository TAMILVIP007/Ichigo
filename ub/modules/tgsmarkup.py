#by Sh1vam
#Kangers stay away

import os
from ub import bot as javes
import subprocess, os , asyncio, shutil
from ub.utils import admin_cmd
@javes.on(admin_cmd("tgsjson"))
async def messup(message):
   await message.edit("`jsoning....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media("tgs.tgs")
   process = await asyncio.create_subprocess_shell(f"lottie_convert.py {stkr} json.json",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
   

  

   await message.client.send_file(message.chat_id, "json.json",force_document=False,reply_to=message_id)
   os.remove("json.json")

   await message.delete()
@javes.on(admin_cmd("video"))
async def messup(message):
   await message.edit("`making VIDEO....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media("tgs.tgs")
   process = await asyncio.create_subprocess_shell(f"lottie_convert.py --frame 0 -if lottie -of video tgs.tgs shivam.mp4",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
  
   await message.client.send_file(message.chat_id, "shivam.mp4",force_document=False,reply_to=message_id)
   os.remove("shivam.mp4")
   #os.remove("tgs.tgs")
   await message.delete()
@javes.on(admin_cmd("html"))
async def messup(message):
   await message.edit("`making HTML....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media("tgs.tgs")
   process = await asyncio.create_subprocess_shell(f"lottie_convert.py --frame 0 -if lottie -of html tgs.tgs shivam.html",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
  
   await message.client.send_file(message.chat_id, "shivam.html",force_document=False,reply_to=message_id)
   os.remove("shivam.html")
   #os.remove("tgs.tgs")
   await message.delete()
@javes.on(admin_cmd("gif"))
async def messup(message):
   await message.edit("`making GIF....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media("tgs.tgs")
   process = await asyncio.create_subprocess_shell(f"lottie_convert.py --frame 0 -if lottie -of gif tgs.tgs shivam.gif",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
  
   await message.client.send_file(message.chat_id, "shivam.gif",force_document=False,reply_to=message_id)
   os.remove("shivam.gif")
   #os.remove("tgs.tgs")
   await message.delete()
   
@javes.on(admin_cmd("png"))
async def messup(message):
   await message.edit("`making PNG....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media("tgs.tgs")
   process = await asyncio.create_subprocess_shell(f"lottie_convert.py --frame 0 -if lottie -of png tgs.tgs shivam.png",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
  
   await message.client.send_file(message.chat_id, "shivam.png",force_document=False,reply_to=message_id)
   os.remove("shivam.png")
   #os.remove("tgs.tgs")
   await message.delete()  
@javes.on(admin_cmd("convert"))
async def messup(message):
   convert_to=message.text[9:]
   await message.edit(f"`making {convert_to}....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media("tgs.tgs")
   process = await asyncio.create_subprocess_shell(f"lottie_convert.py --frame 0 -if lottie -of {convert_to} tgs.tgs shivam.{convert_to}",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
  
   await message.client.send_file(message.chat_id, f"shivam.{convert_to}",force_document=False,reply_to=message_id)
   os.remove(f"shivam.{convert_to}")
   #os.remove("tgs.tgs")
   await message.delete()  
@javes.on(admin_cmd("eframe"))
async def messup(message):
   frame=int(message.text[8:])
   await message.edit(f"`Extracting Frame {frame}....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media("tgs.tgs")
   process = await asyncio.create_subprocess_shell(f"lottie_convert.py --frame {frame} -if lottie -of png tgs.tgs shivam.png",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
  
   await message.client.send_file(message.chat_id, "shivam.png",force_document=False,reply_to=message_id)
   os.remove("shivam.png")
   #os.remove("tgs.tgs")
   await message.delete()
@javes.on(admin_cmd("aconvert"))
async def messup(message):
   a,b=message.text[10:].split(";")
   await message.edit(f"`converting {a} to {b}....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media(f"tgs.{a}")
   os.system(f"lottie_convert.py tgs.{a} shivam.{b}")
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
  
   await message.client.send_file(message.chat_id, f"shivam.{b}",force_document=False,reply_to=message_id)
   os.remove(f"shivam.{b}")
   #os.remove("tgs.tgs")
   await message.delete()
@javes.on(admin_cmd("sanitize"))
async def messup(message):
   await message.edit(f"`sanitizeing....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media(f"tgs.tgs")
   process = await asyncio.create_subprocess_shell(f"lottie_convert.py --sanitize tgs.tgs shivam.tgs",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
  
   await message.client.send_file(message.chat_id,"shivam.tgs",force_document=False,reply_to=message_id)
   os.remove("shivam.tgs")
   #os.remove("tgs.tgs")
   await message.delete()
@javes.on(admin_cmd("cjsontgs"))
async def messup(message):
   await message.edit("`converting json to tgs....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media("json.json")
   os.system("lottie_convert.py json.json shivam.tgs")
   os.remove(stkr)
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
  
   await message.client.send_file(message.chat_id, "shivam.tgs",force_document=False,reply_to=message_id)
   os.remove("shivam.tgs")
   #os.remove("tgs.tgs")
   await message.delete()
@javes.on(admin_cmd("tgsresize"))
async def messup(message):
   ss=message.text[11:]
   await message.edit(f"`tgs resizing to {ss} ....`")
   reply = await message.get_reply_message()
   stkr = await reply.download_media("tgs.tgs")
   process = await asyncio.create_subprocess_shell("lottie_convert.py tgs.tgs json.json",stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
   stdout, stderr = await process.communicate()
   os.remove(stkr)
   file = open("json.json", "rt")
   data = file.read()
   data = data.replace("512",ss)
   file.close()
   file = open("json.json", "wt")
   file.write(data)
   file.close()
   os.system("lottie_convert.py json.json shivam.tgs")
   os.remove("json.json")
   if message.reply_to_msg_id:
        message_id = message.reply_to_msg_id
   await message.client.send_file(message.chat_id, "shivam.tgs",force_document=False,reply_to=message_id)
   os.remove("shivam.tgs")
   await message.delete()