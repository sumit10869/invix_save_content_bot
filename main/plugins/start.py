#Github.com/mrinvisible7

import os
from .. import bot as Invix
from telethon import events, Button

#from ethon.mystarts import start_srb
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@Invix.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Invix = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with Invix.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if 'png' not in mime and 'jpg' not in mime and 'jpeg' not in mime:
            return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")
        
@Invix.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Invix = event.client            
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        
  
@Invix.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    START_PIC = "https://iili.io/J6Blx5b.md.jpg"
    text = "👋 Hi, I am 'Save Restricted Content ' bot.\n\n✅ Send for private channel's messages, send the Invite Link first."
    #await start_srb(event, text)
    '''
    await event.reply(text, 
                      buttons=[
                              [Button.inline("SET THUMB.", data="set"),
                               Button.inline("REM THUMB.", data="rem")],        
                              ])                             
    '''                          
    
    await event.reply(START_PIC,
                      text,
                      buttons=[
                              [Button.inline("SET.", data="set"),
                               Button.inline("REM.", data="rem")],
                              [Button.url("🌐 MR SATYAM 🌐", url="https://telegram.me/MRSATYAM01")]])
    
    
