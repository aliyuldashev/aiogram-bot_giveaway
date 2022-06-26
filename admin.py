import random
import datafetcher
from loader import db
from aiogram.types import Message,CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from loader import bot
from state import Admin,Edit,Elon
from datafetcher import channel_add, give_add
import keyboard

@db.callback_query_handler(keyboard.edit_chanel.filter(),state='*')
async def edit(msg:CallbackQuery,state:FSMContext,callback_data:dict):
    await datafetcher.channel_edit(telegram_id1=callback_data.get('id'))
    await msg.message.delete()
    data = await datafetcher.give_get()
    kanel = []
    for i in data:
        if msg.message.text == i['name']:
            kanel = i['channel']
            idss =  i['id']
            users = i['users']
    await state.update_data({
        'datas': [kanel, idss, users]
    })
@db.message_handler(state=Admin.nomi)
async def start(msg: Message, state:FSMContext):
    await state.update_data({
        'give_name': msg.text
    })
    await bot.send_message(msg.chat.id,'Kanal yoki gruppa IDsini qoldiring❗')
    await Admin.linklar.set()

@db.message_handler(state=Admin.linklar)
async def start(msg: Message, state:FSMContext):
    mark  = await keyboard.yana_tugatish()
    data = await state.get_data()

    try :
        now = data['now_in_count']
    except:
        now = 0
    print(now,data)
    if msg.text[0] == '-':
        id = f'-100{str(msg.text[1:])}'
        try:
            data = await bot.get_chat(id)
            try:
                username = data['invite_link'][13:]
                print(data['invite_link'][13:])
            except Exception as ex:
                print(ex, 1)
                username = data['username']
            await state.update_data({
                f'bot{now + 1}': {
                    'id': data['id'],
                    'title': data['title'],
                    'type': data['type'],
                    'username': username
                },
                'now_in_count': now + 1
            })
            print(username)
            await channel_add(telegram_id=data['id'],username=username,title=data['title'])
            await Admin.yana.set()
            await msg.reply('Qabul qilindi\nAgar yana yubormoqchi bo`lsangiz yana yuborish tugmasini bosing',reply_markup=mark)

        except Exception as ex:
            await bot.send_message(msg.chat.id,f'{ex} Xatolik yuzberdi qaytada IDni tekshirib kriting❗')
    else:
        id = f'-100{str(msg.text)}'
        try:
            data = await bot.get_chat(id)
            try:
                username = data['invite_link'][13:]
                print(data['invite_link'][13:])
            except Exception as ex:
                print(ex,1)
                username = data['username']
            await state.update_data({
                f'bot{now+1}':{
                    'id':data['id'],
                    'title':data['title'],
                    'type':data['type'],
                    'username':username
                },
                'now_in_count':now+1
            })
            print(username)
            await channel_add(telegram_id=data['id'], username=username, title=data['title'])
            await Admin.yana.set()
            await msg.reply('Qabul qilindi \nAgar yana yubormoqchi bo`lsangiz yana yuborish tugmasini bosing',reply_markup=mark)
        except:
            await bot.send_message(msg.chat.id,'Xatolik yuzberdi qaytada IDni tekshirib kriting❗')
    try:
        text = ''
        data = await state.get_data()
        for i in range(1, now + 2):
            text += f'{i}: <a href="t.me/{data[f"bot{i}"]["username"]}">{data[f"bot{i}"]["title"]}</a>\n'
        await bot.send_message(msg.chat.id, text, parse_mode='html')
    except Exception as ex:
        print(ex)
@db.message_handler(state=Admin.yana)
async def yana(msg:Message,state:FSMContext):
    if msg.text == 'Yana id qo`shish':
        await msg.reply('IDni kriting!',reply_markup=ReplyKeyboardRemove())
        await Admin.linklar.set()
    elif msg.text == 'Tugatish':
        data = await state.get_data()
        now_in_count = data['now_in_count']
        text = ''
        give_name = data['give_name']
        for i  in range(1 , now_in_count+1):
            text += f'{i}: <a href="t.me/{data[f"bot{i}"]["username"]}">{data[f"bot{i}"]["title"]}</a>\n'
            await give_add(give=give_name,channel_ids=data[f"bot{i}"]["id"],admin=msg.from_user.id)
        await bot.send_message(msg.chat.id, text, parse_mode='html')
        await state.update_data({
            'admin_give': give_name
        })


@db.message_handler(state=Admin.kutish)
async def yana(msg:Message,state:FSMContext):
    data = await datafetcher.give_get()
    kanel = []
    for i in data:
        if msg.text == i['name']:
            kanel = i['channel']
            idss = i['id']
            users = i['users']
    mark = await keyboard.statistics()
    await bot.send_message(msg.chat.id,'Xizmatni tanlang❗',reply_markup=mark)
    await Admin.kutish_2.set()
    await state.update_data({
        'datas':[kanel,idss,users]
    })


@db.message_handler(state=Admin.kutish_2)
async def yana(msg: Message, state: FSMContext):
    data = await state.get_data()
    if msg.text =='Statistika':
        await bot.send_message(msg.chat.id,f'Kanalar: {len(data["datas"][0])}ta\n'
                                           f'Qatnashuvchilar: {len(data["datas"][2])}')
    elif msg.text == 'Kanal qo`shish':
        await bot.send_message(msg.chat.id,'Kanal IDsini kriting!',reply_markup=ReplyKeyboardRemove())
        await Edit.edit.set()

    elif msg.text == 'Kanallar':
        for i in data['datas'][0]:
            channel_data = await datafetcher.channel_get(i)
            mark = await keyboard.edit_channel(channel_data[0]['telegram_id'])
            await bot.send_message(msg.chat.id,f'Nomi: {channel_data[0]["title"]}\n'
                                               f'Linki: @{channel_data[0]["username"]}\n'
                                               f'ID: {channel_data[0]["telegram_id"]}\n',reply_markup=mark)
    elif msg.text == 'Give o`tqizish':
        kanalar1 = 0
        try:
            taxminiy_inson = random.randrange(1,len(data['datas'][2])+1)
            taxminiy_inson = data['datas'][2][taxminiy_inson-1]
            user = await datafetcher.users_get()
            text = 'G`olibimiz :'
            for i in user:
                if int(i['id']) == int(taxminiy_inson):
                    text += f'{i["id"]}raqamli foydalanuvchi\n' \
                            f'Telegram IDsi: {i["telegram_id"]}\n' \
                            f'Linki: @{i["username"]}\n' \
                            f'Nomi: {i["name"]}'
                    await msg.reply(text)
                    text = ''
                    kanalar = data['datas'][0]
                    for iq in kanalar:
                        kanal_data = await datafetcher.channel_get(iq)
                        typess = await bot.get_chat_member(kanal_data[0]['telegram_id'], i['telegram_id'])
                        print(typess)
                        if  typess['status'] == 'member' or typess['status'] == 'creator':
                            kanalar1 += 1
                            text += f'{kanalar.index(iq)+1} {kanal_data[0]["title"]}✅\n'
                        else:
                            text += f'{kanalar.index(iq)+1} {kanal_data[0]["title"]}❌\n'
                    text += f'{len(kanalar)}-dan {kanalar1}-tasiga obuna bo`lganlar'
                    await msg.reply(text)
        except:
            await bot.send_message(msg.chat.id,'Xatolik yuzberidi\n')
    elif msg.text == 'Elon yuborish':
        mark = await keyboard.xabar()
        await msg.reply('Xabar turini tanlamg❗',reply_markup=mark)
        await Elon.kutish.set()
    elif msg.text == 'Tushuntirib berish':
        text = f'◼Bu bot shu GIVE-dan ro`yxatan o`tgan insonlar orasida taxminiy tarzda bitta insoni tanlab beradi\n\n' \
               f'◼Undan tashqari o`sha tanlangan insonning shu GIVEdan ro`yxatdan o`tgan kanalarga obuna bo`lganliginixam tekshirib beradi\n\n' \
               f'Xozirda\n' \
               f'◼Kanalar soni:{len(data["datas"][0])}ta \n' \
               f'◼Ro`yxatdan o`tgan insonlar: {len(data["datas"][2])}ta\n\n' \
               f'⭕Agar botga ishonmasangiz u g`olib bo`lgan insoni telegram IDsini va linkini hamma foydalanuvchilarga yuboradi xudi shu link orqali g`olib bo`lgan insondan so`rab olaverasiz\n\n' \
               f'ADMINlar uchun\n' \
               f'◼Siz bu bot orqali GIVE-ingizda qatnashayotgan barcha insonlarga xabar yuborsangiz bo`ldai\n' \
               f'◼Yoki g`olibni aniqlab IDsi orqali faqat o`sha insonga xabar yubora olasiz\n' \
               f'◼STATISTIC bo`limi orqali kanalar va qatnashuvchilar sonini ko`rsangiz bo`ladi\n' \
               f'◼Kanal qo`shish va taxrirlashxam juda oson\n'
        await msg.reply(text)
    elif msg.text == 'GIVE-ning vaqtini belgilash':
        await msg.reply('Vaqtini bildiruvchi text yuboring❗\nMisol uchun \"Ertaga soat 19:00-da GIVE-miz o`tqiziladi\"')
        await Admin.time.set()
@db.message_handler(state=Elon.kutish)
async def kutsih(msg:Message,state:FSMContext):
    if msg.text == 'Xammaga':
        await msg.reply('Xabarni yuboring❗',reply_markup=ReplyKeyboardRemove())
        await Elon.xamaga.set()
    elif msg.text == 'Birkishiga':
        await msg.reply('Xabarni yuboring❗',reply_markup=ReplyKeyboardRemove())
        await Elon.bir.set()

@db.message_handler(state=Elon.xamaga)
async def kutsih(msg:Message,state:FSMContext):
    data = await state.get_data()
    users = data['datas'][2]
    user_malumot = await datafetcher.users_get()
    sanoq = 0
    for i in user_malumot:
        try:
            if i['id'] in users:
                await bot.send_message(i['telegram_id'], msg.text)
        except:
            sanoq +=1
    await msg.reply(f'Xabar yuborildi\n'
                    f'{len(users)}-tadan {sanoq}-tasiga yetib bormadi',reply_markup=ReplyKeyboardRemove())

@db.message_handler(state=Elon.bir)
async def kutsih(msg:Message,state:FSMContext):
    data = await state.get_data()
    await state.update_data({
        'admin_xabar':msg.text
    })
    await msg.reply('Foydalanuvchining IDsini yuboring!',reply_markup=ReplyKeyboardRemove())
    await Elon.bir_id.set()
@db.message_handler(state=Elon.bir_id)
async def kutsih(msg:Message,state:FSMContext):
    data = await state.get_data()
    xabar = data['admin_xabar']
    id = msg.text
    try:
        await bot.send_message(chat_id=id,text=xabar)
        await bot.send_message(msg.chat.id, 'Xabar yuborildi✔',reply_markup=ReplyKeyboardRemove())
    except:
        await bot.send_message(msg.chat.id,'Xabar yuborilmadi❌',reply_markup=ReplyKeyboardRemove())



@db.message_handler(state=Edit.edit)
async def kutsih(msg:Message,state:FSMContext):
    mark = await keyboard.statistics()
    if msg.text[0] == '-':
        id = f'-100{str(msg.text[1:])}'
        try:
            data = await state.get_data()
            give_name = data['give_name']
            data = await bot.get_chat(id)
            await channel_add(telegram_id=data['id'], username=data['username'], title=data['title'])
            await give_add(give=give_name, channel_ids=[f'{data["id"]}'], admin=msg.from_user.id)
            await msg.reply('Qabul qilindi',reply_markup=mark)
            await Admin.kutish_2.set()
        except:
            await bot.send_message(msg.chat.id,'Xatolik yuzberdi qaytadan kriting!')
    else:
        id = f'-100{str(msg.text)}'
        try:
            data = await state.get_data()
            give_name = data['give_name']
            data = await bot.get_chat(id)
            await channel_add(telegram_id=data['id'], username=data['username'], title=data['title'])
            await give_add(give=give_name,channel_ids=data["id"],admin=msg.from_user.id)
            await msg.reply('Qabul qilindi',reply_markup=mark)
            await Admin.kutish_2.set()
        except:
            await bot.send_message(msg.chat.id,'Xatolik yuzberdi qaytadan kriting!')
@db.message_handler(state=Admin.time)
async def kutsih(msg:Message,state:FSMContext):
    data = await state.get_data()
    name = data['give_name']
    time = msg.text
    mark = await keyboard.statistics()
    await datafetcher.give_time(give=name,time=time,admin=msg.from_user.id)
    await msg.reply('Qabul qilindi✅\nXizmat turini tanlang❗',reply_markup=mark)
    await Admin.kutish_2.set()