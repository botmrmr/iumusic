import os
import re
import config
import aiohttp
import aiofiles
# from ZeMusic.platforms.Youtube import cookie_txt_file

import yt_dlp
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from youtube_search import YoutubeSearch

from ZeMusic import app, YouTube 
from ZeMusic.plugins.play.filters import command
from ZeMusic.utils.decorators import AdminActual
from ZeMusic.utils.database import is_search_enabled, enable_search, disable_search
import requests, json, redis
import time

ID_CN = -1002256653433
TOOKEN = "7117654702:AAEh_WSXs5ITtNurJKuNdeMl7RzwpT23PEU" 
rds = redis.Redis('localhost', decode_responses=True)
def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":")))
    )
                        
def Yochannel(performer, title, audio_file,thumb):
    if not os.path.exists(audio_file):
        return
    payload = {'thumb': thumb,'title': title,'performer': performer,"chat_id": ID_CN,}
    with open(audio_file, 'rb') as audio:
        files = {'audio': audio}
        response = requests.post(
            f"https://api.telegram.org/bot{TOOKEN}/sendAudio",data=payload,files=files)
    return response.json()


def remove_if_exists(path):
    if os.path.exists(path):
        os.remove(path)
        
lnk = config.CHANNEL_LINK
Nem = config.BOT_NAME + " ابحث"

@app.on_message(command(["song", "/song", "بحث", Nem,"يوت"]) & filters.group)
async def song_downloader(client, message: Message):
    chat_id = message.chat.id 
    if not await is_search_enabled(chat_id):
        return await message.reply_text("<b>⟡عذراً عزيزي اليوتيوب معطل لتفعيل اليوتيوب اكتب تفعيل اليوتيوب</b>")
        
    query = " ".join(message.command[1:])
    m = await message.reply_text("<b>⇜ جـارِ البحث ..</b>")
    
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        if not results:
            await m.edit("- لم يتم العثـور على نتائج حاول مجددا")
            return
        if not results:
            await m.edit("- لم يتم العثـور على نتائج حاول مجددا")
            return
        if not results[0]:
            await m.edit("- لم يتم العثـور على نتائج حاول مجددا")
            return            
        if not results[0]["duration"]:
            await m.edit("- لم يتم العثـور على نتائج حاول مجددا")
            return            
        tim = int(time_to_seconds(results[0]["duration"]))
        desthone = time.strftime('%M:%S', time.gmtime(tim))        
        id_odo = results[0]['url_suffix']
        if rds.hget("yut1", id_odo):
            audio_id = rds.hget("yut1", id_odo)
            audio_file = f'https://t.me/vbbbbnnnm/{audio_id}'
            await message.reply_audio(
            audio=audio_file,
            caption=f"⟡ {app.mention} ↠ {desthone}", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                                              InlineKeyboardButton(text=config.CHANNEL_NAME, url=lnk),
                    ],
                ]
            ),
        )
        
            return await m.delete()
        

        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        title_clean = re.sub(r'[\\/*?:"<>|]', "", title)  # تنظيف اسم الملف
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title_clean}.jpg"

        # تحميل الصورة المصغرة
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(thumb_name, mode='wb')
                    await f.write(await resp.read())
                    await f.close()

        duration = results[0]["duration"]

    except Exception as e:
        await m.edit("- لم يتم العثـور على نتائج حاول مجددا")
        print(str(e))
        return
    
    await m.edit("<b>جاري التحميل ♪</b>")
    
    # ydl_opts = {
        # "format": "bestaudio[ext=m4a]",  # تحديد صيغة M4A
        # "keepvideo": False,
        # "geo_bypass": True,
        # "outtmpl": f"{title_clean}.%(ext)s",  # استخدام اسم نظيف للملف
        # "quiet": True,
        # "cookiefile": cookie_txt_file(),
    # }

    try:
        audio_file = await YouTube.download(results[0]["id"],  None)
        # حساب مدة الأغنية
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60

        # إرسال الصوت
        await message.reply_audio(
            audio=audio_file,
            caption=f"⟡ {app.mention}",
            title=title,
            performer=info_dict.get("uploader", "Unknown"),
            thumb=thumb_name,
            duration=dur
        )
        await m.delete()
        ter = Yochannel(c.me.username, title, audio_file,thumb_name)
        id_audio = ter['result']['message_id']
        rds.hset(f"yut1", id_odo, id_audio)
    except Exception as e:
        await m.edit(f"error, wait for bot owner to fix\n\nError: {str(e)}")
        print(e)

    # حذف الملفات المؤقتة
    try:
        remove_if_exists(audio_file)
        remove_if_exists(thumb_name)
    except Exception as e:
        print(e)


@app.on_message(command(["تعطيل اليوتيوب"]) & filters.group)
@AdminActual
async def disable_search_command(client, message: Message, _):
    chat_id = message.chat.id
    if not await is_search_enabled(chat_id):
        await message.reply_text("<b>⟡اليوتيوب معطل من قبل يالطيب</b>")
        return
    await disable_search(chat_id)
    await message.reply_text("<b>⟡تم تعطيل اليوتيوب بنجاح</b>")


@app.on_message(command(["تفعيل اليوتيوب"]) & filters.group)
@AdminActual
async def enable_search_command(client, message: Message, _):
    chat_id = message.chat.id
    if await is_search_enabled(chat_id):
        await message.reply_text("<b>⟡اليوتيوب مفعل من قبل يالطيب</b>")
        return
    await enable_search(chat_id)
    await message.reply_text("<b>⟡تم تفعيل اليوتيوب بنجاح</b>")
