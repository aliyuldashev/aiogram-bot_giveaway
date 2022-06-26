import datafetcher
from loader import db
from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import bot
from state import Admin,User
import keyboard


@db.callback_query_handler(keyboard.edit_chanel1.filter(),state='*')
async def edit(msg:CallbackQuery,state:FSMContext,callback_data:dict):
    data = await state.get_data()
    kanel =data['channels']
    count = 0
    text = 'Siz ushbu kanalarga obuna bo`lmadingiz\n'
    for i in kanel:
        data_member = await bot.get_chat_member(chat_id=i[0], user_id=msg.from_user.id)
        print(data_member)
        if data_member['status'] == 'member' or data_member['status'] == 'creator':
            pass
        else:
            count += 1
            channel = await datafetcher.channel_get(i[1])
            text += f'{kanel.index(i)+1} <a href=\"t.me/{channel[0]["username"]}\">{channel[0]["title"]}❌</a>\n '
    if count != 0:
        await msg.message.edit_text(text,parse_mode='html')
        await msg.message.edit_reply_markup(reply_markup=await keyboard.check_sub(msg.from_user.id))
    else:
        mark = await keyboard.otish()
        await msg.message.delete()
        await bot.send_message(msg.message.chat.id,'Siz xamma kanallarga azo bo`ldingiz✅',reply_markup=mark)
        await User.otish.set()

@db.message_handler(commands=['start'],state='*')
async def start(msg: Message, state:FSMContext):
    data = await state.get_data()
    gives_admin = await datafetcher.give_get()
    Admins = await datafetcher.admins_get()
    q = 0
    for i in gives_admin:
        print(i,msg.from_user.id)
        if msg.from_user.id == int(i['admin']):
            q +=1
            give_name = i['name']
    e = 0
    for i in Admins:
        if (msg.from_user.id) == int(i['telegram_id']):
            e += 1

    if q != 0:
        mark = await keyboard.give_name(give_name)
        await state.update_data({
            'give_name':give_name
        })
        await msg.reply('Siz GIVE-ni ro`yxatdan o`tqizgansiz\nGIVE-ni tanlang❗',reply_markup=mark)
        await Admin.kutish.set()


    elif e != 0:
        await bot.send_message(msg.chat.id,'Giveda qatnashish uchun shartlar\n'
                                           '◾Botni kanal yoki grupaga qoshing\n'
                                           '◾Botni xechqanday xuquq bermang\n'
                                           '◾Bizning ikkita postni o`z kanalingizga qo`ying  va tarqating\n'
                                           '◾IDlarni to`g`ri kriting\n\n'
                                           'GIVEga nomini yozing❗')
        await Admin.nomi.set()

    else:
        mark = await keyboard.give_mark()
        if mark['keyboard'] != []:
            await bot.send_message(msg.chat.id,'GIVE nomini tanlang❗',reply_markup=mark)
            await User.give.set()
        else:
            await bot.send_message(msg.chat.id,'Xozircha GIVE-lar yo`q',reply_markup=mark)

@db.message_handler(state=User.give)
async def start(msg: Message, state:FSMContext):
    data = await datafetcher.give_get()
    kanel =[]
    e = 0
    for i in data:
        if msg.text == i['name']:
            e += 1
            kanel = i['channel']
            idss = i['id']
            await datafetcher.give_user(telegram_id=msg.from_user.id,username=msg.from_user.username,name=msg.from_user.full_name,give=idss)
            await state.update_data({
                'give_name': msg.text,
                'give_id': idss
            })
            text = 'Bu GIVE-da qatnashish uchun ushbu kanallarga obuna bo`ling❗ \n'
            channels_id = []
            for i in kanel:
                data_channel = await datafetcher.channel_get(i)
                channels_id.append([data_channel[0]['telegram_id'], data_channel[0]['id']])
                text += f'<a href=\"t.me/{data_channel[0]["username"]}\">{kanel.index(i) + 1} {data_channel[0]["title"]}</a>\n\n'
                print(data_channel[0]["username"])
            text += 'Xammasiga obuna bo`lib tekshirish tugmasini bosing❗'
            mark = await keyboard.check_sub(msg.from_user.id)
            await bot.send_message(msg.chat.id, text, reply_markup=mark, parse_mode='html')
            await state.update_data({
                'channels': channels_id
            })
            await User.patpiska.set()
    if e ==0:
        await msg.reply('No`to`g`ri malumot kritingiz❌\nQaytadan GIVE nomini kriting❗')




@db.message_handler(state=User.otish)
async def start(msg: Message, state:FSMContext):
    if msg.text == 'Asosiy kanalga o`tish':
        kanal = await datafetcher.assosiy()
        kanal = kanal[0]['kanal_telegram_id']
        await msg.reply(f'<a href=\"t.me/{kanal}\">ITIONuz kanalli</a>',parse_mode='html')
        await bot.send_message(msg.chat.id,'Shu kanaldagi malumotlarni kuzatib boring va GIVE boshlanishini kuting')
    elif msg.text == 'Asosiy grupaga o`tish':
        kanal = await datafetcher.assosiy()
        kanal = kanal[0]['kanal_nomi']
        await msg.reply(f'<a href=\"t.me/{kanal}\">ALI Gruppasi</a>',parse_mode='html')
        await bot.send_message(msg.chat.id,'Shu grupadagi malumotlarni kuzatib boring❗ va GIVE boshlanishini kuting❗')

    elif msg.text == 'Biz xaqimizda':
        text = f'ITIONuz group tomonidan o`tqizilyapti\n\n' \
               f'◼Bu bot GIVE o`tqizish uchun maxsus ishlab chiqarilgan\n' \
               f'◼Bu botning tanish bilishlari yo`q😉\n' \
               f'◼Bu bot g`oliblarni random(taxminiy) tarzda tanlab beradi\n' \
               f'◼Bu bot g`olibni ID-si,linki va ismini ko`rsatib beradi agar ishonmasangiz unga yozishingiz mumkun😡\n\n' \
               f'◼Bu botning yaratuvchisi va admini @aliyuldashev0526\n\n' \
               f'Taklif, tanqidlar va Xomiylar uchun @aliyuldashev0526'
        await msg.reply(text,parse_mode='html')
    elif msg.text == 'GIVEni o`tqizish vaqti':
        data = await state.get_data()
        give_name = data['give_name']
        gives = await datafetcher.give_get()
        for i in gives:
            if i['name']==give_name:
                await msg.reply(text=i['time'])
    elif msg.text == 'Statistika':
        data = await state.get_data()
        give_name = data['give_name']
        gives = await datafetcher.give_get()
        for i in gives:
            if i['name'] == give_name:
                await msg.reply(text=f'Boshlanish vaqti: {i["time"]}🧭\n'
                                     f'Kanalar soni: {len(i["channel"])}📊\n'
                                     f'Qatnashuvchilar soni:{len(i["users"])}📈')
    else:
        await msg.reply('Xato malumot kritingiz\nQaytadan kriting❗')
